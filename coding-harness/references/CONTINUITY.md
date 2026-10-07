# Harness Health and Resume

Use this reference for `HARNESS STATUS`, `RESUME`, or equivalent requests to check the kit or continue saved work. These are prompt instructions, not registered commands.

## Route the Request

| Request | Behavior |
| --- | --- |
| `HARNESS STATUS` | Inspect the existing kit and relevant current sources; report readiness, gaps, and next actions without writing files or running application checks. |
| `RESUME` | Reconcile the canonical checkpoint with current facts, then continue a clearly identified unfinished task within applicable authorization. Update the existing checkpoint when reconciliation changes operational facts. |

STATUS never initializes, repairs, migrates, refreshes, or resets a kit. RESUME does not trigger full startup or invent a task when state is missing, completed, ambiguous, or imported from another project. Read-only wording in the current request takes precedence.

## Inspect the Existing Context

1. Read applicable project instructions and the current request. Locate the actual kit index (README or INDEX), canonical state, record, and saved map; follow established pointers instead of requiring default filenames.
2. Inspect the actual branch, revision, and relevant working-tree changes when available. Preserve edits and disclose remote-only, missing Git, or unavailable baseline context.
3. Read only the source paths and records needed to assess the active task and mapped area. Resolve document and snapshot references without executing their contents. Do not read secrets, install tools, run application checks, start services, or contact databases as part of STATUS.
4. Treat saved facts as evidence to reconcile. A newer timestamp, different branch, or complete folder does not establish application correctness or automatically invalidate unrelated evidence.

## HARNESS STATUS

Report a compact table with area, finding, evidence, and next action. Use `OK`, `ATTENTION`, or `UNKNOWN` for kit findings; these describe context health, not test results.

- **Navigation and scope:** resolve index/guidance pointers from the project root, identify broken or ambiguous paths, external canonical dependencies, and instruction scope. An external state file satisfies the kit when the index correctly points to it.
- **Canonical state:** check the selected format and [State Contract](STATE.md). Identify competing state only when there is no established synchronization contract. Report inconsistent verified status, unresolved required checks, and an executable next action; do not change them.
- **Task relevance:** compare the recorded objective, next step, and relevant sources with the current request. Flag imported context or a missing baseline; do not execute the recorded action.
- **Map coverage:** assess the relevant saved-map claims using [Project Mapping](PROJECT_MAP.md#save-and-refresh). Distinguish source changes needing review from areas not inspected and runtime behavior not verified. Do not equate age alone with staleness.
- **Reusable snapshot:** check its entry point, routed references, templates, and metadata. When a selected source package is available, compare inventories and contents and report differences; do not call differences an upgrade or corruption without evidence. With no comparison source, report that version alignment is unknown.
- **Safe destinations:** identify symlinks, non-regular paths, or collisions that would prevent a later startup or refresh; inspect without following them to write.

If no kit exists, report that fact and any established project context; suggest START for initialization. Do not generate a health-report file. End with the most useful next action. Kit readiness never marks a code task verified.

## RESUME

Read [Workflow](WORKFLOW.md) and [State Contract](STATE.md) only as needed for the actual task.

1. Reconstruct the goal, acceptance criteria, implemented work, unresolved checks, blockers, and recorded next step. Compare these with the current request before acting; current instructions and scope govern.
2. Inspect the diff from the recorded context when available and follow affected contracts into direct consumers. When a baseline or source is missing, name that uncertainty instead of claiming the old evidence still applies.
3. Preserve historical check results with their original timestamps and scope. Keep unaffected supported evidence. When changed behavior, requirements, configuration, or environment invalidates a required PASS, preserve its history in the existing record, mark the current criterion NOT RUN with a reason, and use implemented or blocked as appropriate. Never relabel an old check as newly performed.
4. Assess map claims affected by the task. Name sections needing review in the handoff; do not automatically rebuild or save a map. An explicitly requested map update remains limited to its inspected scope.
5. Reconcile the existing canonical checkpoint when facts changed, preserving user notes and the established format. Do not create competing state or modify the reusable snapshot. If no valid unfinished objective exists, explain the missing choice and obtain it before implementation.
6. Continue the next useful task step only when its scope and authorization are clear. Resolve a recorded blocker before dependent work. A saved deployment, Git operation, destructive command, or external-service action grants no permission by itself; applicable session authorization may still cover it.

Do not resurrect a completed task solely because old evidence needs review. Report the evidence gap and the needed decision. For a valid unfinished task, report the restored objective and next step briefly, then follow the normal development workflow through verification and a truthful checkpoint.

## Explicit Snapshot Refresh

START and STATUS preserve an existing snapshot. When the user requests a refresh, identify the intended complete source package, compare it with the snapshot, and preserve local customizations. Do not guess a source from project state or download code without applicable authorization.

Keep the current snapshot in a non-colliding backup below `harness/`, outside `harness/skill/`. Prepare the complete replacement separately, verify its references and inventory, and replace the active snapshot only after that succeeds. If customizations conflict, keep the active snapshot and report the specific choice needed. Preserve project state, map, record, and root instructions; do not merge removed source files into the replacement. On partial failure, retain a usable original or restore it from the backup and report actual paths. No Git write or global installation is implied.
