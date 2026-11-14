"""food-picture-01 entry: write the held food image to /output/entry.png.

Deterministic, stdlib only, no network, no randomness, no model calls.
The image is held in the repository as food.png; this program copies it
byte-identically, so two runs produce identical output.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "food.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"


def main():
    if not SRC.is_file():
        print(f"missing source image: {SRC}", file=sys.stderr)
        raise SystemExit(1)
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    if DST.stat().st_size != SRC.stat().st_size:
        print("output size mismatch after copy", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
