# Project State Contract

Use this reference for a structured checkpoint, a handoff, or state migration. Keep state in the target project, outside this skill.

## Choose One Format

Reuse an established project convention. Otherwise, use [Markdown](../assets/templates/PROJECT_STATE.md) for a compact human-readable checkpoint, or [JSON](../assets/templates/PROJECT_STATE.json) when explicit fields help repeated handoffs or consumption by existing tools. Default paths are `agent-state/PROJECT_STATE.md` and `agent-state/PROJECT_STATE.json`; choose one, not both. No new file is required for a small fix or read-only review.

JSON is data, not an executable dependency. Validate its syntax with an available tool when practical; valid syntax alone proves neither truthful evidence nor completed work. No bundled checker, schema package, or runtime is required. Preserve any existing machine/human pair and its synchronization contract.

## Fields and Meaning

The JSON template is a blank starting point. Empty fields and an empty criteria list are allowed only before initialization; they cannot establish verification. For an active checkpoint:

| Field | Contract |
| --- | --- |
| `schema_version` | Integer `1` for this format. Preserve an existing project's version convention instead of silently migrating it. |
| `objective`, `current_task` | Nonempty objective and task title; use an existing task identifier or create a local descriptive identifier. |
| `status` | Exactly `pending`, `in_progress`, `implemented`, `verified`, or `blocked`, as defined in [Workflow](WORKFLOW.md#status-and-checkpoint). |
| `context` | Actual branch, inspected revision, and access mode or limitation. Use `null` for an unavailable branch or revision; never infer clean local status from a remote read. |
| `last_checkpoint` | Actual checkpoint time in ISO 8601 format, including timezone. Do not invent a time for an earlier check. |
| `acceptance_criteria` | Nonempty array of current criteria, each with `id`, `description`, `required` boolean, `result`, `reason`, and `evidence`. |
| `changed_files` | Paths actually changed for this task, relative to the project root; an empty array is valid before implementation. |
| `confirmed_facts`, `hypotheses` | Keep observed facts separate from unconfirmed explanations; concise strings are sufficient. |
| `blockers` | Concrete unresolved conditions and their impact. May be empty. Missing required verification belongs here even when implementation is finished. |
| `next_action` | One executable next step, or an explicit completion statement when no work remains. |

Each criterion has a unique ID. `result` is exactly `PASS`, `FAIL`, `NOT RUN`, or `N/A`. Record the current result for the current scope; put longer history in the project record.

For an observed PASS or FAIL, `evidence` is an object containing `action`, `level`, `observed_at`, `revision`, `scope`, `summary`, and `limitations`. Name the command or inspection actually performed, state what it establishes, and include limitations. Use `null` for an unavailable evidence time or revision and explain the gap; the checkpoint time is not a substitute. Manual evidence is valid when it directly establishes the criterion. Include relevant local changes in the scope: a commit hash alone may not identify the tested working tree.

For NOT RUN or N/A, set `evidence` to `null` and give a nonempty `reason`. N/A applies only to an optional criterion that does not apply. Do not turn an unmet required criterion into optional merely to declare completion; changing acceptance scope needs support from the current request or applicable authorization.

## Verification Gate

Set `verified` only when all of these conditions hold:

1. The active criteria list is nonempty and contains at least one required criterion.
2. Every required criterion has a current PASS and concrete evidence covering its requirement.
3. No unresolved blocker prevents a required criterion from being established.
4. Relevant configured checks and the diff have been reviewed, or their omission is explicitly justified within the accepted scope.

A passing unit check cannot substitute for required integration evidence. A mock proves only the simulated behavior. Mark implementation as `implemented` when changes exist but required verification remains; use `blocked` when the next work itself cannot proceed. Neither status implies completion.

Invalidate affected evidence after changing behavior, requirements, configuration, or the tested environment. Recheck the affected scope before restoring PASS. A later passing check may supersede an earlier failure only for the behavior it actually covers; preserve important failure history in the project record.

## Example: Implementation with Missing Integration Evidence

This illustrative checkpoint describes supplied observations; it does not certify a real project.

```json
{
  "schema_version": 1,
  "objective": "Create orders atomically",
  "current_task": {"id": "orders-transaction", "title": "Add transactional order creation"},
  "status": "implemented",
  "context": {"branch": "feature/orders", "revision": null, "access": "local working tree"},
  "last_checkpoint": "2026-10-07T08:10:00Z",
  "acceptance_criteria": [
    {
      "id": "unit",
      "description": "Unit tests cover order creation behavior",
      "required": true,
      "result": "PASS",
      "reason": "",
      "evidence": {
        "action": "Configured unit test command",
        "level": "unit",
        "observed_at": "2026-10-07T08:05:00Z",
        "revision": null,
        "scope": "src/orders.js and its tests in the current working tree",
        "summary": "Unit tests passed",
        "limitations": "No revision recorded; database rollback is not covered"
      }
    },
    {
      "id": "rollback",
      "description": "Real database rolls back a failed order",
      "required": true,
      "result": "NOT RUN",
      "reason": "No safe test database is available",
      "evidence": null
    }
  ],
  "changed_files": ["src/orders.js"],
  "confirmed_facts": ["Implementation exists; unit tests passed"],
  "hypotheses": [],
  "blockers": ["Required rollback verification needs a safe test database"],
  "next_action": "Obtain an authorized safe test database and run the configured rollback integration check"
}
```

Do not replace NOT RUN with PASS because code looks plausible. A checkpoint with `verified` and an empty criteria list is also invalid.

## Resume and Migrate

On resume, read the current request and project instructions, inspect the actual branch and changes, then reconcile the checkpoint with current facts. A checkpoint records context; it does not grant Git, deployment, data deletion, or external-service permissions.

When migration is requested, transfer current facts without deleting the original automatically. Name the canonical destination, preserve unresolved checks and limitations, and avoid maintaining two independent copies. Do not inherit this source repository's tasks, evidence, or technology choices.
