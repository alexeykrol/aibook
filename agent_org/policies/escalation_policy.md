# Escalation Policy

## Immediate Escalation

Escalate immediately when:
- The request requires actions outside the defined write scope
- Required deliverables cannot be created due to missing information
- A decision will have irreversible high-impact consequences

## Escalation Steps

1. Document the issue in `knowledge/decision_log.md`
2. Add a note in `execution/status_board.md` with status `blocked`
3. Create `project_input/DISCOVERY_LOG.md` with specific questions
4. Pause execution of the blocked work item until guidance arrives

## Bounded Retry Discipline

For transient failures:
- Max retries: 3 attempts
- After 3 failures: mark as `needs_attention` — do not continue retrying
- Preserve partial results from successful work

## Priority of Escalation

| Situation | Action |
|-----------|--------|
| Missing information | Ask via DISCOVERY_LOG.md, continue other work |
| Conflicting requirements | Document conflict, pause affected work item |
| Scope ambiguity | Make a reasonable decision, document rationale |
| Technical blocker | Try alternative approach before escalating |
