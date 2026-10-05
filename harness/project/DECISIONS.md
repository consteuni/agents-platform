# Decisions

## D001 - Language-Independent Guide

Adopted: documents only, no code or stack. The user specifies technologies in the derived project. The historical orchestrator specification is not a kit requirement.

## D002 - One Flat Directory

Superseded by D005. Initially adopted: the whole kit lived in harness/ with internal links and no subdirectories. The rejected alternative was a kit spread outside harness/, making it difficult to copy. The kit remains self-contained, but its internal flat layout has been replaced at the user's request.

## D003 - Separate Git Permissions

Adopted: requested file edits do not authorize changes to branches, history, the index, or publication. Every Git write operation requires a specific request; destructive operations require confirmation of consequences. No automatic branch creation or commits to save checkpoints.

Consequence: guides do not replace branch protections, permissions, or tool approvals. No remote configuration has been performed.

## D004 - English Documentation

Adopted at the user's request: translate the kit, root entry points, and historical reference into English. Filenames and link targets were kept stable during translation. Translation does not turn the historical stack into a default or weaken Git safety rules.

## D005 - Group Documents by Type

Adopted at the user's request: group supporting documents in instructions/, project/, planning/, and verification/ inside harness/. Keep AGENTS.md, README.md, and PROJECT_STATE.md at the kit root for discovery and quick access. Supersedes the flat layout in D002, not the single-copyable-kit requirement.

Consequence: relative links cross internal directories but never depend on files outside the kit. Update both links and plain-text paths when reorganizing documents. No new documents, runtime, dependencies, or Git write operations are required.

## D006 - Remove the Obsolete Domain Specification

Adopted at the user's cleanup request: remove the original orchestrator specification because it is unrelated to the language-independent harness and is not needed to use the kit. Remove its active README link and the empty legacy docs/ directory.

Keep the root README for navigation and root AGENTS.md for agent discovery; they are not duplicates of the operating guides. Earlier task and verification records remain historical evidence, not dependencies on the deleted specification. D001 and D004 describe the earlier state before this cleanup.

## In a Derived Project

Keep only relevant decisions; add an ID, status, context, choice, rationale, and consequences. Do not duplicate operational state.
