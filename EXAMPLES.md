# Fable Mode examples

Worked scenarios showing why Proof Blocks beat "looks correct."

---

## Example 1 — API handler (software proof)

**Task:** Add `/api/usage` returning this month's call count for the authenticated user.

### Without Fable Mode (ships a bug)

```js
export async function GET(req) {
  const user = await getUser(req); // returns null when unauthenticated
  const count = await db.calls.count({ where: { userId: user.id, ... } });
  return Response.json({ count });
}
```

Compiles. Happy path works. **Production:** unauthenticated requests throw 500, not 401.

### With Fable Mode

**Stage map**

```
Stage 1: Read auth + schema → confirm getUser returns null, not throw
Stage 2: Implement handler → JSON count for authed user
Stage 3: Tests → authed 200, unauthed 401, invalid token 401
Done when: all tests pass
```

**Proof 3 — Error path tests**

```
Proof 3 — Error path tests: FAIL → fix → PASS
Check: unauthenticated request returns 401
Command: node --test handler.test.js
Evidence: exit 1 — TypeError on user.id; after null guard, exit 0 — 3/3 pass
```

Fix applied:

```js
const user = await getUser(req);
if (!user) return new Response("Unauthorized", { status: 401 });
```

**Lesson:** Self-review said "looks fine." The proof check failed. That is the difference.

---

## Example 2 — Research attribution (research proof)

**Task:** Summarize PostgreSQL connection pooling best practices.

### Without Fable Mode

> PostgreSQL documentation recommends PgBouncer for production with 100+ connections.
> Each connection uses ~10 MB RAM.

Reads authoritative. **Wrong:** official docs do not recommend PgBouncer by name; 10 MB is a community estimate.

### With Fable Mode

**Proof 2 — Source verification**

```
Proof 2 — Official docs claim: FAIL
Check: search postgresql.org/docs for "PgBouncer"
Evidence: no official recommendation of a specific pooler

Proof 2 — Memory figure: UNVERIFIED → relabeled [Community estimate]
```

**Lesson:** The stage map did not catch bad attribution. The source proof did.

---

## Example 3 — SQL averages (data proof)

**Task:** Average response time per region from API logs.

### Without Fable Mode

```sql
SELECT region, AVG(response_time_ms) FROM api_logs GROUP BY region;
```

**Hidden:** 23% of US-East rows have NULL `response_time_ms`. AVG silently drops them.

### With Fable Mode

```
Proof 1 — Null rate by region: FAIL threshold
Evidence: us-east null_pct = 23.1% — exceeds 20% reporting threshold
```

Report null rate alongside average or define an explicit NULL policy.

---

## Example 4 — Multi-session refactor (continuity proof)

**Work log (session 1 end)**

```
Completed: stages 1–2 (interface + email)
Decision: retry is stage 5, not per-channel
Open: SMS SDK choice pending
```

**Session 2:** re-read log → resume stage 3.

```
Proof 5 — SMS retry test: FAIL
Evidence: retry handler only registered for email channel
```

Caught before ship.

---

## Work log template

Save as `FABLE_LOG.md` for multi-session tasks:

```markdown
# Fable Mode work log

## Done criteria
- [ ] ...

## Decisions
- YYYY-MM-DD: ...

## Stage status
| Stage | Proof | Notes |
|-------|-------|-------|
| 1 | PASS | ... |

## Open
- ...
```

---

## Completion report example

```
Fable Mode summary
Stages: 5 completed
Proofs: 4 pass · 1 fixed · 0 unverified
Delegation: 2 parallel subagents
Open risks: none
```
