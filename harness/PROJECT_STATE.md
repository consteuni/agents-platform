# Project State

Updated: 2026-10-06 | Branch: main | Worktree dirty: true

## Current Objective

Apply the lightweight v0.2 harness rules: compact machine-readable state, executable validation, explicit verification evidence, and token-efficient operation.

## Current Task

TASK-007

## Status

verified

## Last Completed Task

TASK-007

## Completed

- Baseline verification, explicit task statuses, and operational checkpoints are documented.
- Markdown filenames are unique; kit entry points are `HARNESS_RULES.md` and `HARNESS_GUIDE.md`.
- `state.json` and known-failure tracking are runtime-independent; the Python validator is an optional reference tool.
- Token economy, verification levels, stop conditions, and failure escalation are defined.

## Known Blockers

None.

## Next Action

Copy harness/ and PROJECT_START_PROMPT.md into the target repository and initialize both state files for that project.

## Important Context

- `state.json` is the minimal operational state; this file is the compact human-readable handoff.
- Detailed requirements, decisions, and evidence stay in their canonical documents.
- Token savings must not weaken correctness, safety, or required verification.
- The harness must work without requiring any programming-language runtime; optional tools may accelerate equivalent checks.

## Verification

TASK-007 is verified; validator and documentation regression checks pass. Evidence is in `verification/VERIFICATION.md`.

## Last Checkpoint

2026-10-06T12:14:46+02:00

## Resume

Run `git status --short --branch`, read `state.json`, then execute its `next_action`.
