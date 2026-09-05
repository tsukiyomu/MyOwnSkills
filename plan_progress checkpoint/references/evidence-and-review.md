# Evidence And Review

Read this file when deciding whether to mark a task DONE, REVIEW_NEEDED, or BLOCKED.

## Definition Of Done

Mark a task DONE only when all conditions are true:

1. The required change was actually made.
2. The changed file or generated output exists.
3. The result matches the plan.
4. The result does not violate out-of-scope constraints.
5. Concrete evidence exists.
6. No major uncertainty remains.

If tests were not run, do not mark implementation tasks DONE unless the task explicitly did not require execution.

## Review Needed

Use REVIEW_NEEDED aggressively. Do not overclaim completion.

Mark REVIEW_NEEDED when:

1. Code was changed but tests were not run.
2. Tests partially passed.
3. The output depends on user preference.
4. The implementation uses an assumption.
5. The result needs real screenshots, logs, data, deployment output, or manual verification.
6. The task was completed as a draft.
7. Integration with existing project conventions cannot be confirmed.

## Blocked

Use BLOCKED when progress cannot continue safely.

Common blockers:

1. Required files are missing.
2. Dependencies are unavailable.
3. Requirements conflict.
4. Project structure is unknown.
5. A command cannot run because environment information is missing.

When blocked, do not invent missing project structure. State the required input.

## Failure Handling Example

```md
Issues:
- `uv run python -m pytest tests/golden_cases -m golden_case -q` failed because the `golden_case` marker is not registered.

Next recommended task:
- Register the `golden_case` marker in pytest configuration.
```

## Evidence Standards

Bad evidence:

```text
Implemented successfully.
```

Good evidence:

```text
Added `tests/support/golden_cases.py` with `GoldenCase` dataclass and schema error classes.
```

Better evidence:

```text
Added `tests/support/golden_cases.py` with `GoldenCase`, `GoldenCaseSchemaError`, and `GoldenCaseAssertionError`; imported cleanly in pytest collection.
```

## Anti-Patterns

Do not:

1. Mark a task DONE without evidence.
2. Finish all plan steps in one run.
3. Hide assumptions.
4. Convert the whole plan into a new format unnecessarily.
5. Mix progress logs into the specification document when a separate plan exists.
6. Add future-scope features during a constrained v1.
7. Claim tests passed if they were not executed.
8. Use real external services when the plan requires stubs.
9. Overwrite baselines automatically.
10. Use LLM-as-a-Judge for deterministic v1 assertions unless explicitly requested.
