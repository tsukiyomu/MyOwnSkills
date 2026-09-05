# Coding Agent Session Trace Analysis

## Analysis Identity

- Analyzer:
- Analyzed platform:
- Analyzed session ID or trace:
- Original task domain:
- Target repository or artifact:
- Reference repositories or sources:
- Analysis scope:
- Analysis cutoff:
- Analysis date:

## Evidence Labels

- **Observable fact**:
- **Supported inference**:
- **Unknown**:
- **Contradicted**:

## 1. Executive Summary

Summarize:

- original request;
- final outcome;
- completion status;
- main execution path;
- material tool calls;
- files changed;
- code-evidence count;
- failures;
- compaction count;
- subagent count;
- principal strengths;
- principal gaps.

## 2. Available Evidence and Limitations

### Evidence found

### Expected evidence not found

### Resulting limitations

## 3. Original Request and Execution Contract

| ID | Requirement | Source | Explicit or inferred | Final status |
|---|---|---|---|---|

## 4. High-Level Execution Phases

### Phase 1

- Entry condition:
- Actions:
- Evidence:
- Exit condition:

## 5. Chronological Session Timeline

| Sequence | Context epoch | Phase | Event/tool | Purpose | Result | State change | Evidence |
|---:|---:|---|---|---|---|---|---|

## 6. Tool-Call Analysis

### Counting method

| Tool | Call count | Main purpose | Failures | Redundant calls | Important result |
|---|---:|---|---:|---:|---|

### Important calls or call groups

## 7. File and Repository Impact

| File or artifact | Action | Reason | Requirement | Verification |
|---|---|---|---|---|

## 8. Corresponding Code Evidence

Include this section when source, patch, diff, or generated-code evidence is available. Otherwise state that no corresponding code excerpt could be verified.

### 8.1 Code Evidence Index

| Evidence ID | Related claim or requirement | Repository/file | Symbol or lines | Evidence type |
|---|---|---|---|---|

### 8.2 Existing Source Evidence

### CE-01 — <title>

- Evidence type:
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

**Interpretation:**

**Truth boundary:**

### 8.3 Changed Code or Diff Evidence

### CE-02 — <title>

- Evidence type: changed code / diff / patch
- Repository or artifact:
- File:
- Related requirement:
- Related session event:
- Verification:

```diff
<minimal patch>
```

**Change meaning:**

**Verification status:**

### 8.4 Code Evidence Not Available

List material implementation claims for which no source, patch, diff, or reliable excerpt was available.

## 9. Failure and Recovery Analysis

### Failure F1

- Failure stage:
- Trigger:
- Observable error:
- Immediate impact:
- Root cause: confirmed / inferred / unknown
- Recovery:
- Retries:
- Recovery result:
- New risk:
- Final verification:
- Related code evidence:

## 10. Context Compaction Analysis

Use the compaction event block from `compaction-analysis.md`, or state that no confirmed compaction occurred.

## 11. Subagent and Parallel-Work Analysis

- Subagent count:
- Parallel batch count:
- Delegation hierarchy:
- Result integration:
- Duplicated or conflicting work:

## 12. Verification Analysis

| Verification | Scope | Result | Related change or claim | Code evidence | Limitations |
|---|---|---|---|---|---|

## 13. Requirement-to-Evidence Matrix

| Requirement | Agent action | Files/artifacts | Code evidence | Verification | Other evidence | Status |
|---|---|---|---|---|---|---|

## 14. Execution Quality Assessment

| Dimension | Rating | Basis |
|---|---|---|
| Correctness |  |  |
| Traceability |  |  |
| Efficiency |  |  |
| Recovery quality |  |  |
| Context continuity |  |  |
| Verification quality |  |  |

## 15. Final Gaps and Unknowns

## 16. Improvement Recommendations

Only include recommendations tied to observed weaknesses in this session.
