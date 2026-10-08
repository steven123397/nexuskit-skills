---
name: nk-wayfinder
description: "Explore a large, uncertain goal as a shared map of decision tickets in Linear. Resolve questions and their dependencies until the route is clear, then hand the decisions to spec and ticket creation."
argument-hint: "[可选：map 或决策 ticket 的 Linear URL、编号；也可带着新想法开始]"
disable-model-invocation: true
---

一个想法涉及的工作太大，单个会话讨论不完，通往**目的地**的路还看不清。在 Linear 中把这条路绘成一份 **map**，用**决策 tickets** 逐步解决其中的问题，直到路线明确。每张 ticket 承载一个需要回答的问题。

先说清目的地。它可能是一份准备交给后续实施的 spec，也可能是规划前必须确定的决定。目的地决定每张 ticket 的范围；工程、课程设计等工作都可以采用这种方式。

## 规划而非执行

每张 ticket 解决一个决策。当关键问题已经明确，可以开始做事时，map 就完成了。Research、Prototype 和解锁决策所需的 Task 都服务于这个目的。

## 用名称引用

map 和 ticket 都有标题。给用户的说明和 map 中的索引用标题加链接引用，让人一眼看出在讨论什么。

## map

map 是 Linear 中的一张 issue，标记为 `wayfinder:map`；决策 tickets 是它的子 issue。Linear 团队与项目从 `docs/agents/issue-tracker.md`（`nk-init` 的产物）读取，缺失时先询问。标签沿用项目配置，以下 `wayfinder:*` 是默认命名。

map 是**索引**：只放已定决策的一行摘要和 ticket 链接，详细答案留在 ticket 中。未完成的工作通过查询子 issue 获取。

### map 正文

```markdown
## 目的地

<本次探索要形成的 spec 或决定。一两句话；每次选择 ticket 前先对齐它。>

## 补充说明

<领域背景、需要使用的技能与资料、本次工作的偏好。>

## 已定决策

- [<已完成 ticket 的标题>](链接)：<答案的一行摘要>

## 未成形

<范围内还说不清、暂时建不了 tickets 的问题，随着前沿推进逐步成形。>

## 不在范围内

<本次明确排除的工作及原因。>
```

### 决策 tickets

每张 ticket 的问题应能在一个会话中讨论清楚，正文如下：

```markdown
## 问题

<本 ticket 要解决的决定或调查问题。>
```

用 `wayfinder:research`、`wayfinder:prototype`、`wayfinder:grilling` 或 `wayfinder:task` 标记类型。

开始前认领 ticket：核对负责人和状态，将它分配给本次工作的负责人，状态从 Todo 改为 In Progress。同一负责人下有多个会话时，明确各自处理哪张 ticket。

用 Linear 原生阻塞关系表达依赖。**前沿**是尚未解决、依赖已经满足、也未被其他会话接手的 tickets。取消或作废的依赖需要重新判断是否仍影响后续问题。

答案在解决时记录为评论。原型等产物以链接关联到 ticket。

## Ticket 类型

每张 ticket 可以是 **HITL**（与用户共同处理）或 **AFK**（由 Agent 独立处理）。HITL 的决定来自与用户的实际讨论。

- **Research（AFK）**：阅读文档、第三方 API 或知识库，查明某个决策正在等待的事实。调用 `nk-research`；独立研究可以交给子代理并行完成。
- **Prototype（HITL）**：当问题是“应该长什么样”或“应该怎样运作”时，调用 `nk-prototype`，做一个廉价、粗糙而具体的产物供用户判断，例如大纲、草图或一小段 UI、逻辑代码。将产物链接到 ticket。
- **Grilling（HITL）**：默认类型。调用 `nk-grill` 讨论问题；项目领域设计中的领域建模由它调用 `nk-domain-modeling`。
- **Task（HITL 或 AFK）**：决策前必须做的事情，例如开通服务以评估 API、配置访问权限、移动数据以观察其结构。Agent 能独立完成就自行处理，否则给用户明确的操作清单。完成后记录做了什么，以及后续决策需要的事实。

## 未成形的问题

有些问题需要等前面的决定确定后，才能准确描述。先把它们写进**未成形**。解决一张 ticket 后，回头检查这些问题，把已经成形的问题建成新 tickets。

判断标准是**现在能不能把问题说清楚**：

- 问题已经成形，就建 ticket，即使暂时被依赖阻塞。
- 问题还说不清，就留在“未成形”。一处未成形的问题以后可能形成多张 ticket，也可能不再需要处理。

问题成为 ticket 后，从“未成形”移除对应内容。

## 不在范围内

目的地之外的工作放进**不在范围内**，说明为什么排除。以后要做时，重新确定目的地。

已有 ticket 被发现超出范围时，将其取消，在 map 的“不在范围内”留一行摘要、原因和链接。已定决策记录本次范围内实际解决的问题。

## 两种使用方式

### 建立 map

用户带着一个松散想法开始。

1. **确定目的地。** 调用 `nk-grill`，明确要找到的 spec 或决定。澄清模块用途和实际用法，确定这次探索的范围。
2. **标出前沿。** 再从广度上提问，找出各方面尚未解决的决定和现在能开始的问题。如果目的地和做法已经明确，可以直接交给 `nk-to-spec` 整理。
3. **创建 map。** 填好目的地和补充说明，将暂时说不清的问题写进“未成形”，已定决策留空。
4. **创建能说清的 tickets。** 先创建子 issue，拿到编号后再设置阻塞关系；无阻塞的创建为 Todo，被阻塞的留在 Backlog，解锁后由处理 map 的会话推进。
5. **启动研究。** 对前沿上的独立研究，派子代理调用 `nk-research`。查明的事实和来源记录到对应 ticket，维护 map。
6. 汇报 map 和研究结果。已有继续探索的安排时，进入处理 map 的流程。

### 处理 map

用户提供 map 或其中一张 ticket 的 URL、编号。

1. **读取 map。** 如果输入是 ticket，先找到它所属的 map。先看全局摘要，再按需展开相关 tickets 和讨论记录。
2. **选择并认领。** 用户点名就先核对该 ticket 的依赖；否则从前沿中选取。相互独立的问题可以并行研究或放在同轮讨论，有依赖的问题等前提确定后再继续。
3. **解决问题。** 按 ticket 类型调用对应技能，并使用“补充说明”指定的资料。需要用户取舍时，通过 `nk-grill` 讨论。
4. **记录答案。** 将结论作为评论写入 ticket，标为完成，在 map 的“已定决策”补一行摘要和链接。
5. **更新 map。** 把已经成形的问题建成 tickets，再设置依赖；修订受新答案影响的问题，取消已失效的 tickets 并说明原因；把因此解锁的 tickets 从 Backlog 推进到 Todo。

用户可能让多个会话并行处理独立问题，查询和更新以 Linear 当前状态为准。

通往目的地所需的决策全部解决后，完成 map。仍有进行中或阻塞的问题时，保留 map 的未完成状态。需要产出 spec 时调用 `nk-to-spec`，后续由 `nk-to-tickets` 拆出实施工作。
