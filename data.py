import pickle
import numpy as np

US_PKL = r'Z:\FluentifyAI\CodeBase\Final_Data\American_male_composite.pkl'

with open(US_PKL, 'rb') as f:
    data = pickle.load(f)

print(f"{'Phoneme':<10} | {'Mu Shape':<15} | {'Std Mean Value':<15}")
print("-" * 45)
for ph in list(data.keys())[:10]:
    mu_val = data[ph]['mu_global'].mean()
    std_val = data[ph]['std_global'].mean()
    print(f"{ph:<10} | {str(data[ph]['mu_global'].shape):<15} | {std_val:<15.6f}")