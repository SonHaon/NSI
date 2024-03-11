import os
from pathlib import Path

files = os.listdir(Path(__file__).parent / "images")
liste=[f"images/{img}" for img in files]
print(liste)