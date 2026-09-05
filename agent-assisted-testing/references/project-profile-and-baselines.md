# Project Profile and Execution Baselines

Read this reference when bootstrapping, selecting, validating, rebinding, or
auditing project-level context.

## Control Model

```text
Project
→ Project Profile revision (PRF)
→ exact ENV / ACT / DAT / DEP / AGP revisions
→ bounded Task ID
→ task-scoped artifacts and runs
```

The project layer extends the Task artifact chain; it does not replace it.

Every project-level artifact has an immutable revision, human Owner, human
Reviewer, lifecycle status, freshness evidence, review reference, and
supersession history. Agent output remains `Candidate`.

## Project Profile

Each Task must reference exactly one `Reviewed` or `Active`
`project_profile_version`.

The minimum Profile records:

| Area | Required content |
|---|---|
| Identity | `project_id`, name, version, status, Owner, Reviewer, timestamps, effective date, review reference |
| Purpose and boundary | Purpose, users, capability/workflow inventory, in-scope and out-of-scope systems, entry points, state transitions, high-impact operations |
| Repository and architecture | Repository and owner, default branch, services/modules, languages/runtime, architecture/API/data/deployment references |
| Testing context | Existing frameworks, test directories/configuration, fixtures/helpers, CI, report locations, known limitations |
| Constraints | Allowed tools/models, maximum Agent permission, network/cost/time/concurrency limits, production and destructive-operation restrictions |
| Evidence | Log/trace/report/monitoring locations, source-of-truth priority, freshness requirement |

The workflow inventory is descriptive. It must not choose a Task workflow,
assign risk scores, prioritize scenarios, prescribe assertions, recommend
automation, or decide gates.

Create a new Profile revision for material changes to repository ownership,
modules, interfaces, topology, boundaries, frameworks, dependencies,
permissions, model/tool policy, or source-of-truth rules. Retain the old
revision and record `supersedes`.

Reject or block Profile use when the human Owner/Reviewer, boundary, repository
context, workflow inventory, production restrictions, destructive-operation
restrictions, source-of-truth priority, review evidence, or critical freshness
is missing or invalid.

## Common Baseline Envelope

Every `ENV`, `ACT`, `DAT`, `DEP`, and `AGP` revision records:

- `baseline_id`
- immutable `baseline_revision`
- `baseline_type`
- human `owner` and `reviewer`
- lifecycle `status`
- `created_at` and `updated_at`
- `effective_period`
- freshness evidence
- `review_reference`
- `supersedes` when replacing an earlier revision

Task fields must resolve to the exact `(baseline_id, baseline_revision)` pair or
an equivalent immutable reference.

## ENV: Environment Baseline

Record:

- Environment type and authorized purpose
- Endpoint, deployment, configuration, infrastructure, and feature-flag
  references where applicable
- Available and unavailable services
- External integrations and network restrictions
- Observability availability
- Data reset capability
- Production-like differences
- Known limitations
- Owner, Reviewer, status, effective period, freshness, and supersession

Use states such as `Draft`, `Reviewed`, `Available`, `Restricted`, `Blocked`,
`Stale`, `Superseded`, and `Archived`.

Stop execution for an environment mismatch, missing revision, stale/invalid
configuration, undeclared production-like difference, absent required service,
uncontrolled destructive effect, or unavailable reset capability.

## ACT: Account and Role Baseline

Record only non-secret metadata:

- Account alias, role, permission scope, and environment
- Authentication method name
- Secret storage location reference
- Expiration, ownership, shared/isolated state, concurrency restrictions, and
  reset method
- Prohibited operations and approval requirements
- Sensitive-data exposure risk
- Status and human review

Never store password, token, private key, cookie, session secret, or actual
credential material in Markdown, code, logs, screenshots, or reports.

`Not configured`, unknown permission scope, expiration, or revocation blocks
use.

## DAT: Test-Data Baseline

Record:

- Data-set identity and source
- Bound environment
- Data classification and production-derived status
- Allowed and prohibited uses
- Creation, reset, cleanup, uniqueness, and ownership
- Shared-state and side-effect risks
- Retention and deletion requirements
- Expected initial and final state
- Freshness and verification status

Block execution for unknown origin/classification, unmasked sensitive data,
unauthorized production data, irreversible mutation without authorization,
missing reset/cleanup, shared-state contamination, stale data, or unclear
retention/deletion rules.

## DEP: Dependency Baseline

Record:

- Dependency identity, name, and type
- Realism status: `real`, `sandbox`, `mock`, `stub`, `fake`, or `unavailable`
- Owner, endpoint/service and authentication references
- Cost/rate limits and availability assumptions
- Failure, fallback, and observability behavior
- Test responsibility boundary
- Prohibited operations
- Replacement rationale and resulting coverage limitation

Never claim real end-to-end proof when a material dependency is replaced or
unavailable.

## AGP: Agent, Tool, and Model Permissions

Use only:

- `Allowed`
- `Allowed with human confirmation`
- `Restricted`
- `Prohibited`
- `Not configured`

Assign an explicit state to:

- Read-only analysis
- Draft generation
- File modification
- Test execution
- Network access
- External model use
- Repository write access
- CI modification
- Deployment access
- Secret access
- Production access

Omission and `Not configured` never imply permission. Deployment and production
access are prohibited by default. Secret access is prohibited or restricted to
location references only. CI modification is restricted or prohibited unless
the valid policy and human authorization explicitly permit the scoped change.

## Freshness and Rebinding

Trigger review for:

- Repository, architecture, deployment, configuration, or feature-flag changes
- Account permission changes or credential/approval expiration
- Data refresh, masking, retention, or cleanup changes
- Dependency contract, realism, availability, rate, or cost changes
- CI platform, model, tool, access-policy, security, privacy, or compliance
  changes

A Task freezes selected revisions. A `Stale` or `Invalid` revision must not be
silently replaced or remain active. Revalidate it, explicitly rebind with human
review evidence, or mark the Task `Blocked`.

Archived Tasks permanently retain execution-time references even when a later
revision marks them `Superseded`, `Stale`, `Invalid`, `Expired`, or `Revoked`.

## Escalation Routing

| Conflict | Escalate to |
|---|---|
| Environment | Environment or Service Owner |
| Account or access | Access or Security Owner |
| Data or privacy | Data or Privacy Owner |
| External dependency | Service or Integration Owner |
| Agent/tool/model policy | QA, Engineering, or Security Owner |

Record the Task ID, affected baseline revisions, observed conflict, required
Owner, and resolution or reviewed rebind evidence.
