---
name: work-unit-implementation-walkthrough
description: >-
  Turn a work-unit journal or change report into a systematic implementation
  learning walkthrough grounded in the corresponding source revision, diff,
  configuration, and tests. Use when a reader wants to understand how a completed
  or partial change actually works, with a learning map and connected explanations
  of each substantive implementation topic. Not a journal rewrite, project
  onboarding guide, or reconstruction of an agent session.
---

# Work Unit Implementation Walkthrough

Use a Journal as the entry point to teach the implementation of a specific change.
The reader should be able to follow a concrete case through the changed system,
explain how the relevant code or configuration works, and understand how its tests
check the result. Knowing the outcome or the reason for a decision is not enough.

## Scope and sources

Start from the named Journal or change report and its work-unit scope. Inspect its
linked Plan, decisions, source, diff, tests, and artifacts as needed. A standalone
Rationale or agent transcript is not required. Respect the requested unit or batch;
do not expand into the entire project because it shares dependencies.

Identify the repository, work unit, source revision or range, and available evidence.
Prefer the revision referenced by the Journal. Use read-only revision inspection
when available; do not switch the user's checkout to explain historical code.
Distinguish the recorded change from later edits and from uncommitted work. If the
historical revision cannot be read, label a current-code walkthrough as such and
leave the historical implementation uncertain. Without a pre-change source or
diff, do not fabricate a before/after comparison.

Treat the Journal as a source of claims and navigation, not proof of implementation.
If sources conflict, explain the discrepancy at the affected topic. A report-only
input supports a report-based learning map and explanation of available excerpts;
mark code-dependent gaps and name the minimum missing source. Do not invent code,
line numbers, test results, execution history, or the author's motives.

## Build the learning map

Inventory the substantive outcomes, changed behaviors, and supporting mechanisms
within the selected scope. Cross-check against the actual diff and tests so the
Journal's headings do not become the limit of the analysis. Distinguish newly
changed mechanisms from unchanged context needed to understand them.

Group related edits into learning topics and order them by causal or dependency
relationships. Start with enough system context to follow the change, then trace
its implementation and verification. Do not make a section for every file, command,
or technical noun. Configuration, CI, documentation migrations, and removed code
can be central topics even when no application function changed.

Provide a compact map with links to the topic explanations and source entry points.
Every substantive in-scope outcome should be explained or explicitly marked as
unsupported by the available sources. Explain familiar or mechanical topics briefly;
do not silently skip them based on assumed reader expertise. Identify prerequisites
where they first become relevant rather than adding a general textbook chapter.

Default to delivering the complete walkthrough for the selected scope. The map is
navigation, not a substitute for the explanation. If the user asks for interactive
learning, follow that preference. Otherwise do not stop after every topic for a quiz
or confirmation. On a real interruption, preserve the map and the remaining topics
and resume from them without restarting completed material.

## Explain the implementation as a connected account

For each topic, connect the following information in prose, code excerpts, or a
small diagram as appropriate. These are comprehension goals, not mandatory headings
or a template to repeat mechanically:

- **Behavior and contribution:** what this part does, what changed where evidence
  supports comparison, and how it contributes to the work-unit objective.
- **Mechanism:** the concrete entry point, key calls or configuration consumers,
  data transformations, state ownership, side effects, and relevant failure or
  cleanup behavior. Explain only the dependencies needed to follow this topic.
- **Code in context:** show the smallest exact excerpt or diff that explains the
  mechanism, with file, symbol or configuration key, and source revision. Include
  verified line numbers when available. Explain significant operations, not each
  line's syntax. Links alone are insufficient for the central mechanisms.
- **A concrete case:** follow an input, event, command, or document through the
  mechanism to its observable output. Track values or state where useful. Label
  constructed examples and predicted outcomes; never present them as an observed run.
- **Verification:** connect setup, controlled dependencies, triggering action, and
  specific assertions or checks to the claimed behavior. Explain how an assertion
  detects the relevant defect and what it leaves untested. A test definition shows
  intended checks; execution results establish what ran at their recorded revision.
- **Learning:** derive a useful principle from the mechanism and show where it would
  apply again, including a relevant limitation. Tie it back to existing decision
  rationale without repeating a complete ADR or substituting abstract principles
  for the implementation explanation.

For a complex mechanism, deepen the relevant calls, state transitions, or language
semantics until the connection is understandable. For a simple one, a short paragraph
and a focused excerpt may be sufficient. A useful counterfactual can explain what
would break if a guard or step were omitted; label it as analysis unless tested.
Do not change code to demonstrate the counterfactual without that work being requested.

Use an end-to-end thread to connect related topics. Show where each snippet sits in
that thread so the reader does not have to reconstruct the flow from scattered notes.
For CI or document-only work, follow artifact production/consumption or the document
movement and reference changes instead of inventing an application call chain.
Read [walkthrough-examples.md](references/walkthrough-examples.md) when examples would
help choose the right level of implementation explanation.

## Deliver a reusable learning document

Follow the user's output format and location. For a file-based request without an
explicit path, reuse an existing implementation walkthrough for that same unit and
revision; otherwise place a clearly named `<work-unit>-implementation-walkthrough.md`
beside the Journal when project conventions allow. When the user wants an answer
in conversation, give the walkthrough there. Do not overwrite the source Journal.

Open with the learning goal, source/version scope, a brief account of the change,
and the learning map. Follow with connected topic explanations. Close with a short
reading path for any deeper questions and remaining evidence gaps. A few optional
self-check questions may help when requested; do not assign mastery scores or infer
understanding from silence. Avoid fixed word counts or a mandatory appendix.

The finished walkthrough should let the reader locate every substantive change,
explain how it works using concrete code or configuration, and connect it to its
verification. Include missing and unsupported parts visibly instead of implying
complete implementation coverage. Check source links and revision attribution.
Do not claim the reader has learned the material or that this skill's effectiveness
has been validated merely because a document was generated.

## Relationship to other documents

Journal owns the execution result and its evidence. Rationale explains material
engineering choices and may already be embedded in the Journal. Re-entry restores
plan context. Session analysis reconstructs observable agent behavior. This skill
owns the implementation learning walkthrough and can use those documents as sources
without requiring their skills to be installed or invoking them automatically.

A request to explain an implementation does not authorize implementing unfinished
work, modifying project status, rewriting Journal/Rationale, or running commands
just to fill a verification gap. Use existing code and results for explanation;
perform additional execution only when it is part of the authorized task, and report
its actual revision, environment, and limits separately from historical evidence.
