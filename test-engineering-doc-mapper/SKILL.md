---
name: test-engineering-doc-mapper
description: >-
  Create, update, audit, or reconcile evidence-backed test engineering
  documentation by mapping repository tests to architecture ownership, workflow
  position, test layers, dependency authenticity, CI and quality-gate status,
  assertions, failure meaning, and explicit coverage boundaries. Use when Codex
  must produce or verify module testing docs, API or SSE testing docs, integration
  and golden-case documentation, PR gate descriptions, test profile boundaries,
  or mappings between test assets and business or system workflows.
---

# Test Engineering Doc Mapper

## Purpose

Produce testing documentation that is traceable to repository evidence rather than a generic QA plan.

Make every important test claim answer:

1. Which architecture part or boundary owns this behavior?
2. Where does it sit in the runtime or business workflow?
3. What remains real, and what is replaced or controlled?
4. What does the test prove?
5. What does it explicitly not prove?
6. What does a failure most likely mean?

## Operating Modes

Choose one mode before gathering evidence:

- `create`: generate a new testing document from repository evidence.
- `update`: improve an existing document while preserving useful structure, numbering, language, and verified content.
- `audit`: compare an existing document with current code, tests, configuration, and CI; report inaccurate, stale, unsupported, or missing claims.
- `reconcile`: merge overlapping testing documents or resolve conflicting descriptions against repository evidence.

Default to `update` when the user provides an existing target document and asks to improve it. Default to `audit` when the user asks whether a document is accurate or current.

## Evidence Priority

Use this source order:

1. Executed commands and observed results
2. Test code, fixtures, helpers, and production entry points
3. Pytest configuration and CI workflow definitions
4. Generated test inventory
5. Architecture and testing documents
6. Explicit user statements
7. Clearly labeled inference

Never upgrade planned documentation into implemented coverage without code or execution evidence.

Classify important claims as:

- `LANDED`: implemented and supported by repository evidence.
- `PARTIAL`: implemented or covered only in part.
- `PLANNED`: described as future work but not found in current implementation.
- `XFAIL_GAP`: represented by an executable expected-failure contract.
- `INFERRED`: plausible from surrounding evidence but not directly verified.

## Core Workflow

1. Locate the repository root, target document, architecture or Part references, test directories, and relevant CI configuration.
2. Select `create`, `update`, `audit`, or `reconcile` mode.
3. Read `references/evidence-discovery.md` and gather an evidence inventory before drafting.
4. Run `scripts/collect_test_inventory.py` when a Python/pytest repository needs deterministic enumeration of test functions, markers, fixtures, monkeypatch use, configuration files, and CI pytest commands.
5. Inspect representative test bodies, shared fixtures, fake/stub helpers, production entry points, and finalize or cleanup paths. Do not rely on names alone.
6. Separate test layer, authenticity profile, gate status, and implementation status using `references/profile-taxonomy.md`.
7. Map each important suite or case to ownership, workflow position, assertions, dependency control, proof boundary, non-goals, and failure meaning.
8. Select a document depth and section set using `references/document-structure.md`.
9. In update mode, patch only stale, weak, or missing sections. Preserve correct content and local document conventions.
10. Recheck all important claims against evidence and identify unresolved uncertainty explicitly.

## Reference Routing

Read only the references required for the current task:

- Evidence search, source precedence, and evidence inventory: `references/evidence-discovery.md`
- Layer, authenticity, gate, and implementation-status taxonomy: `references/profile-taxonomy.md`
- Core, conditional, and minimal document structures: `references/document-structure.md`
- Per-case detail, grouping, assertions, and failure meaning: `references/test-case-rendering.md`
- CI commands, blocking status, quality reports, and publication flow: `references/ci-and-quality-gate.md`
- Update, audit, and reconcile procedures: `references/update-and-audit.md`

## Mapping Rules

Keep these dimensions separate:

- Ownership: the module owns the behavior, or only exposes/consumes a boundary.
- Test layer: smoke, unit, component, API, integration, staging, or golden case.
- Authenticity: which route, loop, model, tool, persistence, telemetry, or external service remains real.
- Gate status: PR blocking, non-blocking, opt-in, nightly, staging, or not wired to automation.
- Implementation status: LANDED, PARTIAL, PLANNED, XFAIL_GAP, or INFERRED.

Do not use `integration`, `real_loop`, and `real_llm` as interchangeable categories.

## Claim Discipline

Do not claim full workflow coverage when a test proves only route/loop cooperation, protocol behavior, cleanup, or failure attribution.

State replacements directly. Examples:

- `run_agentic_loop` is fake, so the test proves route consumption and finalization but not runtime-loop behavior.
- The route and loop are real while the LLM is fake, so orchestration control flow is covered but model quality is not.
- A real LLM smoke is not automatically a full staging or end-to-end test.

Use code identifiers, test names, file paths, markers, and exact CI commands as evidence. Say `not verified` when execution was not performed.

## Output Rules

- Preserve the target document's language; keep code symbols and commands exact.
- Preserve existing section numbering during updates unless restructuring is required to remove contradictions.
- Use tables for comparisons and numbered flows for execution chains.
- Describe every major group with `what it proves` and `what it does not prove`.
- Use detailed per-case sections for high-risk or semantically distinct tests; summarize repetitive cases in tables.
- Distinguish current implementation from planned extensions.
- End with explicit boundaries, known gaps, and evidence-based extension order.
- Do not create test code or alter CI unless the user explicitly asks for implementation work.

## Completion Check

Before finalizing, confirm:

1. Repository evidence was inspected, not merely the target document.
2. Ownership is distinguished from boundary touchpoints.
3. Test layers are separated from authenticity profiles.
4. CI and gate claims are supported by configuration or labeled unverified.
5. Important cases include assertions, proof limits, and failure meaning.
6. Planned, partial, xfail, and inferred coverage are not presented as landed.
7. The document preserves correct existing content and local conventions.
8. Gaps and uncertainty remain visible.
