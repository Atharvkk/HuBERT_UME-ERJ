import os

base_path = r"Z:\FluentifyAI\dataset\UME-ERJ_3\wav"

for root, dirs, files in os.walk(base_path):
    path_parts = os.path.normpath(root).split(os.sep)
    if len(path_parts) < 3:
        continue
    session = path_parts[-2]  
    speaker = path_parts[-1]  
    for file in files:
        name, ext = os.path.splitext(file)
        if ext.lower() not in [".wav", ".txt"]:
            continue
        new_name = f"{name}_{session}_{speaker}{ext}"
        old_path = os.path.join(root, file)
        new_path = os.path.join(root, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {file} -> {new_name}")
