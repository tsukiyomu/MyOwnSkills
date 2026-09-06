# Status And Ledger Examples

Use these shapes only if they fit the existing plan. Unit IDs, acceptance, and
dependencies already in the plan stay in their original locations.

## Task Annotations

```md
- [ ] [TODO] MIG-3 — Restore CI coverage
- [ ] [IN_PROGRESS] MIG-2 — Port observability integration
```

After checking the full acceptance boundary:

```md
- [x] [DONE] MIG-2 — Port observability integration
  - Run: run-002; report: [MIG-2 journal](../reports/mig-2-journal.md).
```

If required evidence is missing:

```md
- [ ] [REVIEW_NEEDED] MIG-2 — Port observability integration
  - Run: run-002; report: [MIG-2 journal](../reports/mig-2-journal.md).
  - Remaining acceptance: execute the disabled-configuration lifecycle check.
```

For an actual external prerequisite:

```md
- [ ] [BLOCKED] MIG-2 — Port observability integration
  - Required input: the legacy integration revision referenced by the plan;
    checked the available branches and archived patches without finding it.
```

Preserve numbered steps or tables when already used; checkboxes are optional.

## Compact History

```md
| Run ID | Date | Selected Task | Status | Evidence / Report | Next Recommended Task |
|---|---|---|---|---|---|
| run-002 | 2026-09-05 | MIG-2 | REVIEW_NEEDED | [Journal](../reports/mig-2-journal.md): lifecycle port verified; disabled mode unchecked | Complete MIG-2 disabled-mode check |
| run-003 | 2026-09-06 | MIG-2, follow-up to run-002 | DONE | [Verification](../reports/mig-2-verification.md): disabled mode passed | MIG-3, dependencies satisfied |
```

These are separate completed attempts. Retries, delegated checks, or conversation
turns within `run-002` do not each receive a row. Keep long reports and raw logs out
of the task annotations and ledger. If an equivalent tracker exists elsewhere,
update it instead of copying this table into the plan.
