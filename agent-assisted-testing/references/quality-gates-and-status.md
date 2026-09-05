# Quality Gates and Status

## Artifact Status

| Status | Meaning |
|---|---|
| `CANDIDATE` | Generated or proposed; not human reviewed |
| `REVIEWED` | Meaning and evidence reviewed; not necessarily executable |
| `EXECUTABLE` | Human Owner approved the engineered test for execution |
| `VERIFIED` | Real run evidence plus human confirmation |
| `REJECTED` | Removed for duplication, low value, weak evidence, safety, or infeasibility |
| `BLOCKED` | Cannot proceed and must remain visible |
| `SUPERSEDED` | Replaced but retained |
| `ARCHIVED` | Closed record retained |
| `UNRESOLVED` | Evidence is insufficient or conflicting |

Do not use `REVIEWED` as a synonym for passed, covered, or verified.

## Project Context Status

- Profile: `Draft`, `Reviewed`, `Active`, `Stale`, `Invalid`, `Superseded`,
  `Archived`
- Baseline: type-specific active/available/verified states plus `Restricted`,
  `Blocked`, `Stale`, `Invalid`, `Expired`, `Revoked`, `Superseded`, `Archived`

A Task cannot execute against a missing, stale, invalid, expired, or revoked
critical reference unless it is revalidated and explicitly rebound with the
required human evidence.

## Implementation Status

- `LANDED`: implementation exists and repository evidence supports it.
- `PARTIAL`: only part of the intended contract or workflow is implemented.
- `PLANNED`: described but not found in implementation.
- `XFAIL_GAP`: represented by an executable expected-failure contract.
- `INFERRED`: plausible but not directly verified.

## Gate Status

- `PR_BLOCKING`
- `NON_BLOCKING`
- `OPT_IN`
- `NIGHTLY`
- `STAGING`
- `NOT_WIRED`
- `UNKNOWN`

Verify workflow files, project configuration, scripts, triggers, conditions,
secrets, services, and publication steps before assigning gate status.

## Blocking Eligibility

Recommend `PR_BLOCKING` only when the test is:

- Human reviewed and approved by the correct authority
- Deterministic and repeatedly stable
- Isolated or explicitly dependency-controlled
- Fast enough for the accepted PR budget
- Attributable to the current change
- Backed by meaningful assertions
- Clear about failure meaning
- Free of uncontrolled production, paid, or external dependencies
- Bound to valid execution-context revisions
- Actually wired into the PR workflow

Real-LLM, external-service, multi-service staging, exploratory, semantic-judge,
and self-healing signals default to non-blocking unless project owners
explicitly accept their cost, instability, and proof boundary.

## Required Gate Evidence

| Suite/profile | Exact command | Source and baseline revisions | Trigger | Gate status | External dependencies | Publication path | Evidence |
|---|---|---|---|---|---|---|---|

A marker name, local command, or documentation statement does not prove that a
test blocks PRs.

## Closure Report

Report separately:

1. Changes made
2. Commands executed and observed results
3. Frozen Profile/baseline/source references
4. Verified proof
5. Proof limits and non-goals
6. Failures and confirmed classifications
7. Tests not run and reasons
8. Gate recommendation or verified gate status
9. Remaining risks, Owners, and next actions

## Process Metrics

Use metrics for process improvement, not standalone release or individual
performance decisions:

| Metric | Definition |
|---|---|
| Candidate adoption | Retained candidates / generated candidates |
| Executable conversion | Executable tests / approved scenarios |
| First-run success | Passing generated drafts on first execution / first executions |
| Human rework | Material changes or time from draft to executable test |
| Flaky rate | Tests with nondeterministic outcomes / executed tests |
| Valid defect rate | Confirmed product defects / proposed defect candidates |
| Gate false-positive rate | Blocking failures classified as non-product causes / blocking failures |

Interpret metrics by layer, project complexity, environment, data, dependency
realism, and risk.
