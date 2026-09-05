# Test Profile Taxonomy

Classify tests on independent axes. Do not collapse these axes into one label.

## Test Layer

| Layer | Primary purpose |
|---|---|
| Smoke | Fast proof that a critical entry point is minimally usable |
| Unit | Isolated behavior of a function, class, or small module |
| Component | A subsystem with controlled neighboring dependencies |
| API | Route or protocol contract at an exposed interface |
| Integration | Cooperation between multiple real project components |
| Staging | Deployed or environment-level behavior with production-like dependencies |
| Golden case | Stable scenario-level regression contract over normalized inputs and outputs |

`route-level resilience` and `real-loop with fake LLM` are useful profile descriptions, not separate test layers.

## Authenticity Profile

Describe authenticity component by component:

| Component | Values |
|---|---|
| Route / API app | real / replaced / bypassed |
| Runtime loop | real / fake / partial |
| LLM | fake / scripted / real |
| Tool dispatcher | real / fake / bypassed |
| Tool execution | fake / local real / external real |
| Persistence | real / in-memory / spy / disabled |
| Telemetry and notification | real / spy / disabled |
| External infrastructure | real / containerized / fake / absent |

Summarize a profile only after filling these boundaries. Examples:

- `real route + fake loop`
- `real route + real loop + scripted LLM + fake tools`
- `real route + real loop + real LLM + controlled side channels`
- `staging with real external dependencies`

## Gate Status

Use one of:

- `PR_BLOCKING`
- `NON_BLOCKING`
- `OPT_IN`
- `NIGHTLY`
- `STAGING`
- `NOT_WIRED`
- `UNKNOWN`

A PR-blocking test should be fast, stable, offline or minimally dependent, and attributable to the current code change. Verify actual workflow configuration before assigning this status.

## Implementation Status

Use one of:

- `LANDED`
- `PARTIAL`
- `PLANNED`
- `XFAIL_GAP`
- `INFERRED`

Do not use `planned staging`, `real_llm`, or `xfail` as proof that a capability is currently covered.

## Ownership Boundary

Classify the relationship:

- `OWNER`: the module owns the contract or state transition under test.
- `BOUNDARY`: the module exposes, invokes, consumes, or translates another module's behavior.
- `OBSERVABILITY`: the module only reports or publishes evidence about another path.

For cross-module tests, name both the owner and boundary instead of assigning all behavior to the document's Part.

## Required Profile Explanation

For each important profile, state:

1. Goal
2. Real parts
3. Replaced or controlled parts
4. Questions the profile can answer
5. Questions it cannot answer
6. Gate status and evidence
