---
name: evidence-backed-execution-rationale
description: Explain material engineering decisions using repository evidence, the concern it reveals, the chosen implementation, its effect, and verification limits. Use during implementation or when explaining an existing change, especially for integration points, state ownership, dependency control, and test boundaries. Adds engineering principles and recognition cues in learning mode; does not prescribe execution steps or manage plan progress and journals.
---

# Evidence-Backed Execution Rationale

Make engineering judgment visible through concise, inspectable explanations. The agent chooses how to carry out the authorized work; this skill constrains how it explains meaningful decisions.

## Core contract

- Do not prescribe a universal execution workflow.
- Follow the Work Unit objective, concrete implementation requirements, acceptance criteria, and project, language, and team rules.
- Adapt implementation choices to current repository evidence without replanning the objective.
- For each material decision, explain: objective -> evidence -> engineering concern -> decision -> action -> verification, including the proof boundary.
- Explain meaningful decision points, not routine tool usage.
- In learning mode, add an engineering principle and a recognition cue.
- If repository reality contradicts a Plan implementation assumption, preserve the objective, adapt the implementation within the agreed constraints, and explain why.

## Which decisions deserve explanation

A decision is material when it changes behavior, ownership, dependency authenticity, correctness, operational risk, or what the evidence can establish. Typical cases include:

- Choosing an integration point or replacing a proposed approach that no longer fits the code.
- Assigning state or lifecycle ownership to a component.
- Introducing or rejecting a fake, spy, cache, retry, or transaction to address a concrete concern.
- Expanding or narrowing a test boundary.
- Judging whether current evidence is sufficient for a particular acceptance claim.

Opening files, searching, formatting, ordinary renaming, and individual test commands do not each need a decision record. If a seemingly routine edit changes a public contract, explain that contract decision. Do not invent alternatives or risks to make a mechanical task appear educational.

## Evidence -> Concern -> Decision -> Action -> Verification

Anchor the explanation in the current Work Unit objective and relevant constraints. Make these relationships clear:

| Element | What the reader should understand |
|---|---|
| Evidence | What relevant repository fact was observed, and where: file/symbol, configuration, diff, test assertion, or result. Distinguish observations, reported history, assumptions, and inferences. |
| Concern | Why that fact matters to the objective: the invariant, ambiguity, failure mode, or trade-off it exposes. |
| Decision | Why this implementation addresses that concern within the requirements. Explain a rejected approach only when it was a real, relevant alternative. |
| Action | What the choice changes or will change in behavior, ownership, code, or the test boundary. Distinguish planned action from an applied change. |
| Verification | Which assertion or observation would test the decision; what was actually checked, if anything; and what the result establishes and leaves unproven. |

This chain is an explanation structure, not a chronological execution procedure. There is no mandatory inventory, state model, option table, implementation brief, or fixed testing sequence. Use a short paragraph or a compact record, whichever makes the decision understandable. Combine related decisions when their evidence and concern are the same.

Explain decisions near the relevant work or in the explanation the user requested. If later evidence changes the choice, explain the new fact and its effect. Do not repeat the whole analysis after every command or reproduce source files. Link to concrete evidence and keep reusable public rationale separate from private reasoning transcripts.

Planned verification is not a passed check. Missing or inconclusive evidence may justify a narrower claim, but does not remove required acceptance. Historical results remain scoped to their revision and environment; controlled dependencies do not prove real-service behavior. Explain why the available evidence is sufficient or insufficient for the specific claim.

If the user only asks why an existing change was made, inspect and explain the available evidence. Do not invent the author's motives or imply that new implementation or test execution is authorized merely to fill the explanation.

## Learning mode

Use learning mode when the user asks to learn while working, asks for engineering principles, or the task already has an established learning objective. Otherwise keep the decision rationale without the extra learning fields.

For each material decision in learning mode, also include:

- **Engineering principle:** the general engineering idea the decision illustrates, explained through its effect here.
- **Recognition cue:** the concrete pattern to notice in a future task that should prompt considering that principle. Include a relevant limit so the cue is not mistaken for an unconditional recipe.

For example, when many unrelated dependencies can cause failure but the acceptance concerns one local contract, consider controlling those dependencies. That is a cue for test boundary control, not a claim that full integration testing is unnecessary.

Learning mode adds explanation, not quizzes, mastery labels, or automatic pauses. Wait for teach-back only when the user asks for that interaction. Read [decision-examples.md](references/decision-examples.md) only if a concrete example would clarify the desired explanation.

## Plan constraints and responsibility boundaries

Treat explicit implementation requirements and project rules as binding. A stale hook suggested in a Plan is different from a mandated integration boundary. Adapt a disproved assumption within the contract; if the needed change would violate an explicit requirement or alter acceptance, make that conflict clear and obtain the unresolved decision before dependent work. Do not silently relabel a requirement as an assumption.

[Plan Progress Checkpoint](../plan-progress-checkpoint/SKILL.md) owns unit selection, status, and progress. [Work Unit Journal](../evidence-backed-work-unit-journal/SKILL.md) owns the final outcome, evidence, and proof limits. This skill owns the explanation of why an implementation was chosen. Those links describe neighboring responsibilities, not mandatory calls or dependencies.

Applying this skill does not select the next unit, set status, update a ledger, write a journal, or create a separate rationale document. Follow the user's requested communication or artifact location; concise explanations in the conversation are sufficient by default. When the broader task separately includes progress or reporting, avoid duplicating the rationale there.
