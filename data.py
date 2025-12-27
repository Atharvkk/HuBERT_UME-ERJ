import pickle
import numpy as np
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

US_PKL = os.path.join(ROOT_DIR, "CodeBase", "Final_Data", "American_male_composite.pkl")

with open(US_PKL, 'rb') as f:
    data = pickle.load(f)

print(f"{'Phoneme':<10} | {'Mu Shape':<15} | {'Std Mean Value':<15}")
print("-" * 45)
for ph in list(data.keys())[:10]:
    mu_val = data[ph]['mu_global'].mean()
    std_val = data[ph]['std_global'].mean()
    print(f"{ph:<10} | {str(data[ph]['mu_global'].shape):<15} | {std_val:<15.6f}")