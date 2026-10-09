---
name: nk-odyssey
description: "Drive a scoped effort with ready tickets to deliverable state on one integration branch: work the task graph, coordinate parallel implementer subagents, resolve integration issues, then hand off to spec-level acceptance. Single-ticket work belongs to nk-implement."
argument-hint: "[spec 的 Linear URL 或编号]"
disable-model-invocation: true
---

接住已明确的工作：spec 与它的 tickets 已经就绪，目标是把整份 spec 做到可交付状态。持续推进 tickets、协调并行实施、解决集成问题；单个 ticket 的实施纪律见 `nk-implement`，本技能负责长途调度。

tickets 不是步骤清单，而是带阻塞关系的**任务图**：始终存在可以开工的**前沿**。Linear 团队与项目从 `docs/agents/issue-tracker.md`（`nk-init` 的产物）读取，缺失时先询问。

目标是在一条**集成分支**上完成整份 spec，按 Linear 的方式逐张关闭 tickets。

与子代理的通信保持稀疏：主要通过**上下文指针**（spec、tickets、研究记录、已有提交）传递，不复述指针已提供的信息。实施子代理尽量后台并行，换取最大并发。

## 执行底座

开工前确认底座：项目指令文件声明使用 Orca 且 Orca 可用时，询问用户本次是否走 Orca；走 Orca 则工作树与实施、合并子代理的创建全部改用 Orca 方式（派发、交互、完工确认与清理见 `nk-orca-guide`），不落工作树的探索、审查子代理仍走原生。未声明、不可用或用户选择不走时，按仓库惯例（同级工作树 + 原生子代理）执行。两条路径下票状态流转、验收与收尾不变。

## 流程

1. 读取 spec 和全部 tickets，理解任务图；从**前沿**开始。开工时把已解锁但仍在 Backlog 的 tickets 推进到 Todo。
2. （可选）派**探索子代理**完成 tickets 所需的探索——相关代码文件或外部文档。探索记录保存为仓库外的 Markdown，供后续所有子代理取用，让实施子代理专注实施。独立的研究调查走 `nk-research`。
3. 创建集成分支。Linear 按 PR 关闭工作或用户要求时，在首次合入后开 draft PR，标记将关闭 spec 与相关 tickets。
4. 派**实施子代理**逐张处理前沿上的 tickets，每个子代理在独立工作树、自己的分支上：
   - 开工前确认工作树基于集成分支最新提交，不是就重置；
   - 按 `nk-implement` 的纪律完成整张 ticket：认领（Todo → In Progress）、实施、调用 `nk-tdd`、单票适用的审查、提交；
   - 汇报完成前，把集成分支最新提交合入自己的分支。
5. 实施子代理完成后，用**合并子代理**把它的工作合入集成分支；冲突就地解决，集成问题记录到对应 ticket。
6. 前沿因此变化时，为新解锁的 tickets 派更多实施子代理，并把解锁票从 Backlog 推进到 Todo。
7. 全部 tickets 完成后，调用 `nk-spec-close` 做整体验收：跨 ticket 衔接、完整使用场景，需要审查时由它调用 `nk-review`。验收发现缺口就继续处理，直到通过。
8. 有 draft PR 时接 `nk-pr` 完成交付与收尾；否则按 Linear 方式关闭各 tickets，汇报集成分支。实施子代理的工作树用毕即清理。
