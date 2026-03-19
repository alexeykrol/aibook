# Risk Policy

## Risk Tiers

- **Low:** Routine file creation, code changes within existing patterns
- **Medium:** Structural changes that affect multiple components, new dependencies
- **High:** Irreversible actions, scope changes, external service interactions

## Mitigations

- Low risk: proceed autonomously, document in status board
- Medium risk: document rationale in `knowledge/decision_log.md` before proceeding
- High risk: escalate per `policies/escalation_policy.md`

## Common Risk Patterns

| Pattern | Tier | Mitigation |
|---------|------|------------|
| Adding a new file | Low | None needed |
| Modifying existing logic | Medium | Test before and after |
| Deleting files/data | High | Confirm with project owner |
| Adding external dependencies | Medium | Document in decision log |
| Changing public APIs | High | Document breaking changes |
