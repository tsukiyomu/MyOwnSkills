---
name: evidence-backed-plan-executor
description: Execute one scoped unit from an implementation plan, roadmap, test plan, or architecture plan while producing an evidence-backed engineering decision and learning record. Use when Codex must inspect an existing project, explain how the problem should be analyzed, compare implementation choices, map decisions to exact code and tests, implement and verify the selected change, update plan progress, and help the user understand and reproduce the engineering method instead of receiving only a finished result.
---

# Evidence-Backed Plan Executor

## Core contract

Execute exactly one plan unit per run unless the user explicitly defines a different unit.

Produce two outcomes:

1. Delivery outcome: implement and verify the selected work unit.
2. Learning outcome: make the investigation, design choice, code mapping, and verification method reproducible by the user.

Record inspectable engineering rationale: evidence, assumptions, alternatives, trade-offs, decisions, uncertainty, code locations, and results. Do not expose or claim to expose private chain-of-thought.

Never fabricate reviewed code, commands, results, artifacts, or user understanding.

## Select the execution mode

Use guided-learning mode by default.

- In guided-learning mode, present one meaningful decision checkpoint before implementation. Ask the user to predict, compare, or challenge the proposed design, then wait for the response.
- In evidence mode, present the same decision brief but continue without pausing. Use this mode only when the user explicitly requests autonomous or uninterrupted execution.
- For a task with no material design alternative, explain why the choice is mechanical and continue without manufacturing a checkpoint.

## Execute the workflow

### 1. Select and constrain the work unit

Identify and record:

- plan or source document;
- task identifier;
- objective and purpose;
- completion criteria;
- required evidence;
- explicit exclusions;
- dependencies on unfinished work.

Inspect the plan and repository before asking for information that can be discovered locally. Do not silently expand the task.

### 2. Define the learning objective

State what the user should be able to explain after completion:

- the problem model and important invariants;
- the relevant project workflow and code path;
- the selected design and rejected alternatives;
- the mapping from requirements to implementation and tests;
- the evidence that proves the result;
- the remaining limitations and uncertainty.

### 3. Investigate before designing

Inspect the relevant production code, tests, CI, configuration, persistence or state boundaries, failure and retry paths, and current documentation.

Maintain this review inventory:

| File or symbol | Why reviewed | Behavior found | Evidence | Design impact |
|---|---|---|---|---|

Separate confirmed facts, inferences, assumptions, and unknowns. Cite exact files and symbols whenever possible.

For testing work, use an available testing-domain skill for risk analysis and test implementation. For an existing plan or roadmap, use an available checkpoint skill to enforce one work unit and update its progress ledger.

### 4. Model the problem

Record the relevant:

- business and technical invariants;
- inputs, outputs, and state transitions;
- ownership and source-of-truth boundaries;
- concurrency, retry, timeout, cancellation, and partial-failure conditions;
- security and data-safety constraints;
- dependency authenticity boundaries;
- behavior the task does and does not need to prove.

For complex architecture, concurrency, or distributed-state decisions, read `references/decision-quality-checklist.md` before selecting a design.

### 5. Compare viable approaches

Compare realistic options:

| Option | Benefits | Costs and risks | Required assumptions |
|---|---|---|---|

Select an approach only after recording:

- evidence supporting it;
- why the alternatives were rejected;
- conditions that would invalidate the choice;
- rollback, fallback, or migration path;
- complexity introduced by the choice.

Do not select a technology merely because it appears sophisticated or production-grade.

### 6. Present the pre-implementation brief

Present:

- current understanding;
- reviewed project path;
- important findings;
- options and recommendation;
- planned files and symbols;
- planned tests and assertions;
- expected execution evidence;
- unresolved uncertainty.

In guided-learning mode, pause once on the most educational material decision. Ask a focused question that requires the user to reason about a trade-off, risk, or verification strategy. Continue after the response and compare it with repository evidence.

### 7. Map design to implementation

Create this traceability before editing:

| Requirement or risk | Production location | Planned change | Test location | Assertion | Evidence |
|---|---|---|---|---|---|

Use interfaces, pseudocode, or short critical snippets to explain the intended implementation. Keep complete final code in the repository rather than duplicating source files in the journal.

### 8. Implement the selected design

Make only changes required by the selected work unit. Preserve unrelated user changes.

If repository evidence disproves an assumption:

1. stop the affected approach;
2. record the new evidence;
3. revise the decision and mapping;
4. explain the effect on scope, implementation, and tests.

### 9. Verify proportionally to risk

Run the smallest meaningful check first, then the acceptance suite required by the plan.

Record:

- exact command;
- environment and revision when available;
- exit code and result summary;
- generated reports and artifacts;
- behavior proved by each result;
- behavior not proved by the result.

Where safe and relevant, verify expected failure behavior as well as success behavior.

### 10. Write the execution journal

Copy and complete `assets/execution-journal-template.md` in the project's designated evidence or report directory. If no location exists, use `docs/execution-journal/` or ask the user to approve another durable location.

Do not use the journal as a substitute for source code, automated tests, CI evidence, or human review.

### 11. Update progress

Update the source plan and its progress ledger with:

- work-unit result;
- evidence and journal path;
- deviations and unresolved risks;
- next recommended task.

Use only these implementation states:

- `DONE`
- `REVIEW_NEEDED`
- `BLOCKED`

Track learning transfer separately:

- `EXPLAINED`: rationale and evidence were presented.
- `TEACH_BACK_PENDING`: the user has not yet demonstrated independent understanding.
- `MASTERED`: the user confirmed understanding through explanation or application.

Never mark `MASTERED` without user evidence or confirmation.

### 12. Stop after the work unit

Stop after implementing, documenting, and reporting the selected unit. Do not begin the next plan item automatically.

Use this final handoff:

```markdown
## This Run

Selected task:
- ...

Implementation result:
- DONE / REVIEW_NEEDED / BLOCKED

Learning-transfer result:
- EXPLAINED / TEACH_BACK_PENDING / MASTERED

Changed:
- ...

Evidence:
- ...

Decisions learned:
- ...

Remaining risks:
- ...

Next recommended task:
- ...
```
