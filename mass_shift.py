import os
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

src_root = os.path.join(ROOT_DIR, "dataset", "UME-ERJ_3", "wav", "AE")
dst_root = os.path.join(ROOT_DIR, "CodeBase", "Alignment", "audio")

os.makedirs(dst_root, exist_ok=True)

for root, dirs, files in os.walk(src_root):
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dst_root, file)
        shutil.copy2(src_file, dst_file)
