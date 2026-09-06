# Evidence And Review

## Judge The Accepted Unit

`DONE` means its requested output exists, its acceptance is supported by current
evidence, and no material gap remains inside its boundary. Do not promote a whole
unit to `DONE` because the first internal subtask passed.

Match proof to the claim:

| Unit acceptance | Appropriate evidence | Incomplete proof |
|---|---|---|
| Document responsibilities and working links | Inspect the content and resolve relevant links; inspect rendered output if layout matters | File existence alone |
| Add a deterministic runtime lifecycle | Execute focused behavioral checks against the changed runtime boundary | Merely importing the module |
| Integrate with a hosted service | The required authorized integration check in the specified environment | Stub checks presented as hosted proof |
| Create a draft for review | Draft plus checks required for that deliverable | Claiming the downstream approval already happened |

A draft-only unit can be `DONE` when its acceptance is to produce the draft. If the
unit requires approval itself, the pending judgment means `REVIEW_NEEDED`.

## REVIEW_NEEDED And BLOCKED

Use `REVIEW_NEEDED` for remaining required proof or material judgment: unexecuted
acceptance tests, unverified integration, missing mandated screenshots, or a scope
assumption that still changes the meaning of success. State the exact gap and
whether other checks passed. Do not infer review is needed merely because code
tests do not apply, a routine choice was made, or the result is called a draft.

Use `BLOCKED` when a necessary prerequisite is unavailable and meaningful progress
within the selected unit cannot continue. Record what was checked and what input
or external action will unblock it. An unfamiliar project structure calls for
inspection; it is not itself a blocker.

## Recover Before Closing The Run

Suppose a required pytest command fails because a marker was not registered. Check
the cause and the selected unit's boundary. If repairing the configuration is part
of making the authorized checks run, fix it and rerun the affected check in the
same logical run. Do not convert a routine repair into an unrequested next-task
permission gate. If the repair would cross a material explicit boundary, preserve
that boundary and report the unresolved acceptance accurately.

Evidence reports should distinguish the final verification result from recovered
failures when the latter explain a remaining limitation. Keep raw logs as linked
artifacts only when useful; the plan needs a short outcome and evidence pointer.

## Guardrails

- Preserve the user-authorized unit or batch and the plan's dependency order.
- Keep stubs, real services, baselines, and environments within the actual plan's
  stated boundary; a historical example is not a new constraint on another plan.
- Never claim unexecuted checks passed or transfer old-revision results to changed
  code without checking that the evidence still applies.
- Keep unresolved acceptance visible instead of rewriting it to fit the result.
