import pickle

pkl_path = r"Z:\FluentifyAI\CodeBase\Final_Data\Japanese_female_composite.pkl"

with open(pkl_path, "rb") as f:
    baseline = pickle.load(f)

# `baseline` is now a dictionary keyed by phonemes
# Each entry has "mu", "std", and "count"
print(baseline.keys())       # list all phonemes
print(baseline["t"])         # example: mean vector, std, count for phoneme 't'
