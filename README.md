# Coding Harness

A skill that guides an agent through maintainable software development: understanding the project, applying software engineering principles, implementing changes, verifying with evidence, and preserving continuity across sessions.

Follow the languages, frameworks, and tools already used by the project. The skill contains instructions, references, and templates; it requires no additional runtime, scripts, hooks, or dependencies.

## Choose Your Client

| Client | Personal installation, available across local projects | Invocation |
| --- | --- | --- |
| Codex CLI / IDE extension | `~/.agents/skills/coding-harness/` | `$coding-harness` or `/skills` |
| Claude Code | `~/.claude/skills/coding-harness/` | `/coding-harness` |
| Cursor | `~/.cursor/skills/coding-harness/` | Type `/` in Agent chat, then select the skill |
| ChatGPT with skill management | Create a personal skill through `@skill-creator` | Type `@` and select the skill |

Globally available means available across projects for that user on that machine. The agent may choose the skill when the request matches its description; invoke it explicitly at the start of a task to ensure it is used.

Local folders are not automatically installed in ChatGPT or cloud sessions. The [openai.yaml](coding-harness/agents/openai.yaml) metadata configures presentation and permits implicit invocation in clients that support it; it does not replace installation.

## Prepare the Source

The following commands use Bash on Linux, macOS, or WSL. Run installation and update commands from the source folder that contains `coding-harness/`. The folder can have any name and be located anywhere, including a path with spaces.

`repo_dir="$(pwd -P)"` resolves your current source folder. `$HOME` and `~` refer to the current user's home directory. These are portable variables and conventions, not links to a particular computer or user.

If you have already downloaded or cloned the repository, open a terminal in its source folder. Otherwise, replace `<repository-url>` with the URL of the source repository or your fork, then run:

```bash
git clone "<repository-url>" coding-harness-source
cd coding-harness-source
```

Always install the entire `coding-harness/` folder: copying only `SKILL.md` leaves references and templates unavailable. This repository contains the skill source and does not activate itself.

## Install for Your Client

These commands are for a first installation. If the destination already exists, follow [Updating](#updating) to preserve a backup.

### Codex CLI and IDE

```bash
(
  set -eu
  repo_dir="$(pwd -P)"
  skill_dir="$HOME/.agents/skills/coding-harness"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_dir"
  test ! -L "$skill_dir"
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
)
```

Open Codex in your project and enter:

```text
$coding-harness Implement this feature using the project's existing conventions.
```

Use `/skills` to find the skill. Codex detects skill changes; restart it if the skill does not appear.

### Claude Code

```bash
(
  set -eu
  repo_dir="$(pwd -P)"
  skill_dir="$HOME/.claude/skills/coding-harness"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_dir"
  test ! -L "$skill_dir"
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
)
```

Start Claude Code in your project and enter:

```text
/coding-harness Fix this bug and verify the behavior.
```

The personal folder makes the skill available across local projects. Open the `/` menu and search for `coding-harness` to check discovery.

### Cursor

```bash
(
  set -eu
  repo_dir="$(pwd -P)"
  skill_dir="$HOME/.cursor/skills/coding-harness"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_dir"
  test ! -L "$skill_dir"
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
)
```

Open **Customize → Skills**, then type `/` in Agent chat and select `coding-harness`. Reopen the client if it does not discover the skill after installation.

Cursor also reads `~/.agents/skills/` and directories compatible with other clients: if you already installed the skill for Codex, check whether it is available before creating another copy with the same name. For Cloud Agents, the documentation describes syncing skills from `~/.cursor/skills/` through **Settings → Agents → Sync Skills for Cloud Agents**; a local installation alone is not transferred to remote sessions.

### ChatGPT

When the client offers skill management and creation, invoke `@skill-creator` and ask:

> Create a personal skill named coding-harness from the coding-harness folder in the source repository or files I provide. Preserve its references, templates, instruction-only operation, and software engineering principles.

Make the source accessible to the creator through the connected GitHub integration or the folder's files. After the creator confirms saving, select the skill with `@`. To update it, ask the same creator to update the existing personal skill from the repository, preserving any declared customizations.

Having `~/.agents/skills/` on your computer does not install a skill in your ChatGPT account. This repository does not yet contain a plugin package that can be installed from the catalog.

## Updating

For a copied installation, open a terminal in the source folder, update the source, then replace the installed folder. This procedure preserves the previous version outside client discovery directories and prevents files removed from the source from remaining in the new copy.

Choose **one** destination for the client you want to update:

```bash
# Codex
skill_dir="$HOME/.agents/skills/coding-harness"

# Claude Code: use this line instead of the one above
# skill_dir="$HOME/.claude/skills/coding-harness"

# Cursor: use this line instead of the one above
# skill_dir="$HOME/.cursor/skills/coding-harness"
```

Then run:

```bash
(
  set -eu
  repo_dir="$(pwd -P)"
  branch_name="$(git -C "$repo_dir" branch --show-current)"
  if [ -z "$branch_name" ]; then
    echo "The source has a detached HEAD: select the intended branch before updating."
    exit 1
  fi
  git -C "$repo_dir" rev-parse --verify '@{upstream}' >/dev/null
  if [ -n "$(git -C "$repo_dir" status --porcelain)" ]; then
    echo "The source contains local changes: resolve them before updating."
    exit 1
  fi
  git -C "$repo_dir" pull --ff-only
  test -f "$repo_dir/coding-harness/SKILL.md"
  if [ -L "$skill_dir" ]; then
    echo "The skill is a symlink: use the symlink procedure."
    exit 1
  fi
  backup_root="$HOME/.local/share/coding-harness/backups"
  mkdir -p "$backup_root"
  backup_dir="$(mktemp -d "$backup_root/update-XXXXXXXX")"
  if [ -e "$skill_dir" ]; then
    mv "$skill_dir" "$backup_dir/coding-harness"
  fi
  mkdir -p "$skill_dir"
  cp -R "$repo_dir/coding-harness/." "$skill_dir/"
  echo "Skill updated. Backup: $backup_dir"
)
```

The initial checks stop the update if the source has local changes, has a detached HEAD, has no configured upstream, or cannot advance without a merge. The update follows the current branch's configured upstream; it does not assume a branch name, remote name, repository owner, or checkout location. If the folder came from a ZIP archive, download a fresh source version and apply the backup and copy steps: `git pull` requires a Git clone.

If you customized the installed skill, compare the backup with the new version and reapply only the changes you want. Check invocation in the client afterward; open a new session if it continues to use the previous version. Repeat the update for each separate copy you use.

### Alternative: Link to the Source

Codex and Claude Code document support for symlinked skill folders. On Linux, macOS, or WSL, you can avoid a second copy when the destination does not exist:

```bash
(
  set -eu
  repo_dir="$(pwd -P)"
  skill_root="$HOME/.agents/skills"
  # For Claude Code: skill_root="$HOME/.claude/skills"
  test -f "$repo_dir/coding-harness/SKILL.md"
  test ! -e "$skill_root/coding-harness"
  test ! -L "$skill_root/coding-harness"
  mkdir -p "$skill_root"
  ln -s "$repo_dir/coding-harness" "$skill_root/coding-harness"
)
```

If you already have a copy, move it outside the skill directory and preserve it first; do not create a link inside the existing copy. With a symlink, update only the repository using `git pull --ff-only` after checking the branch and local changes. The link sees the updated source without copying files again. Keep the source repository at the same location; local source changes become immediately visible to the skill.

## Install for One Project

Use these destinations inside the project instead of the personal folder:

| Client | Project destination |
| --- | --- |
| Codex | `.agents/skills/coding-harness/` |
| Claude Code | `.claude/skills/coding-harness/` |
| Cursor | `.cursor/skills/coding-harness/` or `.agents/skills/coding-harness/` |

Copy the entire folder and share it with the project when the team needs it. For remote sessions, make it available in the remote environment or repository according to the client. Do not assume a folder on your local computer also exists there.

## If the Skill Does Not Appear

1. Check that the path ends in `coding-harness/SKILL.md`, without an extra `coding-harness/coding-harness/` level.
2. Check that the file starts with frontmatter containing `name: coding-harness` and `description`.
3. Verify that `references/`, `assets/`, and `agents/` were copied with the file.
4. Find the skill in the client's menu and try explicit invocation. Reopen the client if needed.
5. Check that it is enabled in settings and that multiple directories do not contain copies with the same name.

For Codex, run these checks in the terminal:

```bash
codex --version
ls "$HOME/.agents/skills/coding-harness/SKILL.md"
sed -n '1,6p' "$HOME/.agents/skills/coding-harness/SKILL.md"
```

## Complete Project Harness

A bare explicit invocation or START prepares the target project's complete `harness/` kit. The first explicit development invocation also prepares it when missing:

```text
$coding-harness
$coding-harness START
$coding-harness START JSON
$coding-harness START LEARN
```

| Default destination | Purpose |
| --- | --- |
| `harness/README.md` | Kit entry point, usage, actual file locations, and setup limits |
| `harness/AGENTS.md` | Project-local instructions and context pointers |
| `harness/PROJECT_STATE.md` | Objective, task, status, evidence, blockers, and next action |
| `harness/PROJECT_RECORD.md` | Brief, criteria, plan, decisions, and verification history |
| `harness/PROJECT_MAP.md` | Inspected architecture, technologies, connections, and reading order |
| `harness/skill/` | Complete reusable skill copy with its references, templates, and metadata |

START JSON selects JSON instead of Markdown when no state convention exists. START LEARN explains unfamiliar technologies in the map. The map is inspected from actual sources; on an empty project it records that architecture and stack choices are not yet established.

Startup preserves existing files, user notes, progress, and evidence. If a personal harness README already exists, missing kit navigation can be created in harness/INDEX.md without replacing those notes. Repeated startup creates only missing equivalents. Established canonical documents outside `harness/` stay authoritative and are listed in the kit index; such a kit has explicit external document dependencies instead of misleading duplicate state.

All default new files are inside `harness/`. Root instructions and application configuration remain unchanged. Startup writes through authorized agent tools; it is not an executable hook and creates no dependencies, chosen stack, Git repository, branch, commit, or global installation. Missing access or conflicting paths are reported.

Design/plan-only, review/feedback-only, explanations, HARNESS STATUS, CHANGE IMPACT, and default PROJECT MAP/LEARN requests stay read-only unless initialization is also requested. RESUME uses existing context without triggering startup. Implicit selection for a small change does not create a kit. Without a development objective, state remains pending and asks for the next task instead of inventing progress or application verification.

### Use or Adopt the Kit

With the global skill installed, invoke it for the task. Without it, explicitly tell the agent:

```text
Read harness/AGENTS.md and harness/skill/SKILL.md.
Use the canonical project documents listed in harness/README.md for this task.
```

The nested instruction file does not automatically govern application files outside its folder, and the snapshot does not register client commands. Explicit reading lets the agent use the kit without a global installation, subject to current project instructions.

To adopt it in another repo, copy the reusable `harness/skill/` snapshot and request START there to generate fresh project context. If you move the entire folder, reconcile existing project-specific state, map, notes, and evidence before resuming; do not inherit verified status or permissions. Existing snapshot files are preserved; refresh them only on an explicit request with an identified source. The [refresh procedure](coding-harness/references/CONTINUITY.md#explicit-snapshot-refresh) preserves customizations and a backup before replacement. Updating the global installation does not update this project-local copy.

In Claude Code, use `/coding-harness START`; in Cursor or ChatGPT select the skill and request START. See [Startup](coding-harness/references/STARTUP.md) for the complete workflow.

## Design, Plan, and Handle Review Feedback

For work with unclear boundaries or shared interfaces, the skill records enough design and task detail to make implementation verifiable. It follows current project conventions and existing authorization; a known small fix needs no separate design document or repeated approval.

| Request | Result |
| --- | --- |
| `DESIGN <goal>` | Read-only design grounded in current code, constraints, failure behavior, and meaningful alternatives |
| `PLAN <goal>` | Read-only plan of at most five active steps with paths, input/output contracts, dependencies, and expected checks |
| DESIGN or PLAN with SAVE | Save requested sections in the existing project record, or `harness/PROJECT_RECORD.md`; preserve notes and initialize no full kit |
| `REVIEW FEEDBACK <feedback>` | Read-only assessment of suggestions against current requirements, callers, tests, and compatibility |

For example, in Codex:

```text
$coding-harness DESIGN Add cancellation to the existing order workflow
$coding-harness PLAN Add cancellation while preserving the current public order ID
$coding-harness PLAN SAVE Add cancellation without changing the payment contract
$coding-harness REVIEW FEEDBACK Evaluate these review comments against our API contract
$coding-harness Apply the supported review fixes and verify the affected behavior
```

These are prompt instructions, not registered client commands. Design/plan-only requests run no checks and create no application files. SAVE writes only the requested record sections. Applying review fixes requires a request that includes application edits; a comment or suggested patch grants no permission on its own.

A useful plan names a deliverable, affected paths, shared signatures/data, prerequisites, and observable verification for every active step. Expected results stay separate from actual evidence. Producer and consumer contracts are checked before execution; material plan corrections retain their rationale and affected steps in the existing record. Working in slices does not reduce the full accepted goal.

Review first checks required behavior and exact contracts, then engineering quality. Passing tests cannot excuse an omitted requirement. Received suggestions are classified as supported, unsupported, needing context, or out of scope; independent valid fixes can proceed while a dependent item awaits clarification.

Debugging follows bad inputs or failures back through callers and component boundaries, comparing a working path before changing the responsible behavior. Temporary diagnostics use safe metadata and are removed after investigation. Regression checks must demonstrate the intended failure, with expected values derived independently of the implementation; setup errors and mocked return values cannot stand in for behavior evidence.

See [Design and Plans](coding-harness/references/DESIGN.md), [Review](coding-harness/references/REVIEW.md), and [Behavior-First Debugging](coding-harness/references/WORKFLOW.md#behavior-first-debugging). The existing project record holds these details; no new required project file or runtime is added.

## Check, Resume, and Assess Changes

| Request | Result |
| --- | --- |
| `HARNESS STATUS` | Read-only audit of document pointers, canonical state, required check gaps, saved-map coverage, and the reusable snapshot |
| `RESUME` | Reconcile recorded work with current sources, preserve valid evidence, and continue a clearly identified unfinished task |
| `CHANGE IMPACT <proposed change>` | Read-only trace of affected contracts, direct consumers, likely edit locations, and existing checks |

For example, in Codex:

```text
$coding-harness HARNESS STATUS
$coding-harness RESUME
$coding-harness CHANGE IMPACT Add cancellation to the order workflow
$coding-harness CHANGE IMPACT LEARN Explain what adding cancellation would affect
```

In other clients, select coding-harness using the client's invocation above and include the same request. These phrases are instructions, not registered commands.

STATUS reports findings and next actions without repairing files, initializing the kit, running application checks, or refreshing the snapshot. Existing external canonical documents count when correctly linked. Kit readiness is separate from application verification. Snapshot differences are reported against an available source; without one, version alignment remains unknown.

RESUME checks the current request, branch/diff, criteria, evidence, blockers, and next step before continuing. It preserves historical results and invalidates affected current evidence when relevant behavior or requirements changed. Unrelated edits do not reset all progress. A missing, imported, ambiguous, or completed objective is resolved before implementation; a saved action does not grant Git, deployment, destructive, or service permissions. Use STATUS when you only want an assessment.

CHANGE IMPACT helps choose where to start before changing a large project. It confirms relevant map claims against source, distinguishes likely edit locations from consumers needing review, and names useful existing checks without running them. Add LEARN to explain unfamiliar concepts. It does not initialize a kit, implement the proposal, or claim exhaustive impact.

See [Continuity](coding-harness/references/CONTINUITY.md) and [Change Impact](coding-harness/references/PROJECT_MAP.md#change-impact). No new state format or required document is introduced.

## Optional Project Map

When a project becomes difficult to follow, invoke the skill with `PROJECT MAP`. The agent inspects the repository and explains its purpose, current work, major technologies, components, connections, and a representative data flow. Claims include source evidence and distinguish observations from inferences and unknowns.

| Request | Result |
| --- | --- |
| `PROJECT MAP` | Read-only overview in the response |
| `PROJECT MAP LEARN` | Beginner-oriented map that explains an unfamiliar language/framework using real project code |
| `PROJECT MAP <area or question>` | Focused map of a subsystem, flow, or dependency |
| `PROJECT MAP SAVE` | Save a map in existing project documentation, or `docs/PROJECT_MAP.md` |
| `PROJECT MAP UPDATE` | Refresh an existing saved map and preserve user notes; retain earlier inspection context for untouched areas |

For example, in Codex:

```text
$coding-harness PROJECT MAP
$coding-harness PROJECT MAP LEARN I am new to Java and Spring Boot; explain one request through this project
$coding-harness PROJECT MAP document processing: explain storage, APIs, and tracking
$coding-harness PROJECT MAP SAVE
$coding-harness PROJECT MAP UPDATE
```

Use `/coding-harness` in Claude Code, or select the skill in Cursor or ChatGPT and include the same request. These phrases are instructions to the skill; they do not register new client commands.

For an unfamiliar stack, LEARN distinguishes the language from the framework, explains the concepts encountered in the actual code, and provides a reading order. It can explain entry points, annotations, dependency wiring, persistence, and failure handling when those exist in the project. It does not assume a standard architecture or replace your code. Add a named area to narrow the explanation; combine LEARN with SAVE only when you want a saved document.

Mapping activates only when requested. It starts with a compact overview for large repositories and follows source connections instead of reading every file. It can include a Mermaid diagram when useful. It explains where to start a change and which direct consumers and tests to inspect.

The default writes no files and runs no applications, tests, or integrations. SAVE and UPDATE authorize map documentation only. Static source observations do not prove that a service is running or that an integration works. Unknowns and coverage limits remain explicit. Architecture maps complement project checkpoints; they do not replace task state or mark unfinished work verified. Saved maps track inspection context by area: a focused refresh cannot make untouched sections appear current. Relevant changes needing review and unavailable baselines remain visible; elapsed time alone does not invalidate source observations.

Keep generated maps outside the reusable skill. See [Project Mapping](coding-harness/references/PROJECT_MAP.md) for the workflow and [Map Template](coding-harness/assets/templates/PROJECT_MAP.md) for saved output.

## Resources and Usage

| Resource | Purpose |
| --- | --- |
| [Design and Plans](coding-harness/references/DESIGN.md) | Source-grounded design, executable task contracts, and recorded plan corrections |
| [Review](coding-harness/references/REVIEW.md) | Requirement/engineering review and technical assessment of received feedback |
| [Continuity](coding-harness/references/CONTINUITY.md) | Read-only kit health, reconciled resume, and explicit snapshot refresh |
| [Startup](coding-harness/references/STARTUP.md) | Prepare or reuse the complete project-local harness |
| [Kit Index](coding-harness/assets/templates/PROJECT_HARNESS_README.md) | Project harness usage and document pointers |
| [Agent Guidance](coding-harness/assets/templates/PROJECT_AGENT_GUIDANCE.md) | Instructions inside the project harness |
| [SKILL.md](coding-harness/SKILL.md) | Main instructions and selection of the smallest workflow |
| [ENGINEERING.md](coding-harness/references/ENGINEERING.md) | SOLID, KISS, DRY, YAGNI, contracts, security, and testability |
| [WORKFLOW.md](coding-harness/references/WORKFLOW.md) | Retrieval, debugging, verification, review, and checkpoints |
| [Project Mapping](coding-harness/references/PROJECT_MAP.md) | Optional architecture, technology, connection, and change navigation workflow |
| [Map Template](coding-harness/assets/templates/PROJECT_MAP.md) | Blank scaffold for requested saved project maps |
| [STATE.md](coding-harness/references/STATE.md) | State fields, evidence, and verification conditions |
| [PROJECT_STATE.md](coding-harness/assets/templates/PROJECT_STATE.md) | Compact Markdown checkpoint |
| [PROJECT_STATE.json](coding-harness/assets/templates/PROJECT_STATE.json) | Optional structured checkpoint |
| [PROJECT_RECORD.md](coding-harness/assets/templates/PROJECT_RECORD.md) | Longer plans, decisions, and evidence |
| [openai.yaml](coding-harness/agents/openai.yaml) | Metadata and starter prompt for compatible clients |

For ongoing work, reuse project state conventions or choose one canonical Markdown or JSON file in `harness/`. Explicit startup prepares the kit; subsequent small changes and read-only reviews require no additional planning files. Preserve established agent-state/ or other canonical locations. Maintenance state for this source remains in [REPOSITORY_STATE.md](REPOSITORY_STATE.md) and must not be copied into target projects.

In an environment without a skill loader, use [PROJECT_START_PROMPT.md](PROJECT_START_PROMPT.md) and ask the agent to read the source folder. Instructions guide behavior; actual permissions and repository protections determine which operations are available.

## Inspiration and Documentation

Workflow improvements draw on [ECC](https://github.com/affaan-m/ECC), revision `ef648e01899ba3e8dc6371642deaaf64b4477775`: progressive context retrieval, meaningful tests, explicit verification, and checkpoints before phase transitions. The instructions are written for this skill; they include no executable code or substantial text copied from ECC.

Further workflow ideas draw on [superpowers](https://github.com/obra/superpowers), revision `8ca22dba9a94f28898bbce59f2537ff4d87c747d`: concrete task contracts, design tradeoffs, review reception, root-cause tracing, and regression-test integrity. These additions were written independently for this skill; no upstream scripts, hooks, runtime, approval chain, or automatic agent/worktree lifecycle is required.

Client procedures were checked on October 7, 2026 against official documentation:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code: Skills](https://code.claude.com/docs/en/skills)
- [Cursor: Agent Skills](https://cursor.com/docs/skills)

The previous kit was removed from the source; earlier versions remain in Git history.
