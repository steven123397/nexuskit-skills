---
name: nk-ask-ljq
description: "Ask which skill or flow fits your situation. A router over the installed NexusKit skills: one recommended entry point with reason, materials, and expected result - without imposing a fixed pipeline."
argument-hint: "[可选：描述当前处境或问题]"
disable-model-invocation: true
---

不需要记住所有技能，说出现在卡在哪里。

这是一张工作地图。整套安装后任意技能都能作为入口：已有想法、spec、ticket 或代码，就从对应位置开始。小改动不必先写 spec，排障不必先盘问，问路也不会自动启动一整条流程。

## 先回答眼前的问题

根据当前请求和已有上下文，给出**一个首选入口、一句话理由、需要带入的材料和预期结果**。只有两条路线会产生实质不同的结果时才解释分叉；信息不足以选择时，问一个能区分路线的问题，不把整张地图复述给用户。

用户只问怎么用，就推荐后结束。用户已要求执行某项工作，选定后读取该技能的公开入口，携带原请求、范围、已有决定、证据和授权继续，遵守目标技能的调用边界。推荐一个技能不等于用户已调用它，问路不产生写入、提交或发布授权。

## 主线：从想法到交付

常见功能开发沿这条路走，前面已有的成果直接接上，每步调用后汇报结束、不自动进入下一步：

1. **敲定要做什么** → `nk-grill`，设计树逐轮盘问直到共同理解；讨论项目领域设计时同时调用 `nk-domain-modeling` 维护术语与关键决定。已有清楚想法就跳过。
2. **纸面上定不了的问题** → `nk-prototype` 用一次性原型回答（先要查事实走 `nk-research`）；明确的研究问题（选型、上游行为、外部事实）直接 `nk-research`。
3. **写下来**：多会话的构建 → `nk-to-spec` 把讨论整理成 spec，`nk-to-tickets` 拆成带依赖的纵向切片。单个明确的小任务直接 `nk-implement`，不必先写 spec。
4. **实施**：单张 ticket → `nk-implement`（代码纪律调 `nk-codecraft`，测试纪律调 `nk-tdd`，提交前三轴审查 `nk-review`，提交走 `nk-commit`）；整份 spec → `nk-odyssey`，在集成分支上并行派实施子代理。`nk-odyssey` 仍在测试中，推荐时说明多 agent 调度尚缺真实任务的完整验证。
5. **收口**：spec 整体验收 → `nk-spec-close`，通过即关票不等合并；分支交付 → `nk-pr`，draft PR、审查衔接、授权合并与清理。
6. **复盘** → `nk-retro`，看 Agent 工作环境与协作的改进空间，按请求存入 OpenViking。

工作分支按项目流程开；分支可没有 spec（仅解决外部 Issue），不强制一一对应。

## 其他入口

- **出错、回归、异常慢** → `nk-debug`：先建复现回路再追根因；仅诊断是有效交付，授权修复则完成验证、审查与提交。
- **工作中发现独立缺陷或需求，先记下以后做** → `nk-to-issue`，核实查重后记录为 GitHub Issue；记录不等于开始实现。
- **目标巨大、未知相互牵连，连要决定什么都说不清** → `nk-wayfinder`，在 Linear 里维护 map 与决策 tickets 逐步收敛；产出决定而非交付。
- **首次把仓库接入 NexusKit** → `nk-init`，配置 Linear 与 GitHub 去向并写导航指针。

## 随时单独使用

| 你现在想做什么 | 入口与结果 |
| :-- | :-- |
| "这个模块我没想清楚，详细问我" | `nk-grill`，严格追问直到理解对齐 |
| "你刚才说的我没跟上" | `nk-wait-what`，补上下文用平实语言重述 |
| 审查当前改动、分支或 PR | `nk-review`，三轴发现与覆盖边界，不直接修复 |
| 已有完整改动，需要提交 | `nk-commit`，核对范围与证据后提交 |
| 写给人看的中文文本 | `nk-prose`，自然、准确、易读的写作与润色 |
| 一串只有人能完成的配置或操作 | `nk-wizard`，生成交互式 bash 向导交给人运行 |

## 词汇层

`nk-codecraft`（模块形状与代码纪律）、`nk-tdd`（测试纪律）、`nk-domain-modeling`（领域语言与 ADR）是运行在其他技能之下的 model-invoked 参考，各是自己词汇的唯一来源；其他技能会调用它们，遇到"词不对"而非"流程不对"的问题时也可直接查。

## 上下文从哪来

spec、tickets 与进度在 Linear；代码与合入事实在 Git/PR；背景与经验在 OpenViking；术语在 `CONCEPTS.md`，关键决定在 `docs/adr/`。ticket 自包含，新会话从它开始即可，不需要交接或状态文档。

首次使用前先跑 `nk-init` 完成项目接入。
