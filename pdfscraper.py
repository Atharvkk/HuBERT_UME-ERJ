import re
from PyPDF2 import PdfReader as pd

full_text = ""

pattern = re.compile(r'[^a-zA-Z0-9_\s.]+')

for x in range(1,9):
    reader = pd(fr"Z:\FluentifyAI\dataset\UME-ERJ_1\doc\JErecord\s{x}_record.pdf")
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            cleaned_text = pattern.sub(' ', page_text) 
            full_text += cleaned_text + "\n"

with open(f"S{x}Compiled.txt", "w", encoding="utf-8") as f:
    f.write(full_text)



Z:\FluentifyAI\CodeBase>git fetch origin
no such identity: C:/Users/USER/.ssh/DEPLOY_KEY_FILENAME: No such file or directory
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
