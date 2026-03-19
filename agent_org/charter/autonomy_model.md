# Autonomy Model

Autonomy level: **controlled autonomy** within project boundaries.

## Allowed Autonomous Actions

- Create and update artifacts inside the project
- Execute work orders (write code, create files, run tests)
- Make routine technical decisions (library choice, code structure, naming)
- Create evaluation and learning artifacts
- Update pipeline status

## Escalation Required

- Decisions that change the project's business direction or scope
- Actions that are irreversible and high-impact (deleting databases, deploying to production)
- Ambiguous requirements where multiple interpretations lead to very different outcomes
- Budget or resource decisions

## Autonomy Constraints

- Follow the pipeline sequence: intake → product → engineering → execution → review
- Record every cross-stage handoff in `execution/handoff_log.md`
- Log decisions in `knowledge/decision_log.md`
- When in doubt, document the decision and rationale rather than escalating
