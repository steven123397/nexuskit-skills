# Ticket 类型与 HITL/AFK 判定

> 每个 ticket 带一个 `wayfinder:<type>` label。每个 ticket 同时是 **HITL**（human in the loop，与能代表自己发言的人类一起处理）或 **AFK**（Agent 独立驱动）。HITL ticket 只能通过 live exchange 解决——一旦 Agent 开始自问自答，这个 ticket 的处理就已经坏了。

## 四种类型

### Research（AFK）

阅读文档、第三方 API、本地知识库等资源，找出某项 decision 正在等待的事实。当需要当前工作目录之外的知识时使用。

- 客户端支持且允许委派时，可并行派发独立研究；否则主会话内联完成。
- Resolution 记录找到的事实、来源链接，以及它对 pending decisions 意味着什么。
- Research tickets 可批量处理，但先核对实际依赖，不假定所有研究都独立；每项仍须认领、记录结果并维护 map。

### Prototype（HITL）

核心问题是 "how should it look" 或 "how should it behave" 时使用。构建廉价、粗糙、具体的产物提高讨论保真度：outline、rough take、stub，或一小段 UI/逻辑代码。产物作为 asset 从 ticket 链接，不粘贴进 body。

- 廉价是约束不是缺点：原型用来暴露问题供人讨论，不是交付物。一旦开始打磨它，就超出了 ticket 的职责。

### Grilling（HITL，默认类型）

纯对话。拿不准类型时用 grilling。

这是 ticket 类型，不自动调用仅由用户主动发起的 nk-grill。

- 对话按 [`../../conventions/decision-autonomy.md`](../../conventions/decision-autonomy.md) 的提问规则进行：选项驱动、互不依赖的问题合并一轮（至多 3 个）、标注推荐项；收集事实与叙述的问题可以开放式提问。
- 对话中敲定的新领域术语按 [`../../conventions/concepts-vocabulary.md`](../../conventions/concepts-vocabulary.md) 即时写入 `CONCEPTS.md`；用词与术语表冲突时当面指出并对齐。

### Task（HITL 或 AFK）

做出 decision 之前必须完成、但本身没有要 decide、prototype 或 research 的手工工作。例如：注册一个服务以评估其 API、配置访问权限、移动一批数据以看清它的 shape。

- 这是唯一会 **do** 而不是 decide 的类型；它凭借解锁 decision 而存在，不交付 destination。
- Agent 能独立完成时按 AFK 处理；否则给人类一份精确的 checklist（HITL）。
- Resolution 记录做了什么，以及后续 tickets 依赖的事实：凭据位置、新 URL、行数等。

## 无人值守限制

无人值守时，HITL ticket 不可 resolve，也不替用户回答。保留未解决状态并记录卡点；无法继续且无保留认领约定时释放本轮自己的 claim，汇报后结束，或按已有授权处理 AFK 工作。不自动维护 current。

## 每轮一个 ticket

非 research ticket 每轮默认处理一个，先完成 resolution 和 map 维护，再选择下一项。用户要求继续时可在同一会话进入下一轮；不能跨过维护步骤批量关单。
