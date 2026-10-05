# Tasks

Status and next action: [PROJECT_STATE.md](../PROJECT_STATE.md). Plan: [PLAN.md](PLAN.md). Evidence: [verification/VERIFICATION.md](../verification/VERIFICATION.md).

## TASK-001 - Single Kit and Git Safety

Requirement: one self-contained directory for the agent, without a default stack, that makes work and checks visible and prohibits unauthorized dangerous Git operations.

### Affected Files

The links below point to the documents' current locations after TASK-003.

- [AGENTS.md](../AGENTS.md): restore the earlier harness rules and explicit Git restrictions.
- [instructions/AGENT_CONTEXT.md](../instructions/AGENT_CONTEXT.md) and [project/PROJECT_BRIEF.md](../project/PROJECT_BRIEF.md): distinguish context, technology choices, and permissions.
- [PROJECT_STATE.md](../PROJECT_STATE.md): concise state and resume instructions.
- [project/ARCHITECTURE.md](../project/ARCHITECTURE.md): document responsibilities.
- [PLAN.md](PLAN.md), [project/DECISIONS.md](../project/DECISIONS.md), and this file: intentions, rationale, and requirement details.
- [verification/VERIFICATION.md](../verification/VERIFICATION.md): kit checks.
- [README.md](../README.md): copying and usage.

In the source repository, also update root entry points and consolidate the earlier template documents. Do not modify user files unrelated to the requirement. Translate the historical reference only under TASK-002, not as part of restructuring.

### Acceptance

- All kit references are internal to the directory.
- State stays within approximately 100 lines; each task connects files and checks.
- No imposed technologies and no Git write operations performed to prepare the kit.
- A generic request or CHECKPOINT does not authorize Git operations.
- Checks are recorded with actual outcomes and limitations.

Out of scope: dashboards, hooks, automation, application code, and remote branch protection configuration.

## TASK-002 - English Translation

Requirement: translate all documentation into English. Affected files: every document in this kit, the source repository's root README and AGENTS entry point, and the historical specification outside the kit.

Acceptance: preserve meaning, filenames, links, language independence, Git restrictions, and the optional status of the historical reference. Repeat checks after translation and record them under TASK-002 in verification/VERIFICATION.md.

Out of scope: application implementation, Git writes, external translation services, and technical branch protection configuration.

## TASK-003 - Organize Documents by Type

Requirement: categorize harness documents without splitting the copyable kit or changing operating and Git safety rules.

Affected files: move AGENT_CONTEXT into instructions/; PROJECT_BRIEF, ARCHITECTURE, and DECISIONS into project/; PLAN and TASKS into planning/; VERIFICATION into verification/. Update relative references in every affected document and in the kit-root AGENTS.md, README.md, and PROJECT_STATE.md.

Acceptance: keep exactly ten documents, preserve the root entry points and state, resolve every link inside the kit, and record checks under TASK-003 in verification/VERIFICATION.md. Project choices and Git safety rules must remain unchanged.

Out of scope: new document types, application code, stack choices, changes to the historical specification, and Git write operations.

## TASK-004 - Remove Obsolete Material

Requirement: remove files no longer useful to the reusable, technology-independent harness.

Affected paths: delete the obsolete orchestrator specification outside the kit, remove its link from the source repository README, and remove the verified-empty legacy docs/ directory. Preserve the root README and AGENTS entry point and all ten categorized kit documents.

Acceptance: no broken links, no obsolete source specification or empty legacy directory, and no Git write operations. Earlier task and verification records describe past work and do not require deleted material to remain present.

Out of scope: deleting useful kit documents, changing technologies or safety rules, recursively cleaning directories, or modifying Git history or branches.

## Future Tasks

In a derived project, replace the kit tasks with current requirements. For new nontrivial tasks, add an ID, requirement, affected files, acceptance criteria, and exclusions. Record checks using the same ID. A checkpoint is sufficient for small changes; do not duplicate status or next steps here.
