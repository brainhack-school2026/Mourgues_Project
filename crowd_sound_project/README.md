# My presentation

## Resume 

Here is the resume of the project:

This project focuses on the organization, visualization, and exploration of crowd sound stimuli. Crowd vocalizations are widely used to investigate emotion perception, multisensory integration, and social behavior, but current crowd-audio stimuli are often custom-made, difficult to reproduce, poorly standardized, and limited in experimental control.

The objective of this project is to develop an interactive and reproducible framework for exploring crowd sounds through parameter-based organization, audio visualization, and structured metadata. The system aims to support the comparison and analysis of auditory stimuli using spectrograms, waveforms, and acoustic parameter displays.

The project organizes sounds according to several perceptual and acoustic dimensions, including temporal, dynamic, vocal, spectral, and spatial parameters. This framework is intended to facilitate the creation, organization, and reuse of auditory stimuli in experimental research contexts.

The project also emphasizes reproducibility and open science practices through the use of Python, Jupyter notebooks, GitHub, and structured workflows for audio processing and metadata organization. Final deliverables will include reproducible scripts, interactive audio exploration tools, audio visualizations, structured datasets, and documentation to support reuse and long-term accessibility.


## Project Structure

```text
crowd_sound_project/
│
├── README.md
├── data
│   └── sounds
│       ├── A-01.wav
│       ├── A-02.wav
│       ├── A-03.wav
│       ├── A-04.wav
│       ├── A-05.wav
│       ├── A-06.wav
│       ├── J-01.wav
│       ├── J-02.wav
│       ├── J-03.wav
│       ├── J-04.wav
│       ├── J-05.wav
│       └── J-06.wav
├── figures
│   ├── f0_mean_boxplot.png
│   ├── kmeans_mfcc.png
│   ├── pca_mfcc.png
│   ├── pca_mfcc_individual.png
│   └── spectral_centroid_boxplot.png
├── outputs
│   ├── A-01
│   │   └── results.json
│   ├── A-02
│   │   └── results.json
│   ├── A-03
│   │   └── results.json
│   ├── A-04
│   │   └── results.json
│   ├── A-05
│   │   └── results.json
│   ├── A-06
│   │   └── results.json
│   ├── J-01
│   │   └── results.json
│   ├── J-02
│   │   └── results.json
│   ├── J-03
│   │   └── results.json
│   ├── J-04
│   │   └── results.json
│   ├── J-05
│   │   └── results.json
│   ├── J-06
│   │   └── results.json
│   └── feature_inspection.json
└── src
    ├── crowd_analysis.py
    └── visualization.py
```

This structure is designed to support reproducibility, organization, and open science practices throughout the project development process.

## Presentation link

 Click here to view the slides: https://docs.google.com/presentation/d/1v9t9jJARwTjZ2fG6t1Csj8lXJtg4WSRqbLEC1cxJR6A/edit?usp=sharing 


##Production
 
#Step 1 – Audio Feature Extraction

File: src/crowd_analysis.py


Objective

Extract acoustic features from each .wav file.


Package used:

librosa


#Extracted Features

For each sound:

duration
global intensity (RMS)
fundamental frequency (F0)
spectral centroid
spectral bandwidth
spectral rolloff
MFCC (13 coefficients)
Output

Each sound generates:

outputs/A-01/results.json
outputs/J-03/results.json
Example JSON Content
{
  "file": "A-01.wav",
  "duration": 1.5,
  "global_intensity": 0.04,
  "f0_mean": 300.2,
  "f0_variability": 120.1,
  "spectral_centroid_mean": 1600,
  "spectral_bandwidth_mean": 1500,
  "spectral_rolloff_mean": 2400,
  "mfcc_mean": [...]
}

#Step 2 – Visualization and Analysis

File: src/visualization.py

Packages used:

Seaborn
Pandas
Scikit-learn
Objective

Compare sounds individually and between groups (A vs J).


2.1 Boxplots (Statistical Comparison)

Analyzed variables:

F0 (pitch)
spectral centroid (brightness)


Code used:

sns.boxplot(data=df, x="group", y="f0_mean")

sns.boxplot(
    data=df,
    x="group",
    y="spectral_centroid_mean"
)

Interpretation
pitch differences between groups
differences in spectral richness / noisiness



2.2 PCA (Dimensionality Reduction)

Objective

Reduce MFCC dimensions from 13D to 2D.

Method used:

PCA(n_components=2)
Output
pca_mfcc.png → global A vs J visualization
pca_mfcc_individual.png → each sound individually labeled
Interpretation
grouping of similar sounds
class separation or overlap
outlier detection



2.3 Clustering (K-means)

Objective

Check if the algorithm can identify groups without labels.

Method used:

KMeans(n_clusters=2)
Output
kmeans_mfcc.png
Interpretation
clusters ≈ A/J → groups are well separated
mixed clusters → strong internal variability
Step 3 – Result Interpretation
F0 (Pitch)
higher values → higher-pitched sounds
lower values → deeper sounds
Spectral Centroid
high values → noisy / crowd / mixed sounds
low values → stable / pure sounds
PCA MFCC
clear separation → distinct classes
overlap → acoustic similarity
Clustering
validates or questions the natural structure of the dataset


#Step 4 – Feature Inspection (Detailed Sound Analysis)

File: src/visualization.py

Packages used:

Pandas
Seaborn
Objective

Inspect sounds individually according to acoustic features to identify:

highest pitch sounds
lowest pitch sounds
noisiest sounds
most energetic sounds
extreme values and outliers
Method

The data is loaded into a Pandas DataFrame and sorted according to several acoustic parameters.

Code used:

df_sorted_f0 = df.sort_values(by="f0_mean", ascending=False)

df_sorted_centroid = df.sort_values(
    by="spectral_centroid_mean",
    ascending=False
)

df_sorted_bandwidth = df.sort_values(
    by="spectral_bandwidth_mean",
    ascending=False
)

df_sorted_rolloff = df.sort_values(
    by="spectral_rolloff_mean",
    ascending=False
)


#Analyzed Parameters

F0 (Pitch)
high → acute sounds
low → deep sounds

Spectral Centroid
high → noisy / spectrally rich sounds
low → stable / pure sounds

Spectral Bandwidth
high → wide frequency dispersion
low → compact spectrum

Spectral Rolloff
high → strong high-frequency energy
low → weaker energy


A summary JSON file is automatically generated:

outputs/feature_inspection.json

This file contains rankings of sounds according to each feature.



Why This Step Is Useful

This step helps:

interpret the data before classification
detect outliers
understand acoustic differences
prepare machine learning analyses






This project allows:

extraction of audio features
statistical comparison between groups
visualization of data structure
testing class separability
exploration of acoustic variability
