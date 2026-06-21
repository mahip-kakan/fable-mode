#!/usr/bin/env python3
"""Generate Fable Mode Excalidraw diagrams for GitHub README."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).parent

# Fable Mode brand palette (PM: trust + proof + AI)
C = {
    "title": "#312e81",
    "subtitle": "#4f46e5",
    "body": "#64748b",
    "primary_fill": "#eef2ff",
    "primary_stroke": "#4338ca",
    "ai_fill": "#ede9fe",
    "ai_stroke": "#6d28d9",
    "start_fill": "#ffedd5",
    "start_stroke": "#c2410c",
    "success_fill": "#d1fae5",
    "success_stroke": "#047857",
    "fail_fill": "#fee2e2",
    "fail_stroke": "#dc2626",
    "warn_fill": "#fef3c7",
    "warn_stroke": "#b45309",
    "code_bg": "#1e293b",
    "code_text": "#22c55e",
    "line": "#64748b",
    "white": "#ffffff",
}


def _seed(n: int) -> int:
    return 100000 + n


def text(
    id_: str,
    x: float,
    y: float,
    content: str,
    *,
    size: int = 16,
    color: str = C["body"],
    width: float | None = None,
    align: str = "left",
) -> dict:
    w = width or max(120, len(content) * size * 0.55)
    h = size * 1.4
    return {
        "type": "text",
        "id": id_,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "text": content,
        "originalText": content,
        "fontSize": size,
        "fontFamily": 3,
        "textAlign": align,
        "verticalAlign": "top",
        "strokeColor": color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": _seed(hash(id_) % 90000),
        "version": 1,
        "versionNonce": _seed(hash(id_ + "n") % 90000),
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "containerId": None,
        "lineHeight": 1.25,
    }


def rect(
    id_: str,
    x: float,
    y: float,
    w: float,
    h: float,
    label: str,
    *,
    fill: str,
    stroke: str,
    label_color: str = C["title"],
) -> list[dict]:
    tid = f"{id_}_t"
    box = {
        "type": "rectangle",
        "id": id_,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "strokeColor": stroke,
        "backgroundColor": fill,
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": _seed(hash(id_) % 90000),
        "version": 1,
        "versionNonce": _seed(hash(id_ + "v") % 90000),
        "isDeleted": False,
        "groupIds": [],
        "boundElements": [{"id": tid, "type": "text"}],
        "link": None,
        "locked": False,
        "roundness": {"type": 3},
    }
    t = text(tid, x + 12, y + h / 2 - 10, label, size=15, color=label_color, width=w - 24, align="center")
    t["verticalAlign"] = "middle"
    t["containerId"] = id_
    box["boundElements"].append({"id": tid, "type": "text"})
    return [box, t]


def arrow(id_: str, x1: float, y1: float, x2: float, y2: float, *, color: str = C["primary_stroke"]) -> dict:
    return {
        "type": "arrow",
        "id": id_,
        "x": x1,
        "y": y1,
        "width": x2 - x1,
        "height": y2 - y1,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": _seed(hash(id_) % 90000),
        "version": 1,
        "versionNonce": _seed(hash(id_ + "a") % 90000),
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "points": [[0, 0], [x2 - x1, y2 - y1]],
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow",
    }


def code_block(id_: str, x: float, y: float, w: float, h: float, lines: str) -> list[dict]:
    rid = f"{id_}_r"
    tid = f"{id_}_t"
    r = {
        "type": "rectangle",
        "id": rid,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "strokeColor": C["code_bg"],
        "backgroundColor": C["code_bg"],
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": _seed(hash(id_) % 90000),
        "version": 1,
        "versionNonce": _seed(hash(id_ + "c") % 90000),
        "isDeleted": False,
        "groupIds": [],
        "boundElements": [{"id": tid, "type": "text"}],
        "link": None,
        "locked": False,
        "roundness": {"type": 3},
    }
    t = text(tid, x + 10, y + 10, lines, size=13, color=C["code_text"], width=w - 20)
    t["fontFamily"] = 3
    t["containerId"] = rid
    return [r, t]


def save(name: str, elements: list[dict]) -> None:
    data = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {"viewBackgroundColor": "#ffffff", "gridSize": 20},
        "files": {},
    }
    path = OUT / f"{name}.excalidraw"
    path.write_text(json.dumps(data, indent=2))
    print(f"Wrote {path}")


def diagram_product_overview() -> None:
    els: list[dict] = []
    els.append(text("title", 40, 30, "Fable Mode — Product Overview", size=28, color=C["title"]))
    els.append(text("sub", 40, 68, "Turn agent chaos into staged, evidence-backed delivery", size=18, color=C["subtitle"]))

    # Problem lane
    els.append(text("pl", 40, 120, "THE PROBLEM", size=14, color=C["fail_stroke"]))
    els.extend(rect("p1", 40, 145, 200, 70, "Happy-path code\n500s in prod", fill=C["fail_fill"], stroke=C["fail_stroke"]))
    els.extend(rect("p2", 260, 145, 200, 70, "Research from\nmemory", fill=C["fail_fill"], stroke=C["fail_stroke"]))
    els.extend(rect("p3", 480, 145, 200, 70, "Multi-session\ncontext loss", fill=C["fail_fill"], stroke=C["fail_stroke"]))

    els.append(arrow("a1", 340, 230, 340, 270))
    els.append(text("mid", 200, 245, "Fable Mode = procedure, not smarter AI", size=16, color=C["subtitle"], width=280))

    # Solution loop
    els.append(text("sl", 40, 290, "THE FABLE LOOP", size=14, color=C["primary_stroke"]))
    els.extend(rect("s1", 40, 315, 150, 65, "1 Stage map", fill=C["start_fill"], stroke=C["start_stroke"]))
    els.extend(rect("s2", 210, 315, 150, 65, "2 Delegate", fill=C["primary_fill"], stroke=C["primary_stroke"]))
    els.extend(rect("s3", 380, 315, 150, 65, "3 Proof check", fill=C["success_fill"], stroke=C["success_stroke"]))
    els.extend(rect("s4", 550, 315, 150, 65, "4 Review", fill=C["ai_fill"], stroke=C["ai_stroke"]))
    for i in range(3):
        els.append(arrow(f"as{i}", 190 + i * 170, 347, 210 + i * 170, 347))

    # Outcome
    els.append(arrow("a2", 340, 390, 340, 430))
    els.extend(rect("out", 220, 440, 240, 70, "Verifiable output\n+ Fable Mode summary", fill=C["success_fill"], stroke=C["success_stroke"]))

    # Personas
    els.append(text("per", 40, 540, "WHO IT'S FOR", size=14, color=C["primary_stroke"]))
    els.extend(rect("u1", 40, 565, 180, 55, "Engineering leads", fill=C["primary_fill"], stroke=C["primary_stroke"]))
    els.extend(rect("u2", 240, 565, 180, 55, "AI power users", fill=C["ai_fill"], stroke=C["ai_stroke"]))
    els.extend(rect("u3", 440, 565, 180, 55, "Research / data teams", fill=C["primary_fill"], stroke=C["primary_stroke"]))
    els.extend(rect("u4", 640, 565, 120, 55, "PMs shipping\nwith agents", fill=C["warn_fill"], stroke=C["warn_stroke"]))

    save("01-product-overview", els)


def diagram_fable_loop() -> None:
    els: list[dict] = []
    els.append(text("title", 40, 25, "The Fable Loop — Proof at every stage", size=26, color=C["title"]))
    els.append(text("sub", 40, 60, "Each chapter must earn the next", size=16, color=C["body"]))

    y = 110
    stages = [
        ("Stage map", "Numbered plan + done criteria\nBEFORE any edits", C["start_fill"], C["start_stroke"]),
        ("Delegate", "Parallel subagents when\nstages are independent", C["primary_fill"], C["primary_stroke"]),
        ("Proof check", "Proof Block: PASS | FAIL | UNVERIFIED", C["success_fill"], C["success_stroke"]),
        ("Delivery review", "Skeptical read — no fake concerns", C["ai_fill"], C["ai_stroke"]),
    ]
    for i, (name, desc, fill, stroke) in enumerate(stages):
        x = 40 + i * 190
        els.extend(rect(f"st{i}", x, y, 170, 80, name, fill=fill, stroke=stroke))
        els.append(text(f"sd{i}", x, y + 90, desc, size=13, color=C["body"], width=170))
        if i < 3:
            els.append(arrow(f"sa{i}", x + 170, y + 40, x + 190, y + 40))

    # Proof block evidence artifact
    els.append(text("pb_title", 40, 260, "Proof Block (required every stage)", size=18, color=C["success_stroke"]))
    els.extend(
        code_block(
            "pb",
            40,
            290,
            720,
            110,
            "Proof 3 — Error path tests: FAIL → fix → PASS\n"
            "Check: unauthenticated request returns 401\n"
            "Command: node --test handler.test.js\n"
            "Evidence: exit 0 — 3/3 pass",
        )
    )

    # State machine labels
    els.extend(rect("pass", 40, 430, 120, 45, "PASS", fill=C["success_fill"], stroke=C["success_stroke"]))
    els.extend(rect("fail", 180, 430, 120, 45, "FAIL → fix", fill=C["fail_fill"], stroke=C["fail_stroke"]))
    els.extend(rect("unv", 320, 430, 140, 45, "UNVERIFIED", fill=C["warn_fill"], stroke=C["warn_stroke"]))
    els.append(text("foot", 40, 500, "Footer: Fable Mode summary — stages, proofs, delegation, open risks", size=15, color=C["subtitle"], width=700))

    save("02-fable-loop", els)


def diagram_architecture() -> None:
    els: list[dict] = []
    els.append(text("title", 40, 25, "Skill Architecture — Master + Variants", size=26, color=C["title"]))
    els.append(text("sub", 40, 58, "Variants inline the full loop because subagents cannot load sibling skills", size=15, color=C["body"], width=720))

    # User
    els.extend(rect("user", 320, 100, 140, 50, "User task", fill=C["start_fill"], stroke=C["start_stroke"]))

    # Runtime
    els.append(text("rt", 40, 180, "Cursor / Claude Code", size=14, color=C["subtitle"]))
    els.extend(rect("loader", 40, 200, 160, 55, "Skill loader", fill=C["primary_fill"], stroke=C["primary_stroke"]))
    els.extend(rect("host", 240, 200, 160, 55, "Host agent", fill=C["ai_fill"], stroke=C["ai_stroke"]))
    els.append(arrow("au", 380, 125, 320, 200, color=C["line"]))
    els.append(arrow("lh", 200, 227, 240, 227))

    # Master
    els.extend(rect("master", 440, 190, 200, 70, "fable-mode/SKILL.md\nMASTER", fill=C["success_fill"], stroke=C["success_stroke"]))
    els.append(arrow("hm", 400, 227, 440, 227))

    # Variants row
    els.append(text("var", 40, 310, "Model-pinned variants", size=14, color=C["subtitle"]))
    variants = [
        ("fable-sonnet", "Sonnet subagent"),
        ("fable-haiku", "Haiku subagent"),
        ("fable-fast", "alias → haiku"),
    ]
    for i, (name, desc) in enumerate(variants):
        x = 40 + i * 250
        els.extend(rect(f"v{i}", x, 335, 220, 65, name, fill=C["primary_fill"], stroke=C["primary_stroke"]))
        els.append(text(f"vd{i}", x, 408, desc, size=13, color=C["body"], width=220))
        els.append(arrow(f"hv{i}", 540, 260, x + 110, 335, color=C["line"]))

    # Output
    els.extend(rect("out", 260, 480, 280, 60, "Output + Proof Blocks + summary", fill=C["success_fill"], stroke=C["success_stroke"]))
    els.append(arrow("vo0", 150, 400, 300, 480))
    els.append(arrow("vo1", 400, 400, 350, 480))
    els.append(arrow("vo2", 650, 400, 400, 480))

    save("03-skill-architecture", els)


def diagram_before_after() -> None:
    els: list[dict] = []
    els.append(text("title", 40, 25, "Before / After — Why Proof Blocks matter", size=26, color=C["title"]))

    # Before column
    els.append(text("bhead", 60, 80, "ONE-SHOT AGENT", size=16, color=C["fail_stroke"]))
    els.extend(rect("b1", 40, 110, 300, 55, "Write handler", fill=C["fail_fill"], stroke=C["fail_stroke"]))
    els.extend(rect("b2", 40, 180, 300, 55, "Looks correct ✓", fill=C["fail_fill"], stroke=C["fail_stroke"]))
    els.append(arrow("ba1", 190, 165, 190, 180))
    els.append(text("b3", 40, 250, "Ships → 500 on unauth", size=15, color=C["fail_stroke"], width=300))

    # After column
    els.append(text("ahead", 420, 80, "FABLE MODE", size=16, color=C["success_stroke"]))
    els.extend(rect("a1", 400, 110, 140, 50, "Stage map", fill=C["start_fill"], stroke=C["start_stroke"]))
    els.extend(rect("a2", 560, 110, 140, 50, "Tests first", fill=C["primary_fill"], stroke=C["primary_stroke"]))
    els.extend(rect("a3", 400, 180, 300, 55, "Proof FAIL → add null guard", fill=C["warn_fill"], stroke=C["warn_stroke"]))
    els.extend(rect("a4", 400, 250, 300, 55, "Proof PASS → ship safely", fill=C["success_fill"], stroke=C["success_stroke"]))
    els.append(arrow("aa1", 540, 160, 540, 180))
    els.append(arrow("aa2", 550, 235, 550, 250))

    # Metric callout
    els.extend(rect("metric", 140, 320, 460, 70, "Test result: 1 pass / 1 fail  →  3 pass / 0 fail", fill=C["primary_fill"], stroke=C["primary_stroke"]))

    save("04-before-after", els)


if __name__ == "__main__":
    diagram_product_overview()
    diagram_fable_loop()
    diagram_architecture()
    diagram_before_after()
    print("Done — 4 diagrams generated")
