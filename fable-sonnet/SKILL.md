---
name: fable-sonnet
description: >
  Run Fable Mode discipline on a Sonnet subagent — stage plan, proof-backed
  verification, delivery review. Use when the user wants fable mode on Sonnet
  ("fable sonnet", "fable mode sonnet", "systematic on sonnet"). Requires
  Agent/Task tooling. Skip trivial single-pass tasks. For host model use fable-mode;
  for cost-sensitive runs use fable-haiku. Master loop: fable-mode/SKILL.md.
---

# Fable Mode — Sonnet

Run Fable Mode on a **Sonnet** subagent. Same discipline as `fable-mode`; balanced
cost vs quality.

**Master skill:** `fable-mode/SKILL.md` — canonical loop, Proof Blocks, domain
patterns, and operational rules. This variant adds **how to spawn Sonnet** and the
**full instructions to pass the subagent** (inlined below).

Skip for trivial single-pass work.

## How to run (host agent)

1. Confirm Agent / Task tooling exists. If not, run `fable-mode` inline.
2. Spawn `subagent_type: "generalPurpose"` with the best available Sonnet model slug.
3. Brief the subagent with:
   - The user's task
   - Output paths and session context
   - The **Subagent loop** section below (full text — do not summarize)
   - Domain patterns and operational rules below
4. Relay results; surface any `UNVERIFIED` proofs.
5. Append the **Fable Mode summary** footer.

**Parallel fan-out:** independent parts may run as parallel Sonnet agents (cap ~4).
One delegation level only.

---

## Subagent loop (pass this in full to the Sonnet subagent)

You are the delegated worker. Follow the same Fable loop as `fable-mode`.

### When to skip

Skip when: one obvious fix under ~15 minutes, user wants speed only, or no failable
proof exists. Say you are skipping in one line and proceed.

### 1 — Stage map (before any edits)

```
Stage 1: [Name] → [Verifiable output]
Stage 2: [Name] → [Verifiable output]
Done when: [testable criteria]
```

- Each stage produces something checkable; merge non-verifiable stages
- Update the map when facts invalidate the plan
- Multi-session: maintain `FABLE_LOG.md`

### 2 — Sequential execution

Run stages in order. No nested subagents unless the parent authorized it.

### 3 — Proof check (evidence-backed)

Every stage ends with a **Proof Block**:

```
Proof N — [Stage name]: PASS | FAIL | UNVERIFIED
Check: [test, grep, query, file read, diff]
Command: [exact command or tool call]
Evidence: [exit code, assertion, line count, URL, diff hunk]
```

**Acceptable:** test exit codes, grep/diff output, sources read, data row counts.

**Not acceptable:** "looks correct", "should pass", undocumented claims.

Mark `UNVERIFIED` when no failable check exists. Re-run prior proofs when a fix
invalidates earlier stages.

### 4 — Delivery review

- Skeptical read; fix or flag real issues only
- Confirm before flagging — never report unverified problems
- Escalate to `fable-mode` on host Opus if beyond Sonnet capability after two failed proofs

---

## Domain proof patterns (pass to subagent)

| Domain | Proof check |
|--------|-------------|
| **Software** | Tests run; error paths covered |
| **Research** | Claims cite sources actually read |
| **Data** | Null/duplicate profile before aggregates |
| **Multi-session** | Work log re-read; testable done criteria |

### Software engineering

- Read full relevant context before writing
- Tests alongside implementation; exercise error paths
- Large changes: plan diff first, then execute

### Research / knowledge work

- Gather sources before synthesizing
- Label `[Official Docs]`, `[Third-party]`, `[Community consensus]`, `[Inference]`
- Proof: every load-bearing claim traced to a source read

### Data analysis

- Profile data shape; state hypothesis before computing
- Null/duplicate/outlier checks before aggregates

### Long-running / multi-session

- Work log with decisions and stage status table
- Re-read log at start of every continuation

---

## Operational rules (pass to subagent)

**Warning budget.** At **3** minor concerns, stop and report together.

**Replace safety.** Word-boundary sed; grep for corruption after bulk replace.

**Escalation.** Two failed proofs → recommend stronger model or human review.

---

## Completion report

```
Fable Mode summary
Stages: [count]
Proofs: [PASS] pass · [FAIL→fixed] fixed · [UNVERIFIED] unverified
Delegation: Sonnet subagent
Open risks: [none | list]
```

---

## Limits

- Procedure only — does not exceed Sonnet's reasoning ceiling
- Proof Blocks are honor-system unless the runtime enforces tool use
- Skip on trivial tasks
