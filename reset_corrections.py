# python reset_corrections.py

from pathlib import Path
import re


# ROOT = Path(r"docs\T2_Programmation") pour cibler un dossier spécifique
ROOT = Path(r"docs")  # pour cibler tous les fichiers du dossier docs et de ses sous-dossiers

# Match uniquement correction(True, avec espaces variables
pattern = re.compile(r"(correction\s*\(\s*)True(\s*,)", re.IGNORECASE)

for file in ROOT.rglob("*.md"):
    text = file.read_text(encoding="utf-8")

    new_text = pattern.sub(r"\1False\2", text)

    if new_text != text:
        # print(f"Would update {file}") pour lister les fichiers modifiés sans les modifier réellement
        # ou
        # les deux lignes suivantes pour modifier réellement les fichiers
        file.write_text(new_text, encoding="utf-8")
        print(f"Updated: {file}") # print(f"Would update {file}") pour lister les fichiers modifiés sans les modifier réellement