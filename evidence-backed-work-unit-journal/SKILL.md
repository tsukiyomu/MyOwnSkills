---
name: evidence-backed-work-unit-journal
description: >-
  Create or rewrite a concise evidence-backed journal for one engineering work unit:
  final facts, alignment with its plan, acceptance evidence, proof limits, and one
  next step. Use for execution reports and readable rewrites of existing work notes;
  not for implementation execution, architecture design, or project onboarding.
---

# Evidence-Backed Work Unit Journal

Report what one work unit actually accomplished and what the available evidence
supports. Use [the compact journal template](assets/work-unit-journal-template.md)
as the single maintained output template. Adapt its length and headings to the
work; do not add sections simply to fill a form.

## Responsibility boundary

- **Architecture** owns enduring system structure and design rationale.
- **Plan** owns the objective, work units, requirements, sequence, dependencies, scope, risks, and acceptance.
- **Project/language rules and repository instructions** constrain the work; the **agent** independently chooses how to implement and verify it within those constraints and the Plan.
- **Checkpoint** owns unit selection, current context, and final progress registration.
- **Execution rationale** explains why material implementation choices follow from repository evidence and engineering concerns.
- **Journal** records the resulting facts, plan alignment, evidence, and limitations.
- **Plan re-entry guide** compresses the current plan position for someone returning.

Explain the larger objective and this unit's contribution briefly, then link to
the Plan for upstream reasoning. Do not reproduce the design process, option
catalogue, repository inventory, or engineering teaching. Retain a local decision
only when needed to understand a result, deviation, or residual risk: briefly state
the deciding fact and resulting effect. Detailed reasons, engineering principles,
and recognition cues belong to Execution Rationale.

When a useful learning entry exists, an optional **Learning Reference** may name
one or two decision topics and link to their existing Execution Rationale document
or accessible conversation record. Keep it to labels and links, without copying
Teach-back, principles, or recognition cues into the journal. Omit it when it adds
no value or has no usable target. Do not invent a link or require a new standalone
rationale document merely to populate this section.

A request to write or rewrite a journal authorizes reporting, not completion of
the underlying implementation, execution of subsequent units, or changes to the
Plan, re-entry guide, or architecture documents. Inspect relevant sources within
the requested scope; report missing evidence instead of generating it merely to
make a completion claim. An agent carrying out an implementation task can use
this skill to report checks already performed as part of its authorized work.

Follow the user's output path or requested in-place rewrite. Otherwise reuse the
project's report/evidence directory; if none exists, use
`docs/reports/<work-unit>-journal.md`. Preserve unique source evidence before
rewriting as described below. Do not create a parallel report for the same run
merely because another skill also requests its journal.

## Build the journal from evidence

1. Identify the work-unit ID, governing Plan or task input, larger purpose, scope,
   and acceptance criteria. If no Plan exists, cite the supplied task; mark missing
   criteria or uncertain placement instead of inventing a plan or roadmap.
2. Group actual changes into meaningful outcomes and compare them with the agreed
   scope. Distinguish implemented behavior from intended behavior. State whether
   execution followed the Plan; if comparison is impossible, say why.
3. Map material completion claims to source evidence. Record a usable source
   locator and the revision, time, environment, or dependency boundary needed to
   interpret it. Separate observed results, historical records, reported claims,
   and inferences. A commit locates a change; it alone does not prove runtime behavior.
4. Choose evidence by how directly it tests the relevant acceptance criterion,
   not by a hierarchy of hosted, local, runtime, or static evidence. Explain what
   each material result establishes and where its proof stops. Missing, skipped,
   failed, and inaccessible checks are distinct from passed checks.
5. Record only material deviations and recovery: intended outcome, actual outcome,
   deciding fact, and residual impact. Keep these with the relevant result rather
   than repeating them in multiple sections.
6. End with one next action and why it follows. Use the governing Plan where it
   identifies a valid next unit; otherwise label the action as a proposal or name
   the evidence/decision needed to proceed. A next step is not authorization to do it.

Centralize detailed evidence identifiers and proof limits. Add a short overall
proof boundary only when it prevents a wider misunderstanding not already clear
from the evidence table. Use code excerpts only when a material claim would
otherwise be hard to verify; prefer precise links for routine changes.

## Status is a conclusion

Use the project's existing vocabulary and meanings. When none exists, distinguish
tracking states from outcomes:

| Status | Meaning |
|---|---|
| `TODO` | The unit has not started. |
| `IN_PROGRESS` | The task is actively continuing and work or required verification remains; do not imply acceptance. |
| `DONE` | The agreed acceptance criteria are supported by recorded evidence. |
| `REVIEW_NEEDED` | The run has handed off with required verification incomplete, or a required review or decision remains before acceptance can be concluded. |
| `BLOCKED` | A named unresolved condition prevents further work on the unit. |

Do not convert incomplete work into `DONE` because a report was produced, or force
ongoing work into an outcome state. When reporting a stopped run, distinguish an
acceptance gap awaiting verification or review (`REVIEW_NEEDED`) from a named
condition preventing further work (`BLOCKED`); do not silently change the meaning
of an existing checkpoint status. Tests are required when the acceptance criteria
or changed behavior call for them; documentation and other suitable units may be
accepted using other evidence. Do not invent a universal test gate. Historical
`DONE` and green results remain attached to their original revision and environment
unless current evidence supports carrying them forward.

## Rewrite without losing provenance

Keep unique information needed for audit, recovery, or continuation available when
condensing existing notes. Prefer links to the existing raw reports or original
record; if the only copy contains necessary detail, preserve that detail in a
focused appendix or separate linked record before shortening the body. Do not
create an appendix for routine commands that add no future value.

Preserve unresolved unknowns, failures with residual impact, original evidence
context, and conflicting sources. Distinguish historical fact from current
assessment; never silently replace the former with an unsupported current claim.
There is no word minimum, mandatory appendix, teaching pause, or fixed inventory
of sections. The finished journal should let a reader see the result, its basis,
its limits, and the next action without reading raw execution detail.
