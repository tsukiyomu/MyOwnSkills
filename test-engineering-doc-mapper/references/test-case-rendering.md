# Test Case Rendering

Use detailed sections for high-risk, semantically distinct, or failure-attribution-critical tests. Use tables for repetitive parameter variations.

## Detailed Case Template

```markdown
### `[test_name]`

- File: `[path]`
- Layer: `[smoke / unit / component / API / integration / staging / golden case]`
- Authenticity profile: `[real and controlled components]`
- Implementation status: `[LANDED / PARTIAL / PLANNED / XFAIL_GAP / INFERRED]`
- Gate status: `[PR_BLOCKING / NON_BLOCKING / OPT_IN / NIGHTLY / STAGING / NOT_WIRED / UNKNOWN]`

- Core goal:
  - [one sentence]

- Covered workflow:
  1. [step]
  2. [step]

- Key assertions:
  1. [concrete assertion]
  2. [concrete assertion]

- Dependency control:
  1. [fake, stub, monkeypatch, spy, or real dependency]

- What it proves:
  1. [supported claim]

- What it does not prove:
  1. [explicit non-goal]

- Failure meaning:
  - [most likely broken contract, fixture, integration, or environment]
```

## Grouped Case Table

Use this when several tests share the same profile and setup:

| Test | Distinct scenario | Key assertions | Proof boundary | Failure meaning |
|---|---|---|---|---|

Explain shared fixtures, authenticity, and non-goals once above the table.

## Assertion Rules

- Name concrete fields, events, call counts, exceptions, state transitions, or output fragments.
- Distinguish asserted behavior from values merely collected for reporting.
- Do not infer semantic quality from protocol success.
- Do not infer tool execution from a tool event unless the dispatcher and executor path remain real.
- Treat xfail as an executable gap, not passed coverage.
- State when an assertion comes from a helper so readers can trace it.

## Failure Meaning

Attribute failures narrowly. Prefer:

```text
Failure most likely indicates that route finalization or active-state cleanup changed.
```

Avoid:

```text
Failure means the full Agent workflow is broken.
```

Include fixture or environment failure as a possibility when evidence supports it.
