---
name: plan-progress-checkpoint
description: >-
  Track scoped execution of an existing plan: select a runnable work unit,
  preserve its acceptance boundary, maintain task status and a compact progress
  ledger, and hand off the next step. Use for incremental plan execution or
  progress reconciliation; engineering decision explanations and execution
  reports belong to their respective rationale and journal skills.
---

# Plan Progress Checkpoint

## Responsibility

Own selection, status, plan progress, and handoff. Keep each work unit traceable
without turning its plan into another execution report.

- The **plan** owns intent: what, why, work units, requirements, boundaries, acceptance, dependencies, and order.
- **Repository instructions and project/language rules** provide the stable coding and engineering constraints.
- The **agent** executes and verifies the work, choosing its implementation method from the actual repository within the Plan and rules.
- The **execution rationale** explains evidence, engineering concerns, implementation decisions, their effects, and verification limits; it does not prescribe an execution workflow.
- The **journal** records final outcomes, material deviations, evidence, proof limits, and the next step.
- The **re-entry guide** derives a short navigation snapshot from those sources; it does not own status.

Use `evidence-backed-execution-rationale` when material engineering choices need
explanation and `evidence-backed-work-unit-journal` when the task includes a final
execution report. Neither is required to register progress. Do not impose a second
implementation workflow or report template; this skill does not require extra documents.

For a progress-reconciliation-only request, inspect the relevant evidence and
update only the requested status/history. Do not start implementation or mark a
unit `IN_PROGRESS` merely to assess it. The selection workflow below applies when
execution is part of the user's request.

## Select And Preserve Scope

1. Read the current plan and relevant specification or architecture links. Reuse
   its unit IDs, task names, acceptance criteria, and progress location.
2. Honor a unit or batch already selected by the user. Otherwise select one
   meaningful, independently verifiable unit whose dependencies are satisfied,
   following the plan's priorities and order. A resolvable `REVIEW_NEEDED` or
   `BLOCKED` unit may be the best next step; do not blindly select the first `TODO`.
3. Confirm enough of the contract exists to execute. Investigate routine repository
   facts locally. Ask only when a material intent, scope, or acceptance ambiguity
   cannot be resolved from the plan and existing user instructions.
4. Mark the selected unit `IN_PROGRESS` (or its existing project equivalent) in the progress structure before
   changing its outputs. If there is already an active entry, resume it instead
   of creating another task.

Hand the selected unit and its current status/context to the executing agent under
the Plan, repository instructions, and applicable project/language rules. The same
agent can continue the work; this handoff does not require delegation. Material
engineering choices use the Execution Rationale explanation contract, not an
executor skill. Register the resulting status from outcome evidence as described
in Record Progress Once.

Default to one selected unit per run. An explicit request to finish a batch or the
whole plan overrides that default and remains in force across turns and handoffs.
Do not silently shrink an accepted unit to its first implementation fragment and
then mark the original unit `DONE`. Internal subtasks may help execution, but the
original acceptance boundary still governs completion. If a real scope change is
necessary, record it and leave unfinished acceptance visible.

## Status And Recovery

Preserve the project's existing status vocabulary and meanings, mapping these
transitions to its equivalents. Use the labels below only when the project has
no defined scheme; do not introduce a parallel status system.

| Status | Meaning |
|---|---|
| `TODO` | Not started. |
| `IN_PROGRESS` | Active authorized work, including recoverable failures being fixed. |
| `DONE` | The selected unit's acceptance is satisfied by current, relevant evidence. |
| `REVIEW_NEEDED` | Work is available, but required verification or a material judgment remains unresolved. |
| `BLOCKED` | The selected unit cannot make meaningful progress without a missing prerequisite, authorization, or external input. |

Use evidence proportional to acceptance. Documentation can be `DONE` after
appropriate content, link, or rendered-output inspection; code tests are not a
universal requirement. If acceptance requires tests or integration evidence and
they are missing, keep the result `REVIEW_NEEDED`. A file's existence alone does
not prove behavior. Ordinary implementation choices or disclosed, resolved
assumptions do not automatically require human review.

Fix recoverable failures inside the authorized unit and recheck the affected
acceptance. A failed command is evidence to investigate, not an automatic stop.
Use `BLOCKED` only after reasonable local investigation or recovery shows that a
prerequisite is actually unavailable; name it and the action needed to resume.
Do not add a permission checkpoint for already authorized work.

## Record Progress Once

Preserve the plan's existing checklist, tracker, and ledger design. If an equivalent
execution history already exists in a linked progress file, use it; do not create
a duplicate ledger or a parallel checklist. When no history exists, add a compact
ledger to the plan or its established progress file:

```md
| Run ID | Date | Selected Task | Status | Evidence / Report | Next Recommended Task |
|---|---|---|---|---|---|
```

Keep history append-only. Use one outcome row per **logical selected-unit run**,
not per tool call, retry, assistant turn, or subagent. Resume unfinished work under
the same run ID; a later, separate attempt after a recorded outcome gets a new
row referencing the earlier one. An authorized batch can contain multiple unit
rows without requiring permission between them.

At completion or handoff:

- Update the selected unit's current status in place. Check its box only for `DONE`
  or the project's equivalent accepted-completion state.
- Append the outcome row with a short result and links to the journal or evidence.
- Keep acceptance in its original plan location. Record only material contract
  changes or unresolved acceptance beside the status; do not copy the full contract.
- Put final execution details in the journal when one is requested or already part
  of the workflow. Link raw evidence artifacts as needed; do not paste command logs,
  investigation history, or a second report into the ledger.
- Choose the next recommendation from current dependencies and outcomes. A next
  recommendation is not authorization to expand the active scope.

## Handoff

Provide a brief status, what completed, the evidence or journal link, any unresolved
acceptance, and the next runnable step. When a journal skill supplies the report,
link it and avoid a competing final-response template.

After the authorized unit or batch reaches its outcome, hand back control. Continue
with further units only when existing user instructions authorize them. A pause,
compaction, or subagent completion does not reset the user's authorized scope.

## References

Read only what the situation needs:

- [Status and ledger examples](references/status-examples.md): adapting an existing progress format.
- [Evidence and review](references/evidence-and-review.md): acceptance, failure recovery, and outcome judgment.
- [First plan patch](references/first-plan-patch.md): initializing progress when no equivalent structure exists.
- [Golden Cases example](references/golden-cases-v1.md): illustrative selection in a deterministic testing plan; the current plan remains authoritative.
