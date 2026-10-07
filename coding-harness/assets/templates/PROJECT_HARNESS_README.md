# Project Harness

This folder contains the project's development context and a local copy of coding-harness. It requires no additional runtime or dependency.

## Documents

Paths below are relative to the target project root.

- Instructions: `[GUIDANCE_PATH]`
- Canonical state: `[STATE_PATH]`
- Plan, decisions, and evidence: `[RECORD_PATH]`
- Architecture and technologies: `[MAP_PATH]`
- Reusable skill entry point: `[SKILL_PATH]`

[State which files were initialized or reused, any canonical documents outside this folder, and unavailable context. Replace this instruction before saving.]

## Use

With coding-harness installed, invoke it for the task. To use this kit without a global installation, ask the agent:

> Read the project harness instructions and the local skill at the paths listed above, then use the canonical project documents for this task. Follow the current project's instructions and verify actual results.

These are file-reading instructions, not automatically registered client commands. The instruction file inside this folder does not automatically apply to source files elsewhere in the repository.

Request HARNESS STATUS for a read-only kit audit, RESUME to reconcile and continue unfinished work, or CHANGE IMPACT followed by a proposed change to trace its affected contracts before implementation. Request PROJECT MAP to inspect the architecture, PROJECT MAP LEARN for unfamiliar technologies, or PROJECT MAP UPDATE to refresh the saved map. A focused update rechecks only its named area. Keep project facts outside the reusable skill snapshot.

START preserves an existing snapshot; refreshing it requires an explicit request with an identified source and preservation of customizations and the previous copy.

## Portability and Limits

The skill snapshot is reusable across repos; task state, decisions, map, and verification evidence belong to this project. For fresh adoption in another repo, copy the snapshot and request START there to generate new project context. Do not treat old evidence or permissions as current.

[Record actual initialization context and source-only map limits. Preserve user notes on later startup; omit unused placeholders.]
