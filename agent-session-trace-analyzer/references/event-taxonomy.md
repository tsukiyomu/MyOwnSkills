# Event and Tool Taxonomy

## 1. Execution phases

| Phase | Typical evidence |
|---|---|
| Request interpretation | User prompt, clarification, scope statement |
| Instruction loading | Project instructions, system files, SOPs |
| Discovery | Search, file listing, symbol lookup |
| Inspection | Reading source, config, docs, traces |
| Dependency tracing | Call hierarchy, references, data flow |
| Planning | Plan creation, task decomposition, checklist |
| Implementation | File edits, commands changing state |
| Verification | Tests, build, lint, diff review |
| Debugging | Error inspection and hypothesis testing |
| Recovery | Corrective edit, retry, fallback |
| Documentation | Report or doc modification |
| Cleanup | Temporary file removal, state restoration |
| Completion | Final answer, task close, stop event |

## 2. Tool-purpose classes

- discovery;
- inspection;
- dependency tracing;
- planning;
- implementation;
- verification;
- debugging;
- recovery;
- documentation;
- cleanup.

One tool may serve different purposes in different calls.

## 3. Tool-result states

- success;
- partial success;
- failure;
- permission denied;
- cancelled;
- timed out;
- no useful result;
- unknown.

## 4. Value classification

### Necessary

Directly required to obtain evidence, change state, or verify the task.

### Useful

Added relevant confidence or scope, even if not strictly required.

### Redundant

Repeated previously available evidence without a justified reason or new result.

### Ineffective

Did not advance the task because of wrong scope, invalid assumptions, or unusable output.

Do not label repeated calls redundant when caused by:

- new user scope;
- a material error;
- changed repository state;
- context compaction;
- independent verification;
- different subagent assignments.

## 5. Material event rule

Include an event in the detailed timeline when it changed at least one of:

- understanding;
- scope;
- plan;
- file or environment state;
- test or verification state;
- context epoch;
- task completion status.

Summarize repetitive events that do not materially change state.

## 6. Failure classes

- misunderstanding;
- missing evidence;
- wrong repository or file scope;
- command failure;
- build failure;
- test failure;
- dependency failure;
- permission denial;
- tool failure;
- environment failure;
- data issue;
- context loss;
- invalid assumption;
- incomplete implementation;
- flaky external dependency;
- user interruption.

A user interruption is an execution event, not automatically an agent failure.
