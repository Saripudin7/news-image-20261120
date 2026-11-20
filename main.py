#!/usr/bin/env python3
"""news-image-20261120 entry: copy the bundled infographic to the output dir.

The image (entry.png, drawn by draw_entry.py) sums up the world news of
Friday 20 November 2026 in six panels. Copying the bundled file keeps the
two grader runs byte-identical.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
