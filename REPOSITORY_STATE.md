# Repository State

Updated: 2026-10-07T08:22:21.683Z
Branch: main
Access context: connected GitHub repository; local checkout status unavailable.

## Current Objective

Maintain an instruction-only development skill with proportionate engineering guidance, truthful verification, reusable handoffs, and documented client installation.

## Current Task and Status

TASK-012 — verified

Requirement: accept modest additional structure where it makes the skill more useful, and document installation, update, and invocation according to the client.

## Completed Changes

- Add a blank optional JSON checkpoint and a state contract with criterion-level evidence, scope, limitations, invalidation, and verification conditions.
- Preserve a single canonical project checkpoint, existing conventions, and the small-change workflow; Markdown remains available.
- Add optional OpenAI selector metadata, an invocation prompt, and implicit invocation policy without tool dependencies.
- Expand the source README in Italian with Codex CLI/IDE, Claude Code, Cursor, and ChatGPT procedures, project scope, updates with backup, symlink alternatives, and discovery troubleshooting.
- Keep eight reusable skill files and a concise entry point. Add no runtime, executable helpers, hooks, new stack, or mandatory delegation.
- Preserve the ECC refinements delivered in [the previous source update](https://github.com/consteuni/agents-platform/commit/41414162d9fc0e9489042eb517784ba62c0b9dd2).

## Verification Evidence

| Action | Result | Timestamp | Scope and Limitations |
| --- | --- | --- | --- |
| Check document links, heading anchors, whitespace, and package boundaries; parse JSON template and example | PASS | 2026-10-07T08:16:24.387Z | Source structure; instructions cannot enforce future compliance |
| Parse SKILL frontmatter and OpenAI YAML; check metadata fields, description length, prompt, and policy | PASS | 2026-10-07T08:16:24.387Z | Static metadata; actual local-client discovery not exercised |
| Independent agent used the candidate skill to produce a JSON checkpoint from supplied order-transaction facts | PASS: blocked, passing unit/diff evidence, required database checks NOT RUN, concrete resume step, no invented verification | 2026-10-07T08:16:49Z | Handoff reasoning from supplied facts; no database integration ran |
| Check eight Bash blocks and exercise installation for three destination conventions with isolated dummy fixtures | PASS: syntax, full-folder copying, existing-destination preservation, symlink guards | 2026-10-07T08:21:38.597Z | Local command behavior; no real client was installed |
| Exercise the documented update against an isolated local Git remote and installed fixture | PASS: source advances on main, old copy backed up, obsolete files absent in new copy, dirty source rejected before installation changes | 2026-10-07T08:21:38.597Z | Disposable fixture; user machine and production untouched |
| Verify client discovery paths and invocation against official OpenAI, Claude Code, and Cursor documentation | PASS | 2026-10-07T08:22:21.683Z | Documentation checked on 2026-10-07; client versions and interfaces can differ |

The previous ECC update also passed an independent regression-fix exercise: a failing blank-input test was observed before the minimal fix, followed by three passing configured tests. Those results remain in the preceding commit's repository state.

## Blockers and Limits

None for the source update. A copied personal installation must be updated separately. ChatGPT personal creation and local client installation were not performed here.

## Next Action

Follow the README for the chosen client, update the personal copy, and invoke coding-harness on a real project task. Base future changes on observed outcomes.

## Authorization

The established repository-update scope and the current requests authorize source changes in consteuni/agents-platform on existing main. No branch changes, history rewriting, personal installation, or deployment elsewhere are included.
