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
├── myst.yml                        # Jupyter Book configuration
├── methods.md                      # Methods page
├── results.md                      # Results page
├── environment.yml
│
├── data/
│   └── sounds/
│       ├── A1.wav ... A26.wav      # Group A (26 files)
│       └── J1.wav ... J26.wav      # Group J (26 files)
│
├── notebooks/
│   ├── 01_extraction.ipynb         # Feature extraction
│   └── 02_visualization.ipynb      # Visualization and analysis
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

### Output


Each audio file generates a JSON file:

- outputs/J3/results.json
- outputs/A1/results.json

## Step 2 – Visualization and Analysis

Notebook: \`notebooks/02_visualization.ipynb\`

**File:** `src/visualization.py`

### Objective
Compare audio signals between groups (A vs J) and analyze their acoustic structure.

### Packages used
- seaborn
- pandas
- scikit-learn

### 2.1 Boxplots (statistical comparison)

#### Variables analyzed
- F0 (pitch)
- spectral centroid (brightness / noise differences)

#### Interpretation
- pitch differences between groups  
- spectral richness / noise differences  


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


### 2.3 K-means clustering

#### Objective
Check if the algorithm can recover groups without labels.


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



## Step 4 – Feature Inspection

**File:** `src/visualization.py`

### Objective
Inspect each sound individually using acoustic features.

### Features analyzed
- highest / lowest F0  
- highest / lowest spectral centroid  
- highest / lowest spectral bandwidth  
- highest / lowest spectral rolloff  

### Output
- `outputs/feature_inspection.json`

### Why this step is useful
- detect outliers  
- understand acoustic differences  
- prepare machine learning analysis  
- interpret PCA and clustering  


## Step 5 – Run the project

```bash
jupyter nbconvert --to notebook --execute notebooks/01_extraction.ipynb --inplace
jupyter nbconvert --to notebook --execute notebooks/02_visualization.ipynb --inplace
```


## Conclusion

This project allows:
- extraction of acoustic features  
- statistical comparison between groups  
- visualization of dataset structure  
- testing class separability  
- exploration of acoustic variability  
































