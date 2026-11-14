"""food-picture-01 entry: write the held food image to /output/entry.png.

Deterministic, stdlib only, no network, no randomness, no model calls.
The image is held in the repository as food.png; this program copies it
byte-identically, so two runs produce identical output.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "food.png"
DST = Path("/output/entry.png")


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
