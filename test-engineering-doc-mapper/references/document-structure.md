# Document Structure

Choose sections based on evidence and user intent. Do not force every module into the same twelve-section template.

## Core Sections

Include these in a standard module testing document:

1. Document positioning, ownership, and scope
2. Current landed test suites
3. Main workflow and tested position
4. Test layers and authenticity profiles
5. Important test cases and assertions
6. CI or execution commands and gate status
7. Current boundaries, gaps, and extension order

## Conditional Sections

Add only when relevant:

- Protocol or invariant table for HTTP, SSE, lifecycle, state, retry, cancellation, or reporting contracts
- Dependency replacement and fault-injection matrix
- Business or architecture mapping table
- Quality-gate report fields and publication flow
- Golden-case schema, runner, and assertion model
- Real-LLM or staging safety and cost controls
- Xfail executable contract gaps

## Document Depth

### Standard

Use the core sections, detailed explanations for high-risk cases, and summary tables for repetitive cases.

### Full

Use when the user requests an engineering reference or the module has multiple profiles, protocol invariants, CI gates, failure injection, and quality reporting.

### Minimal

Keep:

1. Positioning and scope
2. Main workflow
3. Current suites
4. Important case explanations
5. Boundaries and gaps

Do not remove proof limits from major groups.

## Update Rules

- Preserve the target language and numbering scheme.
- Keep correct existing explanations.
- Add missing sections near related content instead of appending unrelated material at the end.
- Rename sections only when current names are misleading.
- Remove duplicated explanations after consolidating them into one authoritative section.
- Do not rewrite the whole document merely to match this reference.

## Suggested Mapping Tables

Architecture mapping:

| Test point | Owner / boundary | Code entry | Layer | Authenticity | Current proof boundary |
|---|---|---|---|---|---|

Invariant mapping:

| Invariant | Status | Test evidence | Explanation |
|---|---|---|---|

Suite inventory:

| Suite | Layer | Profile | Gate | Status | Proves | Does not prove |
|---|---|---|---|---|---|---|
