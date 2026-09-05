# Evidence Contract

## 1. Identity model

Always distinguish:

| Field | Meaning |
|---|---|
| Analyzer | Agent producing the current report |
| Analyzed platform | Agent or product that created the session |
| Session | Exact trace, transcript, or session ID |
| Task domain | Subject of the original request |
| Target repository/artifact | Object expected to be inspected or changed |
| Reference source | Material used for comparison only |
| Analysis scope | Included turns or events |
| Cutoff | Final included event |

Example:

```text
Analyzer: agent-session-trace-analyzer
Analyzed platform: Codex
Task domain: NagaAgent prompt architecture
Reference repository: claude-code-main
Target artifact: NagaAgent report
```

This does not mean Claude Code analyzed NagaAgent.

## 2. Evidence hierarchy

Prefer stronger evidence when sources conflict:

1. Direct tool output, patch event, test result, or event record.
2. Source file content actually opened during or after the session.
3. Version-control diff or tracked artifact state.
4. Session transcript statement.
5. Architecture or project documentation.
6. Supported inference from sequence and surrounding evidence.
7. Unverified claim in a final answer.

The hierarchy is contextual. A direct runtime trace is stronger for runtime behavior; source is stronger for implementation structure.

## 3. Evidence labels

### Observable fact

Directly supported by a cited event, tool result, source location, artifact, or validation output.

### Supported inference

A reasonable explanation of the observable sequence. State that it is inferred.

### Unknown

Evidence is absent, incomplete, or ambiguous.

### Contradicted

A claim conflicts with stronger evidence. Identify both the claim and the conflicting source.

## 4. Missing evidence

For each missing source, state the resulting limitation.

Examples:

| Missing evidence | Limitation |
|---|---|
| Raw provider payload | Cannot prove exact model-visible prompt |
| Pre/PostCompact events | Cannot establish exact compaction boundary |
| Git metadata | Cannot establish source revision or tracked diff |
| Test output | Cannot confirm behavioral correctness |
| Subagent transcript | Cannot reconstruct delegated activity |

## 5. Attribution rules

- A path mentioned is not necessarily a file read.
- A file read is not necessarily a file changed.
- A patch command is not sufficient unless its result is known.
- A successful command is not sufficient to prove the user requirement.
- A final-answer claim is not proof of implementation.
- Cumulative tokens are not the size of one request.
- Cache hits are not context compaction.
- A new turn or interruption is not automatically a new context epoch.
- Subagent work belongs to the subagent until returned to the main session.

## 6. Code evidence contract

### 6.1 Evidence types

| Type | Meaning |
|---|---|
| Inspected source | Code actually opened during the analyzed session |
| Changed code | Code added or modified during the analyzed session |
| Diff or patch | Recorded before/after change evidence |
| Post-session verification | Code opened later by the analyzer to verify a session claim |
| Generated artifact | Generated code or configuration relevant to the task |

Do not merge these categories. Post-session verification may support a claim, but it is not evidence that the analyzed agent saw or used that code.

### 6.2 Required metadata

Every code excerpt should include, when available:

- code-evidence ID;
- repository or artifact;
- file path;
- symbol or section;
- line range;
- revision, patch state, or analysis timestamp;
- evidence type;
- related requirement or event;
- supported claim.

### 6.3 Excerpt rules

- Quote source verbatim.
- Include only enough surrounding context to understand the branch, call, or change.
- Use an explicit omission marker such as `...` when removing irrelevant regions.
- Do not splice unrelated regions without disclosure.
- Prefer symbols and line ranges over file paths alone.
- Prefer diffs for session changes.
- Redact secrets with an explicit marker without changing surrounding meaning.
- Do not use third-party or generated code unless directly relevant.
- Distinguish comments, declarations, and executable behavior.

### 6.4 Evidence strength

A code excerpt can establish that:

- an implementation structure exists;
- a branch, fallback, or cleanup path exists;
- a dependency is called;
- a configuration value is declared;
- a change was made.

A code excerpt alone cannot establish that:

- the path executed in the analyzed session;
- runtime behavior was correct;
- an external dependency succeeded;
- a test covered the displayed path;
- the analyzed agent understood the excerpt.

Those conclusions require trace, runtime, test, or transcript evidence.

### 6.5 Claim linkage

Each material source-backed claim should reference one or more code-evidence IDs. Each code-evidence item should identify the claim, requirement, or session event it supports.

When no source excerpt can be verified, state that explicitly rather than constructing illustrative code.

## 7. Hidden reasoning boundary

Allowed:

- observable actions;
- visible explanations;
- tool selection and sequence;
- supported purpose inference;
- state changes and validation.

Not allowed:

- reconstructing private chain of thought;
- asserting unrecorded motives;
- presenting a plausible internal plan as fact.
