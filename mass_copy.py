import os
import shutil

source_folder = r"Z:\FluentifyAI\CodeBase\MFA Ready\American\All"
je_base = r"Z:\FluentifyAI\dataset\UME-ERJ_3\wav"

# List all UNI folders under JE
uni_folders = [os.path.join(je_base, d) for d in os.listdir(je_base)
               if os.path.isdir(os.path.join(je_base, d))]

for uni in uni_folders:
    # List all F0X folders under UNI
    f0x_folders = [os.path.join(uni, d) for d in os.listdir(uni)
                   if os.path.isdir(os.path.join(uni, d))]
    
    for target in f0x_folders:
        for root, dirs, files in os.walk(source_folder):
            rel_path = os.path.relpath(root, source_folder)  # maintain subfolder structure from ALL
            dst_root = os.path.join(target, rel_path)
            os.makedirs(dst_root, exist_ok=True)
            
            for file in files:
                shutil.copy2(os.path.join(root, file), os.path.join(dst_root, file))
        print(f"Copied contents to {target}")
print("Mass copy operation completed.")