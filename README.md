###  Measuring Phoneme-Level Pronunciation Deviations in Japanese Learners of English Using Self-Supervised Speech Representations  

 By **Atharv Kulkarni** (Lead Researcher | System Architect), India International School in Japan .

## Overview
 This research addresses the "shyness" or "fear" of mispronunciation that limits English proficiency in Japan[cite: 4, 10].  By using **Self-Supervised Speech Representations (SSSR)**, this study provides the first attempt to quantify specific phoneme-level deviations in Japanese-English (JE) speakers against an American English (AE) baseline .

## Methodology & Pipeline
 The evaluation pipeline integrates a bifurcated workflow to identify phonetic drift:

*  **Data Alignment**: Utilizes the **Montreal Forced Aligner (MFA)** to identify phonemes and temporal boundaries in `.wav` files.
*  **Feature Extraction**: Leverages **Layer 9 of HuBERT** to extract 768-dimensional latent feature encodings.
*  **Distance Metrics**: Quantifies pronunciation deviations using **Cosine Distance** and **Euclidean Distance**.

### Mathematical Framework
 The **Cosine Distance** between vectors $a$ and $b$ is defined as:
$$d_{cos}(a, b) = 1 - \frac{a \cdot b}{\|a\| \|b\|}$$

 The **Euclidean Distance** is given by:
$$d_{eud}(a,b)=\sqrt{\sum_{i=1}^{n}(a_{i}-b_{i})^{2}}$$

---

## Dataset Specifications
 The study utilizes the **UME-ERJ corpus**:
*  **Non-Native Samples**: 69,888 usable data files from 202 Japanese volunteers.
*  **Native Baseline**: 17,055 samples from 20 American English speakers.

---

## Key Findings


### 1. High-Deviation Phonemes ($Drift \ge 3.0$)
 The study identified several phonemes with significant phonetic drift from the baseline:
*  **Alveolar flap /r/**: Exhibited the highest deviation across all cohorts (Global mean: 6.1016).
*  **/gʷ/** (4.9375).
*  **/m/** (4.2461).

### 2. Sex-Based Analysis
 While male speakers generally showed lower average deviation across most phonemes, a few highly divergent phonemes (notably /r/) skewed their global drift metric higher than the female cohort.

| Metric | Value |
| :--- | :--- |
| Japanese Male Average Drift |  2.2363 |
| Japanese Female Average Drift |  2.0625|
| **Difference (Male - Female)** |  **0.1738**  |

 Technical Setup
*  **Primary Hardware**: Intel i-9 13900HX, RTX 4070 Mobile GPU (CUDA acceleration), 32GB DDR5 RAM.
*  **Software Stack**: Python (Seaborn, Matplotlib, SciPy, Numpy).
*  **Processing Speed**: HuBERT encoding performed at approximately 16.67 items per second.

## Availability & Licensing
*  **Weights**: Final `.pkl` weights are included in tise repository.
*  **License**: Standard **LGPL-2.1**.

