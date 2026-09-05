---
name: agent-assisted-testing
description: >-
  Apply the Agent-assisted Software Testing SOP v1.2 to plan, implement, execute,
  triage, audit, or govern evidence-backed software testing with human review,
  deterministic assertions, dependency authenticity, data safety, project-level
  Project Profiles, and exact ENV/ACT/DAT/DEP/AGP baseline revisions. Use when
  Codex should turn requirements, architecture, APIs, UI flows, source code,
  existing tests, logs, traces, defects, or CI results into risk maps, test
  scenarios, automation changes, execution evidence, failure analysis,
  regression coverage, quality reports, or gate recommendations. Also use to
  bootstrap or audit the Project Profile and execution baselines required by the
  SOP. Do not use for evaluating an AI agent as the system under test unless the
  request concerns ordinary software behavior around that agent.
---

# Agent-Assisted Testing SOP v1.2

## Authority

Treat the current integrated SOP and its normative appendices as the source of
truth. This Skill is its operational form.

Apply this rule throughout:

> Ground work in real project evidence, let the Agent produce candidates,
> require humans to review and decide, execute with deterministic tooling, and
> claim only what traceable evidence proves.

## Non-Negotiable Rules

1. Inspect repository or supplied evidence before asserting behavior, coverage,
   implementation, CI wiring, or gate status.
2. Treat generated scenarios, code, diagnoses, repairs, profiles, baselines, and
   decisions as `Candidate` until the required human review occurs.
3. Never self-promote Agent output to `Reviewed`, `Executable`, `Verified`,
   `Approved`, or `Blocking`.
4. Never claim a test passed unless it was executed successfully against the
   recorded revision in the current environment or a trusted run result was
   supplied.
5. Keep test layer, dependency authenticity, artifact lifecycle, implementation
   status, and gate status separate.
6. State what each material test proves, does not prove, and what failure most
   likely means.
7. Preserve repository-native frameworks, fixtures, helpers, naming, data,
   cleanup, configuration, and CI patterns.
8. Never expose secret values, tokens, cookies, personal data, production
   records, or restricted source to an unauthorized model, service, artifact,
   log, screenshot, or report.
9. Do not autonomously merge code, close defects, approve release quality,
   activate a Project Profile, approve a baseline, or change a blocking gate.
10. Do not use an LLM judge, exploratory observation, one green run, or an
    unreviewed self-healing patch as a blocking signal.

## Select the Operating Mode

Choose the smallest mode that fulfills the request:

- `bootstrap`: draft or audit the Project Profile and execution baselines.
- `design`: register scope, inventory evidence, map risks, and generate candidate
  scenarios.
- `implement`: create or update deterministic tests from reviewed behavior and
  repository patterns.
- `execute`: run approved tests and preserve exact execution evidence.
- `triage`: analyze failures, reproduce when feasible, and preserve human-owned
  attribution.
- `govern`: audit coverage, traceability, status, CI wiring, or gate eligibility.
- `end-to-end`: combine Step 1 through Step 10 only when the user requests the
  full lifecycle.

Do not create every named Markdown artifact for a narrow task. Reuse an existing
issue, PR, test report, or repository format when it can preserve the required
fields, IDs, references, and review evidence.

## Bootstrap Project Context

Read `references/project-profile-and-baselines.md` whenever project context or
execution-reality references are absent, stale, invalid, conflicting, or being
created.

Before an executable testing Task begins, bind:

- `project_id`
- exact `project_profile_version`
- exact `environment_baseline_id`
- exact `account_baseline_id`
- exact `data_baseline_id`
- exact `dependency_baseline_id`
- exact `agent_permission_baseline_id`
- exact `source_revision`

Each baseline reference must resolve to an immutable revision. Never use a
floating `latest` alias as the recorded Task binding.

Require the Project Profile to be `Reviewed` or `Active`. Require applicable
baselines to be fresh, valid, reviewed, and usable for the intended action.

When required project context is missing:

1. Inspect available project evidence.
2. Draft `Candidate` Profile or baseline content when requested or useful.
3. Identify the required human Owner and Reviewer.
4. Mark unknown facts and unresolved fields explicitly.
5. Report `REVIEW_NEEDED` or `BLOCKED`; do not imply activation or approval.
6. Do not proceed to implementation or execution when a missing, `Stale`, or
   `Invalid` reference creates safety, data, permission, or proof risk.

## Register the Work Unit

Use one root Task ID for each bounded testing activity:

```text
AST-YYYYMMDD-NNN
```

Record:

- Requested outcome and operating mode
- Human Owner, Reviewer, and any required Approver
- Selected workflow, target system, and architecture owner
- In-scope and out-of-scope behavior
- Allowed Agent actions and execution permissions
- Expected deliverables
- Frozen project/profile/baseline/source references

A material change to the Task objective or selected workflow normally requires
a new Task ID. A material change to environment, account, data, dependency, or
Agent policy normally requires a new baseline revision and an explicit,
reviewed rebind.

## Execute the SOP

Read `references/step-contract.md` when executing or auditing the complete
Step 1–10 contract.

### Step 1: Register Scope

Confirm the trigger, project, reviewed/active Profile, permitted AGP revision,
workflow, target revision, boundaries, roles, and deliverables. Stop when the
project, Owner, target, permission, or scope is unknown.

### Step 2: Gather and Validate Evidence

Prefer evidence in this order:

1. Commands executed now and their observed results
2. Production code, tests, fixtures, helpers, configuration, and CI files
3. Requirements, approved specifications, architecture, API, and workflow docs
4. Historical logs, traces, defects, and trusted reports
5. User statements
6. Clearly labeled inference

Validate Profile and ENV/ACT/DAT/DEP freshness and consistency. Record missing,
conflicting, stale, or unverifiable evidence. Never fill gaps with guesses.

### Step 3: Map Risk

Map workflow states, boundaries, failure paths, side effects, and ownership.
Link every retained risk to evidence. Preserve the project's priority scheme;
otherwise use explicit impact and likelihood reasoning.

### Step 4: Generate Candidate Scenarios

For material scenarios record:

- Goal and risk addressed
- Preconditions and data
- Intended test layer
- Real and controlled dependencies
- Actions and deterministic assertions
- Cleanup and isolation
- Proof boundary and non-goals
- Likely failure meaning
- Applicable ENV/DAT/DEP constraints

Reject duplicates and scenarios without a verifiable expected result.

### Step 5: Select Cases

Select automation candidates only when value, determinism, controllable setup,
repeatability, and maintenance cost are acceptable under the exact
ENV/ACT/DAT/DEP/AGP revisions. Record accepted and rejected reasons. Human
approval owns the selection.

### Step 6: Implement Tests

Before editing, inspect nearby tests, shared fixtures, helpers, configuration,
and the production path. Use the lowest layer that proves the target contract
without hiding the relevant integration boundary.

Assert business results, state transitions, protocol invariants, and relevant
side effects. Make ordering, time, randomness, data ownership, waits, retries,
and cleanup explicit. Stay within the AGP file and repository write scope.

Read `references/review-and-risk-controls.md` before implementing UI tests,
using sensitive data, calling external or paid services, modifying CI, applying
self-healing changes, or causing high-impact side effects.

### Step 7: Execute and Capture Evidence

Run the narrowest relevant command first. Record:

- Exact command and exit code
- Test asset and source revision
- Project Profile and exact ENV/ACT/DAT/DEP/AGP revisions
- Environment and declared production-like differences
- Start/end time and result summary
- Minimum sufficient logs, trace, screenshots, response summaries, and reports

For a proposed blocking test, check repeatability and isolation. Report tests
not run and why.

### Step 8: Triage Failures

Separate observed facts from hypotheses. Rank product defect, test defect,
flaky behavior, environment/infrastructure, data issue, generated-code mistake,
baseline-caused failure, and unresolved explanations.

Reproduce or compare runs when feasible. Keep the result `UNRESOLVED` when
evidence conflicts or reproduction is unavailable. Only a human Reviewer may
confirm final attribution.

### Step 9: Solidify Regression and Gate Basis

Convert confirmed defects into the smallest meaningful regression contract.
Verify stability, isolation, assertion strength, failure meaning, runtime, and
maintenance cost. Human Approvers own blocking decisions.

### Step 10: Report and Close

Preserve the execution-time Project Profile, baseline, source, artifact, review,
run, triage, and gate references. Later supersession must not rewrite archived
Task history.

Close only when another Reviewer can reconstruct what was tested, why, how,
against which exact context, what happened, what the evidence proves, and what
remains unresolved.

## Traceability and Lifecycle

Read `references/artifact-traceability.md` for complete identity, relationship,
supersession, backward-transition, and closure rules.

Use task-scoped artifact IDs:

```text
<TASK-ID>-<TYPE>-<NNN>
```

Core types are `WFM`, `EVI`, `RSK`, `SCN`, `SEL`, `TST`, `RUN`, `FLR`, `TRI`,
`GAT`, and `QRP`. Project-level types are `PRF`, `ENV`, `ACT`, `DAT`, `DEP`, and
`AGP`.

Preserve this minimum chain, explicitly marking non-applicable stages:

```text
TASK → WORKFLOW → EVIDENCE → RISK → SCENARIO → SELECTED CASE
→ TEST ASSET → RUN → TRIAGE (if applicable) → GATE RECORD → QUALITY REPORT
```

Never silently overwrite material meaning. Create a successor ID or record a
`supersedes` relationship and retain the earlier artifact.

## Gate and Status Rules

Read `references/quality-gates-and-status.md` before assigning implementation,
artifact, CI, or gate status.

Verify actual CI configuration before using `PR_BLOCKING`, `NON_BLOCKING`,
`OPT_IN`, `NIGHTLY`, `STAGING`, `NOT_WIRED`, or `UNKNOWN`.

Recommend blocking only for reviewed, deterministic, repeatedly stable,
attributable, appropriately fast tests with meaningful assertions and
controlled dependencies that are actually wired into the blocking workflow.

## Completion Check

Before finishing, confirm:

1. The requested mode and scope were fulfilled.
2. Material claims point to repository, configuration, review, or run evidence.
3. Candidate, Reviewed, Executable, Verified, Approved, and Blocking states were
   not conflated.
4. Exact Profile, baseline, and source revisions are recorded where execution or
   closure claims are made.
5. Test layer, dependency authenticity, proof limits, non-goals, and failure
   meaning are explicit.
6. Tests were run when feasible; exact results or unrun reasons are reported.
7. CI and blocking claims were verified from configuration or marked unknown.
8. Sensitive data, external cost, production impact, and destructive actions
   remained controlled.
9. Unresolved items have human Owners.
10. Human-owned review, approval, activation, attribution, and gate decisions
    remain recommendations unless valid evidence of those decisions exists.

Read `references/workflow-and-artifacts.md` for durable artifact structures.
Read `references/maturity-and-use-cases.md` only for training, adoption, or
capability assessment.
