# Project State

Updated: 2026-10-05 | Branch: main | Status: completed

## Goal

Remove obsolete material outside the English, categorized harness while preserving useful entry points, the ten kit documents, and Git safety rules.

## Relevant Architecture

- Kit root: entry points and current state; [project/ARCHITECTURE.md](project/ARCHITECTURE.md) maps the categories.
- [AGENTS.md](AGENTS.md): rules; [project/PROJECT_BRIEF.md](project/PROJECT_BRIEF.md): derived project choices.
- [planning/TASKS.md](planning/TASKS.md) and [verification/VERIFICATION.md](verification/VERIFICATION.md): details and evidence.

## Done

- [x] Documentation-only scope confirmed: no application code or stack.
- [x] Operating guide, state, tasks, and checks created in one directory.
- [x] File edits distinguished from authorized Git operations.
- [x] Ten English kit documents grouped by type and verified under TASK-001 through TASK-003.
- [x] TASK-004 completed: obsolete specification, active README link, and empty legacy docs/ directory removed; twelve Markdown documents remain, including ten in the kit. Links, Markdown, and whitespace checks passed; no Git write operations performed.

## Next Steps

1. Copy the entire harness/ directory into the target project and use the startup prompt in [README.md](README.md) with the project goal and selected technologies.

## Decisions

Canonical references: [project/DECISIONS.md](project/DECISIONS.md), D001-D006.

## Commands

No installation, runtime, software tests, or build: documentation only. Actual documentation checks are recorded in verification/VERIFICATION.md.

## Known Issues

- Instructions are not technical enforcement: branch protections and permissions must be configured in each project.
- `rg` is unavailable in the current environment: use editor search or `grep`.

## Resume

Run `git status` from the project root; read "In Progress" and the first "Next Step". On first copy, replace this state with facts about the new project; do not inherit kit outcomes or tasks.
