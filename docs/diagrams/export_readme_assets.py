#!/usr/bin/env python3
"""Export README diagram assets from Draw.io sources.

Primary workflow:
1. Edit `.drawio` files in draw.io (diagrams.net) or VS Code Draw.io extension
2. Run this script to refresh `.svg` and `.png` for the README

If draw.io desktop CLI is installed:
  drawio -x -f png -s 2 -o 01-product-overview.png 01-product-overview.drawio

Otherwise this script renders bundled `.svg` files to PNG via cairosvg.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

WIDTH = 1840
STEMS = (
    "01-product-overview",
    "02-fable-loop",
    "03-skill-architecture",
    "04-before-after",
)


def export_png_from_svg(root: Path) -> None:
    try:
        import cairosvg  # type: ignore
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cairosvg"])
        import cairosvg  # type: ignore

    for stem in STEMS:
        svg = root / f"{stem}.svg"
        png = root / f"{stem}.png"
        if not svg.exists():
            print(f"Skip (missing SVG): {svg.name}")
            continue
        cairosvg.svg2png(url=str(svg), write_to=str(png), output_width=WIDTH)
        print(f"✓ {png.name}")


def main() -> int:
    root = Path(__file__).resolve().parent
    export_png_from_svg(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
