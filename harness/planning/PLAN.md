# Plan

## Goal and Assumptions

Make software engineering principles explicit and mandatory for projects using this harness, while preserving the language-independent v0.2 workflow, Git safety, and token economy.

## Architecture

Keep `PROJECT_STATE.md` as the human handoff and `state.json` as the minimal operational state. Keep detailed requirements, history, and evidence in tasks, decisions, known failures, and verification. Agents can validate invariants with available tools; the standard-library validator is optional.

## Kit Tasks

1. Inspect the current rules and run the optional validator as a baseline.
2. Define actionable engineering requirements and completion criteria in HARNESS_RULES.md; reference them from the README and startup prompt.
3. Review the changed documentation, validate links and state, and record TASK-008 evidence and a synchronized checkpoint.
4. Apply the requested documentation update to the connected repository's existing main branch through GitHub, preserving unrelated files and history.

## Completion Criteria

- The kit is self-contained: no document in harness/ requires external files.
- Current state is compact in `PROJECT_STATE.md` and minimal in `state.json`; core fields stay consistent.
- No imposed technologies, dependencies, or application code.
- The agent distinguishes authorized file edits from Git operations that change branches, history, or publication.
- No dangerous commands or branch changes are performed to build the kit.
- Documentation is in English; no obsolete domain-specific specification or empty legacy docs/ directory remains.
- The original ten documents remain, with `state.json`, `KNOWN_FAILURES.md`, and `tools/check.py` added for v0.2 invariants.
- Diagnostics, links, and diffs are checked; unverified limitations are disclosed.
- Baseline, implementation/verification status, and checkpoint rules are documented.
- Every Markdown basename is unique and all renamed-document links resolve.
- Token usage is minimized by default without skipping required context, checks, or safety steps.
- Core validation does not require a language runtime; `tools/check.py` is optional when Python 3 is available.
- TASK-008 explicitly covers SOLID, KISS, DRY, YAGNI, contracts, testability, reliability, security, and maintainability with observable acceptance criteria.
- Engineering requirements have one canonical definition, apply proportionally to the change, and do not prescribe a stack or speculative abstractions.

## In a Derived Project

Replace this plan with the project's plan before writing code: scope, minimal architecture, assumptions, affected files, at most five steps, risks, and verifiable criteria. Do not inherit completed tasks or evidence from the kit.
