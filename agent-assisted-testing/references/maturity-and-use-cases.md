# Maturity and Use Cases

Read this reference only for training, team adoption, capability assessment, or
selecting an initial use case.

## Capability Levels

| Level | Focus | Agent contribution | Human control | Completion signal |
|---|---|---|---|---|
| L1 Understanding | Requirements, modules, workflows, evidence | Summaries and initial map | Verify business and project premises | Claims trace to real inputs |
| L2 Design | Risks, functional, boundary, negative, regression scenarios | Candidate expansion | Remove noise and prioritize | Reviewed scenarios become work |
| L3 Implementation | API, UI, component, integration, performance tests | Code and assertion drafts | Own fixtures, data, cleanup, review | Tests run repeatedly and remain maintainable |
| L4 Exploration | Abnormal paths and suspicious behavior | Charters and hypotheses | Confirm relevance and reproduction | Findings become reproducible evidence |
| L5 Maintenance | Failure analysis and test repair | Ranked triage and patch suggestions | Confirm cause and intent | Failures are correctly classified |
| L6 Governance | Profiles, baselines, coverage, reports, gates | Audit and recommendation drafts | Own activation, policy, and release decisions | Context and gate evidence are explicit |

Advance through demonstrated evidence quality and engineering control, not tool
count.

## Common Use Cases

| Use case | Useful Agent output | Required human check | Deterministic result |
|---|---|---|---|
| Project bootstrap | Candidate Profile and baseline inventory | Context, restrictions, freshness, permissions | Reviewed/Active project context |
| Requirements to scenarios | Candidate workflows, risks, and cases | Requirement meaning, priority, duplicates | Reviewed scenario matrix |
| API test generation | Functional, boundary, auth, and error drafts | Schema, status, business assertions, side effects | Executed API regression |
| UI workflow testing | Paths, locator, wait, and assertion suggestions | User intent, data, locator stability | Stable repeatable UI tests |
| Exploratory assistance | Charters, suspicious points, experiments | Reproducibility and business relevance | Reproduction note or regression candidate |
| Failure analysis | Product, test, flaky, environment, data, baseline hypotheses | Reproduction and final classification | Confirmed triage record |
| Self-healing suggestion | Locator or test-structure patch | Original intent and proof strength | Reviewed and executed patch |
| Coverage audit | Missing and duplicate coverage candidates | Code, test, CI, workflow evidence | Traceable coverage report |

## Adoption Guidance

Start with one repeatable workflow:

1. Establish or audit the Project Profile and required baselines.
2. Select one bounded workflow and create a Task ID.
3. Provide real requirement, code, test, or failure evidence.
4. Let the Agent produce candidates and explicit uncertainty.
5. Review and select a small set.
6. Engineer and execute deterministic tests.
7. Preserve exact context, execution evidence, and review decisions.
8. Compare rework, stability, useful findings, and proof limits.

Avoid starting with autonomous release decisions, an LLM judge as a hard gate,
many tools at once, or a dashboard without trustworthy test assets beneath it.
