# Update And Audit

Use this reference when a target testing document already exists.

## Update Mode

1. Read the complete target document.
2. Inventory its claims, file paths, test names, commands, profiles, and planned gaps.
3. Compare those claims with current repository evidence.
4. Preserve accurate sections and local numbering.
5. Correct stale or unsupported claims.
6. Add missing ownership, authenticity, assertion, CI, or gap information near related sections.
7. Consolidate duplicate explanations.
8. Recheck links, paths, symbols, and commands.

Prefer a focused patch over a full rewrite.

## Audit Mode

Report findings before proposing prose changes. Order findings by impact:

1. False or overclaimed coverage
2. Incorrect real/fake boundaries
3. Incorrect CI or blocking status
4. Stale paths, test names, commands, or profiles
5. Missing assertions, failure meaning, or non-goals
6. Missing planned/partial/xfail distinction
7. Structure and readability issues

For each finding include:

- Document claim
- Repository evidence
- Classification
- Impact
- Recommended correction

If no issue is found, state what was inspected and any residual verification gaps.

## Reconcile Mode

1. Identify overlapping claims across documents.
2. Choose current code and configuration as the primary source of truth.
3. Preserve module-specific ownership explanations in module documents.
4. Keep global policy, shared taxonomy, and CI-wide rules in overview documents.
5. Replace contradictions with explicit boundary statements.
6. Avoid copying the same long explanation into every document.

## Change Discipline

- Do not convert PLANNED items to LANDED without implementation evidence.
- Do not erase known gaps because the desired architecture is clear.
- Do not remove useful historical context unless it is misleading or the user asks for cleanup.
- Do not execute costly, external, staging, or real-LLM tests solely to update documentation without user approval.
- Label claims unverified when the environment cannot run the relevant command.
