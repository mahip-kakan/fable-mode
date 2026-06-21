# Fable Mode — Product Diagrams

Clean block diagrams for the GitHub README and product storytelling.

## Files

| Asset | Description |
|-------|-------------|
| `01-product-overview` | PM hero — problem → Fable loop → outcome |
| `02-fable-loop` | Four-step loop + Proof Block evidence artifact |
| `03-skill-architecture` | Master skill + Sonnet / Haiku / Fast variants |
| `04-before-after` | One-shot vs Fable Mode measured outcome |

Each diagram is available as:

- **`.drawio`** — editable in [draw.io / diagrams.net](https://app.diagrams.net)
- **`.svg`** — crisp vector for docs and web
- **`.png`** — embedded in README

## Edit workflow

1. Open a `.drawio` file in [diagrams.net](https://app.diagrams.net) or the Draw.io VS Code extension
2. Adjust layout, copy, or colors (see `_palette.txt` for the design tokens)
3. Export or sync the matching `.svg` if you change structure significantly
4. Regenerate PNGs for the README:

```bash
cd docs/diagrams
python3 export_readme_assets.py
```

### Optional: draw.io desktop CLI

If [draw.io desktop](https://github.com/jgraph/drawio-desktop/releases) is installed:

```bash
drawio -x -f png -s 2 -o 01-product-overview.png 01-product-overview.drawio
```

Or use the online export helper (requires network):

```bash
python3 export_drawio.py
```

## Design intent

1. **Clean block layout** — rounded rectangles, clear hierarchy, minimal noise
2. **Consistent palette** — indigo (primary), green (success), red (problem), purple (proof)
3. **Multi-zoom** — hero overview + architecture + tactical loop + before/after proof
