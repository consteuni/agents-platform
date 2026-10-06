# Decisions

## D001 - Language-Independent Guide

Adopted: no application code or default stack. The user specifies technologies in the derived project. D009 later adds a stack-independent standard-library validator without changing project technology choices. The historical orchestrator specification is not a kit requirement.

## D002 - One Flat Directory

Superseded by D005. Initially adopted: the whole kit lived in harness/ with internal links and no subdirectories. The rejected alternative was a kit spread outside harness/, making it difficult to copy. The kit remains self-contained, but its internal flat layout has been replaced at the user's request.

## D003 - Separate Git Permissions

Adopted: requested file edits do not authorize changes to branches, history, the index, or publication. Every Git write operation requires a specific request; destructive operations require confirmation of consequences. No automatic branch creation or commits to save checkpoints.

Consequence: guides do not replace branch protections, permissions, or tool approvals. No remote configuration has been performed.

## D004 - English Documentation

Adopted at the user's request: translate the kit, root entry points, and historical reference into English. Filenames and link targets were kept stable during translation. Translation does not turn the historical stack into a default or weaken Git safety rules.

## D005 - Group Documents by Type

Adopted at the user's request: group supporting documents in instructions/, project/, planning/, and verification/ inside harness/. Keep the rules, guide, and PROJECT_STATE documents at the kit root for discovery and quick access. Supersedes the flat layout in D002, not the single-copyable-kit requirement. D008 later changes the two entry-document filenames.

Consequence: relative links cross internal directories but never depend on files outside the kit. Update both links and plain-text paths when reorganizing documents. No new documents, runtime, dependencies, or Git write operations are required.

## D006 - Remove the Obsolete Domain Specification

Adopted at the user's cleanup request: remove the original orchestrator specification because it is unrelated to the language-independent harness and is not needed to use the kit. Remove its active README link and the empty legacy docs/ directory.

Keep the root README for navigation and root AGENTS.md for agent discovery; they are not duplicates of the operating guides. Earlier task and verification records remain historical evidence, not dependencies on the deleted specification. D001 and D004 describe the earlier state before this cleanup.

## D007 - Verifiable Workflow States and Checkpoints

Adopted for TASK-005: require a smallest relevant baseline check before code changes when practical, separate `implemented` from `verified`, and use a structured checkpoint handoff.

Rationale: a persistent document should show whether a failure predated the change and whether acceptance criteria were actually checked. The checkpoint fields make resumption possible without reconstructing session history.

Consequence: the kit documents the protocol but does not enforce it technically. Hooks and CI remain project-specific because the kit has no default stack.

## D008 - Unique Markdown Basenames

Adopted at the user's request: retain conventional `AGENTS.md` and `README.md` names at the repository root, and rename the kit documents to `HARNESS_RULES.md` and `HARNESS_GUIDE.md`.

Rationale: every Markdown document now has a unique basename, while tools can still discover the conventional repository entry points. The root files direct agents and readers to the uniquely named kit documents.

## D009 - Machine State, Validator, and Token Economy

Adopted at the user's request: retain compact `PROJECT_STATE.md`, add minimal `state.json`, include an optional reference validator, and make token economy a permanent agent rule without requiring a programming language.

Rationale: machine state supports reliable resumption and executable consistency checks, while the Markdown state remains readable by humans. The JSON intentionally duplicates only task, status, and next-action essentials. Agents search and read narrowly, bound tool output, and reference canonical documents. Correctness, safety, and required verification take priority over token savings.

Consequence: checkpoints synchronize both state files. Agents validate the same invariants with available tools; `tools/check.py` is an optional shortcut when Python 3 already exists. No language runtime, external package, or project stack is required by the harness.

## In a Derived Project

Keep only relevant decisions; add an ID, date, status, context, choice, rationale, alternatives considered, and consequences. Reserve this log for significant architectural choices and do not duplicate operational state.
