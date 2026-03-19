# Scope and Boundaries

## In Scope

- All work described in `project_input/PROJECT_REQUEST.md`
- Creating and updating artifacts inside the project directory
- Building deliverables (code, documentation, tests) as specified
- Managing the agent_org/ pipeline artifacts

## Out of Scope

- Changes not related to the project request
- Accessing external services without explicit permission
- Decisions that require human judgment on business direction

## Write Scope

The agent organization may write to:
- `agent_org/` — all pipeline artifacts
- Project source directories as defined in the project request
- `project_input/DISCOVERY_LOG.md` — for clarification questions

The agent organization must NOT write to:
- Files outside the project directory
- System configuration files
- Other users' projects or shared infrastructure
