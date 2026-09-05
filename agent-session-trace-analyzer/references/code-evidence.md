# Corresponding Code Evidence

## 1. Purpose

Use code excerpts to connect a session-analysis conclusion to the implementation, change, or artifact that supports it.

The objective is not to reproduce the codebase. The objective is to provide the smallest useful segment that lets a reader verify a material claim.

## 2. Inclusion rule

Include an excerpt only when it supports at least one of:

- a user requirement;
- an execution-phase conclusion;
- an important tool-call result;
- a file change;
- a failure or recovery explanation;
- a verification claim;
- a context-continuity conclusion.

Do not include code merely because a file was opened.

## 3. Evidence identity

Use stable IDs:

- `CE-01`, `CE-02`, ... for code evidence;
- reference the same ID from the timeline, requirement matrix, failure analysis, or verification section.

Keep these categories explicit:

- inspected by the analyzed agent;
- changed by the analyzed agent;
- diff or patch recorded during the session;
- inspected afterward by the analyzer;
- generated artifact.

## 4. Standard block

````markdown
### CE-01 — <short evidence title>

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

**Interpretation:** What the excerpt establishes.

**Truth boundary:** What still requires runtime, test, trace, or other evidence.
````

## 5. Diffs and changed code

For a material change, prefer:

```diff
- old behavior
+ new behavior
```

When a diff is unavailable, provide a concise final-state excerpt and label it accurately. Do not describe final-state source as a recorded patch.

## 6. Placement

Place the canonical excerpt next to the conclusion it supports when that helps comprehension. Add the item to the code-evidence index.

Do not duplicate the full excerpt in multiple sections. Refer to `CE-xx` after its first appearance.

## 7. Minimality and fidelity

- Preserve source exactly.
- Do not invent line numbers.
- Do not silently reformat or rename identifiers.
- Mark omissions explicitly.
- Include enough surrounding context to avoid misleading interpretation.
- Redact sensitive values with `<redacted>` or an equivalent explicit marker.
- Avoid complete-file dumps.

## 8. Static-versus-runtime boundary

Static source can prove implementation structure. It cannot by itself prove execution, correctness, latency, state cleanup, external success, or test coverage.

Use runtime traces, logs, test output, and tool results for those claims.
