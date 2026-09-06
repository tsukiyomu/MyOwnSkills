# Golden Cases v1: Selection Example

This reference illustrates how checkpoint tracking applies to a scoped testing
plan. Its filename is retained for existing callers. "Golden Cases v1" is not a
universal specification: read the current plan for tasks, dependencies, acceptance,
profiles, and exclusions. Do not impose a fixed schema-to-runner sequence or ban
CI, observability, real-service profiles, or other work merely because of that name.

For example, a current plan might define:

| Unit | Dependency | Acceptance |
|---|---|---|
| GC-1 — Load and validate fixture cases | Agreed fixture contract | Required valid and invalid cases pass focused loader checks |
| GC-2 — Run deterministic cases | GC-1 | Runner lifecycle and expected assertions pass with the required stubs |
| GC-3 — Connect the existing CI profile | GC-2 | The plan's specified CI job runs the intended profile |

If GC-1 is `DONE` and GC-2 is runnable, select GC-2. Do not replace it with only a
dataclass creation fragment. If the current plan orders these differently or
includes other units, follow that plan. If dependencies remain unresolved, choose
a runnable prerequisite within the user's scope or report the actual blocker.

When the selected plan requires a stub profile, preserve that boundary and do not
use real LLM, MCP, or staging services to satisfy it. When it explicitly includes
authorized integration work, do not import exclusions from an older v1 example.

Use verification commands from the current repository and plan. Inspect their
actual test paths and configuration instead of assuming `tests/golden_cases` or a
particular marker exists. Missing required execution evidence is `REVIEW_NEEDED`;
documentation acceptance can use appropriate inspection instead of code tests.
