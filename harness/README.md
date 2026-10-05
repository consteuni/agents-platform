# Coding Agent Kit

This directory contains the entire kit. Copy harness/ into your project, open the editor, and tell the agent your goal and technology choices. No installation or dependencies.

## Getting Started

```text
Read harness/AGENTS.md and follow its rules.
Project: [name and goal].
Technologies: [user choices]. Constraints: [requirements].
Initialize the documents in harness/ for this project without inheriting
the kit's state, tasks, or checks. Ask me for blocking choices.
Prepare the plan before writing code. Do not change branches or perform
Git write operations without my specific request.
```

Not every agent automatically reads files inside an arbitrary directory. Use the explicit reading prompt, or add a project-level AGENTS.md entry point linking to harness/AGENTS.md. That entry point is not a dependency of the kit.

## Document Types

```text
harness/
|-- AGENTS.md
|-- README.md
|-- PROJECT_STATE.md
|-- instructions/
|   +-- AGENT_CONTEXT.md
|-- project/
|   |-- PROJECT_BRIEF.md
|   |-- ARCHITECTURE.md
|   +-- DECISIONS.md
|-- planning/
|   |-- PLAN.md
|   +-- TASKS.md
|-- verification/
|   +-- VERIFICATION.md
```

The root files are entry points and the current state. instructions/ holds operating context; project/ holds project definition, architecture, and decisions; planning/ holds plans and tasks; verification/ holds check evidence. Copy the whole harness/ directory, not individual categories.

## Where to Look

- [PROJECT_STATE.md](PROJECT_STATE.md): what is done, in progress, or blocked, and the next action.
- [planning/TASKS.md](planning/TASKS.md): the requirement and files the agent is changing.
- [verification/VERIFICATION.md](verification/VERIFICATION.md): checks actually performed and their limitations.
- [project/ARCHITECTURE.md](project/ARCHITECTURE.md): where behavior lives in the code.
- [project/PROJECT_BRIEF.md](project/PROJECT_BRIEF.md): what to build and the chosen stack.
- [planning/PLAN.md](planning/PLAN.md) and [project/DECISIONS.md](project/DECISIONS.md): the plan and rationale.
- [AGENTS.md](AGENTS.md) and [instructions/AGENT_CONTEXT.md](instructions/AGENT_CONTEXT.md): rules and context.

Send `CHECKPOINT` to save state and the next action, not to create a commit. State is updated at checkpoints, not in real time; Git shows the actual changes.

## Branch Protection

The kit prohibits unauthorized Git operations but cannot technically block them. For effective protection, configure remote branch rules and editor/tool permissions and approvals. Remote protections do not prevent all destructive local operations. Do not enable unrestricted execution of agent commands.
