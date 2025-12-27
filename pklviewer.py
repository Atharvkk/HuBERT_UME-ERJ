import pickle
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pkl_path = os.path.join(ROOT_DIR, "CodeBase", "Final_Data", "Japanese_female_composite.pkl")

with open(pkl_path, "rb") as f:
    baseline = pickle.load(f)

print(baseline.keys())
print(baseline["t"])
