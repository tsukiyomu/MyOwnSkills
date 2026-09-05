# Step 1–10 Execution Contract

Use this reference for full lifecycle execution, process audit, or a durable
handoff. The integrated SOP controls if a wording conflict exists.

## Role Model

| Role | Rule |
|---|---|
| Producer | Agent or human may draft Candidate content |
| Owner | Human accountable for the step result |
| Reviewer | Human checks evidence and rule compliance |
| Approver | Human authorizes blocking or other high-impact decisions |
| Executor | Human or CI runs approved tests |

Agent-generated content cannot self-promote to `Reviewed`, `Executable`,
`Verified`, `Approved`, or `Blocking`.

## Global Completion Rule

A step is complete only when its entry conditions and required inputs are
satisfied, its output exists or is updated, human Owner and Reviewer are
recorded, its exit condition is met, upstream/downstream relationships and IDs
are present, and stop/escalation state is explicit.

A `Blocked` step is not complete.

## Step Contracts

### Step 1 — Register Task and Scope

- Owner: Human SDET / QA Owner
- Reviewer: Requester, Product Owner, or Service Owner
- Entry: Concrete trigger; identified project; `Reviewed`/`Active` Profile; AGP
  permits the task
- Inputs: Request, project/Profile/AGP revisions, target workflow/system,
  revision, objective, constraints, test intent
- Output: Scope/non-scope, roles, human-selected workflow, boundary, frozen
  references
- Artifact: `workflow_map.md` or equivalent; Task binding record
- IDs: `TASK`, `WFM`, project/Profile/AGP
- Exit: Scope and ownership are clear; references are frozen
- Stop: Unknown Owner/project/system/revision/objective; missing/invalid Profile;
  unconfigured/prohibited AGP

### Step 2 — Collect and Validate Evidence

- Owner: Human SDET / QA Owner
- Reviewer: Service Owner, Developer, Data/Security Owner as needed
- Entry: Step 1 reviewed; exact Profile and ENV/ACT/DAT/DEP selected
- Inputs: Workflow, Profile/baselines, requirements, architecture, code, tests,
  environment, defects, logs, interfaces
- Output: Evidence, source, gap, restriction, freshness, and consistency record
- Artifact: `evidence_inventory.md` or equivalent
- IDs: `TASK`, `EVI`, Profile/ENV/ACT/DAT/DEP
- Exit: Evidence exists or gaps are explicit; references are fresh, valid, and
  applicable
- Stop: Silent assumptions, sensitive-data ambiguity, stale/invalid baseline,
  unknown classification/permission, or evidence/configuration conflict

### Step 3 — Build Risk Map

- Owner: Human SDET / QA Owner
- Reviewer: Product Owner, Service Owner, QA Lead for critical workflows
- Entry: Evidence can support risk statements
- Inputs: Workflow, evidence, reviewed descriptive Profile facts, defect/failure
  history
- Output: Reviewed risks tied to evidence and workflow
- Artifact: `risk_map.md` or equivalent
- IDs: `TASK`, `RSK`, Profile
- Exit: Each retained risk has evidence, location, and Owner context
- Stop: Speculative, duplicate, unsupported, or boundary-ambiguous risks;
  escalate security, payment, privacy, and irreversible effects

### Step 4 — Generate Candidate Scenarios

- Owner: Human SDET / QA Owner
- Reviewer: Product Owner, Service Owner, or Peer SDET
- Entry: Risk map and workflow are reviewable; ENV/DAT/DEP are usable
- Inputs: Risk/workflow, expected behavior, environment/data/dependency
  constraints
- Output: Candidate scenarios with layer, expected result, and constraints
- Artifact: `scenario_matrix.md` or equivalent
- IDs: `TASK`, `SCN`, ENV/DAT/DEP
- Exit: Every scenario links to a risk or workflow objective and declares the
  execution-reality boundary
- Stop: Untestable scenario, unknown expectation, unsafe effect, unavailable
  environment, unknown realism, or non-resettable data

### Step 5 — Select Cases

- Owner: Human SDET / QA Owner
- Reviewer: QA Lead, Peer SDET, or Service Owner
- Entry: Scenarios reviewed; ENV/ACT/DAT/DEP/AGP validated
- Inputs: Scenarios, feasibility constraints, determinism expectations
- Output: Accepted/rejected cases with rationale
- Artifact: `selected_cases.md` or equivalent
- IDs: `TASK`, `SEL`, applicable baselines
- Exit: Each selection has rationale, Owner, feasibility, implementation
  direction, and resolved constraints
- Stop: Non-determinism, uncontrollable setup, unjustified selection, or
  unresolved account/data/dependency/permission limits

### Step 6 — Draft and Engineer Tests

- Owner: Human SDET / QA Owner
- Reviewer: Peer SDET, Developer, or Service Owner
- Entry: Cases approved; repository context available; AGP permits actions
- Inputs: Selected cases, Profile/AGP, repository/test context, existing tests,
  code and interfaces
- Output: Reviewable test assets with proof boundary and modification scope
- Artifact: Test code/draft and review or PR reference
- IDs: `TASK`, `TST`, Profile/AGP
- Exit: Asset links to a selected case, follows repository context, remains
  within scope, and is ready for execution review
- Stop: Out-of-scope, unsafe, context-free, unreviewable, or AGP-prohibited
  changes

### Step 7 — Execute and Preserve Evidence

- Owner: Human SDET / QA Owner; Executor may be human or CI
- Reviewer: Human SDET / QA Owner
- Entry: Executable asset, source revision, authorized context, and fresh/valid
  ENV/ACT/DAT/DEP
- Inputs: Test, command, source, and exact baseline revisions
- Output: Pass/fail/error run with frozen context
- Artifact: Run record and optional failure evidence
- IDs: `TASK`, `RUN`, source/ENV/ACT/DAT/DEP
- Exit: Result links command, time, outcome, exact revisions, and declared
  production-like differences
- Stop: Context mismatch, missing/stale/invalid reference, production risk,
  invalid data, dependency/permission failure, or destructive behavior

### Step 8 — Triage Failure

- Owner: Human SDET / QA Owner
- Reviewer: Service Owner, Developer, QA Lead for unresolved critical failures
- Entry: Failed, flaky, disputed, or inconsistent result
- Inputs: Run, logs, trace, screenshots, diff, prior context, ENV/DAT/DEP
- Output: Human-confirmed class or explicit unresolved state
- Artifact: `triage_result.md` or equivalent
- IDs: `TASK`, `TRI`, applicable baselines
- Exit: Classification/attribution exists or unresolved has next Owner
- Stop: Contradictory or insufficient evidence; unverified baseline suspicion;
  escalate security, corruption, ownership disputes, repeated unresolved failure

### Step 9 — Regression and Gate Basis

- Owner: Human SDET / QA Owner
- Reviewer: QA Lead or Engineering Lead for blocking/release impact
- Entry: Required executions and triage decisions are available
- Inputs: Verified runs, triage, updated tests, risk/scenario links
- Output: Regression update and gate-ready decision basis
- Artifact: `gate_decision.md` or equivalent
- IDs: `TASK`, `GAT`
- Exit: Gate basis links to executed evidence and responsible Reviewer
- Stop: Unresolved blocking failure, unknown stability, or missing approval
  authority

### Step 10 — Report and Archive

- Owner: Human SDET / QA Owner
- Reviewer: QA Lead, Engineering Lead, or designated Stakeholder
- Entry: Required artifacts exist; execution-time Profile/baselines can be
  reconstructed
- Inputs: Workflow through gate artifacts plus project/Profile/baseline/source
  references
- Output: Final quality summary and closure record
- Artifact: `quality_report.md` and archive references
- IDs: `TASK`, `QRP`, project/Profile/ENV/ACT/DAT/DEP/AGP/source
- Exit: Another Reviewer can reconstruct project context, what/why/how was
  tested, outcomes, proof boundaries, and unresolved items
- Stop: Missing evidence/reference, ownerless unresolved item, broken chain, or
  temporary sensitive data

## Transition Rules

- Step 7 enters Step 8 when a failure needs triage.
- Step 7 may enter Step 9 when no failure needs triage.
- Step 8 may return to Step 2 for evidence gaps.
- Step 8 may return to Step 4 for scenario-intent defects.
- Step 8 may return to Step 6 for implementation defects.
- Controlled fixes may return from Step 8 to Step 7 for re-execution.
- Backward movement preserves prior artifacts and records supersession.
- The current order remains Step 9 then Step 10.
