# Role Map

Core roles in the agent organization:

## Roles

- **product-lead:** Converts demand/requests into product briefs with clear success criteria.
- **engineering-manager:** Converts product briefs into engineering specs, task graphs, and work orders.
- **implementation-agent:** Executes work orders — writes code, creates files, builds deliverables.
- **review-agent:** Verifies outputs against specs, logs integration results.
- **learning-agent:** Records gaps, failures, and improvement proposals.

## Artifact Ownership

| Role | Primary Artifacts |
|------|-------------------|
| product-lead | Product briefs |
| engineering-manager | Engineering specs, task graphs |
| implementation-agent | Work orders, code, deliverables |
| review-agent | Evaluation traces, integration log |
| learning-agent | Improvement backlog, pattern library |

## How Roles Work

In a single-agent runtime (e.g., one Claude Code session), all roles are played by the same agent sequentially. The role structure ensures each phase of work gets proper attention rather than jumping straight to coding.

In a multi-agent setup, roles can be distributed across parallel agents.
