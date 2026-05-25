import numpy as np
import librosa

# LOAD AUDIO
audio, sr = librosa.load(
    "/mnt/c/Users/ocean/OneDrive - Université du Québec à Trois-Rivières/Bureau/sounds_bq/A-01.wav",
    sr=None
)

print(audio.shape)
print(sr)

# PARAMETERS

# Sound duration
duration = len(audio) / sr
print("Durée (s):", duration)

# Global intensity
rms = librosa.feature.rms(y=audio)
global_intensity = np.mean(rms)
print("Intensité globale:", global_intensity)

# F0 estimation
f0 = librosa.yin(audio, fmin=50, fmax=500)
f0_mean = np.nanmean(f0)
f0_var = np.nanstd(f0)

print("F0 moyenne:", f0_mean)# hauteur moyenne
print("Variabilité F0:", f0_var)# variabilité du pitch

# Spectral centroid (balance grave/aigu)
centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)
spectral_balance = np.mean(centroid)

print("Spectre (centroid moyen):", spectral_balance)
