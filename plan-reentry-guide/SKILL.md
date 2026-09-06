---
name: plan-reentry-guide
description: Create or refresh a concise plan re-entry guide from the current plan, relevant architecture, and work-unit evidence. Use when a returning engineer needs to understand why this work began, where the plan stands, what remains unproven, and why the next unit comes next. Not a full project onboarding guide, replacement roadmap, or execution journal.
---

# Plan Re-entry Guide

Use `$plan-reentry-guide` to recover enough context to continue a specific engineering effort in about five minutes. This skill provides the human navigation layer for an active plan.

## Responsibility boundary

Architecture explains how the system works and why. The plan owns the objective, unit contracts, order, and acceptance. Journals report what each execution actually delivered and proved. This guide connects those sources into a short, dated view of the current effort.

Checkpoint owns the selected unit, current context, and final progress status. The agent chooses how to implement under the Plan, repository instructions, and project/language rules; Execution Rationale explains its material engineering choices. This guide recovers active engineering plan context: why the plan reached this point and why the next unit follows. It does not teach why an individual unit was implemented a particular way.

Keep an implementation adaptation to the brief fact and its significance for plan progress, then link to the existing unit-specific Execution Rationale when the reader needs the detailed reasons. For example, a runtime restructure may explain why an integration needed adaptation; the choice of lifecycle boundary belongs in Rationale. Do not copy its Evidence -> Concern -> Decision explanation, engineering principles, or recognition cues into this guide. Use an existing document or accessible conversation record; do not invent a link or create a separate rationale file just for navigation.

Do not duplicate the roadmap, acceptance matrix, architecture tutorial, or command history. Do not execute the next unit, change plan priorities, or promote a task to `DONE` while writing a guide. If sources disagree, make the discrepancy visible rather than silently reconciling their status.

## Establish the source and currentness

1. Identify the active plan from the user's request and repository context. If several efforts exist, choose the named one. If no active effort can be determined, ask which plan to cover while inspecting shared context; do not combine unrelated plans into an invented roadmap.
2. Read the plan's goal, unit contracts, dependency order, and current progress. Read only the architecture needed to explain that goal and the relevant completed/current unit journals and evidence.
3. Check source dates and revision/environment scope. Use current code or execution evidence only as needed to resolve a material claim. Distinguish plan-reported status, observed implementation, and verified behavior. A migration does not transfer historical green results to the new revision.
4. Record an as-of date, active plan link, and observed revision/branch when available. If only supplied documents are available, label the guide as a snapshot of those sources and leave unknown current state explicit.

If a journal says `DONE` but the plan is pending, or a planned next unit has unmet dependencies, report both facts and the required reconciliation. Recommend confirming the discrepancy before dependent execution. Do not edit source statuses without that work being requested.

## Write the smallest useful navigation guide

Use the following questions as a flexible outline, combining sections when possible:

- **Why this effort exists:** the larger engineering goal and the concrete reason work began. Include only enough system context to understand it, with an architecture link.
- **Where the plan stands:** meaningful completed capability, current unit, and relevant blocker or remaining gap. Explain why completed work matters, with links to the corresponding unit evidence.
- **What is and is not established:** the boundary of current evidence, especially historical versus current implementation, local versus hosted execution, and controlled versus real dependencies. Do not restate every test result.
- **Why the next unit is next:** the next unit from the plan, the dependency or risk it addresses, and any prerequisite still unresolved. If the plan has ended, say so; do not invent future work. Label a new recommendation as a proposal, distinct from the plan.
- **How to resume and where to read:** a short reading path and, when documented, the smallest relevant baseline check. Suggested commands are not evidence of execution. Link to the unit contract for exact acceptance and to the journal for detailed proof.

An ordinary guide should fit a few screens, often about 400-800 words in English or a similar reading time in the user's language. This is a guide, not a quota. Omit empty sections. A workflow sketch or tiny glossary is optional only when needed to understand the current unit; no mandatory project introduction, engineering-principles chapter, or 5-12 term glossary.

Explain project-specific terms through their effect before naming them. For example: "The current tests exercise the streaming API with controlled agent responses. They do not establish real model or tool behavior." This explains the meaning of current evidence; detailed reasons for choosing that test boundary belong in Execution Rationale. Keep identifiers and exact code details in links unless they are needed to resume.

## Location and maintenance

Update an existing guide for this same plan rather than creating competing entry points. Otherwise use `docs/plans/PLAN-REENTRY.md` when that matches the repository. With multiple active plans, use `<plan-name>-reentry.md` beside the respective plan. Follow the user's chosen location and existing conventions.

Refresh the snapshot when requested, or when the current task explicitly includes maintaining it. Do not turn every implementation task into an automatic rewrite. During refresh, replace stale current-state prose with sourced facts while retaining useful links; historical execution belongs in journals and the progress ledger.

The guide is derived navigation, never the authoritative progress ledger. Source plan changes do not become authorized because they would make the guide easier to write.

## Check before delivery

A returning reader should be able to explain why the effort began, what has been achieved, what remains uncertain, what to do next and why, and which source to open for details. Every material completion claim should lead to evidence with the right revision scope. Keep unknowns and source conflicts visible.

Deliver the guide link and any consequential source conflict. Do not attach another project overview or execution report by default.
