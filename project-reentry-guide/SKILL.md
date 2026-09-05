---
name: project-reentry-guide
description: >
  Generate a beginner-friendly project re-entry / quick-start Markdown guide from
  deep project documents, plans, reports, repository notes, or current-state summaries.
  Use this when the reader is technically capable but has not worked on the project
  recently and needs to recover context quickly without rereading deep internal analysis.
---

# Project Re-entry Guide

## Purpose

Create a short, human-readable Markdown guide that helps an engineer quickly return to a project after several days or weeks away.

The guide is **not** a deep design document, implementation report, architecture specification, or agent execution plan.

Its purpose is to answer, in plain language:

1. What is this project?
2. What problem am I solving?
3. How does the important workflow roughly work?
4. What project-specific terms do I need to remember?
5. What have I already completed?
6. Why did those completed items matter?
7. What important gaps remain?
8. What should I work on next?
9. Where should I look if I need deeper detail?

The target reader is:

> A software engineer / SDTE who understands general software engineering concepts,
> but may know little about this particular repository and may have forgotten recent work.

---

## When to Use

Use this skill when the user asks for something like:

- "Give me a quick-start guide for this project."
- "I haven't touched this project for several days. Help me get back into it."
- "Turn these deep notes into something a newcomer can understand."
- "Create a re-entry document."
- "Create a project context recovery guide."
- "Summarize this project so I can continue work quickly."
- "Make this understandable to an SDTE who doesn't know the repository."

Do **not** use this format when the user primarily wants:

- a detailed implementation report;
- a full architecture design;
- a test plan;
- a root-cause analysis;
- a resume bullet;
- a complete project retrospective;
- an agent-facing execution state file.

Those can be linked from the re-entry guide as deeper references.

---

# Core Principle

Always translate:

> repository-specific terminology → engineering meaning → why it matters

Do not assume that the reader remembers project-specific nouns.

Bad:

> The real Route + fake Loop contract passed.

Better:

> The actual HTTP/SSE request path was tested while the Agent execution loop was replaced
> with a controlled test double. This verifies the real streaming API behavior without
> introducing nondeterministic model/tool behavior.

After the plain-language explanation, the internal term may be introduced:

> In the project, this is called the "real Route + fake Loop" test profile.

---

# Required Output Structure

Create a Markdown file with the following structure unless the project clearly requires a small adjustment.

## 1. Project in One Minute

Explain the project in approximately 5–10 sentences.

Cover:

- what the system does;
- what part of it the current work focuses on;
- what the current engineering goal is;
- why this work matters.

Avoid implementation details here.

A reader should understand the project's purpose after reading only this section.

---

## 2. What I Am Trying to Achieve

Describe the current project goal in terms of engineering outcomes.

Prefer statements such as:

- make a workflow deterministic and testable;
- prevent duplicated side effects;
- ensure cancellation cleans up correctly;
- make failures visible in CI;
- make failures diagnosable and reproducible.

Avoid statements that are only task names, issue numbers, file names, or internal milestones.

Bad:

> Complete P3-2 and P3-3.

Better:

> Close two important Agent runtime risks: duplicate tool execution and incomplete
> cleanup when a streaming request is cancelled.

If internal milestone names are useful, mention them only after the human-readable explanation.

---

## 3. How the Important Workflow Works

Show the main execution path with a simple text or Mermaid diagram.

Prefer a workflow such as:

```text
User request
    ↓
API / Stream entry
    ↓
Core workflow / Agent loop
    ↓
Model decision
    ↓
Optional tool call
    ↓
Tool result returned
    ↓
Final response
    ↓
Persistence / cleanup
```

Only include components that matter to the current work.

Do not reproduce the entire repository architecture unless necessary.

After the diagram, explain the workflow in plain language.

---

## 4. Terms I Need to Remember

Create a small glossary for project-specific terms that appear frequently.

For each term, provide:

### Term

**Plain meaning:** one or two sentences.

**Why it matters here:** one sentence.

Example:

### Scripted LLM

**Plain meaning:** A deterministic replacement for a real language model. Instead of
calling an external model, the test provides predefined responses.

**Why it matters here:** It keeps Agent-loop tests reproducible while still exercising
the real workflow logic.

Rules:

- Prefer 5–12 important terms.
- Do not define common programming terms unless the project gives them a special meaning.
- Never use an unexplained project-specific acronym in the definition itself.

---

## 5. What Has Already Been Completed

Summarize only meaningful completed capabilities.

For each completed item, use this format:

### Capability name

**What was done:**  
Explain it in plain language.

**Why it matters:**  
Explain what engineering risk or uncertainty it reduces.

**Evidence:**  
Mention the relevant test, CI result, artifact, report, file, or observed behavior when available.

Avoid raw chronological logs.

Avoid listing every small code edit.

Group related implementation work into capabilities.

---

## 6. What the Current Tests Actually Prove

Separate proven behavior from unproven assumptions.

Use a structure like:

### Proven

- ...
- ...
- ...

### Not yet proven

- ...
- ...
- ...

This section is important.

A quick-start document must prevent the returning engineer from accidentally
overclaiming what a green test means.

Examples of useful distinctions:

- real HTTP route tested vs. real external service not tested;
- deterministic model substitute vs. real LLM;
- local persistence spy vs. production database;
- CI evidence pipeline verified vs. staging deployment not verified.

---

## 7. Important Open Problems

List only the high-value unresolved problems.

For each one:

### Problem

**What can go wrong:**  
Describe the failure in concrete terms.

**Why it matters:**  
Describe the consequence.

**Current status:**  
Use simple wording such as:

- not implemented;
- failing test exists;
- intentionally deferred;
- partially implemented;
- waiting on environment/product decision.

**Do not** begin with internal status codes such as:

- XFAIL_GAP
- LANDED
- NOT_WIRED
- P3-2

If useful, place those internal labels at the end:

> Internal label: P3-2 / XFAIL_GAP

---

## 8. Current Priority

State the current recommended direction in a very small number of items.

Prefer:

```text
Now
↓
Close duplicate-execution risk
↓
Define cancellation behavior
↓
Add minimal tracing
↓
Connect deterministic Agent regression to CI
↓
Add replay for important failures
```

Explain why this order is useful.

Do not copy a large project roadmap into this section.

The reader should know what matters **now**, not every possible future feature.

---

## 9. If I Come Back After a Week

Create a practical re-entry checklist.

Example:

1. Read Sections 1–4 of this guide.
2. Read the "Current Priority" section.
3. Check whether the documented current branch/revision is still relevant.
4. Run the smallest deterministic test set that confirms the baseline.
5. Open the deep analysis document only for the current problem.
6. Do not start unrelated future work until the current high-value gap is understood.

This should help the reader start working within roughly 10–20 minutes.

---

## 10. Where to Read Deeper

Provide a small reference map.

Example:

| Need | Read |
|---|---|
| Understand overall project | README |
| Understand current testing strategy | testing-plan.md |
| Understand why priorities were chosen | final-testing-plan-analyze.md |
| See CI evidence | evidence report |
| Continue current implementation | current work-unit / issue |

Do not dump every project document here.

Only include documents that help answer a specific deeper question.

---

# Writing Rules

## 1. Explain before naming

Always explain the engineering idea before introducing repository-specific terminology.

Bad:

> real Route + scripted Loop + persistence spy

Better:

> Keep the real HTTP streaming path, replace the Agent execution with deterministic
> behavior, and observe whether final persistence is called. In this repository this
> corresponds to the "real Route + fake Loop + persistence spy" profile.

---

## 2. Prefer consequences over component names

Bad:

> Duplicate tool_call_id is XFAIL.

Better:

> The Agent can currently receive the same tool-call identifier across multiple rounds.
> If the runtime does not deduplicate it, a side-effecting tool may execute twice.

---

## 3. Keep implementation detail one layer below the main explanation

The main text should answer:

> What is happening and why does it matter?

Only then mention:

- test filenames;
- function names;
- nodeids;
- workflow names;
- internal labels;
- branches or revisions.

---

## 4. Avoid unexplained status vocabulary

Translate internal project status into normal language.

| Internal | Human-readable |
|---|---|
| LANDED | implemented and currently working |
| PARTIAL | partially implemented |
| XFAIL_GAP | expected failing test documents a known gap |
| NOT_WIRED | code exists but is not connected to the active workflow/CI |
| DELAYED | intentionally postponed |
| NEXT | current next work item |

The original status may be preserved in parentheses when useful.

---

## 5. Do not turn the guide into a history log

Avoid:

- every command that was run;
- every failed attempt;
- every revision;
- every intermediate decision;
- every test count.

Include such details only when they change how the project should be understood or resumed.

Deep evidence belongs in linked documents.

---

## 6. Keep the guide short enough to reread

Default target:

- 1,500–3,000 words for a medium project;
- shorter when possible.

If the source material is very large, summarize aggressively and link to deep references.

The quick-start guide should not become another deep report.

---

# Information Extraction Method

When source documents are available, extract information in this order.

## Step 1 — Find the project goal

Look for:

- project purpose;
- current engineering objective;
- problem being solved;
- intended user/business/technical value.

Summarize this before reading implementation details.

---

## Step 2 — Find the main workflow

Identify the smallest execution path needed to understand the current work.

Examples:

- request → route → service → DB;
- request → Agent loop → model → tool → finalization;
- event → queue → worker → persistence.

Do not model unrelated subsystems.

---

## Step 3 — Extract project-specific vocabulary

Look for repeated terms that a returning engineer may have forgotten.

Examples:

- specific route names;
- test profiles;
- gateway terms;
- internal phases;
- special mock/fake/spy objects;
- evidence terminology.

Translate them into plain language.

---

## Step 4 — Group completed work by capability

Turn many small implementation facts into larger engineering capabilities.

Example:

Instead of:

- added `--junitxml`;
- added `upload-artifact`;
- used `if: always()`;
- tested intentional failure;
- restored green;

write:

> **CI failure-evidence loop completed:** test failures turn the GitHub Check red,
> failure JUnit is retained, and the same workflow returns green after the defect is removed.

---

## Step 5 — Extract unresolved risks

Prefer unresolved items with consequences.

Good:

> cancellation may leave the Agent running after the client stops reading.

Weak:

> `test_chat_stream_user_stop_contract_gap` is xfailed.

The test name may be included as evidence after the risk is explained.

---

## Step 6 — Identify the current next action

Determine:

- what should be done next;
- why it is next;
- what should explicitly **not** be worked on yet.

Keep this section small.

---

# Output Quality Check

Before finishing, verify the document against these questions.

A technically capable engineer who has never seen the repository should be able to answer:

1. What does this project do?
2. What part am I currently working on?
3. What is the main workflow?
4. What do the important project-specific terms mean?
5. What has already been achieved?
6. What do the existing tests prove?
7. What do they not prove?
8. What are the two or three most important remaining risks?
9. What should I do next?
10. Which deeper document should I open if I need implementation details?

If the reader cannot answer these without reading another document first, simplify the guide.

---

# Relationship to Deep Project Documents

Use a layered documentation model:

```text
Project Re-entry Guide
    ↓
Human-readable technical overview
    ↓
Deep analysis / testing plan
    ↓
Implementation notes / evidence / exact test details
```

The re-entry guide is the **entry point**, not the source of every detail.

Do not delete or replace deep engineering documents.

Instead, make them easier to navigate by explaining:

- what each deep document is for;
- when the reader should open it.

---

# Recommended Filename

Default:

```text
PROJECT-QUICKSTART.md
```

Project-specific alternatives:

```text
NAGAAGENT-TESTING-QUICKSTART.md
TESTING-REENTRY-GUIDE.md
PROJECT-REENTRY.md
DEVELOPER-QUICKSTART.md
```

Prefer a filename that clearly communicates that the document is for **context recovery**, not full project documentation.
