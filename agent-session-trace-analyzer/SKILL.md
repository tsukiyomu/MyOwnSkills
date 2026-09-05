---
name: agent-session-trace-analyzer
description: Analyze one observable tool-using agent session from Claude Code, Codex, Hermes, or another coding agent. Reconstruct the request contract, execution timeline, tool calls, file changes, failures and recovery, context compaction epochs, subagents, verification, and requirement-to-evidence traceability. Include minimal, traceable source-code excerpts or diffs for material implementation claims and changes when source evidence is available. Use when asked how an agent handled a complex request, whether it stayed on goal after compaction, why it used particular tools, whether its final claims are supported, or which code segments correspond to its conclusions. Do not use for analyzing only the software feature itself.
---

# Agent Session Trace Analyzer

## Purpose

Analyze **how a tool-using agent executed one request** from observable evidence.

The analysis object is the session, not the software feature alone.

Typical execution chain:

```text
user request
-> interpretation and scope
-> evidence discovery
-> plan or task decomposition
-> tool calls
-> edits or other actions
-> failures and recovery
-> context compaction, if any
-> continued execution
-> verification
-> final response
```

This skill is platform-neutral. The analyzed session may come from Claude Code, Codex, Hermes, NagaAgent, or another tool-using agent.

## Identity rule

Before analyzing behavior, separate these identities:

1. **Analyzer**: the agent currently producing the report.
2. **Analyzed platform**: the product or agent that produced the recorded session.
3. **Analyzed session**: the exact trace, transcript, or session ID.
4. **Task domain**: the subject of the original request.
5. **Target repository or artifact**: what the analyzed agent was expected to inspect or change.
6. **Reference repositories or sources**: material used only for comparison.
7. **Analysis scope and cutoff**: which turns or events are included.

Never infer that Claude Code is analyzing NagaAgent merely because both appear in the evidence. Determine each role explicitly.

Use this identity block near the start of every report:

```markdown
## Analysis Identity

- Analyzer:
- Analyzed platform:
- Analyzed session ID or trace:
- Original task domain:
- Target repository or artifact:
- Reference repositories or sources:
- Analysis scope:
- Analysis cutoff:
```

## Use this skill when

Use this skill for requests such as:

- Explain the complete process of a complex coding-agent task.
- Reconstruct a session containing many tool calls.
- Audit whether the agent satisfied the original request.
- Analyze retries, failures, and recovery.
- Explain what happened before and after context compression.
- Determine whether compaction caused goal drift or repeated discovery.
- Analyze subagent delegation or parallel work.
- Map final claims to files, tool results, tests, and other evidence.
- Include corresponding source-code excerpts or diffs for material claims.
- Compare execution quality across two agent sessions.

## Do not use this skill when

Do not use it as the primary workflow when the request is only:

- explaining what one function or software module does;
- tracing a business workflow without analyzing an agent session;
- reviewing source code without a transcript or execution trace;
- reconstructing hidden chain of thought.

For feature or workflow behavior, use a feature/workflow analyzer instead.

## Supported analysis modes

Choose the narrowest mode that satisfies the request.

### Full session

Analyze the complete observable session from the original request to the final response.

### Selected range

Analyze only specified turns, events, or a defined cutoff. State excluded evidence.

### Compaction focus

Prioritize context epochs, compact summaries, information preservation, repeated work, and goal continuity.

### Tool-use focus

Prioritize tool chronology, purpose, failures, redundancy, state changes, and verification value.

### Comparative

Compare two sessions using the same evidence contract and rating dimensions. Do not compare raw call counts without accounting for scope and available tools.

## Required inputs

Accept any available combination of:

- original user request and later corrections;
- main session transcript or rollout trace;
- hook or lifecycle event logs;
- tool inputs and outputs;
- `PreCompact`, `PostCompact`, or compact-summary records;
- subagent transcripts;
- task or plan records;
- source files and generated artifacts;
- code excerpts, source locations, symbols, or line ranges;
- git diff, patch events, or version-control history;
- test, build, lint, type-check, or validation output;
- project instructions such as `CLAUDE.md`, `AGENTS.md`, SOPs, or execution contracts.

Not every source must exist. Missing evidence must become an explicit limitation, not an invented fact.

## Evidence labels

Use these labels throughout the report:

- **Observable fact**: directly recorded in the trace, transcript, source, tool output, patch, test result, or artifact.
- **Supported inference**: strongly suggested by the observable sequence but not directly stated.
- **Unknown**: insufficient evidence for a reliable conclusion.
- **Contradicted**: a claim conflicts with stronger available evidence.

Never claim access to hidden chain of thought. Analyze visible decisions and actions only.

## Core workflow

### Step 1: Fix the analysis boundary

Record:

- analyzed session identifier;
- start event or first included turn;
- end event or cutoff;
- whether later trace-analysis work is excluded to avoid recursive self-analysis;
- repositories and artifacts in scope;
- whether the task changed during the session.

Stop and request clarification only when no reliable session target can be identified.

### Step 2: Inventory evidence

Inspect available evidence before drafting conclusions.

Create two lists:

1. Evidence found.
2. Expected evidence not found.

For each missing source, state what cannot be established without it.

Do not treat a file path mentioned in a transcript as evidence that the file was actually opened or changed.

### Step 3: Reconstruct the original execution contract

Extract:

- original goal;
- requested deliverables;
- explicit constraints;
- prohibited actions;
- expected scope;
- success criteria;
- later corrections;
- agent-introduced assumptions;
- unresolved ambiguity.

Create requirement IDs and track their final status:

- satisfied;
- partially satisfied;
- not satisfied;
- unverifiable;
- removed by later instruction.

### Step 4: Build the chronological timeline

Reconstruct materially important events in order.

Recommended fields:

| Sequence | Context epoch | Phase | Event or tool | Purpose | Result | State change | Evidence |
|---:|---:|---|---|---|---|---|---|

Use phases such as:

- request interpretation;
- instruction loading;
- discovery;
- inspection;
- planning;
- implementation;
- verification;
- debugging;
- recovery;
- documentation;
- cleanup;
- completion.

Summarize repetitive low-value calls as a batch, but preserve counts and overall purpose.

### Step 5: Analyze important tool calls

For each important call, identify:

- context epoch;
- phase;
- tool and input summary;
- intended purpose;
- actual result;
- success, failure, denied, or partial status;
- files or state affected;
- evidence obtained;
- relationship to previous and next steps;
- whether the call was necessary, useful, redundant, or ineffective.

Do not judge efficiency from call count alone.

### Step 6: Reconstruct file and state impact

Distinguish:

- files inspected only;
- files created;
- files modified;
- files deleted;
- configuration or environment state changed;
- tests or reports generated;
- pre-existing unrelated changes.

Map each material change to a requirement and verification result.

### Step 6A: Capture corresponding code evidence

When source files, patches, or diffs are available, extract minimal code segments that directly support material claims in the report.

Use code evidence for claims about:

- implementation structure;
- branches, fallbacks, or cleanup paths;
- dependencies and side effects;
- code added or changed during the session;
- failure causes or recovery changes;
- verification coverage;
- context-continuity claims that depend on reloaded project code or instructions.

Do not include code merely because the analyzed agent opened a file.

Keep these evidence types separate:

1. **Inspected source**: code actually opened during the analyzed session.
2. **Changed code**: code added or modified during the analyzed session.
3. **Diff or patch**: recorded before/after change evidence.
4. **Post-session verification**: code opened later by the analyzer to verify a session claim.
5. **Generated artifact**: generated code or configuration relevant to the task.

For every excerpt, record:

- code-evidence ID;
- evidence type;
- repository or artifact;
- file path;
- symbol or section;
- line range when reliably available;
- revision, patch state, or analysis timestamp when available;
- related requirement or session event;
- claim supported;
- minimal relevant excerpt;
- concise interpretation;
- truth boundary.

Use this block:

````markdown
### CE-01 — <short evidence title>

- Evidence type: inspected source / changed code / diff / post-session verification / generated artifact
- Repository or artifact:
- File:
- Symbol or section:
- Lines:
- Revision or source state:
- Related requirement:
- Related session event:
- Supports:

```<language>
<minimal relevant code excerpt>
```

**Interpretation:** Explain what the excerpt establishes.

**Truth boundary:** Explain what the excerpt does not establish without runtime, test, or trace evidence.
````

Prefer a concise diff or before/after excerpt when the session changed code.

Do not:

- dump complete source files;
- invent omitted code or line numbers;
- silently rewrite source for readability;
- splice unrelated regions without disclosure;
- expose secrets, credentials, tokens, or sensitive values;
- treat documentation pseudocode as implementation evidence;
- claim that static code proves a branch executed in the analyzed session;
- imply that post-session verification code was opened by the analyzed agent.

Place a code excerpt immediately after the conclusion it supports when that improves readability. Assign it a code-evidence ID and include the same ID in the code-evidence index. Do not duplicate the full excerpt elsewhere; refer to its ID.

Read `references/code-evidence.md` for the detailed contract.

### Step 7: Analyze failures and recovery

For each material failure, record:

- failure stage;
- triggering action;
- observable error;
- immediate impact;
- confirmed or inferred root cause;
- recovery action;
- retry count;
- recovery outcome;
- new risk introduced;
- final verification.

Do not describe a user interruption as a tool failure. Do not describe a failed command as a product defect without evidence.

### Step 8: Analyze context compaction

If compaction occurred, split the session into context epochs:

```text
Epoch 1
-> PreCompact
-> compact summary
-> PostCompact
-> Epoch 2
```

For every compaction event, determine:

- trigger type and sequence position;
- work completed before compaction;
- work still pending;
- active requirements and constraints;
- facts preserved in the compact summary;
- important facts omitted;
- instructions reloaded afterward;
- first post-compaction actions;
- repeated discovery;
- new assumptions or goal drift;
- continuity result.

Allowed continuity results:

- continuous;
- continuous with minor repetition;
- partially degraded;
- significant context loss;
- goal drift;
- unverifiable.

If no compaction occurred, state that directly. Do not treat interruption, a new turn, caching, summarization in prose, or high cumulative token usage as compaction unless the evidence supports it.

Read `references/compaction-analysis.md` for detailed criteria.

### Step 9: Analyze subagents and parallel work

For each subagent or parallel branch, identify:

- assigned objective;
- supplied context;
- tools and files used;
- result returned;
- whether the main agent used the result;
- duplicated or conflicting work;
- independent verification;
- impact on main-context usage.

Do not merge subagent-private activity into the main session unless its result was returned or otherwise exposed.

If no subagents or parallel calls occurred, record zero rather than inventing a hierarchy.

### Step 10: Analyze verification quality

List every verification action:

- unit, integration, or end-to-end tests;
- build;
- lint;
- type check;
- static analysis;
- manual inspection;
- diff review;
- artifact validation.

For each verification, record scope, result, related change, and limitation.

Do not equate command success with requirement satisfaction. Confirm that the verification actually covers the changed behavior.

### Step 11: Build requirement-to-evidence traceability

Create a final matrix:

| Requirement | Agent action | Files or artifacts | Code evidence | Verification | Other evidence | Status |
|---|---|---|---|---|---|---|

Every final completion claim must map to observable evidence.

### Step 12: Assess execution quality

Use qualitative ratings only unless the user asks for scoring:

- strong;
- acceptable;
- weak;
- unverifiable.

Assess:

- correctness;
- traceability;
- efficiency;
- recovery quality;
- context continuity;
- verification quality.

Tie every rating to evidence from the analyzed session.

### Step 13: Produce the report

Use the template in `references/report-template.md`.

When code evidence is available, include a code-evidence index and minimal excerpts or diffs. Prefer inline placement near the supported conclusion, while keeping one canonical copy of each excerpt. When source evidence is unavailable, state that no corresponding code excerpt could be verified.

The report must clearly separate:

- analyzed platform;
- task domain;
- target repository;
- reference repositories;
- analyzer;
- analysis cutoff.

A domain-specific task may dominate the report content, but it must not be mistaken for a built-in assumption of this skill.

## Minimum output contract

Every complete report must include:

1. Analysis identity.
2. Executive summary.
3. Evidence inventory and limitations.
4. Original request and execution contract.
5. High-level phases.
6. Chronological timeline.
7. Tool-call analysis.
8. File and repository impact.
9. Corresponding code evidence for material implementation claims and changes, when source, patch, or diff evidence is available.
10. Failure and recovery analysis.
11. Context compaction analysis.
12. Subagent and parallel-work analysis.
13. Verification analysis.
14. Requirement-to-evidence matrix.
15. Execution quality assessment.
16. Final gaps and session-specific recommendations.

Sections with no events must remain present in concise form, for example: `Context compactions: 0`.

## Stop conditions

Stop and mark the analysis incomplete when:

- the session cannot be identified;
- the trace is truncated before the requested scope ends;
- the available material contains only a final answer with no execution evidence, while the user requests tool-level reconstruction;
- evidence sources conflict and cannot be reconciled;
- the requested claim requires hidden reasoning rather than observable evidence.

Do not stop merely because some optional evidence is absent. Continue with explicit limitations.

## Quality checks before finalizing

Confirm that:

- identity roles are not confused;
- the report does not assume NagaAgent, Claude Code, or any other platform without evidence;
- facts, inferences, unknowns, and contradictions are distinguishable;
- context compaction is not confused with caching or interruption;
- tool purposes are explained, not only counted;
- file changes are separated from files merely inspected;
- inspected source, changed code, diffs, and post-session verification are distinguished;
- material source-backed claims reference code-evidence IDs;
- every code excerpt identifies its file and source state;
- excerpts are minimal, verbatim, relevant, and free of sensitive values;
- static code evidence is not overstated as proof of runtime behavior;
- final claims map to verification evidence;
- recommendations address observed weaknesses rather than generic best practices;
- no hidden chain of thought is claimed;
- the report cutoff prevents recursive self-analysis where relevant.

## Reference files

Use these supporting files when needed:

- `references/evidence-contract.md`
- `references/code-evidence.md`
- `references/event-taxonomy.md`
- `references/compaction-analysis.md`
- `references/report-template.md`
