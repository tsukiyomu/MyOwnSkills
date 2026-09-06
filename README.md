# Myown · 工程协作 Skills

这里收录了我整理的 9 个 AI Agent skill，用于推进开发计划、开展软件测试，以及整理工程记录和 Agent 会话。

我希望这些记录能让人看清 Agent 做了什么、为什么这样做、结果有什么依据。以后修改实现或排查错误时，也能沿着文档找到相关代码、日志和验证结果。各个 skill 都要求分清已经验证的内容和仍需确认的问题。

下面按用途分为 4 类。点击技能名称，可以查看对应的 `SKILL.md`。

## 分类导航

| 分类 | 数量 | 用途 |
| --- | ---: | --- |
| [计划推进与执行记录](#计划推进与执行记录) | 4 | 管理进度、解释工程决策、记录结果，恢复当前计划的上下文 |
| [软件测试与 CI/CD](#软件测试与-cicd) | 3 | 设计与执行测试、梳理覆盖范围、分析流水线结果 |
| [项目回归](#项目回归) | 1 | 重新熟悉项目目标、主要流程和术语 |
| [Agent 会话分析](#agent-会话分析) | 1 | 复盘 Agent 的执行过程，核对最终结论 |

## 计划推进与执行记录

这四个 skill 围绕一份已有计划分工：进度记在哪里，重要实现选择怎样解释，一次工作结束后留下什么，以及隔一段时间回来从哪里继续读。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [plan-progress-checkpoint](./plan-progress-checkpoint/SKILL.md) | 选择可执行的工作单元，保留约定的范围和验收要求，核对或登记进度 | 计划状态、简短进度台账、验收依据链接和下一步建议 |
| [evidence-backed-execution-rationale](./evidence-backed-execution-rationale/SKILL.md) | 实现过程中或回看已有改动时，解释重要工程选择及其依据 | 仓库事实、由此发现的问题、实现选择、实际影响和验证范围之间的说明 |
| [evidence-backed-work-unit-journal](./evidence-backed-work-unit-journal/SKILL.md) | 记录一次迁移、开发、修复、测试或重构的结果，也可精简已有记录 | 实际成果、与计划的差异、验收证据、尚未验证的部分和下一步 |
| [plan-reentry-guide](./plan-reentry-guide/SKILL.md) | 回到某份正在推进的计划，恢复足够继续工作的上下文 | 带日期的计划回归指南，说明工作起因、当前进展、未解决的问题、下一步理由和阅读入口 |

计划负责约定目标、要求和验收条件。Agent 在这些约束及项目规则下选择实现方式；`plan-progress-checkpoint` 负责选择任务、维护状态和登记结果。未指定范围时，它默认选择一个可独立验收的工作单元；已经明确要求完成一批任务或整份计划时，则保留该范围。

`evidence-backed-execution-rationale` 由原来的 `evidence-backed-plan-executor` 调整而来，职责收敛到解释重要决策。它不规定统一的实现流程，也不接管进度或 Journal。需要边做边学时，可以补充工程原则和以后识别类似问题的线索；学习模式本身不要求自动暂停或提问。

`evidence-backed-work-unit-journal` 让读者先看清这次工作的结果，再通过引用查到证据。详细日志、测试报告和已有决策说明按需链接，精简正文时保留追溯所需的原始信息。`plan-reentry-guide` 则从计划、相关架构和 Journal 中整理当前上下文，具体状态仍以原计划及其进度记录为准。

这些 skill 可以按需组合，不要求每次任务都生成四份文档。比如一次修复可以更新已有台账、在对话中解释关键选择，再留下简短 Journal；需要重新接上计划时，再整理回归指南。这次职责调整能否让记录更好读、更方便追溯，还需要在后续实际使用中检验。

## 软件测试与 CI/CD

这组 skill 分别用于开展测试、编写测试文档和整理流水线结果，可按当前任务单独选择。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [agent-assisted-testing](./agent-assisted-testing/SKILL.md) | 设计、编写和执行测试，分析失败，补充回归测试或审计质量门禁 | 按模式生成项目与执行基线候选文档、风险与场景清单、测试代码、执行证据或质量报告 |
| [test-engineering-doc-mapper](./test-engineering-doc-mapper/SKILL.md) | 对照代码和测试，新建、更新、审计或合并测试工程文档 | 测试与架构、业务流程的对应关系，以及测试层级、依赖、断言、覆盖范围和 CI 门禁说明 |
| [ci-cd-agent-result-reporter](./ci-cd-agent-report/SKILL.md) | 运行或检查 CI/CD，整理测试、构建和部署结果，分析失败阶段 | 执行结果报告、阶段与门禁状态、失败分析、产物引用，可选 JSON 摘要 |

`agent-assisted-testing` 是我个人 Testing SOP 项目的一部分实现，基于 Agent-assisted Software Testing SOP v1.2 编写。它包含项目 Profile、执行 Baseline 和人工评审要求，使用前需要阅读对应模式的前置条件。

`test-engineering-doc-mapper` 会说明测试覆盖了哪些行为、用了哪些真实或替代依赖，以及哪些结论还没有证据。它主要负责文档核对，修改测试或 CI 需要另行明确任务。

## 项目回归

目录里仍保留 `project-reentry-guide`，用于重新熟悉整个项目。它覆盖的背景比 `plan-reentry-guide` 更广；如果只是想接着某份计划往下做，可以从上面的计划回归指南开始。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [project-reentry-guide](./project-reentry-guide/SKILL.md) | 离开项目一段时间后，重新了解目标、关键流程、术语和进展 | 项目回归指南，说明系统用途、已完成的工作、测试所能证明的内容、剩余问题和参考文档 |

## Agent 会话分析

用会话记录检查 Agent 如何处理一项请求，包括中途出错后怎样恢复、上下文压缩后有没有偏离目标。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [agent-session-trace-analyzer](./agent-session-trace-analyzer/SKILL.md) | 复盘工具调用、文件变更、失败恢复、上下文压缩和子 Agent 协作，核对任务完成情况 | 执行时间线、需求与证据对应表、验证质量分析，以及有来源的代码片段或 diff |

使用时提供会话记录、工具输出、相关代码或验证结果，并说明要分析哪一段。Journal 侧重一次工作的最终成果；会话分析会沿着可观察的记录还原执行过程，缺少证据的地方会明确标出。

## 使用方式

1. 选择适合当前任务的 skill，阅读其 `SKILL.md`，确认适用范围和所需材料。
2. 按所用 Agent 工具的加载方式引入完整技能目录，保留其中已有的 `references/`、`assets/`、`scripts/` 和 `agents/`。
3. 提供目标仓库或材料，并说明本次要做什么、做到哪里、需要什么产出。

可以参考下面的请求，补上自己的项目材料：

- 使用 `plan-progress-checkpoint` 推进这份实施计划中的下一个可独立验收任务，完成实现和验证后更新进度。重要工程选择用 `evidence-backed-execution-rationale` 解释，并用 `evidence-backed-work-unit-journal` 记录结果和证据。
- 使用 `evidence-backed-execution-rationale`，结合当前代码和测试解释这次依赖替换的依据、影响及验证范围，并补充相关工程原则。
- 使用 `evidence-backed-work-unit-journal`，把这份冗长记录改写为简短 Journal，保留实际成果、与计划的差异、验收依据和未解决的问题，并链接原始证据。
- 使用 `plan-reentry-guide`，结合这份计划和近期 Journal，说明为什么做这项工作、进展到了哪里，以及下一步为什么先做这个任务。
- 使用 `agent-assisted-testing` 的 design 模式，结合需求、现有测试和项目基线，整理当前功能的风险及候选测试场景。
- 使用 `test-engineering-doc-mapper`，对照代码、测试和 CI 检查这份测试说明，修正覆盖范围和依赖描述。
- 使用 `ci-cd-agent-result-reporter`，根据这次流水线日志和测试报告整理结果，说明失败原因及依据，列出未执行的阶段。
- 使用 `project-reentry-guide`，结合项目文档和近期报告，整理项目用途、主要流程、必要术语和当前问题，帮助我重新熟悉仓库。
- 使用 `agent-session-trace-analyzer`，分析这份会话记录，检查需求是否完成、上下文压缩后是否偏离目标，以及最终结论有无证据。

能执行哪些操作、获取哪些日志和产物，取决于 Agent 工具、可访问的材料和项目环境。具体规则见各技能的 `SKILL.md` 及其引用文件。

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
├── evidence-backed-execution-rationale/
│   └── SKILL.md
├── evidence-backed-work-unit-journal/
│   └── SKILL.md
├── plan-progress-checkpoint/
│   └── SKILL.md
├── plan-reentry-guide/
│   └── SKILL.md
├── project-reentry-guide/
│   └── SKILL.md
└── test-engineering-doc-mapper/
    └── SKILL.md
```

`ci-cd-agent-report` 的目录名与 `SKILL.md` 中声明的名称 `ci-cd-agent-result-reporter` 不同，查找文件时以目录名为准。

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
