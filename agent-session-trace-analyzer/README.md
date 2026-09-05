# agent-session-trace-analyzer

A platform-neutral agent skill for reconstructing and auditing one observable coding-agent session.

It separates:

- the analyzer;
- the analyzed platform;
- the task domain;
- the target repository or artifact;
- reference repositories or sources.

It can also include minimal, traceable source-code excerpts or diffs for material implementation claims and changes. Each excerpt is linked to a requirement, session event, interpretation, and truth boundary.

This prevents:

- a session about NagaAgent that inspects Claude Code from being mislabeled as “Claude Code analyzes NagaAgent”;
- code opened after the session from being attributed to the analyzed agent;
- static source from being overstated as proof of runtime execution.

Install by placing this directory in the skill location used by your agent runtime. The exact location depends on the platform.

Primary file: `SKILL.md`
