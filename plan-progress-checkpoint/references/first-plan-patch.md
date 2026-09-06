# First Plan Patch

Read this when execution needs progress tracking and the existing plan has no
usable status or history structure.

Before adding anything, inspect the plan's linked trackers and task tables. Reuse
an equivalent progress file even if it is not called "Progress Ledger". Preserve
the task hierarchy and stable IDs; do not generate a second execution checklist
beside a plan that already has tasks.

For a plan with numbered work units, a minimal patch can be:

```md
## MIG-2 — Port observability integration

Status: IN_PROGRESS

<!-- Existing purpose, boundary, acceptance, and dependencies remain here. -->

## Progress Ledger

| Run ID | Date | Selected Task | Status | Evidence / Report | Next Recommended Task |
|---|---|---|---|---|---|
```

Add the outcome row when the logical unit run reaches an outcome or must hand off
with unresolved work. A run resumed after a routine pause keeps the same identity.

If the document only describes a broad phase, derive a bounded unit only when its
intent and acceptance are sufficiently clear. Add the minimum unit contract needed
to remove ambiguity; do not invent a roadmap or choose arbitrary code fragments.
If material intent is missing, record that gap before dependent implementation.

Select using user instructions, priorities, and satisfied dependencies. The first
listed step is not necessarily runnable. Existing user authorization to execute a
batch remains valid after this initialization.
