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



## Procedure

---

## Step 1 – Audio Feature Extraction

**File:** `src/crowd_analysis.py`

# Objective
Extract acoustic features from each `.wav` audio file using `librosa`.

# Extracted Features

- duration  
- global intensity (RMS)  
- fundamental frequency (F0)  
- spectral centroid  
- spectral bandwidth  
- spectral rolloff  
- MFCC (13 coefficients)  

# Output

Each audio file generates a JSON file:

- outputs/J-03/results.json
- outputs/A-01/results.json

# Example JSON

```json
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

## Step 2 – Visualization and Analysis

**File:** `src/visualization.py`

### Objective
Compare audio signals between groups (A vs J) and analyze their acoustic structure.

### Packages used
- seaborn
- pandas
- scikit-learn

---

### 2.1 Boxplots (statistical comparison)

#### Variables analyzed
- F0 (pitch)
- spectral centroid (brightness / noisiness)

#### Code
```python
sns.boxplot(data=df, x="group", y="f0_mean")
sns.boxplot(data=df, x="group", y="spectral_centroid_mean")
```

#### Interpretation
- pitch differences between groups  
- spectral richness / noise differences  

---

### 2.2 PCA (dimensionality reduction)

#### Objective
Reduce MFCC features from 13D → 2D

#### Method
```python
PCA(n_components=2)
```

#### Output
- `pca_mfcc.png` → global visualization  
- `pca_mfcc_individual.png` → individual labeled points  

#### Interpretation
- clustering of similar sounds  
- separation or overlap between groups  
- detection of outliers  

---

### 2.3 K-means clustering

#### Objective
Check if the algorithm can recover groups without labels.

#### Method
```python
KMeans(n_clusters=2)
```

#### Output
- `kmeans_mfcc.png`

#### Interpretation
- clusters ≈ A/J → good separability  
- mixed clusters → strong variability  

---

## Step 3 – Feature Interpretation

### F0 (Pitch)
- high → high-pitched sounds  
- low → low-pitched sounds  

### Spectral centroid
- high → noisy / crowd / mixed sounds  
- low → stable / pure sounds  

### PCA (MFCC)
- clear separation → distinct classes  
- overlap → acoustic similarity  

### Clustering
- validates or questions dataset structure  

---

## Step 4 – Feature Inspection

**File:** `src/visualization.py`

### Objective
Inspect each sound individually using acoustic features.

### Features analyzed
- highest / lowest F0  
- highest / lowest spectral centroid  
- highest / lowest spectral bandwidth  
- highest / lowest spectral rolloff  

### Method
```python
df_sorted_f0 = df.sort_values(by="f0_mean", ascending=False)
df_sorted_centroid = df.sort_values(by="spectral_centroid_mean", ascending=False)
df_sorted_bandwidth = df.sort_values(by="spectral_bandwidth_mean", ascending=False)
df_sorted_rolloff = df.sort_values(by="spectral_rolloff_mean", ascending=False)
```

### Output
- `outputs/feature_inspection.json`

### Why this step is useful
- detect outliers  
- understand acoustic differences  
- prepare machine learning analysis  
- interpret PCA and clustering  

---

## Step 5 – Run the project

### Feature extraction
```bash
python src/crowd_analysis.py
```

### Visualization
```bash
python src/visualization.py
```

### Check outputs
```bash
ls outputs/
ls figures/
```

---

## Conclusion

This project allows:
- extraction of acoustic features  
- statistical comparison between groups  
- visualization of dataset structure  
- testing class separability  
- exploration of acoustic variability  
































