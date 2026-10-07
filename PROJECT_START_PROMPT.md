# Start a New Project

Copy the entire `harness/` directory into the new repository before starting work.

Read [harness/HARNESS_RULES.md](harness/HARNESS_RULES.md) completely and follow its rules. Read [harness/state.json](harness/state.json) first, then [harness/PROJECT_STATE.md](harness/PROJECT_STATE.md) only for the human-readable context you need. Replace the copied kit state, tasks, plan, and verification history with facts about this project. Do not inherit completed work from the kit.

## Project

- Name: `[project name]`
- Goal: `[what the project should do]`
- Audience: `[who will use it]`
- First complete workflow: `[the smallest useful end-to-end result]`

## Technologies

- Language and version: `[choice or to be decided]`
- Frameworks and libraries: `[choices or to be decided]`
- Persistence and external services: `[choices or none]`
- Development environment and execution target: `[local, server, cloud, mobile, etc.]`
- Installation, startup, and validation commands: `[commands or to be defined]`

## Requirements and constraints

- Required behavior: `[requirements]`
- Error cases: `[known cases]`
- Data, privacy, and permissions: `[constraints]`
- Compatibility, performance, and cost constraints: `[constraints]`
- Out of scope: `[explicit exclusions]`

## Working rules

- Do not change branches or perform Git write operations without my specific request.
- Do not choose unspecified technologies without first identifying the choice as blocking.
- Preserve existing user changes and inspect the repository before editing.
- Follow the **Software Engineering Requirements** in [harness/HARNESS_RULES.md](harness/HARNESS_RULES.md): apply SOLID, KISS, DRY, YAGNI, separation of concerns, explicit contracts, testability, reliability, and security in proportion to the project.
- Use the engineering completion criteria during implementation and review; record evidence and significant tradeoffs before declaring the result verified.
- Minimize token usage by default: search before reading, read only relevant ranges, limit tool output, and avoid repeating unchanged context or completed work.
- When model selection is available, use the lightest capable model for routine, well-scoped changes and escalate only when complexity or risk requires it.
- Keep responses and state concise; expand only when uncertainty, risk, or verification requires more context.
- Before changing code, run the smallest relevant baseline check when practical.
- Prepare or update `harness/planning/PLAN.md` before nontrivial implementation.
- Implement the smallest complete path, then run targeted checks and record actual outcomes in `harness/verification/VERIFICATION.md`.
- Mark work `implemented` only when the requested change is complete and `verified` only when the acceptance criteria have evidence.
- End with a compact checkpoint: update both `harness/state.json` and `harness/PROJECT_STATE.md`, keeping their status, current task, and next action consistent.
- Validate harness state and structure with the tools already available in the project. If Python 3 is available, `python3 harness/tools/check.py` is an optional shortcut, not a requirement.

## First actions

1. Inspect the repository and run `git status --short --branch`.
2. Read the project instructions and the copied harness documents.
3. Replace the kit's placeholder project brief and inherited state with the project facts above.
4. Identify blocking technology choices; ask only for choices that cannot be inferred safely.
5. Create the project plan before writing code.
6. Report the baseline, plan, affected files, and next action before implementation.

Start by orienting yourself and updating the harness documents. Do not write application code until the project choices and first workflow are clear.
