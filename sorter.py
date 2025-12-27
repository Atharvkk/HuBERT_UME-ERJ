import os
import shutil

src = r"Z:\FluentifyAI\CodeBase\Phoneme_Normalize\AE\FEMALE\textgrid"
dst = r"Z:\FluentifyAI\CodeBase\Phoneme_Normalize\AE\MALE\textgrid"

os.makedirs(dst, exist_ok=True)

for filename in os.listdir(src):
    if 'M0' in filename:
        shutil.move(os.path.join(src, filename), os.path.join(dst, filename))