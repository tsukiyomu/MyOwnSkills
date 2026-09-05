# Artifact Traceability

Read this reference when creating durable artifacts, moving backward in the
workflow, superseding content, assigning lifecycle state, or closing a Task.

## Identity

Create one root Task ID:

```text
AST-YYYYMMDD-NNN
```

Create task-scoped artifact IDs:

```text
<TASK-ID>-<TYPE>-<NNN>
```

| Type | Artifact |
|---|---|
| `WFM` | Workflow map |
| `EVI` | Evidence inventory item |
| `RSK` | Risk |
| `SCN` | Scenario |
| `SEL` | Selected-case decision |
| `TST` | Test asset or draft |
| `RUN` | Execution record |
| `FLR` | Failure occurrence or evidence node |
| `TRI` | Triage result |
| `GAT` | Gate decision record |
| `QRP` | Quality report |

Project-level types are `PRF`, `ENV`, `ACT`, `DAT`, `DEP`, and `AGP`. Their
project-defined IDs and revisions are separate from the Task ID.

## Required Task Binding

Preserve:

- `project_id`
- exact `project_profile_version`
- exact ENV/ACT/DAT/DEP/AGP revisions
- exact `source_revision`

Each baseline ID must resolve to an immutable revision, not `latest`.

## Required Artifact Metadata

Record:

| Field | Rule |
|---|---|
| `artifact_id` | Required |
| `task_id` | Required |
| `artifact_type` | Required |
| `title` | Required |
| `status` | Required |
| `owner` | Required and human |
| `reviewer` | Human or `PENDING` before review |
| `created_at` / `updated_at` | Required |
| `source_revision` | Required where applicable |
| `upstream_ids` | Required unless root |
| `downstream_ids` | Required once known |
| `review_reference` | Required for Reviewed/Approved |
| `supersedes` | Required for material replacement |
| `uncertainty_notes` | Required for assumptions or evidence gaps |

Material task artifacts also carry the applicable frozen project/Profile/
baseline references.

## Lifecycle

| State | Meaning |
|---|---|
| `Candidate` | Drafted, not human reviewed |
| `Reviewed` | Human reviewed for next-stage use |
| `Executable` | Human Owner approved execution |
| `Verified` | Real execution evidence plus human confirmation |
| `Rejected` | Explicitly not accepted |
| `Blocked` | Cannot proceed and remains visible |
| `Superseded` | Replaced but retained |
| `Archived` | Closed record retained |

Never use `Reviewed` as a synonym for executed, passed, covered, or verified.
Record non-applicable stages explicitly.

## Relationship Rules

- Every retained risk links to evidence.
- Every scenario links to a risk or explicit workflow objective.
- Every selected case links to a scenario.
- Every test asset links to a selected case.
- Every run links to the exact test asset and source/context revisions.
- Every triage result links to a run.
- Every gate record links to actual supporting evidence.
- Every quality report links to all material evidence and decisions.

## Supersession and Backward Movement

Never silently overwrite material scope, expected behavior, selected intent,
execution target, or decision basis.

When meaning changes:

1. Create a successor ID or record `supersedes`.
2. Retain the earlier artifact.
3. Keep the originating run and triage references.
4. Record the affected IDs and destination step.
5. Preserve unresolved and blocked states until their exit conditions are met.
6. Record any reviewed Profile/baseline rebind as a new trace event.

Archived Task references are immutable historical facts. Later baseline or
Profile revisions never rewrite them.

## Review Authority

| Action | Authority |
|---|---|
| Draft Candidate | Agent or human |
| Mark Reviewed | Human Reviewer only |
| Mark test Executable | Human Owner only |
| Mark result Verified | Run evidence plus human confirmation |
| Approve Blocking | Human Approver only |

## Closure Chain

```text
TASK
→ WORKFLOW
→ EVIDENCE
→ RISK
→ SCENARIO
→ SELECTED CASE
→ TEST ASSET
→ RUN
→ TRIAGE (if applicable)
→ GATE RECORD
→ QUALITY REPORT
```

Do not close when evidence is missing, unresolved items lack Owners,
traceability is broken, temporary sensitive material remains, applicable exact
revisions cannot be reconstructed, or review/approval requirements are
incomplete.
