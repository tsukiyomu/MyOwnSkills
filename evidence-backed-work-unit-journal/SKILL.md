---
name: evidence-backed-work-unit-journal
description: >
  Create or rewrite a concise engineering execution journal for one work unit.
  Use this when the user wants to record what a specific migration, feature, bug fix,
  test, CI/CD, observability, refactor, performance, or recovery unit accomplished,
  how it differs from plan, what evidence supports completion, what remains unproven,
  and what should happen next. Keep the main journal human-readable and move low-level
  execution detail to an optional Agent appendix.
---

# Evidence-Backed Work Unit Journal

## Purpose

Create a short execution journal for **one engineering work unit**.

The journal is not a raw activity log and not a full design document.
Its job is to let a human reader quickly answer:

1. What larger plan does this work unit belong to?
2. What exactly was this unit supposed to cut or complete?
3. What actually changed?
4. Did execution differ from the plan?
5. What evidence supports the completion claim?
6. What does that evidence prove, and what does it not prove?
7. Did anything go wrong, and how was it recovered?
8. What is the next work unit?
9. If this unit has a learning goal, what engineering idea should the reader retain?

The target reader is:

> A software engineer / QA / SDTE who understands general engineering concepts,
> but wants to recover the progress of one work unit quickly without reading every
> command, experiment, inventory, or internal reasoning record.

---

# Core Principle

Always structure the journal as:

```text
Overall plan
    ↓
Current work unit
    ↓
Actual execution result
    ↓
Evidence
    ↓
Proof boundary
    ↓
Next step
```

If something unusual happened:

```text
Deviation
    ↓
Recovery
    ↓
Residual impact
```

If the work unit has a learning objective:

```text
Engineering idea
    ↓
Why this approach was chosen
    ↓
What the reader should be able to explain
```

The main journal is **human-first**.
Low-level execution details may be preserved for later Agent use, but they must not
obscure the progress narrative.

---

# Main Design Rule

For every journal, separate two information layers.

## Layer 1 — Human Progress Narrative

This is the journal body.
It should answer:

- Why does this work unit exist?
- What did it accomplish?
- How do we know?
- What remains outside the proof boundary?
- What happens next?

## Layer 2 — Agent Execution Memory

This is optional detail for later review, audit, debugging, or autonomous continuation.
It may contain:

- commands;
- repository inventory;
- assumptions and unknowns;
- option comparisons;
- exact metadata;
- requirement-to-code mappings;
- failed attempts;
- raw check output;
- environment details;
- recovery history.

Put this information in an appendix or a separate Agent-facing file.
Do not let it dominate the main report.

---

# When to Use

Use this skill when the user asks for something like:

- "Write the execution journal for this task."
- "Summarize this work unit."
- "Rewrite this long engineering journal so it is easier to read."
- "Record what MIG-1 completed."
- "Create a concise evidence-backed report for this CI change."
- "Turn these execution notes into a work-unit journal."
- "I want a human-readable journal but keep the detailed evidence for the Agent."

Typical work units include:

- migration / upstream sync;
- feature implementation;
- bug fix;
- test architecture;
- CI/CD change;
- observability integration;
- dependency upgrade;
- refactor;
- performance tuning;
- incident recovery;
- data migration;
- release hardening.

Do not use this as the primary format when the user wants:

- a project-wide quick-start / re-entry guide;
- a full architecture design;
- a complete test plan;
- a root-cause analysis;
- a daily diary of everything attempted;
- a raw autonomous-agent trace.

Those can reference this journal instead.

---

# Required Output Structure

Use the following structure by default.
Sections marked optional must disappear when they add no value.

## 1. One-Line Conclusion

This section must provide both the **upper-level narrative** and the **current cut**.

Use this structure:

```markdown
## 1. One-Line Conclusion

**Overall objective:**
<What larger plan or migration this work unit belongs to.>

**This work unit:**
<What this unit specifically changes, closes, migrates, proves, or isolates.>

**Status:**
<DONE / PARTIAL / BLOCKED / REVIEW_NEEDED>

**Next:**
<The next work unit or immediate next action.>
```

A reader should understand the current project position after reading only this section.

### Good example

> Overall objective: reconnect the existing testing architecture and Langfuse work to
> the latest upstream codebase. This work unit creates the upstream-rooted migration
> branch and moves the existing engineering documentation without transferring stale
> test claims. Status: DONE. Next: port the Langfuse integration and deterministic tests.

### Bad example

> MIG-1 completed branch creation, restore, docs staging, ignore updates, migration status,
> architecture notices, and commit 0cd39102.

The bad example lists implementation facts before explaining the engineering story.

---

## 2. Execution Result

Record only meaningful changes.

Use:

```markdown
## 2. Execution Result

### Actual changes
- ...
- ...
- ...

### Difference from plan
None.
```

If there was a meaningful difference:

```markdown
### Difference from plan

- **Planned:** ...
- **Actual:** ...
- **Why:** ...
- **Impact:** ...
```

Rules:

- Group small edits into engineering outcomes.
- Do not list every command or file touch.
- Do not repeat evidence here unless the result is impossible to understand without it.
- If there is no difference from plan, write `None.` and stop.

---

## 3. Evidence

Evidence must be centralized here.

Prefer a compact table:

```markdown
## 3. Evidence

| Check | Result | Proves | Does not prove |
|---|---|---|---|
| ... | ... | ... | ... |
```

Evidence may include:

- test execution;
- CI run;
- commit / revision;
- artifact;
- digest / checksum;
- runtime observation;
- structured report;
- schema / contract check;
- static repository inspection.

Important identifiers such as commit, run, artifact, revision, and digest should be
concentrated in this section instead of scattered throughout the report.

### Evidence rule

Every important completion claim should have at least one corresponding proof source.

Bad:

> Stream evidence is complete.

Better:

> Hosted failure run produced a red pytest result, the upload step still succeeded,
> the downloaded artifact digest matched GitHub metadata, and the JUnit XML contained
> the expected failing testcase.

---

## 4. Deviation and Recovery — Optional

Delete this entire section when there was no meaningful deviation.

Use it only when execution departed from the intended path in a way worth remembering.

```markdown
## 4. Deviation and Recovery

### <Problem>

**What happened:**
...

**Why:**
...

**Recovery:**
...

**Residual impact:**
None / ...
```

Do not turn every typo, shell quoting issue, or temporary failed command into a major
journal event unless it changed the engineering decision, created risk, or is likely to
matter during future re-entry.

Minor failures belong in Agent Execution Detail.

---

## 5. Proof Boundary

Keep this short.

Use:

```markdown
## 5. Proof Boundary

This work unit proves that ...

It does not prove that ...
```

The proof boundary should prevent overclaiming.

Useful distinctions include:

- migrated documentation vs migrated implementation;
- real route vs real full workflow;
- deterministic model substitute vs real LLM;
- persistence spy vs production database;
- local test result vs hosted CI result;
- artifact metadata vs downloaded artifact content;
- test execution vs branch-protection enforcement.

---

## 6. Next Step

State the next work unit, not the entire roadmap.

Use:

```markdown
## 6. Next Step

**Next work unit:** ...

**Why next:** ...
```

Prefer one clear next step.
Use two only when the plan explicitly contains parallel workstreams.

---

## 7. Teach-Back — Optional

Only include this section when the work unit has an explicit learning objective.

The goal is not to quiz vocabulary.
It is to extract the reusable engineering judgment behind the work.

Use:

```markdown
## 7. Teach-Back

**Engineering idea:**
<General principle demonstrated by this work.>

**Why this approach was chosen:**
<Why this was preferable to the obvious alternative.>

**The reader should be able to explain:**
<One or two questions or statements.>
```

Examples of reusable engineering ideas:

- control the test boundary before increasing realism;
- isolate nondeterministic dependencies;
- preserve failure evidence, not only success evidence;
- separate execution truth from evidence storage;
- make retries attributable rather than overwriting old state;
- separate historical evidence from current revision validity;
- prefer reversible migration steps;
- keep source control and runtime artifacts in different lifecycles;
- verify that a test can fail when the protected behavior is broken.

Delete this section if there is no learning objective.

---

# Optional Appendix — Agent Execution Detail

Use an appendix only when the detailed execution context is useful for later Agent work.

Recommended heading:

```markdown
# Appendix — Agent Execution Detail
```

Possible subsections:

```markdown
## A. Initial Understanding
## B. Repository / Project Inventory
## C. Assumptions and Unknowns
## D. Invariants / Problem Model
## E. Options and Trade-offs
## F. Requirement-to-Change-to-Evidence Mapping
## G. Raw Commands and Checks
## H. Detailed Deviation History
## I. Environment and Metadata
```

Do not create these sections automatically.
Only preserve details that are genuinely useful for future execution, debugging, audit,
or Agent continuation.

The appendix is allowed to be technical and verbose.
The main journal is not.

---

# Writing Rules

## 1. Start from the larger plan

Never begin a journal with a list of files, commands, or internal status codes.

First answer:

> What larger engineering objective does this work unit serve?

Then answer:

> What exact slice of that objective does this unit complete?

---

## 2. Report outcomes, not activity

Bad:

> Edited two workflows, changed `.gitignore`, ran pytest, parsed XML, checked artifact.

Better:

> Both CI suites now publish independent JUnit evidence for successful and failing runs,
> with missing reports treated as evidence-pipeline failures.

Use raw activity only as supporting evidence.

---

## 3. Keep plan difference explicit but small

The reader should quickly know whether execution followed the plan.

If nothing meaningful changed:

> Difference from plan: None.

Do not invent a deviation section merely because small implementation details changed.

---

## 4. Centralize proof

Do not scatter commit hashes, run IDs, artifact names, digests, and test counts across
many sections.

Put them in `Evidence` unless another section truly needs the identifier.

---

## 5. Every evidence item has a boundary

For every important check, ask:

```text
What does this prove?
What does this not prove?
```

A green result must never silently expand into a larger claim than the test boundary
supports.

---

## 6. Delete empty structure

No section exists merely because the template contains it.

Delete:

- `Deviation and Recovery` when nothing meaningful happened;
- `Teach-Back` when there is no learning goal;
- appendix sections that add no future value.

A shorter truthful journal is better than a complete-looking but repetitive one.

---

## 7. Human-first, Agent-recoverable

The main journal should normally be readable in a few minutes.

Detailed technical context should remain available to the Agent through:

- an appendix;
- linked plans;
- detailed evidence files;
- raw reports;
- separate agent-facing execution notes.

Do not destroy useful detail just to shorten the report.
Move it to the correct layer.

---

## 8. Preserve the distinction between status and proof

A status such as `DONE` is a conclusion.
Evidence is what justifies that conclusion.

Do not use status labels as evidence.

Likewise, historical `DONE`, `LANDED`, or green results remain tied to the revision and
environment that produced them unless revalidated.

---

# Information Extraction Method

When rewriting a long execution journal or raw notes, extract information in this order.

## Step 1 — Find the overall plan

Identify:

- the larger migration / implementation / testing goal;
- where the current work unit sits in that plan;
- what comes immediately before and after it.

Write this before reviewing low-level detail.

---

## Step 2 — Identify the exact work-unit cut

Ask:

> If this unit had to be described as one engineering outcome, what is it?

Examples:

- establish an upstream-rooted migration baseline;
- connect Langfuse instrumentation to the current runtime;
- make streaming-contract tests run in hosted CI;
- retain structured failure evidence;
- remove duplicate side-effect execution;
- make cancellation clean up active state.

---

## Step 3 — Extract actual changes

Group implementation details into 3–7 meaningful outcomes.

Do not reproduce a chronological command log.

---

## Step 4 — Compare plan and reality

Look for:

- scope expansion;
- scope reduction;
- changed implementation strategy;
- unexpected repository behavior;
- environment problems that changed the decision;
- deferred acceptance criteria.

If none materially affected the unit, write `None.`

---

## Step 5 — Collect acceptance evidence

For every acceptance claim, identify the strongest available evidence.

Prefer, roughly in this order when relevant:

```text
real hosted/runtime evidence
    ↓
structured artifact / parsed result
    ↓
local executable test
    ↓
static configuration / source inspection
    ↓
assumption / inference
```

Do not upgrade a weaker evidence type into a stronger claim.

---

## Step 6 — Define the proof boundary

Ask:

> What tempting larger claim could someone incorrectly make after seeing this result?

Explicitly deny that larger claim when necessary.

---

## Step 7 — Keep only meaningful deviations

Move incidental failures to Agent detail.
Keep a deviation in the human journal only when it affects:

- scope;
- design;
- risk;
- reproducibility;
- recovery strategy;
- future continuation.

---

## Step 8 — Extract the next action

Use the plan to identify the next work unit.
Do not replace it with every unresolved risk in the project.

---

## Step 9 — Extract engineering thought when useful

If the unit has a learning purpose, ask:

> Why did an engineer choose this approach instead of the obvious alternative?

Examples:

```text
Full E2E immediately
    → too many variables / nondeterminism
    → choose controlled test boundary first
    → engineering idea: progressive integration
```

```text
Only keep console logs
    → weak machine-readable evidence
    → publish JUnit artifacts
    → engineering idea: failure observability and traceability
```

This is the preferred form of Teach-Back.

---

# Recommended Status Vocabulary

Use a small status set unless the project already defines one.

| Status | Meaning |
|---|---|
| `DONE` | Acceptance criteria are supported by the recorded evidence |
| `PARTIAL` | Meaningful implementation exists, but acceptance is incomplete |
| `BLOCKED` | Progress depends on an unresolved external or project condition |
| `REVIEW_NEEDED` | Implementation/evidence exists but requires an explicit human decision or review |

Do not create many internal status codes in the human-facing journal.
If detailed internal labels already exist, place them in evidence or appendix.

---

# Relationship to Other Engineering Documents

Use a layered documentation model:

```text
Project Re-entry Guide
    ↓
Plan / Roadmap
    ↓
Work Unit Execution Journal
    ↓
Agent Execution Detail / Raw Evidence
```

The documents answer different questions.

## Project Re-entry Guide

> What is this project, where are we now, and how do I resume after time away?

## Plan / Roadmap

> What sequence of work units should move the project toward the target state?

## Work Unit Execution Journal

> What did this specific unit accomplish, how do we know, and what is next?

## Agent Execution Detail / Raw Evidence

> Exactly what was inspected, executed, attempted, recovered, and observed?

Do not make one document perform all four jobs.

---

# Output Quality Check

Before finishing, verify that a reader can answer these questions without reading the appendix:

1. What larger plan is currently being executed?
2. Which part of that plan is this work unit?
3. What changed in this unit?
4. Did execution differ materially from the plan?
5. What evidence supports the status?
6. What does that evidence not prove?
7. Was there a meaningful deviation or recovery?
8. What happens next?
9. If this was a learning unit, what engineering principle should be retained?

If the reader must inspect raw commands or inventory tables to answer these questions,
the main journal is too detailed or poorly structured.

---

# Default Length

For a normal work unit, target roughly:

- 500–1,200 words for the human journal;
- shorter when the unit is simple;
- longer only when evidence or deviations genuinely require it.

The optional Agent appendix may be much longer.

---

# Recommended Filenames

Generic:

```text
<work-unit>-execution-journal.md
```

Examples:

```text
mig-1-execution-journal.md
c0-3-execution-journal.md
langfuse-integration-execution-journal.md
stream-contract-ci-execution-journal.md
```

If Agent detail is separated:

```text
<work-unit>-agent-execution-detail.md
```

---

# Minimal Default Template

When there is no reason to expand, prefer this compact form:

```markdown
# <Work Unit> Execution Journal

## 1. One-Line Conclusion

**Overall objective:** ...

**This work unit:** ...

**Status:** DONE / PARTIAL / BLOCKED / REVIEW_NEEDED

**Next:** ...

## 2. Execution Result

### Actual changes
- ...
- ...

### Difference from plan
None.

## 3. Evidence

| Check | Result | Proves | Does not prove |
|---|---|---|---|
| ... | ... | ... | ... |

## 5. Proof Boundary

This work unit proves that ...

It does not prove that ...

## 6. Next Step

**Next work unit:** ...

**Why next:** ...
```

Add `Deviation and Recovery`, `Teach-Back`, or the Agent appendix only when they add
real information.
