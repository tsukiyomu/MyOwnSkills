---
name: ci-cd-agent-result-reporter 
description: Use this skill when the user wants an agent to run or inspect CI/CD, collect execution evidence, analyze pass/fail results, and generate a clear result report or showcase document.
---

# CI/CD Agent Result Reporter Skill

## 1. Purpose

This skill guides an agent to inspect, run, collect, analyze, and document CI/CD execution results.

The goal is not only to say whether the pipeline passed or failed, but to produce a trustworthy engineering report that explains:

- What pipeline was executed
- Which commit, branch, environment, and commands were used
- Which stages passed, warned, failed, or were skipped
- What test, build, lint, security, deployment, or performance evidence was collected
- Why failures happened
- What should be fixed next
- Which results can be shown in a project portfolio, website, README, or technical report

The output must be evidence-based. Do not invent CI/CD results, test numbers, coverage values, logs, or deployment status.

------

## 2. When to Use

Use this skill when the user asks for any of the following:

- Run CI/CD using an agent
- Inspect GitHub Actions, GitLab CI, Jenkins, or local pipeline results
- Generate a CI/CD result report
- Explain test/build/deploy results
- Summarize failed pipeline logs
- Convert CI/CD logs into a readable result说明书
- Prepare CI/CD evidence for a personal website, portfolio, internship summary, or project documentation
- Generate quality gate reports for automated testing, agent testing, performance testing, or deployment verification

------

## 3. Core Principle

Always separate three things:

1. **Observed facts**
   Directly proven by logs, reports, CI files, test output, screenshots, or artifact files.
2. **Reasonable analysis**
   Inference based on observed facts, such as likely failure causes or risk points.
3. **Suggested actions**
   Fixes, optimizations, retry suggestions, or next engineering steps.

Never mix these together.

------

## 4. Required Inputs

Before producing the final report, collect as many of these inputs as available:

### Repository Information

- Repository name
- Branch name
- Commit hash
- Pull request ID, if any
- Trigger type: push, pull request, manual, scheduled, tag, release
- CI platform: GitHub Actions, GitLab CI, Jenkins, local script, Docker Compose, custom runner

### CI/CD Configuration Files

Check for:

- `.github/workflows/*.yml`
- `.gitlab-ci.yml`
- `Jenkinsfile`
- `Dockerfile`
- `docker-compose.yml`
- `package.json`
- `pom.xml`
- `build.gradle`
- `pytest.ini`
- `pyproject.toml`
- `requirements.txt`
- `Makefile`
- `scripts/`
- test configuration files
- deployment configuration files

### Execution Evidence

Collect evidence from:

- CI logs
- terminal output
- test reports
- JUnit XML
- coverage reports
- Allure reports
- Playwright/Cypress reports
- pytest output
- JMeter `.jtl` or HTML reports
- Docker build logs
- deployment logs
- artifact links
- screenshots, if provided

### Environment Information

Record:

- OS
- runtime version
- Java / Node / Python / Go version
- Docker version
- database or Redis dependency
- environment variables used, excluding secrets
- test profile, such as dev, test, staging, production
- whether the run was local or remote

Secrets must never be printed.

------

## 5. Execution Workflow

Follow this workflow strictly.

### Step 1: Identify the CI/CD Entry Point

Inspect the repository and determine how the pipeline is defined.

Examples:

- GitHub Actions workflow
- GitLab CI stages
- Jenkins pipeline
- local command sequence
- Makefile target
- package script
- Maven/Gradle lifecycle
- Docker Compose integration test flow

Output a short summary of the discovered pipeline.

### Step 2: Build the Pipeline Map

Map the pipeline into stages.

Common stages include:

- checkout
- dependency installation
- static analysis
- lint
- unit test
- integration test
- API test
- UI test
- performance test
- security scan
- build
- Docker image build
- deployment
- smoke test
- artifact upload
- notification

For each stage, identify:

- command
- input
- output
- success condition
- failure condition
- produced artifact

### Step 3: Run or Inspect the Pipeline

If execution is allowed, run the safest available command.

Prefer non-destructive commands first:

- test
- lint
- build
- dry-run deploy
- local smoke test

Do not perform destructive deployment, production release, database reset, force push, or secret modification unless explicitly instructed.

If execution is not possible, inspect existing CI logs or reports instead.

### Step 4: Collect Evidence

For each stage, collect:

- status: pass / warn / fail / skipped / blocked
- command or job name
- duration, if available
- key log excerpt
- report file path
- artifact path
- failure message, if any

Evidence must reference concrete files, commands, logs, or report outputs.

### Step 5: Normalize Result Status

Use the following status model:

- **PASS**: Stage completed successfully and met its quality gate.
- **WARN**: Stage completed, but there are risks such as flaky tests, low coverage, high latency, warnings, skipped tests, or non-blocking errors.
- **FAIL**: Stage failed and blocks merge, release, or deployment.
- **SKIPPED**: Stage was intentionally not executed.
- **BLOCKED**: Stage could not run due to missing environment, permission, dependency, token, secret, or external service.

### Step 6: Analyze Failures

For each failure, explain:

- Failed stage
- Direct error message
- Most likely cause
- Affected module
- Whether it is code issue, environment issue, dependency issue, config issue, test data issue, or flaky issue
- Suggested fix
- Whether rerun is meaningful

Do not overclaim root cause if evidence is insufficient.

### Step 7: Generate the Result Report

Generate a structured CI/CD result说明书.

The report must be readable by both engineers and non-engineering reviewers.

------

## 6. Output Format

Use this structure for the final report.

# CI/CD 执行结果说明书

## 1. 执行概览

Include:

- 项目名称
- 仓库/分支
- Commit
- 执行时间
- 触发方式
- 执行环境
- CI/CD 平台
- 总体结论

Example status:

- 总体结果：PASS
- 总体结果：WARN
- 总体结果：FAIL
- 总体结果：BLOCKED

## 2. Pipeline 阶段说明

Use a table:

| 阶段 | 命令/任务 | 状态 | 耗时 | 产物 | 说明 |
| ---- | --------- | ---- | ---- | ---- | ---- |
|      |           |      |      |      |      |

Each row should explain one pipeline stage.

## 3. 质量门禁结果

Explain whether the pipeline meets the required gate.

Common gates:

- 代码能否正常构建
- 单元测试是否通过
- 接口测试是否通过
- UI 自动化是否通过
- 性能指标是否达标
- 安全扫描是否存在阻塞问题
- Docker 镜像是否构建成功
- 部署后服务是否可访问
- Smoke Test 是否通过

Use this table:

| 门禁项 | 期望标准 | 实际结果 | 结论 |
| ------ | -------- | -------- | ---- |
|        |          |          |      |

## 4. 测试结果摘要

If test reports exist, summarize:

- total tests
- passed
- failed
- skipped
- error count
- flaky tests, if detected
- coverage, if available

For API/UI/Agent tests, include business meaning.

Example:

- 登录链路测试通过，说明用户身份认证主流程可用。
- 职位推荐接口测试通过，说明核心推荐入口具备基本可用性。
- SSE 流式返回测试通过，说明 AI 对话链路可以持续返回内容。
- 支付链路使用 mock/sandbox 验证，不能等同于生产支付成功。

## 5. 构建与部署结果

Explain:

- build result
- package result
- image result
- deployment result
- service health check
- rollback or release status

If deployment was not executed, clearly say so.

## 6. 失败与风险分析

For each issue:

### 问题 1：问题标题

- 所属阶段：
- 直接证据：
- 可能原因：
- 影响范围：
- 修复建议：
- 优先级：

Do not hide failures. A good report should make problems clear.

## 7. 可展示成果总结

This section is for personal website, README, portfolio, or internship summary.

Explain the engineering value in a polished but truthful way.

Possible angles:

- 建立了自动化测试回归流程
- 接入了 CI/CD 质量门禁
- 将接口测试、UI 测试、性能测试或 Agent workflow 测试纳入流水线
- 通过报告沉淀测试结果，提升问题定位效率
- 支持每次提交后自动生成质量反馈
- 为后续持续交付提供基础

Do not exaggerate. If only local CI was run, do not say production CI/CD is complete.

## 8. 后续改进建议

List concrete next steps.

Examples:

- 补充失败用例重跑机制
- 增加测试报告 artifact 上传
- 接入 Allure 或 HTML Report
- 增加覆盖率门禁
- 增加 Docker 镜像扫描
- 增加部署后 smoke test
- 增加性能基准对比
- 增加 Agent workflow golden cases
- 增加通知机制，如 GitHub Check、Slack、企业微信或邮件

## 9. 附录

Include:

- executed commands
- important log excerpts
- report file paths
- artifact paths
- CI configuration file paths
- environment summary
- known limitations

------

## 7. Agent Behavior Rules

The agent must follow these rules.

### Evidence Rules

- Every important conclusion must be supported by logs, files, reports, or command output.
- If evidence is missing, say “未发现直接证据”.
- If a result is inferred, mark it as “推测”.
- Do not fabricate successful deployment, passed tests, coverage rate, or performance numbers.

### Safety Rules

- Never print secrets.
- Never expose tokens, private keys, passwords, cookies, or production credentials.
- Never run destructive commands unless the user explicitly approves.
- Never force push, delete remote branches, reset production databases, or deploy to production without explicit instruction.
- Redact sensitive environment variables.

### Reporting Rules

- Prefer clear engineering language.
- Avoid vague words such as “应该没问题”.
- Explain failures directly.
- Separate “已完成”, “未执行”, “失败”, and “受阻”.
- Make the report useful for both debugging and portfolio展示.

------

## 8. Recommended Report Tone

The final report should be:

- factual
- structured
- engineering-oriented
- readable
- suitable for README, personal website, internship report, or project documentation

Avoid overly promotional language unless the user asks for a resume-style version.

------

## 9. Example Final Summary

Example:

本次 CI/CD 流水线完成了依赖安装、后端构建、接口自动化测试和 Docker 镜像构建四个阶段。其中构建与接口测试通过，Docker 镜像构建成功，但部署阶段未执行，因此本次结果可以证明项目具备基础自动化回归能力和可构建性，但不能证明生产环境发布成功。

从质量门禁角度看，当前流水线已经覆盖核心接口回归，但仍缺少覆盖率统计、UI 自动化报告归档、部署后 smoke test 和性能基准对比。后续建议将测试报告作为 artifact 上传，并增加失败用例定位说明，以便每次提交后形成稳定的质量反馈闭环。

------

## 10. Suggested Artifact Names

Generated files may use these names:

- `ci_cd_result_report.md`
- `ci_cd_result_report.html`
- `ci_cd_quality_gate_summary.json`
- `ci_cd_failure_analysis.md`
- `ci_cd_portfolio_summary.md`
- `agent_ci_cd_runbook.md`

------

## 11. JSON Summary Schema

When possible, also generate a machine-readable summary.

```json
{
  "project": "",
  "branch": "",
  "commit": "",
  "ci_platform": "",
  "trigger": "",
  "overall_status": "PASS | WARN | FAIL | BLOCKED",
  "stages": [
    {
      "name": "",
      "command": "",
      "status": "",
      "duration_seconds": null,
      "artifact": "",
      "summary": ""
    }
  ],
  "quality_gates": [
    {
      "name": "",
      "expected": "",
      "actual": "",
      "status": ""
    }
  ],
  "test_summary": {
    "total": null,
    "passed": null,
    "failed": null,
    "skipped": null,
    "coverage": null
  },
  "failures": [
    {
      "stage": "",
      "evidence": "",
      "possible_cause": "",
      "suggested_fix": "",
      "priority": ""
    }
  ],
  "risks": [],
  "next_steps": []
}
```

------

## 12. Quality Checklist

Before finishing, verify:

- Pipeline entry point was identified
- Commands or CI jobs were listed
- Each stage has a clear status
- Failed stages include direct evidence
- Missing evidence is clearly marked
- Secrets are redacted
- Deployment status is not exaggerated
- The final report has both engineering analysis and display-ready summary
- JSON summary is generated if useful