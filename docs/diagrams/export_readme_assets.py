#!/usr/bin/env python3
"""Export Fable Mode README diagram assets as SVG (+ PNG when rsvg/cairosvg available)."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

OUT = Path(__file__).parent

# Brand palette
P = {
    "indigo": "#4f46e5",
    "indigo_light": "#eef2ff",
    "purple": "#7c3aed",
    "purple_light": "#ede9fe",
    "green": "#059669",
    "green_light": "#d1fae5",
    "red": "#dc2626",
    "red_light": "#fee2e2",
    "amber": "#d97706",
    "amber_light": "#fef3c7",
    "orange": "#c2410c",
    "orange_light": "#ffedd5",
    "slate": "#64748b",
    "title": "#312e81",
    "code_bg": "#0f172a",
    "code_text": "#34d399",
    "white": "#ffffff",
}


def svg_header(w: int, h: int) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#312e8120"/>
    </filter>
    <linearGradient id="heroGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{P['indigo_light']}"/>
      <stop offset="100%" stop-color="{P['purple_light']}"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="{P['white']}"/>'''


def box(x, y, w, h, fill, stroke, label, fs=14, rx=12) -> str:
    lines = label.split("\n")
    ty = y + h / 2 - (len(lines) - 1) * 8
    text = "".join(
        f'<text x="{x + w/2}" y="{ty + i*18}" text-anchor="middle" font-family="Inter,Segoe UI,sans-serif" font-size="{fs}" fill="{P["title"]}">{ln}</text>'
        for i, ln in enumerate(lines)
    )
    return f'''
  <g filter="url(#shadow)">
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>
    {text}
  </g>'''


def arrow(x1, y1, x2, y2, color=P["indigo"]) -> str:
    return f'''
  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2.5" marker-end="url(#arrowhead)"/>
  <defs><marker id="arrowhead" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{color}"/></marker></defs>'''


def label(x, y, text, size=24, color=P["title"], weight="700") -> str:
    return f'<text x="{x}" y="{y}" font-family="Inter,Segoe UI,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{text}</text>'


def sublabel(x, y, text, size=15, color=P["slate"]) -> str:
    return f'<text x="{x}" y="{y}" font-family="Inter,Segoe UI,sans-serif" font-size="{size}" fill="{color}">{text}</text>'


def code_panel(x, y, w, h, lines: list[str]) -> str:
    body = "\n".join(
        f'<tspan x="{x+16}" dy="{20 if i else 24}">{line}</tspan>' for i, line in enumerate(lines)
    )
    return f'''
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{P['code_bg']}"/>
  <text font-family="Menlo,Monaco,monospace" font-size="13" fill="{P['code_text']}">
    <tspan x="{x+16}" y="{y+24}">{lines[0]}</tspan>
    {''.join(f'<tspan x="{x+16}" dy="18">{ln}</tspan>' for ln in lines[1:])}
  </text>'''


def hero_banner() -> str:
    w, h = 920, 640
    s = svg_header(w, h)
    s += label(40, 48, "Fable Mode", 32)
    s += sublabel(40, 78, "Plan in chapters. Prove each scene before the next.", 18, P["indigo"])
    s += f'<rect x="40" y="100" width="840" height="4" rx="2" fill="url(#heroGrad)"/>'

    s += sublabel(40, 130, "THE PROBLEM — procedure failures, not intelligence failures", 13, P["red"])
    s += box(40, 145, 250, 72, P["red_light"], P["red"], "Happy-path code\n500s in production")
    s += box(310, 145, 250, 72, P["red_light"], P["red"], "Research from\nmemory, not sources")
    s += box(580, 145, 250, 72, P["red_light"], P["red"], "Session 2 loses\nthe thread")

    s += arrow(460, 230, 460, 265)
    s += box(280, 275, 360, 52, P["indigo_light"], P["indigo"], "Fable Mode = staged discipline + Proof Blocks", 15)

    s += sublabel(40, 360, "THE FABLE LOOP", 13, P["indigo"])
    s += box(40, 378, 190, 68, P["orange_light"], P["orange"], "1  Stage map")
    s += box(250, 378, 190, 68, P["indigo_light"], P["indigo"], "2  Delegate")
    s += box(460, 378, 190, 68, P["green_light"], P["green"], "3  Proof check")
    s += box(670, 378, 190, 68, P["purple_light"], P["purple"], "4  Review")
    s += arrow(230, 412, 250, 412)
    s += arrow(440, 412, 460, 412)
    s += arrow(650, 412, 670, 412)

    s += arrow(460, 456, 460, 490)
    s += box(300, 500, 320, 58, P["green_light"], P["green"], "Deliver with evidence + summary footer", 14)

    s += sublabel(40, 590, "Built for: Engineering  ·  AI power users  ·  Research  ·  Data  ·  PMs", 13, P["slate"])
    s += "</svg>"
    return s


def fable_loop() -> str:
    w, h = 920, 520
    s = svg_header(w, h)
    s += label(40, 42, "The Fable Loop", 28)
    s += sublabel(40, 70, "Every stage ends with a Proof Block that can fail", 16, P["indigo"])

    stages = [
        (40, "Stage map", "Plan before edits", P["orange_light"], P["orange"]),
        (250, "Delegate", "Parallel when independent", P["indigo_light"], P["indigo"]),
        (460, "Proof check", "PASS · FAIL · UNVERIFIED", P["green_light"], P["green"]),
        (670, "Review", "Real issues only", P["purple_light"], P["purple"]),
    ]
    for x, name, desc, fill, stroke in stages:
        s += box(x, 110, 190, 64, fill, stroke, name, 15)
        s += sublabel(x + 10, 195, desc, 13)
    s += arrow(230, 142, 250, 142)
    s += arrow(440, 142, 460, 142)
    s += arrow(650, 142, 670, 142)

    s += sublabel(40, 240, "Evidence artifact (from EXAMPLES.md)", 14, P["green"])
    s += code_panel(40, 258, 840, 120, [
        "Proof 3 — Error path tests: FAIL → fix → PASS",
        "Check: unauthenticated request returns 401",
        "Command: node --test handler.test.js",
        "Evidence: exit 0 — 3/3 pass",
    ])

    s += box(40, 410, 130, 44, P["green_light"], P["green"], "PASS", 14)
    s += box(190, 410, 150, 44, P["red_light"], P["red"], "FAIL → fix", 14)
    s += box(360, 410, 160, 44, P["amber_light"], P["amber"], "UNVERIFIED", 14)
    s += sublabel(40, 480, "Completion: Fable Mode summary — stages · proofs · delegation · risks", 14, P["indigo"])
    s += "</svg>"
    return s


def architecture() -> str:
    w, h = 920, 560
    s = svg_header(w, h)
    s += label(40, 42, "Skill Architecture", 28)
    s += sublabel(40, 70, "Master skill + model-pinned variants (full loop inlined)", 16, P["indigo"])

    s += box(390, 100, 140, 50, P["orange_light"], P["orange"], "User task", 14)
    s += box(40, 190, 170, 54, P["indigo_light"], P["indigo"], "Skill loader", 14)
    s += box(240, 190, 170, 54, P["purple_light"], P["purple"], "Host agent", 14)
    s += box(460, 180, 220, 74, P["green_light"], P["green"], "fable-mode/SKILL.md\nMASTER", 14)
    s += arrow(460, 125, 400, 190)
    s += arrow(210, 217, 240, 217)
    s += arrow(410, 217, 460, 217)

    s += sublabel(40, 290, "Variants — pass complete loop to subagent", 13, P["slate"])
    s += box(40, 310, 250, 62, P["indigo_light"], P["indigo"], "fable-sonnet", 15)
    s += box(310, 310, 250, 62, P["indigo_light"], P["indigo"], "fable-haiku", 15)
    s += box(580, 310, 250, 62, P["amber_light"], P["amber"], "fable-fast (alias)", 15)
    for ax in (165, 435, 705):
        s += arrow(570, 254, ax, 310, P["slate"])

    s += box(290, 430, 340, 58, P["green_light"], P["green"], "Output + Proof Blocks + summary", 14)
    s += arrow(165, 372, 340, 430)
    s += arrow(435, 372, 400, 430)
    s += arrow(705, 372, 460, 430)

    s += sublabel(40, 520, "Install: cp -R fable-mode/fable-mode ~/.cursor/skills/fable-mode", 13, P["slate"])
    s += "</svg>"
    return s


def before_after() -> str:
    w, h = 920, 420
    s = svg_header(w, h)
    s += label(40, 42, "Before / After", 28)
    s += sublabel(40, 70, "Same task — different procedure", 16, P["indigo"])

    s += sublabel(60, 110, "ONE-SHOT", 15, P["red"])
    s += box(40, 125, 300, 50, P["red_light"], P["red"], "Write handler", 14)
    s += box(40, 190, 300, 50, P["red_light"], P["red"], "Looks correct", 14)
    s += arrow(190, 175, 190, 190, P["red"])
    s += sublabel(40, 270, "Ships → 500 on unauthenticated request", 14, P["red"])

    s += sublabel(440, 110, "FABLE MODE", 15, P["green"])
    s += box(400, 125, 140, 48, P["orange_light"], P["orange"], "Stage map", 13)
    s += box(560, 125, 140, 48, P["indigo_light"], P["indigo"], "Tests first", 13)
    s += box(400, 190, 300, 50, P["amber_light"], P["amber"], "Proof FAIL → null guard", 14)
    s += box(400, 255, 300, 50, P["green_light"], P["green"], "Proof PASS → ship", 14)
    s += arrow(540, 173, 540, 190, P["green"])
    s += arrow(550, 240, 550, 255, P["green"])

    s += box(180, 320, 560, 56, P["indigo_light"], P["indigo"], "Measured: 1 pass / 1 fail  →  3 pass / 0 fail", 15)
    s += "</svg>"
    return s


def write_assets() -> None:
    diagrams = {
        "01-product-overview": hero_banner(),
        "02-fable-loop": fable_loop(),
        "03-skill-architecture": architecture(),
        "04-before-after": before_after(),
    }
    for name, svg in diagrams.items():
        svg_path = OUT / f"{name}.svg"
        svg_path.write_text(svg, encoding="utf-8")
        print(f"Wrote {svg_path}")

        png_path = OUT / f"{name}.png"
        if shutil.which("rsvg-convert"):
            subprocess.run(["rsvg-convert", "-w", "1840", str(svg_path), "-o", str(png_path)], check=True)
            print(f"Wrote {png_path}")
        else:
            try:
                import cairosvg  # type: ignore
                cairosvg.svg2png(bytestring=svg.encode(), write_to=str(png_path), output_width=1840)
                print(f"Wrote {png_path}")
            except Exception:
                print(f"PNG skip for {name} (install rsvg-convert or cairosvg)")


if __name__ == "__main__":
    write_assets()
