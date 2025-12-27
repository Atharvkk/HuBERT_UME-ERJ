import os
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

src = os.path.join(ROOT_DIR, "CodeBase", "Phoneme_Normalize", "AE", "FEMALE", "textgrid")
dst = os.path.join(ROOT_DIR, "CodeBase", "Phoneme_Normalize", "AE", "MALE", "textgrid")

os.makedirs(dst, exist_ok=True)

for filename in os.listdir(src):
    if 'M0' in filename:
        shutil.move(os.path.join(src, filename), os.path.join(dst, filename))