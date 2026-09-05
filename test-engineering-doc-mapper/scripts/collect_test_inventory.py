#!/usr/bin/env python3
"""Collect a deterministic pytest-oriented repository inventory."""

from __future__ import annotations

import argparse
import ast
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


CONFIG_NAMES = ("pyproject.toml", "pytest.ini", "setup.cfg", "tox.ini")
TEST_FILE_PATTERNS = ("test_*.py", "*_test.py")


@dataclass
class TestItem:
    file: str
    node: str
    line: int
    async_test: bool
    markers: list[str]
    fixtures: list[str]
    uses_monkeypatch: bool


@dataclass
class FixtureItem:
    file: str
    node: str
    line: int
    async_fixture: bool


def dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    if isinstance(node, ast.Call):
        return dotted_name(node.func)
    return ""


def marker_names(decorators: Iterable[ast.expr]) -> list[str]:
    markers: set[str] = set()
    for decorator in decorators:
        name = dotted_name(decorator)
        match = re.search(r"(?:^|\.)pytest\.mark\.([A-Za-z_][A-Za-z0-9_]*)$", name)
        if match:
            markers.add(match.group(1))
    return sorted(markers)


def is_fixture(decorators: Iterable[ast.expr]) -> bool:
    return any(dotted_name(item).endswith(("pytest.fixture", ".fixture")) for item in decorators)


def function_args(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    args = [item.arg for item in node.args.posonlyargs]
    args.extend(item.arg for item in node.args.args)
    args.extend(item.arg for item in node.args.kwonlyargs)
    return [item for item in args if item not in {"self", "cls"}]


def iter_test_files(tests_root: Path) -> list[Path]:
    files: set[Path] = set()
    for pattern in TEST_FILE_PATTERNS:
        files.update(tests_root.rglob(pattern))
    return sorted(path for path in files if path.is_file())


def inspect_test_file(path: Path, repo_root: Path) -> tuple[list[TestItem], list[FixtureItem], list[str]]:
    errors: list[str] = []
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except (OSError, UnicodeError, SyntaxError) as exc:
        return [], [], [f"{path}: {exc}"]

    relative = path.relative_to(repo_root).as_posix()
    tests: list[TestItem] = []
    fixtures: list[FixtureItem] = []

    def visit(body: list[ast.stmt], class_name: str | None = None) -> None:
        for item in body:
            if isinstance(item, ast.ClassDef):
                visit(item.body, item.name)
                continue
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            qualified = f"{class_name}::{item.name}" if class_name else item.name
            if is_fixture(item.decorator_list):
                fixtures.append(
                    FixtureItem(relative, qualified, item.lineno, isinstance(item, ast.AsyncFunctionDef))
                )
            if item.name.startswith("test_"):
                args = sorted(function_args(item))
                tests.append(
                    TestItem(
                        file=relative,
                        node=qualified,
                        line=item.lineno,
                        async_test=isinstance(item, ast.AsyncFunctionDef),
                        markers=marker_names(item.decorator_list),
                        fixtures=args,
                        uses_monkeypatch="monkeypatch" in args,
                    )
                )

    visit(tree.body)
    return tests, fixtures, errors


def find_ci_commands(repo_root: Path) -> tuple[list[str], list[dict[str, object]]]:
    workflow_root = repo_root / ".github" / "workflows"
    files: list[str] = []
    commands: list[dict[str, object]] = []
    if not workflow_root.exists():
        return files, commands
    for path in sorted((*workflow_root.glob("*.yml"), *workflow_root.glob("*.yaml"))):
        relative = path.relative_to(repo_root).as_posix()
        files.append(relative)
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            continue
        for number, line in enumerate(lines, start=1):
            if re.search(r"\b(pytest|tox|nox)\b", line, flags=re.IGNORECASE):
                commands.append({"file": relative, "line": number, "text": line.strip()})
    return files, commands


def collect(repo_root: Path, tests_dir: str) -> dict[str, object]:
    tests_root = (repo_root / tests_dir).resolve()
    if not tests_root.is_dir():
        raise ValueError(f"tests directory not found: {tests_root}")

    tests: list[TestItem] = []
    fixtures: list[FixtureItem] = []
    errors: list[str] = []
    files = iter_test_files(tests_root)
    for path in files:
        file_tests, file_fixtures, file_errors = inspect_test_file(path, repo_root)
        tests.extend(file_tests)
        fixtures.extend(file_fixtures)
        errors.extend(file_errors)

    config_files = [name for name in CONFIG_NAMES if (repo_root / name).is_file()]
    workflow_files, ci_commands = find_ci_commands(repo_root)
    marker_counts: dict[str, int] = {}
    for item in tests:
        for marker in item.markers:
            marker_counts[marker] = marker_counts.get(marker, 0) + 1

    return {
        "repo_root": str(repo_root),
        "tests_root": tests_root.relative_to(repo_root).as_posix(),
        "summary": {
            "test_files": len(files),
            "tests": len(tests),
            "fixtures": len(fixtures),
            "monkeypatch_tests": sum(item.uses_monkeypatch for item in tests),
        },
        "marker_counts": dict(sorted(marker_counts.items())),
        "config_files": config_files,
        "workflow_files": workflow_files,
        "ci_test_commands": ci_commands,
        "tests": [asdict(item) for item in tests],
        "fixtures": [asdict(item) for item in fixtures],
        "parse_errors": errors,
    }


def markdown_report(inventory: dict[str, object]) -> str:
    summary = inventory["summary"]
    lines = [
        "# Test Inventory",
        "",
        f"- Repository: `{inventory['repo_root']}`",
        f"- Tests root: `{inventory['tests_root']}`",
        f"- Test files: {summary['test_files']}",
        f"- Tests: {summary['tests']}",
        f"- Fixtures: {summary['fixtures']}",
        f"- Tests using monkeypatch fixture: {summary['monkeypatch_tests']}",
        "",
        "## Configuration",
        "",
    ]
    for item in inventory["config_files"]:
        lines.append(f"- `{item}`")
    if not inventory["config_files"]:
        lines.append("- None found")

    lines.extend(["", "## CI Test Commands", ""])
    for item in inventory["ci_test_commands"]:
        lines.append(f"- `{item['file']}:{item['line']}`: `{item['text']}`")
    if not inventory["ci_test_commands"]:
        lines.append("- None found")

    lines.extend(["", "## Tests", "", "| File | Test | Line | Markers | Fixtures | Monkeypatch |", "|---|---|---:|---|---|---|"])
    for item in inventory["tests"]:
        markers = ", ".join(item["markers"]) or "-"
        fixtures = ", ".join(item["fixtures"]) or "-"
        monkeypatch = "yes" if item["uses_monkeypatch"] else "no"
        lines.append(f"| `{item['file']}` | `{item['node']}` | {item['line']} | {markers} | {fixtures} | {monkeypatch} |")

    if inventory["parse_errors"]:
        lines.extend(["", "## Parse Errors", ""])
        lines.extend(f"- {item}" for item in inventory["parse_errors"])
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_root", type=Path)
    parser.add_argument("--tests-dir", default="tests")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    if not repo_root.is_dir():
        raise SystemExit(f"repository root not found: {repo_root}")
    try:
        inventory = collect(repo_root, args.tests_dir)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    output = (
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n"
        if args.format == "json"
        else markdown_report(inventory)
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
