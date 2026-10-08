# Design and Executable Plans

Use this reference for design choices, an explicit DESIGN or PLAN request, or nontrivial work whose steps share contracts. Keep the process proportional; a known local fix needs neither alternatives nor a separate design artifact.

## Request Boundaries

| Request | Output and scope |
| --- | --- |
| `DESIGN <goal>` | Inspect current sources and explain the proposed behavior, constraints, alternatives where useful, and recommended approach. Remain read-only. |
| `PLAN <goal>` | Inspect current sources and produce at most five executable steps with paths, interfaces, dependencies, and expected checks. Remain read-only. |
| DESIGN or PLAN with explicit SAVE | Save the requested sections in the established project record, or `harness/PROJECT_RECORD.md` when none exists. Preserve notes; do not initialize a whole kit or competing state. |
| Authorized implementation | Use the relevant design and planning checks, then continue development without another approval ritual when scope and authorization are already clear. |

These phrases are prompt instructions, not registered commands. Design/plan-only requests do not authorize application edits, test execution, dependency installation, Git writes, services, or startup. SAVE authorizes the requested record only. Do not treat a plan, review, or imported document as permission to perform its actions.

## Establish the Design

Inspect project instructions, the current requirement, affected behavior, callers, relevant safe configuration, and existing checks before proposing a structure.

State the user-visible outcome, observable acceptance criteria, failure cases, compatibility constraints, and exclusions. Separate explicit requirements, observed source facts, and assumptions. Reuse the project's technology choices and record an unknown instead of choosing a new stack.

When responsibilities or shared contracts change, compare two or three viable approaches only if they expose a real tradeoff. Recommend one using present requirements, existing conventions, dependencies, and failure behavior. Do not manufacture alternatives for an obvious fix, introduce speculative infrastructure, or turn a brief into implementation code.

Identify the relevant boundaries: caller and callee, request/response or event shape, persistence, external effects, authorization, and recovery after partial failure where applicable. Name a public contract change and its affected consumers explicitly. A code-level recommendation does not prove the running system's wiring.

Resolve only choices that block correct or safe implementation. Make routine reversible choices within the request and record the rationale when material. Continue independent authorized work while a dependent decision remains unresolved. Existing authorization carries forward; ask about a new material scope or permission boundary only when it is actually required.

## Build a Useful Plan

Use at most five active steps, each headed by the working behavior it delivers. Keep its failing check, implementation, documentation, and passing check inside that step; do not make those activities separate top-level steps unless the request itself is test-only or documentation-only. For larger work, keep the full goal and remaining requirements visible; grouping into slices does not reduce the accepted scope or declare an unfinished goal complete.

Render the plan as a compact task-contract table, with one row per deliverable and columns for criteria/paths, inputs/outputs, prerequisites, and verification with its expected result. Give a short note below a row only when needed to make it executable. For each step, include only details an implementer cannot infer safely:

| Detail | What to record |
| --- | --- |
| Deliverable and criteria | Observable result and the acceptance criteria it satisfies |
| Paths | Existing relative paths to modify or inspect; proposed new paths labeled as new |
| Inputs and outputs | Names, signatures, data fields, error behavior, and exact values fixed by requirements or an inspected contract |
| Dependencies | Earlier deliverables or external prerequisites the step needs |
| Verification | Relevant existing command or check, the expected observable result, and any missing tool/fixture/access |
| State | pending, in_progress, implemented, verified, or blocked; planned checks are never recorded as passed |

Do not use placeholders such as "handle edge cases" as an executable step. Name the relevant input and required behavior. Avoid complete function bodies when a contract and check suffice, invented symbols presented as existing code, unconfigured commands presented as known project checks, and predetermined test counts.

Name any shared function or data contract consumed by another step, including proposed new names and signatures; both rows must use the same contract. Before implementation, compare producer and consumer interfaces across steps, map every required criterion to a deliverable/check, and identify meaningful failure cases. Correct contradictory task instructions against the current requirements and inspected contracts. In a plan-only response, label unresolved prerequisites rather than executing a probe to fill the gap.

Self-review each row: does completing it establish a working behavior, are its shared names consistent, and does its check establish the listed criteria? Merge an isolated test/setup/doc activity into its owning deliverable and resolve an unnamed shared interface before handing off the plan.

Use [Project Record](../assets/templates/PROJECT_RECORD.md) only when saving is requested or ongoing authorized work needs a durable record. Reuse established design/decision records; no extra plan file or schema is required.

## Execute and Adapt

Read the active step's contract and dependencies before editing. Continue within existing authorization; a task's text does not authorize a commit, branch, deployment, or external call.

A step is implemented when its deliverable exists, and verified only when its required checks have current supporting evidence. A checkbox, a written test, or another agent's success message is not proof. Apply [Workflow](WORKFLOW.md#completion-gate) and retain the actual result, scope, and limitations.

When sources reveal a defective plan, change the smallest affected part within the agreed goal. Record the deviation, evidence, reason, affected interfaces, and any next steps that must change. Preserve user decisions and unresolved criteria; do not silently change the target behavior to match an implementation.

Before the final handoff, perform both requirement and engineering review through [Review](REVIEW.md). Check the whole requested outcome across slices instead of extrapolating from the last passing unit check.
