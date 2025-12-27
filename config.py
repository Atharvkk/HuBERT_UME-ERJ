import os

# Configuration file for the project
# This file defines paths relative to the repository root.

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directories
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")
CODEBASE_DIR = os.path.join(ROOT_DIR, "CodeBase")

# Specific paths used in scripts
PHONEME_DATA_DIR = os.path.join(CODEBASE_DIR, "Phoneme_Data", "ALL", "ALL")
PHONEME_NORMALIZE_DIR = os.path.join(CODEBASE_DIR, "Phoneme_Normalize", "AE")
FINAL_DATA_DIR = os.path.join(CODEBASE_DIR, "Final_Data")
MFA_READY_DIR = os.path.join(CODEBASE_DIR, "MFA Ready", "American", "All")
ALIGNMENT_DIR = os.path.join(CODEBASE_DIR, "Alignment", "audio")
RESEARCH_OUTPUT_DIR = os.path.join(ROOT_DIR, "Final research data")

# UME-ERJ dataset paths
UME_ERJ_WAV_DIR = os.path.join(DATASET_DIR, "UME-ERJ_3", "wav")
UME_ERJ_AE_DIR = os.path.join(UME_ERJ_WAV_DIR, "AE")

# Example usage:
# from config import PHONEME_DATA_DIR
# wav_dir = os.path.join(PHONEME_DATA_DIR, "WAV")