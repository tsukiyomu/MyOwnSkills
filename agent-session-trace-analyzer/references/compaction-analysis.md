# Context Compaction Analysis

## 1. Compaction evidence

Treat compaction as confirmed only when supported by platform-specific evidence such as:

- `PreCompact` or `PostCompact` events;
- a recorded compact summary;
- a transcript marker identifying compaction;
- an explicit platform event with the same meaning.

Do not infer compaction only from:

- cumulative token counts;
- cache statistics;
- a user interruption;
- a new conversation turn;
- the agent summarizing work in normal prose;
- reopening files.

## 2. Context epochs

Define one epoch as the observable working context between two compaction boundaries.

```text
Epoch 1
-> compaction event 1
-> Epoch 2
-> compaction event 2
-> Epoch 3
```

Record each event's sequence position and available timestamp.

## 3. Pre-compaction snapshot

Capture:

- active user goal;
- explicit constraints;
- completed work;
- pending work;
- files inspected;
- files changed;
- known failures;
- active plan or tasks;
- completion criteria;
- unresolved ambiguity.

## 4. Compact-summary preservation check

Compare the summary against the pre-compaction snapshot.

Mark each important item:

- preserved accurately;
- preserved partially;
- omitted;
- distorted;
- cannot determine.

Prioritize user constraints, pending tasks, changed files, failures, and completion criteria.

## 5. Post-compaction continuity check

Inspect the first meaningful actions after compaction:

- Were project instructions reloaded?
- Did the agent resume the correct pending step?
- Did it repeat discovery that had already been completed?
- Did it forget a user correction?
- Did it re-edit already completed work?
- Did it introduce a new unsupported assumption?
- Did it still verify against the original success criteria?

## 6. Continuity results

### Continuous

Goal, constraints, pending work, and evidence remain intact with no material loss.

### Continuous with minor repetition

The task remains correct, but some low-cost discovery or file reading is repeated.

### Partially degraded

Some useful detail is lost, causing avoidable repetition, weaker traceability, or a small omission.

### Significant context loss

Important requirements, changes, failures, or pending tasks are forgotten or reconstructed incorrectly.

### Goal drift

The post-compaction work pursues a materially different target or violates preserved constraints.

### Unverifiable

Compaction is known to have occurred, but the pre/post evidence is insufficient to assess continuity.

## 7. Compaction report block

```markdown
### Compaction Event <N>

- Trigger type:
- Sequence position:
- Execution phase:
- Work completed before compaction:
- Work pending before compaction:
- Important facts and constraints:
- Preserved in compact summary:
- Omitted or distorted:
- Instructions reloaded afterward:
- First post-compaction actions:
- Repeated discovery:
- New assumptions or drift:
- Continuity result:
- Evidence limitations:
```

## 8. No-compaction report

When no event occurred, use:

```markdown
## Context Compaction Analysis

No confirmed compaction event occurred in the analyzed scope.

| Item | Result |
|---|---|
| Context epochs | 1 |
| Confirmed compaction events | 0 |
| Compact summaries | 0 |
| Continuity result | Continuous within the observable scope |
```
