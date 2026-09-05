# CI And Quality Gate Mapping

Use this reference when the document describes PR checks, markers, profiles, scheduled tests, report fields, or quality-gate publication.

## Verify CI Status

Inspect actual configuration:

1. `.github/workflows/*.yml` and `.yaml`
2. `pyproject.toml`, `pytest.ini`, `setup.cfg`, or `tox.ini`
3. Project scripts or task runners invoked by workflows
4. Environment variables, service containers, secrets, and conditions
5. Artifact or report publication steps

Record the exact command and triggering event. Do not infer PR-blocking status from a marker name or documentation statement.

## Gate Classification

Classify each suite as:

- PR blocking
- Non-blocking PR signal
- Opt-in local profile
- Nightly or scheduled
- Staging or release-before
- Not wired to automation
- Unknown because configuration was not available

Explain why the classification is appropriate.

Do not recommend real LLM, external-service, or multi-service staging tests as required PR checks unless the project explicitly accepts their cost and instability.

## Quality Report Fields

Distinguish:

- Asserted contract fields
- Diagnostic fields collected by helpers
- Fields published to a quality gate
- Fields only planned in documentation

Example fields include latency, event count, terminal-event presence, finalization, save count, cleanup state, failure stage, and unhandled exceptions.

For every report path, map:

```text
test execution
  -> local report builder
  -> case publication helper
  -> suite aggregation
  -> quality-gate decision
  -> CI status or artifact
```

Do not claim a field influences a gate merely because it is collected.

## Required Evidence Table

| Suite or profile | Exact command | Trigger | Blocking | External dependencies | Publication path | Evidence status |
|---|---|---|---|---|---|---|
