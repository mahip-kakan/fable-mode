---
name: fable-fast
description: >
  Alias for fable-haiku — Run Fable Mode on a fast/cheap subagent (Haiku-class).
  Prefer invoking fable-haiku by name. Same loop as fable-mode/SKILL.md. Use for
  high-volume structured work ("fable fast", "cheap fable mode"). Requires
  Agent/Task tooling.
---

# Fable Mode — Fast

> **Note:** `fable-fast` is an alias for **`fable-haiku`**. Both names load the same
> discipline. Prefer `fable-haiku` for clarity. Full instructions: `fable-haiku/SKILL.md`.

This file exists for backward compatibility. Read and follow **`fable-haiku/SKILL.md`**
in full — it contains the complete subagent loop, domain patterns, and operational rules
from the master `fable-mode/SKILL.md`.

## Quick reference (host agent)

1. Confirm Agent / Task tooling exists.
2. Spawn Haiku-class subagent with `subagent_type: "generalPurpose"`.
3. Pass the user task, paths, context, and the **entire Subagent loop** from
   `fable-haiku/SKILL.md` — do not summarize.
4. Relay results; surface `UNVERIFIED` proofs.
5. Append Fable Mode summary footer.

See `fable-haiku/SKILL.md` for the complete loop.
