import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os
import unicodedata


ROOT_OUTPUT = 'Final research data'
BASE_SOURCE_PATH = r'Z:\FluentifyAI\CodeBase\Final_Data\\'

def get_cat_dir(cat_name):
    path = os.path.join(ROOT_OUTPUT, cat_name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def normalize_phoneme(p):
    if not isinstance(p, str): return str(p)
    nfd_form = unicodedata.normalize('NFD', p)
    return "".join([c for c in nfd_form if not unicodedata.combining(c)]).strip()

def load_pkl(filename):
    path = os.path.join(BASE_SOURCE_PATH, filename)
    with open(path, 'rb') as f:
        return pickle.load(f)

def analyze_pair(jp_data, us_data):
    jp_norm_map = {normalize_phoneme(k): k for k in jp_data.keys()}
    us_norm_map = {normalize_phoneme(k): k for k in us_data.keys()}
    common_keys = [k for k in (set(jp_norm_map.keys()) & set(us_norm_map.keys())) if k not in {'spn', 'sil', ''}]
    
    drift, stability = [], []
    for k in common_keys:
        j_k, u_k = jp_norm_map[k], us_norm_map[k]
        d = np.linalg.norm(jp_data[j_k]['mu_global'] - us_data[u_k]['mu_global'])
        drift.append({'Phoneme': k, 'Drift': d})
        
        ratio = np.mean(jp_data[j_k]['std_global']) / (np.mean(us_data[u_k]['std_global']) + 1e-9)
        stability.append({'Phoneme': k, 'Ratio': ratio})

    return pd.DataFrame(drift).sort_values('Drift', ascending=False), \
           pd.DataFrame(stability).sort_values('Ratio', ascending=False)

def export_results(df_d, df_s, title, folder_name, filename):
    target_dir = get_cat_dir(folder_name)
    
    txt_path = os.path.join(target_dir, f"{filename}.txt")
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(f"TEST CATEGORY: {title}\nDATE: {datetime.datetime.now()}\n" + "="*50 + "\n")
        f.write(f"MEAN GLOBAL DRIFT: {df_d['Drift'].mean():.6f}\n")
        f.write(f"MEAN STABILITY RATIO: {df_s['Ratio'].mean():.6f}\n\n")
        f.write(df_d.to_string(index=False))

    plt.figure(figsize=(10, 5))
    import seaborn as sns
    sns.barplot(data=df_d.head(12), x='Phoneme', y='Drift', palette='viridis')
    plt.title(f"Phonetic Drift: {title}")
    plt.savefig(os.path.join(target_dir, f"{filename}_plot.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    print("Initializing Full Research Suite on RTX 4070...")
    
    jf = load_pkl('Japanese_female_composite.pkl')
    af = load_pkl('American_female_composite.pkl')
    d1, s1 = analyze_pair(jf, af)
    export_results(d1, s1, "Japanese Female vs Am Female", "Category_1_Female", "Female_Comparison")

    jm = load_pkl('Japanese_male_composite.pkl')
    am = load_pkl('American_male_composite.pkl')
    d2, s2 = analyze_pair(jm, am)
    export_results(d2, s2, "Jp Male vs Am Male", "Category_2_Male", "Male_Comparison")

    cat3_dir = get_cat_dir("Category_3_Sex_Comparison")
    with open(os.path.join(cat3_dir, "Sex_Comparison_Summary.txt"), 'w') as f:
        f.write("COMPARISON OF DEVIATION BY SEX\n" + "="*30 + "\n")
        f.write(f"Male Avg Drift: {d2['Drift'].mean():.6f}\n")
        f.write(f"Female Avg Drift: {d1['Drift'].mean():.6f}\n")
        diff = d2['Drift'].mean() - d1['Drift'].mean()
        f.write(f"Difference (Male - Female): {diff:.6f}\n")
        f.write("Positive value indicates males deviate more from baseline.")

    j_all = load_pkl('Japanese_composite.pkl')
    a_all = load_pkl('American_composite.pkl')
    d4, s4 = analyze_pair(j_all, a_all)
    export_results(d4, s4, "Global Aggregate Composite", "Category_4_Aggregate", "Global_Aggregate")

    print(f"\nAll tests complete. Check the subfolders in '{ROOT_OUTPUT}'.")