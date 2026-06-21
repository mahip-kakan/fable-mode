---
name: fable-fast
description: >
  Run Fable Mode discipline on a fast/cheap subagent (Haiku-class) — stage plan,
  proof-backed verification, delivery review. Use for high-volume structured work
  ("fable fast", "cheap fable mode", "fable on haiku"). Requires Agent/Task
  tooling. Skip tasks needing deep synthesis — use fable-mode or fable-sonnet.
---

# Fable Mode — Fast

Run Fable Mode on a **fast model** subagent. Same checklist, lower cost — not peak synthesis.

Skip trivial tasks and work needing top-tier reasoning.

## How to run

1. Confirm Agent / Task tooling exists. If not, run `fable-mode` inline.
2. Spawn `subagent_type: "generalPurpose"` with the fastest Haiku-class model.
3. Pass task, paths, context, and **Subagent loop** below.
4. Highlight `UNVERIFIED` proofs in the relay.

Parallel fan-out for independent chunks (cap ~6). One delegation level only.

## Subagent loop

**1. Stage map** before edits.

**2. Sequential execution** — no nesting unless authorized.

**3. Proof Block** — PASS / FAIL / UNVERIFIED with command + evidence.

**4. Delivery review** — confirm before flagging.

Escalate to `fable-sonnet` or `fable-mode` if two proofs fail or quality is insufficient.

Return Fable Mode summary footer.
