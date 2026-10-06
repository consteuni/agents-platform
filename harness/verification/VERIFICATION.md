# Verification

Tasks: [planning/TASKS.md](../planning/TASKS.md). Human state: [PROJECT_STATE.md](../PROJECT_STATE.md). Machine state: [state.json](../state.json).

For current work, record command or action, result, timestamp, scope, verification level (`targeted`, `regression`, `integration`, or `manual`), and status. Record reproducible pre-existing failures in [KNOWN_FAILURES.md](KNOWN_FAILURES.md).

## TASK-001

These checks were performed on the kit before translation. They do not certify the English version or the categorized layout.

| Check | Tool or Command | Outcome |
| --- | --- | --- |
| Kit Markdown | `get_errors` on the ten kit documents and root entry points | No errors |
| Internal links | Bash extraction with grep and internal path checks | All resolved; no external dependencies |
| State size | `wc -l harness/PROJECT_STATE.md` | 44 lines before translation |
| Tracked diff | `git diff --check` and `git diff -- README.md` | No whitespace errors; changes reviewed |
| New files | `git diff --no-index -- /dev/null` for each kit document and root AGENTS.md | Diffs reviewed; documentation only |
| Potential secrets | `grep_search`: private keys, AWS/GitHub credential formats, and credential assignments | No matches for the searched patterns |
| Software tests/build | No runtime configured | Not applicable |
| Technical branch protections | No remote configuration authorized | Not performed |

## TASK-002

These checks describe the translated flat layout before TASK-003.

| Check | Tool or Command | Outcome |
| --- | --- | --- |
| English documentation and preserved safety rules | Translation review and `grep_search` for common remaining Italian words | No matches for the searched words; filenames, identifiers, and Git restrictions preserved |
| Markdown | `get_errors` on all 13 documents | No errors; historical heading hierarchy and URL formatting corrected |
| Local links | Bash link extraction with grep and relative file existence checks | All local links resolved; harness links stay inside the kit |
| State size | `wc -l harness/PROJECT_STATE.md` | Within 100 lines |
| Tracked diff | `git diff --check` and `git diff -- README.md` | No whitespace errors; diff reviewed |
| New documents | `git diff --no-index --check -- /dev/null` for root AGENTS.md, the historical reference, and harness documents | No whitespace errors |
| Potential secrets | `grep_search`: private keys, AWS/GitHub credential formats, and credential assignments across Markdown documents | No matches for the searched patterns |
| Branch | `git status --short --branch` | Still main; no Git write operations or remote actions performed |
| Software tests and technical branch protections | No runtime; no protection configuration authorized | Not performed; documentation checks do not prove technical enforcement |

## TASK-003

| Check | Tool or Command | Outcome |
| --- | --- | --- |
| Categorized layout and preserved documents | Bash document list: `harness/*.md` and `harness/*/*.md` | Exactly ten documents; root entry points preserved |
| Links and kit independence | Extract links with grep, resolve each using `realpath -m`, and check path boundaries and existence | All links resolve inside harness/ |
| Markdown | `get_errors` on the ten kit documents; repeat on README after fixing diagram tabs | No errors |
| State size | `wc -l harness/PROJECT_STATE.md` | Within 100 lines |
| Diffs and whitespace | `git diff --no-index --check -- /dev/null` on all kit documents; review `git diff --no-index -- /dev/null harness/AGENTS.md` | No whitespace errors; safety rules unchanged except updated links |
| Potential secrets | `grep_search` within harness/: private keys, AWS/GitHub credential formats, and credential assignments | No matches for the searched patterns |
| Branch and operations | Initial `git status --short --branch` and review of operations performed | Branch main; no Git write operations or remote actions performed |

## TASK-004

The obsolete domain specification and its active README link were removed. The legacy docs/ directory was inspected and found empty before removal with `rmdir docs`; no recursive cleanup was used. Earlier verification records describe the files present at the time, not dependencies on deleted material.

| Check | Tool or Command | Outcome |
| --- | --- | --- |
| Surviving documents | `file_search` for Markdown files | Twelve documents remain: ten in harness/ and two root entry points |
| Links and removed specification | Bash extraction with grep, relative existence checks, and deleted-file absence check | All surviving document links resolve; obsolete specification absent |
| Markdown | `get_errors` on root README, PLAN, TASKS, DECISIONS, and PROJECT_STATE | No errors |
| Diffs and whitespace | `git diff --check`, review of `git diff -- README.md`, and `git diff --no-index --check -- /dev/null` on updated kit documents | No whitespace errors; root README preserves discovery and safety guidance |
| Potential secrets | `grep_search` across Markdown documents for private keys, AWS/GitHub credential formats, and credential assignments | No matches for the searched patterns |
| Branch and operations | Initial `git status --short --branch` and review of operations performed | Branch main; no Git write operations, branch changes, or remote actions performed |

## TASK-005

| Check | Tool or Command | Outcome |
| --- | --- | --- |
| Baseline | `git status --short --branch` before edits | Branch `main`; no runtime baseline exists because this is a documentation-only repository |
| Workflow rules | Review `harness/AGENTS.md`, `planning/TASKS.md`, and `project/DECISIONS.md` | Pass; baseline, status, and checkpoint rules are present |
| Checkpoint fields | Review the `CHECKPOINT` template in `harness/AGENTS.md` | Pass; all required handoff fields are present |
| Markdown and links | `git diff --check`; shell link resolution across Markdown; ten-file count; state line count | Pass; no whitespace errors, all local links resolve, ten kit documents, state is 43 lines |
| Potential secrets | Recursive Markdown scan for private-key, AWS, and GitHub credential patterns | No matches for searched patterns |
| Git safety | Review commands performed | No Git write operations, branch changes, or remote actions performed |

Status: verified.

## TASK-006

Earlier task records retain the filenames that existed when their checks ran. Current documents use the unique names introduced by this task.

| Check | Tool or Command | Outcome |
| --- | --- | --- |
| Unique Markdown names | `find` basenames, `sort`, and `uniq -d` across the working tree | Pass; no duplicate Markdown basenames |
| Renamed entry documents | File listing and reference search | Pass; kit entry documents are `HARNESS_RULES.md` and `HARNESS_GUIDE.md`; conventional root names remain |
| Local links | Shell extraction and relative existence checks across Markdown documents | Pass; all local links resolve |
| Kit independence | Resolve links from every kit document and compare them with the `harness/` boundary | Pass; all kit links remain inside `harness/` |
| Structure and state size | Markdown file count and `wc -l harness/PROJECT_STATE.md` | Pass; ten kit documents and state below 100 lines |
| Diffs and Git safety | `git diff --check`, `git diff --cached --check`, and operation review | Pass; no whitespace errors and no Git write operations performed |

Status: verified.

## TASK-007

| Level | Command or Action | Result | Timestamp | Scope | Status |
| --- | --- | --- | --- | --- | --- |
| Targeted | `python harness/tools/check.py` | Python launcher alias unavailable in this environment; canonical command changed to `python3` | 2026-10-06T12:10:52+02:00 | Validator launcher | NOT RUN |
| Targeted | `python3 harness/tools/check.py` | Structure, state, task consistency, links, and safety passed; 0 warnings and 0 errors | 2026-10-06T12:10:52+02:00 | Harness invariants | PASS |
| Regression | `jq` state contract check; repository link, basename, line-count, whitespace, secret-pattern, and Git diff checks | Valid 10-line state; all links resolve; unique Markdown basenames; 52-line human state; no whitespace or searched secret-pattern findings | 2026-10-06T12:10:52+02:00 | Machine state and repository documentation | PASS |

The machine and human states agree on TASK-007, `verified`, and the executable next action. No known failures or blockers are recorded.

Status: verified.

## Limitations

Pattern searches do not guarantee the absence of every secret. The validator checks consistency and obvious patterns but cannot technically prevent dangerous commands: tool permissions, approvals, and repository protections remain required. No software integrations are tested here. No Git write operations, branch changes, or remote actions have been performed for this work.

## In a Derived Project

Replace kit checks with project-specific checks. For each check, record the task, actual command or tool, outcome, blockers, and residual risk. Do not include full output or sensitive data, or present a mock as real validation.
