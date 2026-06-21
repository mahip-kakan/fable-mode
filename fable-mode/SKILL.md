---
name: fable-mode
description: >
  Fable-style agent discipline for complex work: a written stage plan, parallel
  subagent delegation when tooling allows, a proof-backed verification check at
  each stage, and a skeptical delivery review. Use when the user asks for fable
  mode, systematic execution, deep work, or thorough handling OR when the task
  spans multiple files, sources, or sessions. Skip single-pass trivial tasks.
  For model-pinned runs use fable-sonnet or fable-haiku (alias: fable-fast).
---

# Fable Mode

Complex agent work needs structure the way a fable needs scenes — each one must
**earn the next**. This skill encodes that discipline: plan first, delegate where
it helps, prove each stage with evidence, then review before delivery.

This shapes *procedure*, not intelligence. It is a checklist, not a capability upgrade.

## When to skip

Do **not** use Fable Mode when:

- One file, one obvious fix, under ~15 minutes
- The user wants speed ("quick fix", "just answer")
- No failable check exists and output is purely subjective

Say you are skipping Fable Mode in one line, then proceed directly.

## The Fable loop

### 1 — Stage map (before any edits)

Write numbered stages with expected outputs **before** touching anything.

```
Stage 1: [Name] → [Verifiable output]
Stage 2: [Name] → [Verifiable output]
Done when: [testable criteria]
```

- Each stage produces something checkable; merge stages that only produce vibes
- Update the map when new facts invalidate the plan
- Multi-session work: maintain a work log (see `EXAMPLES.md`)

### 2 — Delegate when independent

| Runtime | Action |
|---------|--------|
| No Agent/Task tooling | Run stages sequentially |
| Subagent tooling available | Parallel agents only for independent stages |

Brief each subagent with: task, deliverable path, context, and this loop. Keep
delegation **one level deep** unless the user allows nesting.

Good: research sources while writing tests. Bad: one function split across three agents.

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

### 4 — Delivery review

- Read output as a skeptical reviewer
- Fix or flag real weaknesses only — do not invent problems for ceremony
- Confirm any issue with grep, diff, run, or read before flagging

## Domain proof patterns

| Domain | Proof check |
|--------|-------------|
| **Software** | Tests run; error paths covered, not just happy path |
| **Research** | Load-bearing claims cite a source actually read |
| **Data** | Null/duplicate profile before aggregates |
| **Multi-session** | Work log re-read; done criteria are testable |

## Operational rules

**Warning budget.** At **3** minor concerns, stop and surface them together.

**Replace safety.** Use word boundaries in sed (`\bterm\b`); grep for corruption after bulk replace.

**Escalation.** After two failed proof attempts, recommend a stronger model or human review.

## Completion report

End every Fable Mode run with:

```
Fable Mode summary
Stages: [count]
Proofs: [PASS] pass · [FAIL→fixed] fixed · [UNVERIFIED] unverified
Delegation: [none | N subagents]
Open risks: [none | list]
```

## Limits

- Does not auto-enforce — proof blocks require the agent to run real commands
- Does not replace CI, review, or human judgment
- Adds latency; skip on trivial tasks
