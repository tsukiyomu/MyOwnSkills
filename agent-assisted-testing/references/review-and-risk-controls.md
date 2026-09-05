# Review and Risk Controls

Read this reference for test implementation, high-impact execution, sensitive
data, UI automation, external dependencies, CI changes, or generated repairs.

## Generated Test Review

Verify:

- Every imported symbol, route, schema, locator, fixture, marker, and helper
  exists.
- The test follows nearby directory, naming, setup, and cleanup patterns.
- Assertions cover the intended business contract and important side effects.
- Mocks and fakes do not bypass the behavior the test claims to prove.
- Test data is isolated and can be safely reset and cleaned.
- Ordering, clocks, time zones, randomness, concurrency, waits, and retries are
  controlled.
- Failure output is attributable and useful for triage.
- Repeated execution does not leak state or depend on prior cases.
- The proposed change stays within the exact AGP and repository scope.

## UI Automation

- Prefer user-visible behavior and stable, user-facing locators.
- Use framework-native waits and web-first assertions.
- Avoid fixed sleeps except as an explicitly documented diagnostic measure.
- Capture trace or equivalent evidence for CI failures when supported.
- Confirm a locator repair still exercises the original user intent.

## API and Integration Tests

- Assert response structure, business result, state transition, and side effects.
- Cover authorization, invalid input, conflict, retry, idempotency, and
  rate-limit behavior when in scope.
- Distinguish route behavior from downstream service behavior.
- State whether persistence, messaging, telemetry, and external services are
  real or controlled.
- Do not call a real-loop/fake-dependency test full end-to-end coverage.

## Performance Tests

- Use the project's non-interactive runner and production-safe configuration.
- Control test data and result volume.
- Avoid debugging listeners or expensive result capture during real load.
- Require explicit authorization for shared, staging, paid, production-like, or
  production targets.
- Report load model, duration, concurrency, environment, limits, and exact
  baseline revisions.

## Data Safety

Before sending context to any model or external service:

1. Minimize inputs to the approved task need.
2. Remove credentials, tokens, cookies, personal data, and customer content.
3. Replace production values with synthetic or masked examples.
4. Confirm the AGP permits the selected tool/model for the data class.
5. Preserve only audit evidence allowed by retention policy.

Stop when authorization, origin, classification, retention, deletion, reset, or
cleanup rules are unclear.

## External and Paid Dependencies

- Default paid or side-effecting services to sandbox, mock, stub, or fake.
- Require explicit authorization for real charges, messages, entitlements,
  destructive mutations, broad network calls, or material compute.
- Record realism status, replacement rationale, and proof limitation in DEP.
- Do not infer real dependency behavior from a replaced dependency.

## Self-Healing and Repair

Treat repair output as a patch proposal. Review:

- Original test intent
- Changed locator, assertion, timing, dependency, or data behavior
- Whether the patch hides a product regression
- Whether proof strength decreased
- Execution results before and after the patch

Never accept a repair solely because the test turned green.

## Hard Stops

Stop and escalate when:

- Execution can alter production or irreversible state without authorization.
- The task uses paid APIs, real LLMs, broadly external services, or material
  compute without approval.
- Credentials, personal information, restricted source, or production records
  are exposed.
- Data origin/classification is unknown or sensitive data is not safely masked.
- Profile or a critical baseline is missing, stale, invalid, expired, revoked,
  or inconsistent with observed reality.
- Permission scope is unclear or the AGP prohibits the action.
- A requested change modifies CI blocking policy or release approval without
  valid authority.
- Evidence conflicts and further action could conceal or destroy failure state.

For an exception, record reason, impact, compensating control, human Approver,
expiry, and rollback condition.
