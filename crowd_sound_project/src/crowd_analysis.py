import os
import json
import numpy as np
import librosa
import matplotlib.pyplot as plt
import librosa.display

# Audio folder
audio_folder = "../data/sounds"

print(os.listdir(audio_folder))

# Loop
for file in os.listdir(audio_folder):

    if file.endswith(".wav"):

        path = os.path.join(audio_folder, file)
        audio, sr = librosa.load(path, sr=None)

        # Output folder
        sound_name = file.replace(".wav", "")
        output_folder = f"../outputs/{sound_name}"
        os.makedirs(output_folder, exist_ok=True)

        print("FILE:", file)
        print("LENGTH:", len(audio))

        # Duration
        duration = len(audio) / sr
        print("Durée (s):", duration)

        # Intensity
        rms = librosa.feature.rms(y=audio)
        global_intensity = float(np.mean(rms))
        print("Intensité globale:", global_intensity)

        # F0
        f0 = librosa.yin(audio, fmin=50, fmax=500)
        f0_mean = float(np.nanmean(f0))
        f0_var = float(np.nanstd(f0))

        print("F0 moyenne:", f0_mean)
        print("Variabilité F0:", f0_var)

        # Spectral centroid
        centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)
        spectral_balance = float(np.mean(centroid))

        print("Spectre (centroid moyen):", spectral_balance)

        # Waveform
        plt.figure(figsize=(10, 3))
        librosa.display.waveshow(audio, sr=sr)
        plt.title(f"Waveform - {file}")
        plt.tight_layout()
        plt.savefig(f"{output_folder}/waveform.png")
        plt.close()

        # Spectrogram
        S = librosa.feature.melspectrogram(y=audio, sr=sr)
        S_db = librosa.power_to_db(S, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f"Mel Spectrogram - {file}")
        plt.tight_layout()
        plt.savefig(f"{output_folder}/spectrogram.png")
        plt.close()

        # JSON per sound
        results = {
            "duration": duration,
            "global_intensity": global_intensity,
            "f0_mean": f0_mean,
            "f0_variability": f0_var,
            "spectral_balance": spectral_balance
        }

        with open(f"{output_folder}/results.json", "w") as f:
            json.dump(results, f, indent=4)

print("DONE - all files processed")

