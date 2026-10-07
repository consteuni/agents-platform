# Coding Agent Kit

> Historical source-kit document retained for reference. For current development guidance, use [Coding Harness](../coding-harness/SKILL.md). Do not copy this repository's completed tasks or evidence into a target project.


This directory records the earlier project-oriented kit and its usage. For new work, use the Coding Harness skill linked above; its guidance requires no executable helper or project dependency.

## Getting Started

```text
Read harness/HARNESS_RULES.md and follow its rules.
Project: [name and goal].
Technologies: [user choices]. Constraints: [requirements].
Initialize the documents in harness/ for this project without inheriting
the kit's state, tasks, or checks. Ask me for blocking choices.
Prepare the plan before writing code. Do not change branches or perform
Git write operations without my specific request.
```

Not every agent automatically reads files inside an arbitrary directory. Use the explicit reading prompt, or add a project-level AGENTS.md entry point linking to harness/HARNESS_RULES.md. That entry point is not a dependency of the kit.

## Document Types

```text
harness/
|-- HARNESS_RULES.md
|-- HARNESS_GUIDE.md
|-- PROJECT_STATE.md
|-- state.json
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
|   |-- VERIFICATION.md
|   +-- KNOWN_FAILURES.md
|-- tools/ (legacy utilities outside the current skill)
```

The root files are entry points and current state. instructions/ holds operating context; project/ holds project definition, architecture, and decisions; planning/ holds plans and tasks; verification/ holds evidence and known failures; tools/ holds optional helpers. The former setup copied this directory; new projects should use the current skill and clean templates.

## Where to Look

- [state.json](state.json): minimal machine-readable status, current task, and next action.
- [PROJECT_STATE.md](PROJECT_STATE.md): compact human-readable context and handoff.
- [planning/TASKS.md](planning/TASKS.md): the requirement and files the agent is changing.
- [verification/VERIFICATION.md](verification/VERIFICATION.md): checks actually performed and their limitations.
- [project/ARCHITECTURE.md](project/ARCHITECTURE.md): where behavior lives in the code.
- [project/PROJECT_BRIEF.md](project/PROJECT_BRIEF.md): what to build and the chosen stack.
- [planning/PLAN.md](planning/PLAN.md) and [project/DECISIONS.md](project/DECISIONS.md): the plan and rationale.
- [HARNESS_RULES.md](HARNESS_RULES.md) and [instructions/AGENT_CONTEXT.md](instructions/AGENT_CONTEXT.md): rules and context.

Send `CHECKPOINT` to update both state files with current facts and an executable next action, not to create a commit. State is updated at checkpoints, not in real time; Git shows the actual changes. Validate structure, state, tasks, links, and basic safety with available tools.

## Language-Independent Validation

Using the tools already available, check that required paths exist, `state.json` is valid and agrees with `PROJECT_STATE.md`, task IDs and statuses are consistent, verified tasks have evidence, local links resolve inside the kit, and no obvious secrets or absolute local links are present. Record the exact actions and results in `verification/VERIFICATION.md`.

## Design Limits

Keep the kit lightweight, copyable, and language-independent. Avoid mandatory language runtimes, databases, agent-specific SDKs, workflow DAGs, layered configuration systems, custom runtimes, and complex plugin architectures.

## Branch Protection

The kit prohibits unauthorized Git operations but cannot technically block them. For effective protection, configure remote branch rules and editor/tool permissions and approvals. Remote protections do not prevent all destructive local operations. Do not enable unrestricted execution of agent commands.
