import os
import shutil
import sys
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    src = Path(__file__).resolve().parent / "food.png"
    if not src.is_file():
        print(f"error: source image not found: {src}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        print(
            f"error: output size mismatch: {dst.stat().st_size} != {src.stat().st_size}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
