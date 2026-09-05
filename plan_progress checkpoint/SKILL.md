---
name: plan-progress-checkpoint
description: >-
  Use when Codex needs to execute a plan, implementation checklist, task document,
  revision plan, test plan, roadmap, or Codex task incrementally. Enforce one
  task unit per run, progress ledger updates, plan status annotations, evidence
  recording, DONE / REVIEW_NEEDED / BLOCKED status discipline, and a hard stop
  after the selected task is completed, reviewed, or blocked.
---

# Plan Progress Checkpoint

## Purpose

Make one traceable unit of progress against a plan:

1. Select one executable task unit.
2. Execute only that task unit.
3. Update the plan with status, evidence, and a Progress Ledger row.
4. Mark uncertainty as REVIEW_NEEDED or blockers as BLOCKED.
5. Stop after the selected task is completed, reviewed, or blocked.

## Reference Routing

Read references only when the situation calls for them:

- Golden Cases v1 plan: `references/golden-cases-v1.md`
- Status, ledger, checkbox, or annotation examples: `references/status-examples.md`
- DONE / REVIEW_NEEDED / BLOCKED judgment, failure handling, or evidence standards: `references/evidence-and-review.md`
- First-time plan initialization with ledger and checklist: `references/first-plan-patch.md`

## Core Rule

Complete at most one task unit per run.

A task unit is the smallest meaningful item that can be independently checked. If the selected task expands into a larger task, split it and complete only the first independently checkable subtask.

Do not execute the next task unless the user explicitly asks to continue, run the next task, or proceed.

## Document Handling

Classify files before editing:

- Specification document: defines what should be built. Do not heavily rewrite it or add long progress logs unless there is no separate plan document.
- Plan document: records phases, implementation order, priorities, acceptance criteria, and progress. Add status annotations and Progress Ledger entries here.
- Output or code files: files required by the selected task. Modify only files required for that task.

When multiple documents exist, prefer updating progress in the plan document.

## Status Labels

Use these labels consistently:

- `TODO`: task has not started.
- `IN_PROGRESS`: task selected for the current run.
- `DONE`: task completed and verified with concrete evidence.
- `REVIEW_NEEDED`: useful work was done, but verification, judgment, data, logs, screenshots, or assumptions still need review.
- `BLOCKED`: task cannot proceed safely because required input, files, dependencies, or project structure are missing or conflicting.

If formatting is unclear, read `references/status-examples.md`.

## Progress Ledger

If the plan document has no Progress Ledger, add one. Keep it append-only.

Required columns:

```md
| Run ID | Date | Selected Task | Status | Evidence | Next Recommended Task |
```

Use one row per agent run. Do not delete previous rows or rewrite history unless the user explicitly asks.

## Task Selection

Before executing:

1. Read the plan document and related specification document.
2. Identify implementation tasks and statuses.
3. Select the first task that is TODO, or REVIEW_NEEDED/BLOCKED and now resolvable.
4. Prefer the smallest task with clear acceptance criteria.
5. Mark only the selected task as IN_PROGRESS before changing code or outputs.

If the plan has no status labels, infer order from implementation order, priority, acceptance criteria, and checklist order. If needed, read `references/first-plan-patch.md`.

## Execution Rules

During execution:

1. Work only on the selected task.
2. Do not silently complete later tasks.
3. Do not rename or rewrite unrelated files.
4. Do not expand the task into a larger framework.
5. Do not introduce out-of-scope features.
6. Do not use real external services when the plan requires stubs or deterministic execution.
7. Capture commands run, outputs checked, files changed, and verification results.

## Evidence Rule

Never mark DONE without concrete evidence.

Concrete evidence may include a created file, implemented function, added test, executed command, passing test, generated output, or specific diff summary.

If tests were not run, verification is uncertain, assumptions were made, or human judgment is required, mark REVIEW_NEEDED instead of DONE. If progress cannot continue safely, mark BLOCKED and state the required input.

## Plan And File Edits

Update only the selected task's status and supporting notes. Put longer run details in the Progress Ledger or final response.

Preserve the plan's existing style when possible, including checkboxes, step numbers, headings, and task names.

Edit only files required by the selected task. Avoid rewriting specification documents unless the selected task is documentation cleanup.

## Failure Handling

If a command or task fails:

1. Capture the failing command or action.
2. Capture the error summary.
3. Decide whether the selected task is REVIEW_NEEDED or BLOCKED.
4. Update the plan and Progress Ledger.
5. Stop without continuing to unrelated tasks.

## Final Response Format

At the end of every run, respond in this exact structure:

```md
## This Run

Selected task:
- ...

Result:
- DONE / REVIEW_NEEDED / BLOCKED

Changed:
- ...

Evidence:
- ...

Issues:
- ...

Plan update:
- ...

Next recommended task:
- ...
```

## Hard Stop

After one task unit is completed, marked REVIEW_NEEDED, or marked BLOCKED, stop.

The agent may recommend the next task but must not execute it.

## Success Criteria

This skill is working correctly when one task is selected, one task is executed, the plan records status and evidence, DONE is evidence-backed, uncertain work is REVIEW_NEEDED, blocked work states required input, and the agent stops after one task.
