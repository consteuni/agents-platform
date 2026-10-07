# Coding Harness

A documentation-only skill that guides an agent in developing maintainable code using the project's existing stack and tools.

The reusable skill is in [coding-harness/SKILL.md](coding-harness/SKILL.md). Its entry point stays short; engineering and workflow references are loaded when relevant. It includes clean optional templates for project continuity and no executable helpers or required dependencies.

## Use

Give the agent this instruction, or use [PROJECT_START_PROMPT.md](PROJECT_START_PROMPT.md):

> Read coding-harness/SKILL.md and use its workflow for this task. Follow this project's instructions and existing stack. Keep changes focused, verify the result, and report actual checks and limitations.

Make the `coding-harness/` folder available to the agent or add its SKILL.md to the skill loader supported by your environment. This repository contains the skill source; it does not install or activate itself.

| Resource | Purpose |
| --- | --- |
| [SKILL.md](coding-harness/SKILL.md) | Entry point, scope, minimal workflow, and reference routing |
| [ENGINEERING.md](coding-harness/references/ENGINEERING.md) | Proportionate design and quality requirements |
| [WORKFLOW.md](coding-harness/references/WORKFLOW.md) | Nontrivial work, verification, checkpoints, and safety |
| [PROJECT_STATE.md template](coding-harness/assets/templates/PROJECT_STATE.md) | Clean target-project checkpoint |
| [PROJECT_RECORD.md template](coding-harness/assets/templates/PROJECT_RECORD.md) | Optional brief, plan, decisions, and evidence |

Keep target-project state outside the reusable skill. Reuse the project's conventions, or use `agent-state/` when ongoing work needs a state location. Small changes and read-only reviews require no new planning documents.

Source-repository maintenance facts stay in [REPOSITORY_STATE.md](REPOSITORY_STATE.md) and must not be copied into target projects. Earlier source-kit documents remain in `harness/` for reference and migration; they are not part of the reusable skill. Earlier versions also remain in repository history.

Instructions do not enforce access controls. Configure actual repository protections and tool permissions for the environment.
