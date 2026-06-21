---
name: fable-haiku
description: >
  Run Fable Mode discipline on a Haiku subagent — stage plan, proof-backed
  verification, delivery review. Use for high-volume or cost-sensitive work
  ("fable haiku", "fable on haiku", "cheap fable mode"). Requires Agent/Task
  tooling. Skip tasks needing deep synthesis — use fable-mode or fable-sonnet.
  The full master loop lives in fable-mode/SKILL.md; this file adds Haiku
  orchestration and the complete subagent instructions to pass downstream.
---

# Fable Mode — Haiku

Run Fable Mode on a **Haiku** subagent. Same discipline as `fable-mode`; lower cost,
not peak synthesis.

**Master skill:** `fable-mode/SKILL.md` — canonical loop, Proof Blocks, domain
patterns, and operational rules. This variant adds **how to spawn Haiku** and the
**full instructions to pass the subagent** (inlined below so the subagent never runs
without context).

Skip for trivial single-pass work or tasks needing top-tier reasoning.

## How to run (host agent)

1. Confirm Agent / Task tooling exists. If not, run `fable-mode` inline on the host model.
2. Spawn `subagent_type: "generalPurpose"` with the best available Haiku model slug.
3. Brief the subagent with:
   - The user's task
   - Output paths and session context
   - The **Subagent loop** section below (full text — do not summarize)
   - Domain patterns and operational rules below
4. When the subagent returns, relay results and surface any `UNVERIFIED` proofs.
5. Append the **Fable Mode summary** footer (see Completion report).

**Parallel fan-out:** for independent sub-parts, spawn multiple Haiku agents (cap ~6).
One delegation level only — subagents run sequentially inside their scope and do not
nest further subagents unless you explicitly authorize it.

---

## Subagent loop (pass this in full to the Haiku subagent)

You are the delegated worker. Follow the same Fable loop as `fable-mode`.

### When to skip

Skip Fable Mode when: one obvious fix under ~15 minutes, user wants speed only, or no
failable proof exists. Say you are skipping in one line and proceed.

### 1 — Stage map (before any edits)

Write numbered stages with expected outputs **before** touching anything.

```
Stage 1: [Name] → [Verifiable output]
Stage 2: [Name] → [Verifiable output]
Done when: [testable criteria]
```

- Each stage produces something checkable; merge stages that only produce vibes
- Update the map when new facts invalidate the plan
- Multi-session work: maintain a work log (`FABLE_LOG.md`)

### 2 — Sequential execution (you are the worker)

Run your stages in order. **Do not spawn nested subagents** unless the parent
explicitly authorized a second level.

### 3 — Proof check (must be evidence-backed)

Every stage ends with a **Proof Block**. No evidence → mark `UNVERIFIED`.

```
Proof N — [Stage name]: PASS | FAIL | UNVERIFIED
Check: [test, grep, query, file read, diff]
Command: [exact command or tool call]
Evidence: [exit code, assertion, line count, URL, diff hunk]
```

**Acceptable:** test exit codes, grep output, sources actually read, data row counts.

**Not acceptable:** "looks correct", "should pass", "the docs say" without citation.

If a stage has no failable check, mark `UNVERIFIED` and explain. When stage N
invalidates stage M, re-run M's proof before continuing.

The cost of catching an error at stage 3 is trivial; at stage 8 it is catastrophic.

### 4 — Delivery review

- Read output as a skeptical reviewer
- Fix or flag real weaknesses only — do not invent problems for ceremony
- Confirm any issue with grep, diff, run, or read before flagging
- Step 3 is the check that can fail; step 4 is judgment after proofs pass

Before flagging any problem — verify it actually exists. Absence of evidence is not
the finding. Confirm, then flag.

When a task is genuinely beyond Haiku's capability, flag it and recommend escalating
to `fable-sonnet` or `fable-mode` — do not ship plausible wrong output.

---

## Domain proof patterns (pass to subagent)

| Domain | Proof check |
|--------|-------------|
| **Software** | Tests run; error paths covered, not just happy path |
| **Research** | Load-bearing claims cite a source actually read; label inference vs fact |
| **Data** | Null/duplicate/outlier profile before aggregates |
| **Multi-session** | Work log re-read at start; done criteria are testable |

### Software engineering

- Read the entire relevant codebase section before writing a line
- Write tests before (or alongside) implementation, not after
- For large changes: plan the diff, then execute it
- Proof check: tests run; error paths exercised

### Research / knowledge work

- Gather sources before synthesizing; do not write as you search
- For each claim: what's the evidence? what would falsify it?
- Proof check: every load-bearing claim traces to a source actually read

### Data analysis

- Understand data shape before analysis; state hypothesis before computing
- Check nulls, duplicates, outliers first
- Proof check: data quality assertions run against actual data

### Long-running / multi-session tasks

- Maintain a work log; re-read it before any continuation
- Define done criteria upfront
- Proof check: done criteria are testable, not vibes

---

## Operational rules (pass to subagent)

**Warning budget.** At **3** minor concerns, stop and surface them together.

**Replace safety.** Use word boundaries in sed (`\bterm\b`); grep for corruption after
bulk replace.

**Escalation.** After two failed proof attempts, stop and recommend `fable-sonnet`,
`fable-mode`, or human review.

---

## Completion report

End every run with:

```
Fable Mode summary
Stages: [count]
Proofs: [PASS] pass · [FAIL→fixed] fixed · [UNVERIFIED] unverified
Delegation: Haiku subagent
Open risks: [none | list]
```

---

## Limits

- Does not raise Haiku's reasoning ceiling — structure only
- Does not self-enforce — Proof Blocks require real commands and evidence
- Adds latency; skip on trivial tasks
