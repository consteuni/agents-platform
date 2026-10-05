# Plan

## Goal and Assumptions

Keep the categorized documentation kit and its root entry points, removing obsolete material outside the kit. No default language, framework, or provider. The user supplies technology choices after copying the kit. All documentation must remain in English.

## Architecture

Keep AGENTS.md, README.md, and PROJECT_STATE.md at the kit root for quick access. Group operating context under instructions/, project definition and architecture under project/, plans and tasks under planning/, and check evidence under verification/. All links must resolve within the kit. No runtime or automation.

## Kit Tasks

1. Delete the obsolete, domain-specific orchestrator specification and remove its active README link.
2. Remove the verified-empty legacy docs/ directory with a nonrecursive operation; preserve the ten kit documents and root entry points.
3. Record TASK-004 and the cleanup rationale without treating earlier verification records as current requirements.
4. Check surviving links, Markdown, file counts, and diffs; save the checkpoint without Git write operations.

## Completion Criteria

- The kit is self-contained: no document in harness/ requires external files.
- State, affected files, and checks are visible; PROJECT_STATE stays within approximately 100 lines.
- No imposed technologies, dependencies, or application code.
- The agent distinguishes authorized file edits from Git operations that change branches, history, or publication.
- No dangerous commands or branch changes are performed to build the kit.
- Documentation is in English; no obsolete domain-specific specification or empty legacy docs/ directory remains.
- All ten kit documents are preserved exactly once; entry points remain at the kit root.
- Diagnostics, links, and diffs are checked; unverified limitations are disclosed.

## In a Derived Project

Replace this plan with the project's plan before writing code: scope, minimal architecture, assumptions, affected files, at most five steps, risks, and verifiable criteria. Do not inherit completed tasks or evidence from the kit.
