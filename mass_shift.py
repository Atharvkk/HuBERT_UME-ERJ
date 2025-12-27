import os
import shutil

src_root = r"Z:\FluentifyAI\dataset\UME-ERJ_3\wav\AE"
dst_root = r"Z:\FluentifyAI\CodeBase\Alignment\audio"

os.makedirs(dst_root, exist_ok=True)

for root, dirs, files in os.walk(src_root):
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dst_root, file)
        shutil.copy2(src_file, dst_file) 
