#Measuring Phoneme-Level Pronunciation Deviations in Japanese Learners of English Using Self-Supervised Speech Representations [cite: 1]

[cite_start]By **Atharv Kulkarni** (Lead Researcher | System Architect), India International School in Japan[cite: 2].

## 📄 Overview
[cite_start]This research addresses the "shyness" or "fear" of mispronunciation that limits English proficiency in Japan[cite: 4, 10]. [cite_start]By using **Self-Supervised Speech Representations (SSSR)**, this study provides the first attempt to quantify specific phoneme-level deviations in Japanese-English (JE) speakers against an American English (AE) baseline[cite: 6].

## 🛠️ Methodology & Pipeline
[cite_start]The evaluation pipeline integrates a bifurcated workflow to identify phonetic drift[cite: 119]:

* [cite_start]**Data Alignment**: Utilizes the **Montreal Forced Aligner (MFA)** to identify phonemes and temporal boundaries in `.wav` files[cite: 75, 76].
* [cite_start]**Feature Extraction**: Leverages **Layer 9 of HuBERT** to extract 768-dimensional latent feature encodings[cite: 18, 78, 80].
* [cite_start]**Distance Metrics**: Quantifies pronunciation deviations using **Cosine Distance** and **Euclidean Distance**[cite: 87, 100].

### Mathematical Framework
[cite_start]The **Cosine Distance** between vectors $a$ and $b$ is defined as[cite: 90, 91]:
$$d_{cos}(a, b) = 1 - \frac{a \cdot b}{\|a\| \|b\|}$$

[cite_start]The **Euclidean Distance** is given by[cite: 101]:
$$d_{eud}(a,b)=\sqrt{\sum_{i=1}^{n}(a_{i}-b_{i})^{2}}$$

---

## 📊 Dataset Specifications
[cite_start]The study utilizes the **UME-ERJ corpus**[cite: 19]:
* [cite_start]**Non-Native Samples**: 69,888 usable data files from 202 Japanese volunteers[cite: 19].
* [cite_start]**Native Baseline**: 17,055 samples from 20 American English speakers[cite: 20].

---

## 📈 Key Findings


### 1. High-Deviation Phonemes ($Drift \ge 3.0$)
[cite_start]The study identified several phonemes with significant phonetic drift from the baseline[cite: 268]:
* [cite_start]**Alveolar flap /r/**: Exhibited the highest deviation across all cohorts (Global mean: 6.1016)[cite: 282, 301].
* [cite_start]**/gʷ/** (4.9375)[cite: 254].
* [cite_start]**/m/** (4.2461)[cite: 254].

### 2. Sex-Based Analysis
[cite_start]While male speakers generally showed lower average deviation across most phonemes, a few highly divergent phonemes (notably /r/) skewed their global drift metric higher than the female cohort[cite: 126, 303].

| Metric | Value |
| :--- | :--- |
| Japanese Male Average Drift | [cite_start]2.2363 [cite: 246] |
| Japanese Female Average Drift | [cite_start]2.0625 [cite: 246] |
| **Difference (Male - Female)** | [cite_start]**0.1738** [cite: 246] |

 Technical Setup
* [cite_start]**Primary Hardware**: Intel i-9 13900HX, RTX 4070 Mobile GPU (CUDA acceleration), 32GB DDR5 RAM[cite: 104].
* [cite_start]**Software Stack**: Python (Seaborn, Matplotlib, SciPy, Numpy)[cite: 86, 105].
* [cite_start]**Processing Speed**: HuBERT encoding performed at approximately 16.67 items per second[cite: 108].

## 📂 Availability & Licensing
* [cite_start]**Weights**: Final `.pkl` weights are included in tise repository[cite: 309].
* [cite_start]**License**: Standard **LGPL-2.1**[cite: 309].

