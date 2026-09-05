# Myown · 工程协作 Skills

这里收录了我整理的 8 个 AI Agent skill，主要用于推进开发计划、开展软件测试，以及整理工程记录和 Agent 会话。

各个 skill 都要求根据代码、测试、日志或文档说明结果，分清已经验证的内容和仍需确认的问题。

下面按用途分为 4 类。点击技能名称，可以查看对应的 `SKILL.md`。

## 分类导航

| 分类 | 数量 | 用途 |
| --- | ---: | --- |
| [计划执行与进度管理](#计划执行与进度管理) | 2 | 完成计划中的一个任务，记录进度和验收依据 |
| [软件测试与 CI/CD](#软件测试与-cicd) | 3 | 设计与执行测试、梳理覆盖范围、分析流水线结果 |
| [工程记录与项目回归](#工程记录与项目回归) | 2 | 记录工作成果，恢复项目上下文 |
| [Agent 会话分析](#agent-会话分析) | 1 | 复盘 Agent 的执行过程，核对最终结论 |

## 计划执行与进度管理

适合已经有计划、路线图或任务清单的项目。每次选择一个可独立验收的任务，完成后记录结果，再决定下一步。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [plan-progress-checkpoint](./plan_progress%20checkpoint/SKILL.md) | 选择本次任务，控制范围，更新完成、待复核或受阻状态 | 计划状态、进度台账（Progress Ledger）、验收依据和下一步建议 |
| [evidence-backed-plan-executor](./evidence-backed-plan-executor/SKILL.md) | 检查仓库现状，比较方案，实现并验证一个计划任务，解释决策依据 | 代码或其他交付物、验证结果、执行记录和计划更新 |

两者可以配合使用：`plan-progress-checkpoint` 管任务范围和进度，`evidence-backed-plan-executor` 负责具体实现，并解释为什么这样做。

`evidence-backed-plan-executor` 默认采用引导学习模式，遇到需要权衡的方案时，会先讨论一次再实现。如果明确要求自主、连续执行，可使用它的 evidence mode。

## 软件测试与 CI/CD

这组 skill 分别用于开展测试、编写测试文档和整理流水线结果，可按当前任务单独选择。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [agent-assisted-testing](./agent-assisted-testing/SKILL.md) | 设计、编写和执行测试，分析失败，补充回归测试或审计质量门禁 | 按模式生成项目与执行基线候选文档、风险与场景清单、测试代码、执行证据或质量报告 |
| [test-engineering-doc-mapper](./test-engineering-doc-mapper/SKILL.md) | 对照代码和测试，新建、更新、审计或合并测试工程文档 | 测试与架构、业务流程的对应关系，以及测试层级、依赖、断言、覆盖范围和 CI 门禁说明 |
| [ci-cd-agent-result-reporter](./ci-cd-agent-report/SKILL.md) | 运行或检查 CI/CD，整理测试、构建和部署结果，分析失败阶段 | 执行结果报告、阶段与门禁状态、失败分析、产物引用，可选 JSON 摘要 |

`agent-assisted-testing` 是我个人 Testing SOP 项目的一部分实现，基于 Agent-assisted Software Testing SOP v1.2 编写。它包含项目 Profile、执行 Baseline 和人工评审要求，使用前需要阅读对应模式的前置条件。

`test-engineering-doc-mapper` 会说明测试覆盖了哪些行为、用了哪些真实或替代依赖，以及哪些结论还没有证据。它主要负责文档核对，修改测试或 CI 需要另行明确任务。

## 工程记录与项目回归

一次工作结束后，可以用执行记录说明成果；隔一段时间再回来，则用项目回归指南找回目标、进展和接下来要做的事。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [evidence-backed-work-unit-journal](./evidence-backed-work-unit-journal/SKILL.md) | 记录一次迁移、功能开发、修复、测试或重构，也可精简已有的冗长记录 | 实际改动、与计划的差异、完成依据、尚未验证的部分和下一步；必要时附执行细节 |
| [project-reentry-guide](./project-reentry-guide/SKILL.md) | 离开项目一段时间后，重新了解目标、关键流程、术语和进展 | 项目回归指南，说明已完成的工作、剩余问题、当前优先级和参考文档 |

## Agent 会话分析

用会话记录检查 Agent 如何处理一项请求，包括中途出错后怎样恢复、上下文压缩后有没有偏离目标。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [agent-session-trace-analyzer](./agent-session-trace-analyzer/SKILL.md) | 复盘工具调用、文件变更、失败恢复、上下文压缩和子 Agent 协作，核对任务完成情况 | 执行时间线、需求与证据对应表、验证质量分析，以及有来源的代码片段或 diff |

使用时提供会话记录、工具输出、相关代码或验证结果，并说明要分析哪一段。分析只依据可观察的记录，缺少证据的地方会明确标出。

## 使用方式

1. 选择适合当前任务的 skill，阅读其 `SKILL.md`，确认适用范围和所需材料。
2. 按所用 Agent 工具的加载方式引入完整技能目录，保留其中已有的 `references/`、`assets/`、`scripts/` 和 `agents/`。
3. 提供目标仓库或材料，并说明本次要做什么、做到哪里、需要什么产出。

可以参考下面的请求，补上自己的项目材料：

- 使用 `plan-progress-checkpoint` 和 `evidence-backed-plan-executor`，读取这份实施计划，完成下一个可独立验收的任务，验证结果并更新进度。
- 使用 `test-engineering-doc-mapper`，对照代码、测试和 CI 检查这份测试说明，修正覆盖范围和依赖描述。
- 使用 `ci-cd-agent-result-reporter`，根据这次流水线日志和测试报告整理结果，说明失败原因及依据，列出未执行的阶段。
- 使用 `evidence-backed-work-unit-journal`，把这次修复的改动、验收依据、与计划的差异和下一步写成简短记录。
- 使用 `project-reentry-guide`，结合计划、近期执行记录和仓库现状，写一份方便继续开发的项目回归指南。
- 使用 `agent-session-trace-analyzer`，分析这份会话记录，检查需求是否完成、上下文压缩后是否偏离目标，以及最终结论有无证据。

能执行哪些操作，取决于 Agent 工具、可访问的材料和项目环境。具体规则见各技能的 `SKILL.md` 及其引用文件。

## 目录结构

下图只列出技能入口文件：

```text
.
├── README.md
├── agent-assisted-testing/
│   └── SKILL.md
├── agent-session-trace-analyzer/
│   └── SKILL.md
├── ci-cd-agent-report/
│   └── SKILL.md
├── evidence-backed-plan-executor/
│   └── SKILL.md
├── evidence-backed-work-unit-journal/
│   └── SKILL.md
├── plan_progress checkpoint/
│   └── SKILL.md
├── project-reentry-guide/
│   └── SKILL.md
└── test-engineering-doc-mapper/
    └── SKILL.md
```

有两个目录名与 `SKILL.md` 中的 `name` 不同，查找文件时以目录名为准：

| 目录名 | Skill 声明名称 |
| --- | --- |
| `plan_progress checkpoint` | `plan-progress-checkpoint` |
| `ci-cd-agent-report` | `ci-cd-agent-result-reporter` |

部分技能还附有以下资源：

| 资源 | 用途 |
| --- | --- |
| `references/` | 按需读取的规则、示例和补充说明 |
| `assets/` | 输出文档模板 |
| `scripts/` | 辅助脚本，例如测试清单收集脚本 |
| `agents/` | Agent 界面使用的技能元数据 |

## 补充阅读

- [Agent-assisted Testing 中文流程说明](./agent-assisted-testing/agent-assisted-testing%20README.md)
- [Agent Session Trace Analyzer 简介](./agent-session-trace-analyzer/README.md)
