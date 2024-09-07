import os
from pathlib import Path

files = [
    'requirements.txt',
    'setup.py',
    'README.md',
    'src/__init__.py',
    'src/main.py',
    'app.py',
    '.env',
    'Notebook_Experiments/Trials.ipynb'
]

for filepath in files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filedir.mkdir(parents=True, exist_ok=True)
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()