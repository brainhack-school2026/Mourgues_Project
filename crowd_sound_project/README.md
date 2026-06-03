# Crowd Sound Project

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/brainhack-school2026/Mourgues_Project/main?urlpath=%2Fdoc%2Ftree%2Fcrowd_sound_project%2Fnotebooks%2F03_interactive.ipynb)

## Dataset Description

- **Name:** Crowd Sound Project
- **Version:** 1.0.0
- **Authors:** Oceane Mourgues
- **License:** MIT
- **DOI:** N/A


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
├── myst.yml                        # Jupyter Book configuration
├── environment.yml
│
├── data/
│   └── sounds/
│       ├── A1.wav ... A26.wav      # Group A (26 files)
│       └── J1.wav ... J26.wav      # Group J (26 files)
│
├── notebooks/
│   ├── 01_extraction.ipynb         # Feature extraction
│   ├── 02_visualization.ipynb      # Visualization and analysis
│   └── 03_interactive.ipynb        # Interactive visualizations, UMAP, │
│
├── src/
│   ├── crowd_analysis.py
│   └── visualization.py
│
├── figures/
│   ├── boxplots_by_group.png
│   ├── pca_mfcc_individual.png
│   └── kmeans_mfcc.png
│
└── outputs/
    ├── A1/results.json ... 
    └── feature_inspection.json

```

This structure is designed to support reproducibility, organization, and open science practices throughout the project development process.

## Presentation link

 Click here to view the slides: https://docs.google.com/presentation/d/1v9t9jJARwTjZ2fG6t1Csj8lXJtg4WSRqbLEC1cxJR6A/edit?usp=sharing 

## Site link 

Site : https://brainhack-school2026.github.io/Mourgues_Project/



# Procedure


## Step 1 – Audio Feature Extraction

Notebook: \`notebooks/01_extraction.ipynb\`

**File:** `src/crowd_analysis.py`

### Objective
Extract acoustic features from each `.wav` audio file using `librosa`.

### Extracted Features

- duration  
- global intensity (RMS)  
- fundamental frequency (F0)  
- spectral centroid  
- spectral bandwidth  
- spectral rolloff  
- MFCC (13 coefficients)  

**Output**
Each audio file generates a JSON file in `outputs/<sound_name>/results.json`.

### Step 2 – Visualization and Analysis

Notebook: `notebooks/02_visualization.ipynb`
File: `src/visualization.py`

**Objective**
Compare audio signals between groups (A vs J) and analyze their acoustic structure.

**2.1 Feature Inspection**
Ranks sounds by each feature (highest/lowest F0, centroid, bandwidth, rolloff).
Output saved to `outputs/feature_inspection.json`.

**2.2 Boxplots**
- F0 (pitch)
- Spectral centroid (brightness / noise differences)

**2.3 PCA (dimensionality reduction)**
Reduces MFCC features from 13D → 2D using `PCA(n_components=2)`.
- `pca_mfcc_individual.png` → individual labeled points

**2.4 K-Means clustering**
Checks if the algorithm can recover groups without labels (k=2).
- `kmeans_mfcc.png`

### Step 3 – Interactive Exploration

Notebook: `notebooks/03_interactive.ipynb`

**Objective**
Explore sounds interactively with Plotly and ipywidgets.

**Features**
- PCA and UMAP projections with toggle selector (group filter)
- Click any point → play the corresponding audio
- Waveform + spectrogram display per sound (Plotly)
- Acoustic parameters table per sound
- Free feature scatter plot (X/Y dropdowns) with audio playback on click

**Statistical comparison (Group A vs J)**
- Boxplots for all features (F0, RMS, centroid, bandwidth, rolloff, duration)
- Mann-Whitney U tests with p-values

**Key results**
- F0 mean: p=0.0001 *** — Group J significantly higher pitch (300 Hz vs 204 Hz)
- Spectral centroid: p=0.047 * — Group J slightly brighter
- Other features: no significant difference

### Step 4 – Feature Interpretation

| Feature | High value | Low value |
|---|---|---|
| F0 | High-pitched sounds | Low-pitched sounds |
| Spectral centroid | Noisy / mixed sounds | Stable / pure sounds |
| PCA separation | Distinct classes | Acoustic similarity |
| K-Means clusters | Good separability | High variability |


## Step 5 – Run the project

```bash
jupyter nbconvert --to notebook --execute notebooks/01_extraction.ipynb --inplace
jupyter nbconvert --to notebook --execute notebooks/02_visualization.ipynb --inplace
jupyter nbconvert --to notebook --execute notebooks/03_interactive.ipynb --inplace
```

Or run the original scripts directly:

```bash
python src/crowd_analysis.py
python src/visualization.py
```
## Conclusion

This project allows:
- extraction of acoustic features from 52 crowd sound stimuli
- statistical comparison between groups A and J (Mann-Whitney U tests)
- visualization of dataset structure via PCA, UMAP, and K-Means
- interactive exploration with audio playback, waveform, and spectrogram
- testing class separability
- exploration of acoustic variability































