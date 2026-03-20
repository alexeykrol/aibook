# Startup Sequence

## Step 0: Check INBOX

Read `agent_org/intake/INBOX.md`. If **Pending Tasks** section contains tasks:
- Process them through the full pipeline (intake → product → engineering → execution → review → report)
- Skip Step 3 fallback to improvement backlog

If INBOX is empty → proceed to Step 3 for demand queue / improvement backlog fallback.

## Core Startup

1. Read `agent_org/charter/mission.md` and `charter/scope_and_boundaries.md`.
2. Read `policies/` for escalation and quality gates.
3. Review `intake/` for active demand signals (demand_queue.md, external_signals.md). Fallback if INBOX empty.
4. Confirm product brief exists in `product/active_product_briefs/`.
5. Confirm engineering spec and task graph exist.
6. Check execution status in `execution/status_board.md`.
7. Review evaluation artifacts and open improvement items.

## Run Lifecycle

Every run MUST follow this sequence:

```
1. STATUS in_progress — update status signal to in_progress with current run id
2. Artifacts          — run work products created/modified
3. Summary            — run summary written
4. Evaluation         — evaluation trace written
5. STATUS completed   — update status signal to completed
```

## ACK Freshness Check

At session start, compare directive_id in the observer directive with the runtime ACK.
If they differ → update the ACK immediately before proceeding.

## Retry Budget Check

Before relaunching under the same directive:
1. Check retry_count against retry_budget (default: 3).
2. If exhausted → set status to `retry_budget_exhausted`, escalate.
3. If within budget → increment counter and proceed.
