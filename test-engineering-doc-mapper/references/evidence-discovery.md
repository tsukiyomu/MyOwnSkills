# Evidence Discovery

Use this workflow before creating, updating, or auditing testing documentation.

## Locate Sources

Identify:

1. Repository root and test directories
2. Target testing document
3. Architecture, Part, or workflow documents
4. Production entry points named by tests
5. Shared fixtures, fakes, stubs, spies, and test helpers
6. `pyproject.toml`, `pytest.ini`, `setup.cfg`, or `tox.ini`
7. `.github/workflows`, other CI definitions, and quality-gate publishers

Prefer `rg --files` and `rg` for discovery.

Useful searches:

```text
rg --files tests .github docs
rg -n "def test_|async def test_|pytest.mark|xfail|monkeypatch" tests
rg -n "pytest|coverage|quality.gate|workflow_dispatch|pull_request" .github pyproject.toml pytest.ini setup.cfg tox.ini
rg -n "run_agentic_loop|finalize|cleanup|active|publish|report" tests src app apiserver
```

Adapt paths to the repository. Do not assume every directory exists.

## Optional Inventory Script

For Python/pytest repositories, run:

```bash
python scripts/collect_test_inventory.py <repo-root> --format markdown
```

Use the generated inventory as a discovery aid, not as proof of runtime semantics. Read representative test bodies and helpers before describing what tests prove.

## Build An Evidence Inventory

For each important suite or test, record:

| Field | Evidence |
|---|---|
| Test file and symbol | Exact path and test name |
| Architecture owner | Owning module or boundary |
| Production entry | Route, function, class, or workflow |
| Assertions | Concrete asserted fields or events |
| Real parts | Components executed without replacement |
| Controlled parts | Fake, stub, monkeypatch, spy, fixture, or environment control |
| Run command | Local or CI command found in configuration |
| Gate status | Blocking, non-blocking, opt-in, nightly, staging, or unwired |
| Implementation status | LANDED, PARTIAL, PLANNED, XFAIL_GAP, or INFERRED |
| Failure meaning | Most likely contract or infrastructure failure |

## Evidence Rules

- A test name is not enough to establish semantics; inspect its body and helpers.
- A fixture name is not enough to establish authenticity; inspect what it replaces.
- A documentation claim is not implementation evidence.
- A local command in documentation is not a CI gate until the workflow invokes it.
- A test file existing does not mean it is collected, enabled, or passing.
- Do not say tests pass unless they were executed successfully in the current environment or a trusted result was provided.
- Prefer exact symbols and paths over broad statements.

## Claim Status

Use:

- `LANDED` for directly observed implementation.
- `PARTIAL` when only part of the described workflow or contract is present.
- `PLANNED` when documentation describes future implementation.
- `XFAIL_GAP` for executable expected failures.
- `INFERRED` when evidence supports a conclusion indirectly.

When evidence conflicts, prefer current code and configuration, record the conflict, and avoid silently rewriting history.
