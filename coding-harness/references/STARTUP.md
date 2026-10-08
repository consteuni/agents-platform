# Project Startup

A bare explicit invocation of coding-harness, `START`, or the first explicit development invocation prepares a complete project-local kit. Keep the installed skill unchanged; create the kit in the target project's `harness/` folder.

## Route Before Writing

| Request | Action |
| --- | --- |
| Bare explicit invocation or `START` | Prepare the complete kit, inspect/save its project map, and report readiness and the next task. |
| First explicit development invocation | Prepare missing kit files before development; reuse an existing kit. |
| `START JSON` | Use JSON instead of Markdown for new canonical state; preserve an existing convention. |
| `START LEARN` or `START MAP LEARN` | Prepare the same kit and explain unfamiliar technologies in its map. |
| Design/plan-only, review/feedback-only, explanation, HARNESS STATUS, CHANGE IMPACT, or default `PROJECT MAP` / `PROJECT MAP LEARN` | Remain read-only; do not initialize the kit. |
| DESIGN or PLAN SAVE | Save requested record sections through [Design and Plans](DESIGN.md); do not initialize the kit or application. |
| RESUME | Use existing context through [Continuity](CONTINUITY.md); do not initialize a kit automatically. |
| Implicit selection for a small change | Use the smallest workflow; do not initialize merely because the skill was selected. |

START includes authorization for project-kit files and its saved map only. It does not authorize application changes, root instruction/configuration edits, Git writes, execution, or external services. These phrases are prompt instructions, not client commands or startup hooks.

## Establish Scope and Preserve Existing Work

1. Identify the target project root from the request, workspace, and repository boundaries. Ask which target to initialize only when multiple projects are ambiguous. Do not initialize ancestors or every nested project.
2. Read applicable instructions and inspect relevant changes, existing state/records, architecture documentation, and any `harness/` folder. With remote-only access, inspect the actual branch/ref and disclose unavailable local checks. Report unavailable write access rather than claiming success.
3. Keep existing canonical project state and equivalent records. When they live outside `harness/`, retain their authority and point to them from the kit index; do not create competing copies or silently migrate them. Explain this external dependency before describing that kit as self-contained.
4. Respect source-maintenance conventions when editing this skill's own repository; do not initialize a target kit there for routine skill-source maintenance.

## Complete Default Kit

| Destination | Purpose and source |
| --- | --- |
| `harness/README.md` | Entry point, actual document locations, usage, and setup limits; use [Kit Index](../assets/templates/PROJECT_HARNESS_README.md). |
| `harness/AGENTS.md` | Local instructions and pointers; use [Agent Guidance](../assets/templates/PROJECT_AGENT_GUIDANCE.md). |
| `harness/PROJECT_STATE.md` | Canonical objective, task, status, evidence, blockers, and next action; use [Markdown State](../assets/templates/PROJECT_STATE.md). |
| `harness/PROJECT_RECORD.md` | Brief, acceptance criteria, plan, decisions, and verification history; use [Project Record](../assets/templates/PROJECT_RECORD.md). |
| `harness/PROJECT_MAP.md` | Source-backed technologies, components, connections, and reading order; use [Project Mapping](PROJECT_MAP.md) and [Map Template](../assets/templates/PROJECT_MAP.md). |
| `harness/skill/` | Self-contained copy of this reusable skill: `SKILL.md`, `references/`, `assets/`, and `agents/`. |

For START JSON with no state convention, create `harness/PROJECT_STATE.json` from [JSON State](../assets/templates/PROJECT_STATE.json) instead of Markdown and follow [State Contract](STATE.md). Do not create both by default. Existing equivalents satisfy the kit; list which are reused. If an existing harness README contains user notes but lacks kit navigation, preserve it and place the missing index in `harness/INDEX.md`; reuse that index on later startup.

Copy the complete reusable skill package into a missing `harness/skill/`, preserving relative references and templates. Copy no source-repository maintenance state, Git metadata, credentials, caches, unrelated files, or user-home paths. This snapshot allows explicit use in a repo without a global installation; it does not install or activate itself. Keep project state outside that snapshot. If a snapshot already exists, inspect and preserve it; report incomplete/conflicting files rather than merging over personal edits. Refreshing it requires an explicit request and the preservation procedure in [Continuity](CONTINUITY.md#explicit-snapshot-refresh).

Populate newly created project documents with current facts, replacing template placeholders. Use a supplied development objective and at most five actionable steps. Without a task, record `pending`, the absence of an objective, observed context, and a next action to obtain it; leave acceptance criteria unset until a task exists. Never invent a feature, stack, architecture, test result, or copied source task. Setup completion does not mean application verification.

Inspect a representative flow and save the map during initial kit creation. On an empty project, document that no application architecture exists yet, known files, and unresolved choices. LEARN adds concept explanations when requested. Existing maps and user notes are preserved on repeated startup; use PROJECT MAP UPDATE for an explicit refresh.

## Repeated Startup and Portability

Create only missing documents or equivalents. Preserve existing bytes, notes, task status, evidence, and plans; startup is not a checkpoint reset. Reuse the same paths without duplicate files. Check destination symlinks, non-regular files, case/path collisions, and conflicting state instructions; do not follow symlinks to overwrite another project or delete/truncate a destination to make setup succeed.

Keep all default writes below `harness/`. Do not create or append root `AGENTS.md`, README, build files, or client configuration. `harness/AGENTS.md` has directory scope in clients that load instruction files; it does not automatically govern application files outside that folder. To use the kit without installation, explicitly ask the agent to read its instructions and local skill as described in the kit index. Root-level integration may be added only on a separate explicit request.

A kit can be copied to another repo, but its task state, map, evidence, and permissions are project-specific. On startup in a new repo, reconcile those documents with current instructions and sources; flag imported/stale context and do not inherit verified status. Preserve imported notes instead of resetting them automatically. For clean adoption, copy the reusable `harness/skill/` snapshot and request START in the new repo to generate fresh context; do not transplant the old project's operational records.

## Verify and Report

Read back created files, resolve references within the skill snapshot, check index/guidance pointers against actual canonical documents, and confirm the selected state format. Report created/reused files, external canonical documents, skipped/conflicting paths, source-only map limits, and the next action. If writes partly fail, report what exists and what remains rather than claiming a complete kit.

Keep README and guidance instructions current only through authorized edits; repeated startup preserves their content. If no development task was supplied, ask for the next objective after setup. Create no repository, branch, commit, chosen application stack, dependencies, environment, executable helper, service, or global installation. Subsequent work remains subject to existing permissions.
