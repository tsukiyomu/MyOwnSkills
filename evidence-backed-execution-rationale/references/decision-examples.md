# Examples of Decision Rationale

These examples are illustrative, not repository evidence or a workflow to repeat.
Use only facts and verification results actually available in the current task.

## Choosing a new trace boundary

**Objective:** preserve one trace across an execution, including failure cleanup.

**Evidence -> Concern:** suppose the old loop hook is gone and the current runtime
owns completion and cleanup. Copying the old patch would miss the active lifecycle.

**Decision -> Action:** attach tracing to the lifecycle owner so trace completion
follows execution completion; adapt the integration rather than restoring an
obsolete hook solely to reuse the old patch. This is a planned change until applied.

**Verification:** exercise success, failure, and disabled instrumentation with a
controlled tracer. Until run, these are proposed checks. Passing them could establish
the local lifecycle contract, not delivery to a hosted tracing service.

**Engineering principle:** lifecycle ownership keeps resource creation and cleanup
with the component that knows when the operation ends.

**Recognition cue:** when several paths can end an operation and cleanup is split
among callers, look for the actual lifecycle owner before adding another hook.
Respect a mandated integration boundary; a convenient location alone is insufficient.

## Controlling a test dependency

**Objective:** verify stream termination independently of model behavior.

**Evidence -> Concern:** suppose the route formats events while a remote model drives
the loop. A model outage can fail the test without a streaming-contract defect.

**Decision -> Action:** keep the real route and supply controlled loop responses,
making termination assertions attributable to the route's behavior.

**Verification:** assert the required event sequence and terminal event. Report the
observed check result only if available. This boundary cannot establish real model,
tool, or hosted-service integration, nor satisfy acceptance that explicitly requires it.

**Engineering principle:** test boundary control isolates the contract being proved.

**Recognition cue:** when unrelated dependencies can explain a test failure but only
one local contract is under investigation, consider controlling those dependencies.
Use more authentic integration evidence when that dependency interaction is the claim.
