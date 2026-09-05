# Workflow and Artifacts

Use these structures only when the request needs durable planning, execution,
triage, governance, or reporting records. Reuse project-native formats when
possible.

## Common Header

For a material Task artifact, record:

| Field | Content |
|---|---|
| Task and artifact IDs | Root Task and typed artifact identity |
| Status | Candidate, Reviewed, Executable, Verified, Rejected, Blocked, Superseded, or Archived |
| Owner and Reviewer | Human responsibility and review state |
| Project context | Project ID and exact Profile revision |
| Execution context | Exact ENV/ACT/DAT/DEP/AGP and source revisions as applicable |
| Relationships | Upstream/downstream IDs and supersession |
| Uncertainty | Evidence gaps, assumptions, conflicts, or non-applicable stages |

## Workflow Map

| Field | Content |
|---|---|
| Objective | Business or system behavior under test |
| Selected workflow | Task-specific workflow chosen by the human Owner |
| Architecture owner | Team, module, or service responsible |
| Boundaries | Modules, services, interfaces, and external systems touched |
| Entry and terminal states | Start, meaningful transitions, completion |
| Side effects | Persistence, notifications, telemetry, files, or external calls |
| In scope / out of scope | Explicit proof target and exclusions |
| Revision | Branch, commit, build, or deployment |
| Permissions | Allowed Agent and execution actions |

## Evidence Inventory

| Evidence | Source and revision | Supports | Limit or conflict | Status |
|---|---|---|---|---|

Use `VERIFIED`, `UNVERIFIED`, `STALE`, or `CONFLICTING`.

Include Profile/baseline freshness and consistency checks.

## Risk Map

| Risk | Workflow position | Evidence | Impact | Likelihood | Priority | Owner |
|---|---|---|---|---|---|---|

Prioritize security, authorization, privacy, payments, data integrity,
irreversible effects, lifecycle cleanup, and protocol termination when relevant.

## Scenario Matrix

| Scenario | Risk | Layer | Real parts | Controlled parts | Assertions | Proves | Does not prove | Failure meaning | ENV/DAT/DEP constraints | Status |
|---|---|---|---|---|---|---|---|---|---|---|

For detailed cases add:

- Preconditions and test data
- Action sequence
- Expected events or state transitions
- Cleanup and isolation
- Exact test file and symbol after implementation
- Local and CI commands after wiring

## Selection Record

| Scenario | Decision | Reason | Baseline feasibility | Determinism | Maintenance cost | Approver |
|---|---|---|---|---|---|---|

Prefer automation when the expected result is deterministic, risk is meaningful,
the setup is controllable, and repeated execution has lasting value.

## Run Record

Record:

- Exact command, test asset, source revision, and exit code
- Start/end time
- Project/Profile and exact ENV/ACT/DAT/DEP/AGP revisions
- Environment and production-like differences
- Real and controlled dependencies
- Pass/fail/error summary
- Report, log, trace, screenshot, and response-summary locations

## Failure Package

- Test file and failing symbol
- Exact command and exit code
- Source and execution-context revisions
- Timestamp
- Assertion and relevant stack segment
- Logs, trace, screenshot, request/response summary, or report path
- Real and controlled dependencies
- Retry or comparison results
- Known environment or baseline incidents

Never send raw secrets, personal records, restricted source, or unrestricted
production logs to an external model.

## Triage Result

| Failure | Observed facts | Hypotheses | Reproduction | Final class | Baseline-caused status | Confidence | Owner | Next action |
|---|---|---|---|---|---|---|---|---|

Allowed final classes:

- `PRODUCT_DEFECT`
- `TEST_DEFECT`
- `FLAKY`
- `ENVIRONMENT`
- `DATA_ISSUE`
- `GENERATED_CODE_MISTAKE`
- `UNRESOLVED`

An Agent may propose hypotheses. Human review owns final attribution.

## Gate Decision

Record:

- Candidate gate class
- Exact supporting tests and runs
- Stability and isolation evidence
- Assertion and failure meaning
- Runtime and maintenance budget
- Actual CI trigger and wiring evidence
- Human Approver
- Effective scope and rollback method

## Quality Report

Include:

1. Objective, scope, source revision, and frozen project execution context
2. Exact commands and observed results
3. Verified results and failures
4. Test layers and authenticity profiles
5. Assertions, proof boundaries, and non-goals
6. Landed, partial, planned, xfail, and inferred coverage
7. Gate status with configuration evidence
8. Defects, flaky tests, unresolved risks, and Owners
9. Review/approval references
10. Archive and supersession references

Do not convert candidates, documentation claims, diagnostics, or unexecuted
scripts into coverage claims.
