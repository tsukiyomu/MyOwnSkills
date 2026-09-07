# Myown · 工程协作 Skills

这里整理了我用于真实软件工程工作的 AI Agent skills，重点是学习工程判断、开展测试，并留下可追溯的执行记录。目前使用 8 个 skill，另保留 1 个已停用的 `plan-progress-checkpoint` 目录供历史参考。

我希望这些记录能让人看清 Agent 做了什么、为什么这样做、结果有什么依据。以后修改实现或排查错误时，也能沿着文档找到相关代码、日志和验证结果。各个 skill 都要求分清已经验证的内容和仍需确认的问题。

## 分类导航

当前使用的技能按用途分为 5 类。点击名称可查看对应的 `SKILL.md`。

| 分类 | 数量 | 用途 |
| --- | ---: | --- |
| [项目理解与计划回归](#项目理解与计划回归) | 2 | 熟悉项目，恢复某份计划的目标、进展和下一步上下文 |
| [工程决策说明](#工程决策说明) | 1 | 根据仓库事实解释重要实现选择及其验证范围 |
| [软件测试与 CI/CD](#软件测试与-cicd) | 3 | 设计与执行测试、梳理覆盖范围、分析流水线结果 |
| [执行结果记录](#执行结果记录) | 1 | 记录一次工作的实际成果、验收证据和未解决的问题 |
| [Agent 会话分析](#agent-会话分析) | 1 | 复盘 Agent 的执行过程，核对最终结论 |

`plan-progress-checkpoint` 不计入以上分类，原因见[停用说明](#为什么不再使用-plan-progress-checkpoint)。

## 项目理解与计划回归

重新熟悉整个项目时，用 `project-reentry-guide` 梳理背景；已经知道项目在做什么、只需要接着某份计划往下做时，用 `plan-reentry-guide` 恢复当前上下文。两者按需要选择，不要求依次使用，也不代替计划本身。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [project-reentry-guide](./project-reentry-guide/SKILL.md) | 离开项目一段时间后，重新了解目标、关键流程、术语和进展 | 项目回归指南，说明系统用途、已完成的工作、测试所能证明的内容、剩余问题和参考文档 |
| [plan-reentry-guide](./plan-reentry-guide/SKILL.md) | 回到某份正在推进的计划，恢复足够继续工作的上下文 | 带日期的计划回归指南，说明工作起因、当前进展、未解决的问题、下一步理由和阅读入口 |

## 工程决策说明

计划中的实现设想可能与当前仓库不完全一致。这里需要说明的是：发现了什么事实，它为什么影响任务，以及实际选择如何满足约定的要求。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [evidence-backed-execution-rationale](./evidence-backed-execution-rationale/SKILL.md) | 实现过程中或回看已有改动时，解释重要工程选择及其依据 | 仓库事实、由此发现的问题、实现选择、实际影响和验证范围之间的说明 |

这个 skill 由原来的 `evidence-backed-plan-executor` 调整而来，职责收敛到解释重要决策。它不规定统一的实现流程，也不接管进度或 Journal。需要边做边学时，可以补充工程原则和以后识别类似问题的线索；学习模式本身不要求自动暂停或提问。

## 软件测试与 CI/CD

这组 skill 分别用于开展测试、编写测试文档和整理流水线结果，可按当前任务单独选择。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [agent-assisted-testing](./agent-assisted-testing/SKILL.md) | 设计、编写和执行测试，分析失败，补充回归测试或审计质量门禁 | 按模式生成项目与执行基线候选文档、风险与场景清单、测试代码、执行证据或质量报告 |
| [test-engineering-doc-mapper](./test-engineering-doc-mapper/SKILL.md) | 对照代码和测试，新建、更新、审计或合并测试工程文档 | 测试与架构、业务流程的对应关系，以及测试层级、依赖、断言、覆盖范围和 CI 门禁说明 |
| [ci-cd-agent-result-reporter](./ci-cd-agent-report/SKILL.md) | 运行或检查 CI/CD，整理测试、构建和部署结果，分析失败阶段 | 执行结果报告、阶段与门禁状态、失败分析、产物引用，可选 JSON 摘要 |

`agent-assisted-testing` 是我个人 Testing SOP 项目的一部分实现，基于 Agent-assisted Software Testing SOP v1.2 编写。它包含项目 Profile、执行 Baseline 和人工评审要求，使用前需要阅读对应模式的前置条件。

`test-engineering-doc-mapper` 会说明测试覆盖了哪些行为、用了哪些真实或替代依赖，以及哪些结论还没有证据。它主要负责文档核对，修改测试或 CI 需要另行明确任务。

## 执行结果记录

一次工作结束后，先让读者看清实际成果和验收情况，再通过引用找到详细证据。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [evidence-backed-work-unit-journal](./evidence-backed-work-unit-journal/SKILL.md) | 记录一次迁移、开发、修复、测试或重构的结果，也可精简已有记录 | 实际成果、与计划的差异、验收证据、尚未验证的部分和下一步 |

详细日志、测试报告和已有决策说明按需链接。精简正文时保留追溯所需的原始信息，包括相关版本、执行环境和仍有影响的失败记录。Journal 的结论应能查回证据，生成了报告本身不代表任务已经通过验收。

## Agent 会话分析

用会话记录检查 Agent 如何处理一项请求，包括中途出错后怎样恢复、上下文压缩后有没有偏离目标。

| Skill | 适用场景 | 主要产出 |
| --- | --- | --- |
| [agent-session-trace-analyzer](./agent-session-trace-analyzer/SKILL.md) | 复盘工具调用、文件变更、失败恢复、上下文压缩和子 Agent 协作，核对任务完成情况 | 执行时间线、需求与证据对应表、验证质量分析，以及有来源的代码片段或 diff |

使用时提供会话记录、工具输出、相关代码或验证结果，并说明要分析哪一段。Journal 侧重一次工作的最终成果；会话分析会沿着可观察的记录还原执行过程，缺少证据的地方会明确标出。

## 为什么不再使用 plan-progress-checkpoint

**`plan-progress-checkpoint` 已退出当前使用方案，本地文件保留供历史参考。** 这次调整将重点放在工程判断、测试验证和执行记录上。

原来的 checkpoint 承担任务选择、范围维护和进度登记，也包含执行前的检查。重新梳理后，我认为这些职责可以放回计划、项目规则和已有任务记录中，没有必要再用一个独立 skill 作为计划与执行之间的中间层。

约束需要在执行之前明确，并在执行过程中持续遵守。例如，任务是“增加确定性的 SSE 契约测试，只修改测试层，不改变生产 API”，这些边界就应直接写进 Plan 和 Work Unit。Agent 选择实现方案时应检查是否符合约束，Review 再依据改动和证据核对结果。等越界改动完成后才靠 checkpoint 提醒，已经太晚。

当前采用以下分工：

| 层次 | 负责什么 |
| --- | --- |
| Architecture | 说明系统结构和长期设计依据，为计划提供背景 |
| Plan / Work Unit | 定义目标、范围、非目标、验收条件、依赖和本次任务的约束 |
| Global Rules / Repository Instructions | 规定长期适用的编码风格、测试框架、安全要求、依赖策略等规则 |
| Agent Execution | 在计划和规则内，根据当前仓库选择实现方法，完成授权范围内的工作与验证 |
| Execution Rationale | 解释重要选择如何来自仓库事实、解决了什么问题，以及验证能说明什么 |
| Evidence / Review | 用测试、CI、日志或其他适当证据核对结果，判断是否满足验收要求 |
| Work Unit Journal | 记录实际成果、偏差、证据和仍未解决的问题 |
| Plan Re-entry | 从计划和执行记录中恢复当前上下文，给出继续阅读和工作的入口 |

这些约束和说明贯穿实际工作，不是要求每次都依次调用的八个步骤。比如计划建议的旧 hook 已经不存在，Agent 可以在约定范围内寻找合适的接入位置，再用 Rationale 解释选择依据；如果必须改变任务边界或验收条件，应先明确处理这个冲突。

停用 checkpoint 后，进度仍记录在项目已有的计划清单、Issue 或任务台账中。执行任务的 Agent 按项目约定更新状态并链接证据，验收缺口保持可见。Rationale、Journal 和 Re-entry 各自提供说明，不另建一套进度系统。

长周期自动运行、多 Agent 协作或 CI 流程仍可能需要 checkpoint，保存“完成到哪里、下一步允许执行什么”等状态。这类需求适合由项目管理工具或工作流编排机制承担；当前这组核心技能不承担该职责。

[旧版 plan-progress-checkpoint 文件](./plan-progress-checkpoint/SKILL.md) 继续保留。本次只更新 README，相关 `SKILL.md` 中尚存的 checkpoint 分工描述属于待同步的旧说明，不表示仍推荐启用它。

这些 skill 可以按需组合，不要求每次任务生成一整套文档。这次调整能否让记录更好读、更方便追溯，仍需要在后续实际使用中检验。

## 使用方式

1. 选择适合当前任务的 skill，阅读其 `SKILL.md`，确认适用范围和所需材料。
2. 按所用 Agent 工具的加载方式引入完整技能目录，保留其中已有的 `references/`、`assets/`、`scripts/` 和 `agents/`。
3. 提供目标仓库或材料，并说明本次要做什么、做到哪里、需要什么产出。

可以参考下面的请求，补上自己的项目材料：

- 按这份实施计划和仓库规则完成指定任务，依据验收结果更新已有任务记录。重要工程选择用 `evidence-backed-execution-rationale` 解释，并用 `evidence-backed-work-unit-journal` 记录结果和证据。
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

下图列出技能入口文件；`plan-progress-checkpoint` 保留在本地作为历史参考，不再使用：

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
├── plan-progress-checkpoint/  # 不再使用，保留历史文件
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
