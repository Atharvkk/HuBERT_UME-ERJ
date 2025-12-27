import pickle

pkl_path = r"Z:\FluentifyAI\CodeBase\Final_Data\Japanese_female_composite.pkl"

with open(pkl_path, "rb") as f:
    baseline = pickle.load(f)

print(baseline.keys())
print(baseline["t"])
