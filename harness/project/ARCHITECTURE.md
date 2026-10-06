# Project Map

## Current Kit Structure

Language-independent harness documentation plus one optional Python 3 reference validator: no application modules, APIs, required language runtime, or runtime contracts. Supporting documents are grouped by type; entry points and current state stay at the kit root.

| File | Responsibility |
| --- | --- |
| [HARNESS_GUIDE.md](../HARNESS_GUIDE.md) | Copying and using the kit |
| [HARNESS_RULES.md](../HARNESS_RULES.md) | Rules and operational safety |
| [instructions/AGENT_CONTEXT.md](../instructions/AGENT_CONTEXT.md) | Context and workflow |
| [PROJECT_BRIEF.md](PROJECT_BRIEF.md) | Project goals, stack, and constraints |
| [state.json](../state.json) | Minimal machine-readable operational state |
| [PROJECT_STATE.md](../PROJECT_STATE.md) | Human-readable current context and resume instructions |
| [planning/PLAN.md](../planning/PLAN.md) | Planned steps and criteria |
| [planning/TASKS.md](../planning/TASKS.md) | Requirements and affected files |
| [verification/VERIFICATION.md](../verification/VERIFICATION.md) | Evidence from checks |
| [verification/KNOWN_FAILURES.md](../verification/KNOWN_FAILURES.md) | Pre-existing failures separated from regressions |
| [tools/check.py](../tools/check.py) | Optional reference validator; not a project requirement |
| [DECISIONS.md](DECISIONS.md) | Choices and rationale |

## In a Derived Project

Replace this map with actual modules: paths, responsibilities, entry points, contracts, and significant dependencies. Show where each behavior lives by linking existing files and symbols. Do not copy the entire tree or invent modules before technologies are chosen.

Update only when responsibilities, structure, or contracts change. Operational state remains in kit-root `state.json` with a human-readable mirror in `PROJECT_STATE.md`.
