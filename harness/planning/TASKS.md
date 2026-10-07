# Tasks

> Historical source-kit document retained for reference. For current development guidance, use [Coding Harness](../../coding-harness/SKILL.md). Do not copy this repository's completed tasks or evidence into a target project.


Status and next action: [state.json](../state.json) and [PROJECT_STATE.md](../PROJECT_STATE.md). Plan: [PLAN.md](PLAN.md). Evidence: [verification/VERIFICATION.md](../verification/VERIFICATION.md).

## TASK-001 - Single Kit and Git Safety

Status: verified

Requirement: one self-contained directory for the agent, without a default stack, that makes work and checks visible and prohibits unauthorized dangerous Git operations.

### Affected Files

The links below point to the documents' current locations after TASK-003.

- [HARNESS_RULES.md](../HARNESS_RULES.md): restore the earlier harness rules and explicit Git restrictions.
- [instructions/AGENT_CONTEXT.md](../instructions/AGENT_CONTEXT.md) and [project/PROJECT_BRIEF.md](../project/PROJECT_BRIEF.md): distinguish context, technology choices, and permissions.
- [PROJECT_STATE.md](../PROJECT_STATE.md): concise human state and resume instructions.
- [project/ARCHITECTURE.md](../project/ARCHITECTURE.md): document responsibilities.
- [PLAN.md](PLAN.md), [project/DECISIONS.md](../project/DECISIONS.md), and this file: intentions, rationale, and requirement details.
- [verification/VERIFICATION.md](../verification/VERIFICATION.md): kit checks.
- [HARNESS_GUIDE.md](../HARNESS_GUIDE.md): copying and usage.

In the source repository, also update root entry points and consolidate the earlier template documents. Do not modify user files unrelated to the requirement. Translate the historical reference only under TASK-002, not as part of restructuring.

### Acceptance

- All kit references are internal to the directory.
- State stays within approximately 100 lines; each task connects files and checks.
- No imposed technologies and no Git write operations performed to prepare the kit.
- A generic request or CHECKPOINT does not authorize Git operations.
- Checks are recorded with actual outcomes and limitations.

Out of scope: dashboards, hooks, automation, application code, and remote branch protection configuration.

## TASK-002 - English Translation

Status: verified

Requirement: translate all documentation into English. Affected files: every document in this kit, the source repository's root README and AGENTS entry point, and the historical specification outside the kit.

Acceptance: preserve meaning, filenames, links, language independence, Git restrictions, and the optional status of the historical reference. Repeat checks after translation and record them under TASK-002 in verification/VERIFICATION.md.

Out of scope: application implementation, Git writes, external translation services, and technical branch protection configuration.

## TASK-003 - Organize Documents by Type

Status: verified

Requirement: categorize harness documents without splitting the copyable kit or changing operating and Git safety rules.

Affected files: move AGENT_CONTEXT into instructions/; PROJECT_BRIEF, ARCHITECTURE, and DECISIONS into project/; PLAN and TASKS into planning/; VERIFICATION into verification/. Update relative references in every affected document and in the kit-root rules, guide, and PROJECT_STATE documents.

Acceptance: keep exactly ten documents, preserve the root entry points and state, resolve every link inside the kit, and record checks under TASK-003 in verification/VERIFICATION.md. Project choices and Git safety rules must remain unchanged.

Out of scope: new document types, application code, stack choices, changes to the historical specification, and Git write operations.

## TASK-004 - Remove Obsolete Material

Status: verified

Requirement: remove files no longer useful to the reusable, technology-independent harness.

Affected paths: delete the obsolete orchestrator specification outside the kit, remove its link from the source repository README, and remove the verified-empty legacy docs/ directory. Preserve the root README and AGENTS entry point and all ten categorized kit documents.

Acceptance: no broken links, no obsolete source specification or empty legacy directory, and no Git write operations. Earlier task and verification records describe past work and do not require deleted material to remain present.

Out of scope: deleting useful kit documents, changing technologies or safety rules, recursively cleaning directories, or modifying Git history or branches.

## TASK-005 - Verifiable Agent Workflow

Status: verified

Requirement: make the harness distinguish pre-existing failures from regressions, distinguish implementation from verification, and preserve an operational checkpoint format across sessions.

### Affected Files

- [HARNESS_RULES.md](../HARNESS_RULES.md): baseline, status, and checkpoint rules.
- [PROJECT_STATE.md](../PROJECT_STATE.md): current implementation and verification state.
- [PLAN.md](PLAN.md), [project/DECISIONS.md](../project/DECISIONS.md), and this file: scope and rationale.
- [verification/VERIFICATION.md](../verification/VERIFICATION.md): evidence and limitations.

### Acceptance

- The workflow requires a smallest relevant baseline check before code changes when practical.
- The workflow defines `pending`, `in_progress`, `implemented`, `verified`, and `blocked` without treating implementation as verification.
- The workflow provides a structured checkpoint template with task, status, changed files, checks, issues, next action, branch, and worktree state.
- The documentation remains stack-independent and performs no Git write operations.

### Out of scope

Executable hooks, CI enforcement, dashboards, and application code. Those require a selected project stack and repository-specific authorization.

## TASK-006 - Unique Markdown Filenames

Status: verified

Requirement: remove duplicate Markdown basenames while preserving conventional repository entry points and the self-contained kit.

### Affected Files

- Root `AGENTS.md` and `README.md`: retain conventional discovery names and update their kit links.
- [HARNESS_RULES.md](../HARNESS_RULES.md) and [HARNESS_GUIDE.md](../HARNESS_GUIDE.md): uniquely named kit entry documents.
- The startup prompt and all kit documents that reference the renamed files.

### Acceptance

- Every Markdown file in the repository has a unique basename.
- Root `AGENTS.md` and `README.md` remain available for conventional discovery.
- All local Markdown links resolve after the rename.
- No Git write operations are performed.

## TASK-007 - Machine-Readable State and Token Economy

Status: verified

Requirement: implement the lightweight v0.2 invariants and minimize token usage by default without weakening correctness, safety, or verification.

### Affected Files

- [state.json](../state.json) and [PROJECT_STATE.md](../PROJECT_STATE.md): synchronized machine and human checkpoints.
- [HARNESS_RULES.md](../HARNESS_RULES.md): state contract, verification levels, blockers, stop conditions, failure escalation, and token economy.
- Historical optional helper: optional reference implementation of invariant checks.
- [verification/KNOWN_FAILURES.md](../verification/KNOWN_FAILURES.md): pre-existing failure register.
- Root startup prompt, guide, project map, plan, decisions, and verification evidence.

### Acceptance

- `state.json` is valid JSON, remains intentionally small, and contains every required state field.
- `PROJECT_STATE.md` remains compact and its current task, status, and next action match `state.json`.
- Startup and checkpoint instructions update both state representations.
- Token-economy rules require targeted reads, bounded output, canonical references, concise communication, and the lightest capable model when selectable, without skipping required checks or safety.
- Verification rules distinguish levels and require command or action, result, timestamp, scope, and status.
- Blocked tasks, known failures, stop conditions, and repeated-failure escalation are explicit.
- The core workflow and checks are independent of any bundled helper; historical optional-tool results remain in the verification record.
- All links resolve, the kit remains self-contained, and no Git write operations are performed.

### Out of scope

Agent orchestration, workflow DAGs, mandatory language runtimes or databases, agent-specific SDKs, layered configuration systems, custom runtimes, and complex plugin architectures.

## TASK-008 - Software Engineering Requirements

Status: verified

Requirement: make respect for software engineering principles explicit, actionable, and verifiable for every project using this kit.

### Affected Files

- [HARNESS_RULES.md](../HARNESS_RULES.md): canonical principles and engineering completion criteria.
- Source repository README and startup prompt: references to the canonical requirements.
- [PLAN.md](PLAN.md), this file, both state files, and [verification/VERIFICATION.md](../verification/VERIFICATION.md): scope, checkpoint, and evidence.

### Acceptance

- Explicit obligations explain all five SOLID principles, KISS, DRY, YAGNI, separation of concerns, cohesion, and coupling.
- Contracts, data consistency, errors, security, performance constraints, and testability have concrete guidance.
- Completion criteria require observable behavior, design review, relevant checks, and evidence with limitations.
- Requirements remain stack-independent, proportionate, and free of speculative architecture; definitions live only in HARNESS_RULES.md.
- Startup and discovery documents reference those requirements; links, state, task consistency, whitespace, and searched secret patterns pass checks.
- The optional validator is explicitly distinguished from verification of application design quality.

Out of scope: application code, new tooling, CI enforcement, stack choices, branch changes, and history rewriting. The current request authorizes applying this documentation update to the connected repository's existing main branch through GitHub.

## Future Tasks

In a derived project, replace the kit tasks with current requirements. For new nontrivial tasks, add an ID, requirement, affected files, acceptance criteria, and exclusions. Record checks using the same ID. A checkpoint is sufficient for small changes; do not duplicate status or next steps here.
