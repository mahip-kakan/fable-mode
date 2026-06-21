# Fable Mode — Product Diagrams

Visual assets for the GitHub README and product storytelling.

## Files

| Asset | Description |
|-------|-------------|
| `01-product-overview` | PM hero — problem → Fable loop → outcome |
| `02-fable-loop` | Four-step loop + Proof Block evidence artifact |
| `03-skill-architecture` | Master skill + Sonnet / Haiku / Fast variants |
| `04-before-after` | One-shot vs Fable Mode measured outcome |

Each diagram is available as:

- **`.excalidraw`** — editable in [Excalidraw](https://excalidraw.com)
- **`.svg`** — crisp vector source
- **`.png`** — embedded in README

## Regenerate

```bash
cd docs/diagrams
python3 generate_diagrams.py          # .excalidraw sources
python3 -m venv .venv && .venv/bin/pip install cairosvg
.venv/bin/python export_readme_assets.py  # .svg + .png
```

## Design intent (PM lens)

1. **Argue visually** — structure mirrors meaning (loop, fan-out, before/after)
2. **Evidence artifacts** — Proof Block shows real command output, not vibes
3. **Multi-zoom** — hero overview + architecture + tactical loop detail
