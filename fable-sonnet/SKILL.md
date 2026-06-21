---
name: fable-sonnet
description: >
  Run Fable Mode discipline on a Sonnet subagent — stage plan, proof-backed
  verification, delivery review. Use when the user wants fable mode on Sonnet
  ("fable sonnet", "fable mode sonnet", "systematic on sonnet"). Requires
  Agent/Task tooling. Skip trivial single-pass tasks. For host model use fable-mode;
  for cost-sensitive runs use fable-fast.
---

# Fable Mode — Sonnet

Run Fable Mode on a **Sonnet** subagent. Same loop, balanced cost vs quality.

Skip for trivial single-pass work.

## How to run

1. Confirm Agent / Task tooling exists. If not, run `fable-mode` inline.
2. Spawn `subagent_type: "generalPurpose"` with the best available Sonnet model.
3. Pass: user task, output paths, session context, and the **Subagent loop** below.
4. Relay results; surface any `UNVERIFIED` proofs.

Parallel Sonnet agents for independent parts (cap ~4). One delegation level only.

## Subagent loop

**1. Stage map** — numbered stages + done criteria, before edits.

**2. Sequential execution** — no nested subagents unless authorized.

**3. Proof Block per stage:**

```
Proof N — [Stage]: PASS | FAIL | UNVERIFIED
Check / Command / Evidence
```

**4. Delivery review** — real issues only; confirm before flagging.

## Pass to subagent

Domain proofs: software tests, research sourcing, data quality, multi-session work log.

Rules: warning budget (3), replace safety, escalate after two failed proofs.

Return the Fable Mode summary footer.
