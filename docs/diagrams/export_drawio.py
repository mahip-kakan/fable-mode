#!/usr/bin/env python3
"""Export .drawio files to PNG and SVG using the diagrams.net export service."""

from __future__ import annotations

import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

EXPORT_URL = "https://exp-pdf.draw.io/ImageExport4/export"
FORMATS = ("png", "svg")


def export_diagram(drawio_path: Path, fmt: str, scale: float = 2.0) -> bytes:
    xml = drawio_path.read_text(encoding="utf-8")
    data = urllib.parse.urlencode(
        {
            "format": fmt,
            "xml": xml,
            "bg": "#ffffff",
            "scale": str(scale),
            "border": "10",
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        EXPORT_URL,
        data=data,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        body = resp.read()
    if not body or body[:20].startswith(b"Error"):
        raise RuntimeError(f"Export failed for {drawio_path.name}: {body[:200]!r}")
    return body


def main() -> int:
    root = Path(__file__).resolve().parent
    drawio_files = sorted(root.glob("*.drawio"))
    if not drawio_files:
        print("No .drawio files found.", file=sys.stderr)
        return 1

    for drawio in drawio_files:
        stem = drawio.stem
        for fmt in FORMATS:
            out = root / f"{stem}.{fmt}"
            print(f"Exporting {drawio.name} → {out.name} ...", flush=True)
            try:
                content = export_diagram(drawio, fmt)
                out.write_bytes(content)
                print(f"  ✓ {out.name} ({len(content):,} bytes)")
            except (urllib.error.URLError, RuntimeError) as exc:
                print(f"  ✗ {out.name}: {exc}", file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
