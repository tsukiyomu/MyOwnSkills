# Golden Cases v1

Read this file when the selected plan is explicitly about Golden Cases v1.

## Task Order

Treat the implementation order in the plan as authoritative. If the plan does not provide a clearer order, use this default sequence:

1. Create schema dataclass and schema error classes.
2. Implement file discovery and loader.
3. Add four minimal case files.
4. Implement runner with stub LLM and stub tool results.
5. Implement assertion checker.
6. Add pytest parametrized entry file.
7. Register the `golden_case` marker.
8. Run local pytest command and fix failures.

For the first run, usually select:

```text
Step 1: Create schema dataclass and schema error classes.
```

unless that task is already completed.

## Out of Scope

Do not implement these during v1 unless the user explicitly changes scope:

- Golden Case baseline file
- Quality Gate integration
- Allure integration
- Langfuse integration
- LangSmith integration
- `real_llm` profile
- `staging` profile
- Memory governance cases
- Context compression cases
- LLM-as-a-Judge
- Semantic scoring
- Dashboard
- CI workflow

## Execution Constraints

Keep v1 deterministic. Use stub LLM behavior and stub tool results when the plan calls for them.

Do not call real LLMs, real MCP services, real OpenClaw services, external network services, or staging systems when the selected task belongs to the stub profile.

## Verification Examples

Use the command from the project plan when one is provided. If the plan does not specify one, likely local checks include:

```bash
uv run python -m pytest tests/golden_cases -m golden_case -q
python -m pytest tests/golden_cases -m golden_case -q
```

If tests are not run, mark implementation work REVIEW_NEEDED unless the selected task explicitly does not require execution.
