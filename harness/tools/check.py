#!/usr/bin/env python3
"""Validate the copied harness with Python's standard library only."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "state.json"
TASKS_PATH = ROOT / "planning" / "TASKS.md"
PROJECT_STATE_PATH = ROOT / "PROJECT_STATE.md"
VERIFICATION_PATH = ROOT / "verification" / "VERIFICATION.md"

REQUIRED_FILES = (
    "HARNESS_GUIDE.md",
    "HARNESS_RULES.md",
    "PROJECT_STATE.md",
    "state.json",
    "instructions/AGENT_CONTEXT.md",
    "planning/PLAN.md",
    "planning/TASKS.md",
    "project/ARCHITECTURE.md",
    "project/DECISIONS.md",
    "project/PROJECT_BRIEF.md",
    "verification/KNOWN_FAILURES.md",
    "verification/VERIFICATION.md",
    "tools/check.py",
)
REQUIRED_DIRS = ("instructions", "planning", "project", "verification", "tools")
REQUIRED_STATE_FIELDS = {
    "schema_version",
    "status",
    "current_task",
    "branch",
    "last_checkpoint",
    "next_action",
    "blocked_by",
    "verified",
}
VALID_STATUSES = {"pending", "in_progress", "implemented", "verified", "blocked"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
TASK_RE = re.compile(r"^## (TASK-\d+)\b[^\n]*$", re.MULTILINE)
SECRET_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    (
        "credential assignment",
        re.compile(
            r"(?i)\b(?:password|secret|api[_-]?key|access[_-]?token)\s*[:=]\s*"
            r"[\"'][^\"'\n]{8,}[\"']"
        ),
    ),
)
CATEGORIES = ("structure", "state", "task consistency", "links", "safety")


class Report:
    def __init__(self) -> None:
        self.errors: dict[str, list[str]] = {category: [] for category in CATEGORIES}
        self.warnings: list[str] = []

    def error(self, category: str, message: str) -> None:
        self.errors[category].append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def error_count(self) -> int:
        return sum(len(messages) for messages in self.errors.values())

    def print(self) -> None:
        print("Harness validation\n")
        for category in CATEGORIES:
            messages = self.errors[category]
            if messages:
                print(f"FAIL {category}")
                for message in messages:
                    print(f"  - {message}")
            else:
                print(f"PASS {category}")
        for warning in self.warnings:
            print(f"WARN {warning}")
        print(f"\n{len(self.warnings)} warning(s)")
        print(f"{self.error_count} error(s)")


def read_text(path: Path, report: Report, category: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(category, f"cannot read {path.relative_to(ROOT)}: {exc}")
        return ""


def markdown_section(text: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$\n+(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def task_sections(text: str) -> list[tuple[str, str]]:
    matches = list(TASK_RE.finditer(text))
    return [
        (match.group(1), text[match.start() : matches[index + 1].start()])
        for index, match in enumerate(matches)
        if index + 1 < len(matches)
    ] + ([(matches[-1].group(1), text[matches[-1].start() :])] if matches else [])


def check_structure(report: Report) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            report.error("structure", f"missing required file: {relative}")
    for relative in REQUIRED_DIRS:
        if not (ROOT / relative).is_dir():
            report.error("structure", f"missing required directory: {relative}")


def load_state(report: Report) -> dict[str, object] | None:
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error("state", f"state.json is not valid readable JSON: {exc}")
        return None
    if not isinstance(state, dict):
        report.error("state", "state.json root must be an object")
        return None
    missing = sorted(REQUIRED_STATE_FIELDS - state.keys())
    if missing:
        report.error("state", f"missing fields: {', '.join(missing)}")
    return state


def check_state(state: dict[str, object] | None, report: Report) -> None:
    if state is None:
        return
    if state.get("schema_version") != 1:
        report.error("state", "schema_version must be 1")
    status = state.get("status")
    if status not in VALID_STATUSES:
        report.error("state", f"invalid status: {status!r}")
    current_task = state.get("current_task")
    if current_task is not None and not isinstance(current_task, str):
        report.error("state", "current_task must be a string or null")
    if not isinstance(state.get("branch"), str) or not state.get("branch"):
        report.error("state", "branch must be a non-empty string")
    checkpoint = state.get("last_checkpoint")
    if checkpoint is not None:
        if not isinstance(checkpoint, str):
            report.error("state", "last_checkpoint must be an ISO-8601 string or null")
        else:
            try:
                datetime.fromisoformat(checkpoint)
            except ValueError:
                report.error("state", "last_checkpoint must be valid ISO-8601")
    next_action = state.get("next_action")
    if next_action is not None and not isinstance(next_action, str):
        report.error("state", "next_action must be a string or null")
    if status != "verified" and not next_action:
        report.error("state", "next_action is required while work is incomplete")
    blocked_by = state.get("blocked_by")
    if not isinstance(blocked_by, list):
        report.error("state", "blocked_by must be an array")
    elif status == "blocked" and not blocked_by:
        report.error("state", "blocked status requires at least one blocker")
    verified = state.get("verified")
    if not isinstance(verified, bool):
        report.error("state", "verified must be a boolean")
    elif verified != (status == "verified"):
        report.error("state", "verified must be true exactly when status is verified")


def check_tasks(state: dict[str, object] | None, report: Report) -> None:
    tasks_text = read_text(TASKS_PATH, report, "task consistency")
    verification_text = read_text(VERIFICATION_PATH, report, "task consistency")
    sections = task_sections(tasks_text)
    ids = [task_id for task_id, _ in sections]
    duplicates = sorted({task_id for task_id in ids if ids.count(task_id) > 1})
    if duplicates:
        report.error("task consistency", f"duplicate task IDs: {', '.join(duplicates)}")
    statuses: dict[str, str] = {}
    for task_id, section in sections:
        status_match = re.search(r"^Status:\s*(\w+)\s*$", section, re.MULTILINE)
        if not status_match:
            report.error("task consistency", f"{task_id} has no Status field")
            continue
        status = status_match.group(1)
        statuses[task_id] = status
        if status not in VALID_STATUSES:
            report.error("task consistency", f"{task_id} has invalid status {status!r}")
        if "acceptance" not in section.lower():
            report.error("task consistency", f"{task_id} has no acceptance criteria")
        if status == "verified" and f"## {task_id}" not in verification_text:
            report.error("task consistency", f"{task_id} is verified without evidence")
    if state is None:
        return
    current_task = state.get("current_task")
    if current_task is not None:
        if current_task not in statuses:
            report.error("task consistency", f"current task {current_task!r} does not exist")
        elif state.get("status") != statuses[current_task]:
            report.error("task consistency", "state status does not match current task status")
        current_evidence = re.search(
            rf"^## {re.escape(str(current_task))}\s*$\n(.*?)(?=^## |\Z)",
            verification_text,
            re.MULTILINE | re.DOTALL,
        )
        if current_evidence:
            for field in ("Command", "Result", "Timestamp", "Scope", "Level", "Status"):
                if field not in current_evidence.group(1):
                    report.error("task consistency", f"{current_task} evidence lacks {field}")


def check_project_state(state: dict[str, object] | None, report: Report) -> None:
    if state is None:
        return
    text = read_text(PROJECT_STATE_PATH, report, "state")
    comparisons = {
        "Current Task": state.get("current_task"),
        "Status": state.get("status"),
        "Next Action": state.get("next_action"),
    }
    for heading, expected in comparisons.items():
        actual = markdown_section(text, heading)
        expected_text = "None." if expected is None else str(expected)
        if actual != expected_text:
            report.error("state", f"PROJECT_STATE.md {heading!r} does not match state.json")


def check_links(report: Report) -> None:
    root_resolved = ROOT.resolve()
    for path in sorted(ROOT.rglob("*.md")):
        text = read_text(path, report, "links")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            if Path(target).is_absolute() or re.match(r"^[A-Za-z]:[\\/]", target):
                report.error("safety", f"absolute local link in {path.relative_to(ROOT)}: {target}")
                continue
            resolved = (path.parent / target).resolve()
            if root_resolved not in (resolved, *resolved.parents):
                report.error("links", f"link escapes harness: {path.relative_to(ROOT)} -> {target}")
            elif not resolved.exists():
                report.error("links", f"broken link: {path.relative_to(ROOT)} -> {target}")


def check_safety(report: Report) -> None:
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".json"}:
            continue
        text = read_text(path, report, "safety")
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                report.error("safety", f"possible {name} in {path.relative_to(ROOT)}")


def main() -> int:
    report = Report()
    check_structure(report)
    state = load_state(report)
    check_state(state, report)
    check_tasks(state, report)
    check_project_state(state, report)
    check_links(report)
    check_safety(report)
    report.print()
    return 1 if report.error_count else 0


if __name__ == "__main__":
    sys.exit(main())
