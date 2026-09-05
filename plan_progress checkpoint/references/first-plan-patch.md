# First Plan Patch

Read this file when the plan has no Progress Ledger and no task status labels.

Add a Progress Ledger and a current execution checklist. Adapt task names to the actual plan. Do not force Golden Cases task names onto unrelated plans.

## Generic Template

```md
## Progress Ledger

| Run ID | Date | Selected Task | Status | Evidence | Next Recommended Task |
|---|---|---|---|---|---|

## Current Execution Checklist

- [TODO] Step 1: First independently checkable task.
- [TODO] Step 2: Second independently checkable task.
- [TODO] Step 3: Third independently checkable task.
```

Then select only Step 1 for the current run.

## Golden Cases v1 Template

Use this only for Golden Cases v1 plans.

```md
## Progress Ledger

| Run ID | Date | Selected Task | Status | Evidence | Next Recommended Task |
|---|---|---|---|---|---|

## Current Execution Checklist

- [TODO] Step 1: Create schema dataclass and schema error classes.
- [TODO] Step 2: Implement file discovery and loader.
- [TODO] Step 3: Add four minimal case files.
- [TODO] Step 4: Implement runner with stub LLM and stub tool results.
- [TODO] Step 5: Implement assertion checker.
- [TODO] Step 6: Add pytest parametrized entry file.
- [TODO] Step 7: Register golden_case marker.
- [TODO] Step 8: Run local pytest command and fix failures.
```

Then execute only Step 1 unless it is already complete.
