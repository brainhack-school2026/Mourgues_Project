import os
import json
import numpy as np
import librosa

# Audio folder
audio_folder = "../data/sounds"
output_folder = "../outputs"

os.makedirs(output_folder, exist_ok=True)

print(os.listdir(audio_folder))

# Global results (optionnel si tu veux un résumé global)
results = {}

# Loop
for file in os.listdir(audio_folder):

    if file.endswith(".wav"):

        path = os.path.join(audio_folder, file)
        audio, sr = librosa.load(path, sr=None)

        print("\nFILE:", file)
        print("LENGTH:", len(audio))

        # Duration
        duration = len(audio) / sr

        # Intensity
        rms = librosa.feature.rms(y=audio)
        global_intensity = float(np.mean(rms))

        # F0
        f0 = librosa.yin(audio, fmin=50, fmax=500)
        f0_mean = float(np.nanmean(f0))
        f0_var = float(np.nanstd(f0))

        # Spectral features
        spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
        spectral_rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)

        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

        spectral_features = {
            "spectral_centroid_mean": float(np.mean(spectral_centroid)),
            "spectral_bandwidth_mean": float(np.mean(spectral_bandwidth)),
            "spectral_rolloff_mean": float(np.mean(spectral_rolloff)),
            "mfcc_mean": mfcc.mean(axis=1).tolist()
        }

        # Output folder per sound
        sound_name = file.replace(".wav", "")
        sound_output_folder = os.path.join(output_folder, sound_name)

        os.makedirs(sound_output_folder, exist_ok=True)

        # JSON per sound
        result = {
            "file": file,
            "duration": float(duration),
            "global_intensity": global_intensity,
            "f0_mean": f0_mean,
            "f0_variability": f0_var,
            **spectral_features
        }

        # save per file
        json_path = os.path.join(sound_output_folder, "results.json")

        with open(json_path, "w") as f:
            json.dump(result, f, indent=4)

        results[file] = result

        print("Saved:", json_path)

print("\nDONE - all files processed")
