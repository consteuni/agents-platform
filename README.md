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

## Resources and Usage

| Resource | Purpose |
| --- | --- |
| [SKILL.md](coding-harness/SKILL.md) | Main instructions and selection of the smallest workflow |
| [ENGINEERING.md](coding-harness/references/ENGINEERING.md) | SOLID, KISS, DRY, YAGNI, contracts, security, and testability |
| [WORKFLOW.md](coding-harness/references/WORKFLOW.md) | Retrieval, debugging, verification, review, and checkpoints |
| [STATE.md](coding-harness/references/STATE.md) | State fields, evidence, and verification conditions |
| [PROJECT_STATE.md](coding-harness/assets/templates/PROJECT_STATE.md) | Compact Markdown checkpoint |
| [PROJECT_STATE.json](coding-harness/assets/templates/PROJECT_STATE.json) | Optional structured checkpoint |
| [PROJECT_RECORD.md](coding-harness/assets/templates/PROJECT_RECORD.md) | Longer plans, decisions, and evidence |
| [openai.yaml](coding-harness/agents/openai.yaml) | Metadata and starter prompt for compatible clients |

For ongoing work, reuse project state conventions or choose one canonical Markdown or JSON file in `agent-state/`. Small changes and reviews require no new planning files. Maintenance state for this source remains in [REPOSITORY_STATE.md](REPOSITORY_STATE.md) and must not be copied into target projects.

In an environment without a skill loader, use [PROJECT_START_PROMPT.md](PROJECT_START_PROMPT.md) and ask the agent to read the source folder. Instructions guide behavior; actual permissions and repository protections determine which operations are available.

## Inspiration and Documentation

Workflow improvements draw on [ECC](https://github.com/affaan-m/ECC), revision `ef648e01899ba3e8dc6371642deaaf64b4477775`: progressive context retrieval, meaningful tests, explicit verification, and checkpoints before phase transitions. The instructions are written for this skill; they include no executable code or substantial text copied from ECC.

Client procedures were checked on October 7, 2026 against official documentation:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code: Skills](https://code.claude.com/docs/en/skills)
- [Cursor: Agent Skills](https://cursor.com/docs/skills)

The previous kit was removed from the source; earlier versions remain in Git history.
