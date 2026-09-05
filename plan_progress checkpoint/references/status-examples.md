# Status Examples

Read this file when status annotation format is unclear.

## Task Status Formats

```md
- [TODO] Task name
```

```md
- [IN_PROGRESS] Task name
```

```md
- [DONE] Task name
  - Completed in: run-001
  - Evidence: Added `tests/support/golden_cases.py` with schema classes and imported it successfully.
  - Notes: Kept validation simple and deterministic.
```

```md
- [REVIEW_NEEDED] Task name
  - Completed in: run-004
  - Evidence: Added runner code and stub dispatcher.
  - Issue: Local pytest was not executed, so integration is unverified.
  - Suggested next step: Run the golden case pytest command and fix failures.
```

```md
- [BLOCKED] Task name
  - Reason: Cannot locate the real `run_agentic_loop` import path.
  - Required input: Confirm module path or provide the project tree.
```

## Progress Ledger Example

```md
## Progress Ledger

| Run ID | Date | Selected Task | Status | Evidence | Next Recommended Task |
|---|---|---|---|---|---|
| run-001 | 2026-06-17 | Create schema dataclass and schema error classes | DONE | Added `GoldenCase`, `GoldenCaseSchemaError`, and `GoldenCaseAssertionError` | Implement file discovery and loader |
```

## Plan Annotation Example

When the plan has plain steps:

```md
Step 1: Create schema dataclass and schema error classes.
Step 2: Implement file discovery and loader.
Step 3: Add four minimal case files.
```

Rewrite only the selected item:

```md
Step 1: [DONE] Create schema dataclass and schema error classes.
  - Completed in: run-001
  - Evidence: Added `GoldenCase`, `GoldenCaseSchemaError`, and `GoldenCaseAssertionError`.
  - Notes: Kept validation simple and readable.
Step 2: [TODO] Implement file discovery and loader.
Step 3: [TODO] Add four minimal case files.
```

When the plan already uses checkboxes, preserve them:

```md
- [x] [DONE] Create schema dataclass and schema error classes.
- [ ] [TODO] Implement file discovery and loader.
```

Do not add long logs under every task. Put long run details in the Progress Ledger or final response.
