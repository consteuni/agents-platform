# Operational Context

## Purpose

This kit is a documentation guide that can be copied into a project. It contains no application or runtime and does not choose technologies. It also applies to projects without AI features.

## Sources and Responsibilities

- [AGENTS.md](../AGENTS.md): operating rules, Git safety, and checkpoints.
- [PROJECT_STATE.md](../PROJECT_STATE.md): the single current state summary.
- [PROJECT_BRIEF.md](../project/PROJECT_BRIEF.md): goal, user-selected technologies, and constraints.
- [PLAN.md](../planning/PLAN.md): intentions, sequence, and work criteria.
- [TASKS.md](../planning/TASKS.md): requirements and affected paths, without duplicating state.
- [VERIFICATION.md](../verification/VERIFICATION.md): actual checks and limitations.
- [ARCHITECTURE.md](../project/ARCHITECTURE.md): where behavior lives in the project's actual files.
- [DECISIONS.md](../project/DECISIONS.md): rationale for choices.

The current request defines scope and may update an earlier requirement. Historical specifications do not become requirements unless the user says so. Report contradictions between documents, code, and tests without inventing requirements or permissions.

## Workflow

Follow the startup procedure in AGENTS.md and resume the next still-valid step. For a new goal, update the project brief and ask only for blocking choices. Prepare a plan before writing code; implement a minimal complete path, validate the change, and save a checkpoint.

Task details and checks remain in their respective documents. State links to them without copying them. Do not create extra files or processes for trivial tasks.

## Safety Limitations

Instructions do not technically block commands or access. Configure branch protections, permissions, and editor/tool approvals in the project. Branch protection safeguards the remote; it does not itself prevent local resets or deletions. The kit cannot guarantee that an agent follows the rules.

Do not send confidential, personal, or health data to unauthorized external services. Do not claim a real integration was validated after testing only a mock.
