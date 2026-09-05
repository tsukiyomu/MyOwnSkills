# agent-assisted-testing README

## 简介

`agent-assisted-testing` 是 Agent-assisted Software Testing SOP v1.2 的可执行
Skill，用于让 AI Agent 在人工控制下辅助完成测试设计、测试实现、执行取证、
失败分析、回归建设和质量门禁审计。

它的核心原则是：

> 使用真实项目证据作为输入，由 Agent 负责扩展、分析和起草，由人工负责评审与
> 决策，由测试框架或 CI 负责执行，只声明证据能够证明的结论。

本文档是供人阅读的步骤概览。实际执行规则以 `SKILL.md` 和 `references/`
中的规范为准。

## 整体流程

```text
选择运行模式
→ 检查项目 Profile 和执行 Baseline
→ 登记测试任务
→ 收集证据
→ 分析风险
→ 设计测试场景
→ 选择自动化用例
→ 编写测试
→ 执行并保存证据
→ 分析失败
→ 固化回归和门禁依据
→ 报告与归档
```

## 运行模式

Skill 会根据请求选择满足目标的最小模式：

| 模式 | 用途 |
|---|---|
| `bootstrap` | 创建或审计 Project Profile 和执行 Baseline |
| `design` | 确定范围、收集证据、分析风险和设计场景 |
| `implement` | 根据已评审行为编写或修改确定性测试 |
| `execute` | 运行测试并保存准确的执行证据 |
| `triage` | 分析失败、复现问题并提出归因假设 |
| `govern` | 审计覆盖、追溯关系、CI 接入和门禁资格 |
| `end-to-end` | 执行完整的 Step 1–10 流程 |

小任务不需要机械生成全部文档，可以复用现有 issue、PR 或测试报告，只要保留
必要的证据、状态和引用。

## 执行前：项目上下文与 Baseline

在正式实现或执行测试前，Skill 会确认并冻结：

- `project_id`
- `project_profile_version`
- `environment_baseline_id`（ENV，测试环境）
- `account_baseline_id`（ACT，账号和权限）
- `data_baseline_id`（DAT，测试数据）
- `dependency_baseline_id`（DEP，外部依赖）
- `agent_permission_baseline_id`（AGP，Agent、工具和模型权限）
- `source_revision`（代码、构建或发布版本）

这些引用必须指向明确、不可变的 revision，不能使用会漂移的 `latest`。

如果 Profile 或关键 Baseline 缺失、过期、无效或相互冲突，Agent 可以起草候选
内容，但不能自行批准，也不能在存在安全、数据、权限或证明风险时继续执行。

## Step 1：登记任务和范围

确认：

- 测什么以及不测什么；
- 目标系统、workflow 和代码 revision；
- Human Owner、Reviewer 和必要的 Approver；
- Agent 可以读取、修改或执行到什么程度；
- 预期交付物。

每个有边界的测试活动使用一个根 Task ID：

```text
AST-YYYYMMDD-NNN
```

项目、目标、责任人、权限或范围不清楚时停止。

## Step 2：收集和验证证据

优先检查：

1. 当前实际执行的命令及结果；
2. 生产代码、已有测试、fixture、helper、配置和 CI；
3. 需求、架构、API 和流程文档；
4. 历史日志、trace、缺陷和可信报告；
5. 用户说明；
6. 明确标记的推断。

记录缺失、冲突、过期或无法验证的内容，不把猜测补写成事实。

## Step 3：建立风险图

识别主流程、异常路径、状态转换、边界、外部依赖和副作用。

每个保留的风险都必须关联真实证据，并明确影响、可能性、优先级和责任上下文。
安全、支付、权限、隐私、数据完整性和不可逆操作需要重点评审。

## Step 4：生成候选测试场景

针对风险生成 smoke、positive、negative、boundary、regression 或 exploratory
场景，并记录：

- 测试目标和对应风险；
- 前置条件、数据和操作；
- 测试层级；
- 真实依赖与 mock、stub、fake；
- 确定性断言；
- cleanup 和隔离；
- 能证明什么、不能证明什么；
- 失败最可能意味着什么。

没有可验证预期结果的场景不应进入后续自动化。

## Step 5：选择自动化用例

人工根据以下条件选择值得实现的用例：

- 风险和业务价值明确；
- 预期结果可以确定性断言；
- 环境、账号、数据和依赖可控；
- 可以稳定重复执行；
- 自动化收益高于维护成本；
- AGP 允许所需操作。

接受或拒绝都需要记录理由。

## Step 6：编写和工程化测试

Agent 在获批范围内起草或修改测试，并遵循项目现有的：

- 测试框架和目录；
- fixture、helper 和命名规则；
- 数据、隔离和 cleanup 方式；
- 配置、标记和 CI 习惯。

断言应覆盖业务结果、状态转换和重要副作用，不能只检查状态码、进程退出或页面
可见。Agent 生成的测试必须经过人工 Review，不能自行声明为 `Executable`。

## Step 7：执行并保存证据

从最小相关命令开始执行，并记录：

- 准确命令和退出码；
- 测试资产和 source revision；
- Profile 与 ENV/ACT/DAT/DEP/AGP 精确 revision；
- 环境以及与生产环境的差异；
- 开始和结束时间；
- pass、fail 或 error；
- 必要的日志、trace、截图和报告。

没有真实执行证据时，不能声称测试已经通过或行为已经验证。

## Step 8：分析失败

先区分观察事实和分析假设，再考虑：

- Product defect；
- Test defect；
- Flaky behavior；
- Environment / infrastructure；
- Data issue；
- Agent-generated mistake；
- Baseline-caused failure；
- Unresolved。

Agent 可以排序和解释假设，但最终归因必须由人工确认。证据不足时保持
`UNRESOLVED`。

必要时可以返回前面步骤：

```text
证据不足       → Step 2
场景意图错误   → Step 4
测试实现错误   → Step 6
受控修复完成   → Step 7 重新执行
```

向后返回时必须保留旧工件和历史，不得静默覆盖。

## Step 9：固化回归和门禁依据

把已确认缺陷转化为最小且有意义的回归测试，并检查：

- 人工评审是否完成；
- 断言是否充分；
- 是否多次执行稳定；
- 环境、数据和依赖是否明确；
- 失败含义是否清楚；
- CI 时间和维护成本是否可接受；
- 是否真实接入对应 CI workflow。

Blocking 或发布相关决定只能由有权限的人类 Approver 批准。

## Step 10：报告、关闭和归档

最终报告应说明：

- 测试目标、范围和 source revision；
- 使用的 Profile 和 Baseline；
- 执行命令和观察结果；
- 已验证行为、失败行为和未执行项目；
- 测试证明什么、不证明什么；
- 真实依赖和被替换依赖；
- CI 和门禁状态；
- 未解决风险、负责人和后续动作。

关闭后的 Task 必须保留执行当时的精确引用。以后产生的新 Profile 或 Baseline
不能改写历史记录。

## 状态边界

必须区分：

```text
Candidate  ≠ Reviewed
Reviewed   ≠ Executable
Executable ≠ Verified
Verified   ≠ Blocking
```

- Agent 或人工可以起草 `Candidate`。
- 只有人类 Reviewer 可以标记 `Reviewed`。
- 只有人类 Owner 可以批准 `Executable`。
- `Verified` 需要真实执行证据和人工确认。
- `Blocking` 需要稳定性、CI 接入证据和人类 Approver。

## 最小追溯链

完整任务应能重建：

```text
TASK
→ WORKFLOW
→ EVIDENCE
→ RISK
→ SCENARIO
→ SELECTED CASE
→ TEST ASSET
→ RUN
→ TRIAGE（适用时）
→ GATE RECORD
→ QUALITY REPORT
```

不适用的阶段可以省略具体文件，但必须显式记录为不适用。

## 主要文件

| 文件 | 用途 |
|---|---|
| `SKILL.md` | 核心运行规则和流程入口 |
| `agents/openai.yaml` | Skill 在 Codex 中的显示名称和默认提示 |
| `references/step-contract.md` | Step 1–10 的详细输入、输出和停止条件 |
| `references/project-profile-and-baselines.md` | Project Profile 与 ENV/ACT/DAT/DEP/AGP 规则 |
| `references/artifact-traceability.md` | ID、生命周期、关系、替代和关闭规则 |
| `references/workflow-and-artifacts.md` | 常用工件字段与报告结构 |
| `references/review-and-risk-controls.md` | 实现、安全、数据和高风险控制 |
| `references/quality-gates-and-status.md` | 状态、CI 和门禁标准 |
| `references/maturity-and-use-cases.md` | 团队采用、能力级别和典型场景 |

## 使用示例

```text
使用 $agent-assisted-testing 分析这个支付 API 的主要风险并设计候选测试场景。
```

```text
使用 $agent-assisted-testing 为这个缺陷编写最小回归测试并运行验证。
```

```text
使用 $agent-assisted-testing 审计当前测试是否真的接入 PR blocking gate。
```

