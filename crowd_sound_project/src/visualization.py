import os
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from sklearn.decomposition import PCA

# paths

outputs_folder = "../outputs"
figures_folder = "../figures"

os.makedirs(figures_folder, exist_ok=True)

# load json files

data = []

for sound_folder in os.listdir(outputs_folder):

    json_path = os.path.join(outputs_folder, sound_folder, "results.json")

    if os.path.exists(json_path):

        with open(json_path, "r") as f:
            result = json.load(f)

            result["file"] = sound_folder
            result["group"] = sound_folder[0]

            data.append(result)

# dataframe

df = pd.DataFrame(data)

df_sorted_f0 = df.sort_values(by="f0_mean", ascending=False)
df_sorted_centroid = df.sort_values(by="spectral_centroid_mean", ascending=False)
df_sorted_bandwidth = df.sort_values(by="spectral_bandwidth_mean", ascending=False)
df_sorted_rolloff = df.sort_values(by="spectral_rolloff_mean", ascending=False)

print("\n" + "="*40)
print("feature inspection")
print("="*40)

print("data overview")
print(df.head())

print("\nhighest f0 (most acute sounds)")
print(df_sorted_f0[["file", "f0_mean"]].head(5))

print("\nhighest spectral centroid (most noisy / rich sounds)")
print(df_sorted_centroid[["file", "spectral_centroid_mean"]].head(5))

print("\nhighest spectral bandwidth (spread of frequencies)")
print(df_sorted_bandwidth[["file", "spectral_bandwidth_mean"]].head(5))

print("\nhighest spectral rolloff (high energy sounds)")
print(df_sorted_rolloff[["file", "spectral_rolloff_mean"]].head(5))

print("\nlowest f0 (most grave sounds)")
print(df_sorted_f0[["file", "f0_mean"]].tail(5))

print("\nlowest spectral centroid (most stable / pure sounds)")
print(df_sorted_centroid[["file", "spectral_centroid_mean"]].tail(5))

print("\nlowest spectral bandwidth")
print(df_sorted_bandwidth[["file", "spectral_bandwidth_mean"]].tail(5))

print("\nlowest spectral rolloff")
print(df_sorted_rolloff[["file", "spectral_rolloff_mean"]].tail(5))

# feature inspection dictionary

inspection_results = {
    "highest_f0": df_sorted_f0[
        ["file", "f0_mean"]
    ].head(5).to_dict(orient="records"),

    "lowest_f0": df_sorted_f0[
        ["file", "f0_mean"]
    ].tail(5).to_dict(orient="records"),

    "highest_spectral_centroid": df_sorted_centroid[
        ["file", "spectral_centroid_mean"]
    ].head(5).to_dict(orient="records"),

    "lowest_spectral_centroid": df_sorted_centroid[
        ["file", "spectral_centroid_mean"]
    ].tail(5).to_dict(orient="records"),

    "highest_spectral_bandwidth": df_sorted_bandwidth[
        ["file", "spectral_bandwidth_mean"]
    ].head(5).to_dict(orient="records"),

    "lowest_spectral_bandwidth": df_sorted_bandwidth[
        ["file", "spectral_bandwidth_mean"]
    ].tail(5).to_dict(orient="records"),

    "highest_spectral_rolloff": df_sorted_rolloff[
        ["file", "spectral_rolloff_mean"]
    ].head(5).to_dict(orient="records"),

    "lowest_spectral_rolloff": df_sorted_rolloff[
        ["file", "spectral_rolloff_mean"]
    ].tail(5).to_dict(orient="records")
}

# save json

with open("../outputs/feature_inspection.json", "w") as f:
    json.dump(inspection_results, f, indent=4)

print("\nfeature inspection json saved")

# seaborn

sns.set(style="whitegrid")

# f0 boxplot

plt.figure(figsize=(8, 6))

sns.boxplot(
    data=df,
    x="group",
    y="f0_mean"
)

plt.title("F0 mean by group")
plt.xlabel("group")
plt.ylabel("f0 mean (hz)")

plt.tight_layout()
plt.savefig("../figures/f0_mean_boxplot.png")
plt.close()

# spectral centroid boxplot

plt.figure(figsize=(8, 6))

sns.boxplot(
    data=df,
    x="group",
    y="spectral_centroid_mean"
)

plt.title("Spectral centroid by group")
plt.xlabel("group")
plt.ylabel("spectral centroid")

plt.tight_layout()
plt.savefig("../figures/spectral_centroid_boxplot.png")
plt.close()

# pca mfcc

mfcc_data = []
labels = []
files = []

for item in data:
    mfcc_data.append(item["mfcc_mean"])
    labels.append(item["group"])
    files.append(item["file"])

X = np.array(mfcc_data)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

df_pca = pd.DataFrame({
    "pc1": X_pca[:, 0],
    "pc2": X_pca[:, 1],
    "group": labels,
    "file": files
})

# pca plot

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=df_pca,
    x="pc1",
    y="pc2",
    hue="group",
    s=120
)

for i in range(len(df_pca)):
    plt.text(
        df_pca["pc1"][i],
        df_pca["pc2"][i],
        df_pca["file"][i],
        fontsize=8
    )

plt.title("pca of mfcc features (individual sounds)")
plt.xlabel("pc1")
plt.ylabel("pc2")

plt.tight_layout()
plt.savefig("../figures/pca_mfcc_individual.png")
plt.close()

# clustering k-means on MFCC

kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X)

df_pca["cluster"] = clusters

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=df_pca,
    x="pc1",
    y="pc2",
    hue="cluster",
    palette="Set1",
    s=120
)

for i in range(len(df_pca)):
    plt.text(
        df_pca["pc1"][i],
        df_pca["pc2"][i],
        df_pca["file"][i],
        fontsize=8
    )

plt.title("k-means clustering on MFCC (unsupervised)")
plt.xlabel("pc1")
plt.ylabel("pc2")

plt.tight_layout()
plt.savefig("../figures/kmeans_mfcc.png")
plt.close()

print("done - figures saved")
