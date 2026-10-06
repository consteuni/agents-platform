# Plan

## Goal and Assumptions

Apply the lightweight v0.2 rules while keeping the core fully language-independent: compact state, reproducible validation, and permanent token economy without weakening correctness, Git safety, or portability.

## Architecture

Keep `PROJECT_STATE.md` as the human handoff and `state.json` as the minimal operational state. Keep detailed requirements, history, and evidence in tasks, decisions, known failures, and verification. Agents can validate invariants with available tools; the standard-library validator is optional.

## Kit Tasks

1. Add and synchronize compact Markdown and JSON state contracts.
2. Add token economy, verification evidence and levels, blockers, stop conditions, and failure escalation rules.
3. Add known-failure tracking and an optional reference validator for structure, state, tasks, links, and safety.
4. Run equivalent targeted and regression checks with available tools; record actual evidence without Git write operations.

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

## In a Derived Project

Replace this plan with the project's plan before writing code: scope, minimal architecture, assumptions, affected files, at most five steps, risks, and verifiable criteria. Do not inherit completed tasks or evidence from the kit.
