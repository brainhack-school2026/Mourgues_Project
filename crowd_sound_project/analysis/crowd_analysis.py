import os
import json
import numpy as np
import librosa
import matplotlib.pyplot as plt
import librosa.display

# Audio folder
audio_folder = "/mnt/c/Users/ocean/OneDrive - Université du Québec à Trois-Rivières/Bureau/sounds_bq"

print(os.listdir(audio_folder))

# Results dictionary
results = {}

# Loop
for file in os.listdir(audio_folder):

    if file.endswith(".wav"):

        path = os.path.join(audio_folder, file)

        audio, sr = librosa.load(path, sr=None)

        print("FILE:", file)
        print("LENGTH:", len(audio))

        # PARAMETERS

        # Sound duration
        duration = len(audio) / sr
        print("Durée (s):", duration)

        # Global intensity
        rms = librosa.feature.rms(y=audio)
        global_intensity = float(np.mean(rms))
        print("Intensité globale:", global_intensity)

        # F0 estimation
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
        plt.savefig(f"waveform_{file}.png")
        plt.close()

        # Spectrogram
        S = librosa.feature.melspectrogram(y=audio, sr=sr)
        S_db = librosa.power_to_db(S, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f"Mel Spectrogram - {file}")
        plt.tight_layout()
        plt.savefig(f"spectrogram_{file}.png")
        plt.close()

        # Store results
        results[file] = {
            "duration": duration,
            "global_intensity": global_intensity,
            "f0_mean": f0_mean,
            "f0_variability": f0_var,
            "spectral_balance": spectral_balance
        }

# Save json
with open("results.json", "w") as f:
    json.dump(results, f, indent=4)

print("JSON file created successfully!")
