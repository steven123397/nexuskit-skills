# 两种模式的详细步骤 (Modes)

每轮调用默认处理一个非 research ticket，完成记录与 map 维护后才进入获授权的下一轮；可在同一会话继续。用户可能并行处理 tickets，claim 与查询以 tracker 实时状态为准。

## Chart the map（用户带着松散想法调用）

1. **Name the destination.** 与用户对话确定 map 要找到的 spec、decision 或 change。Destination 固定 scope，先解决它。
2. **Map the frontier.** 再对话一轮，**breadth-first** 覆盖整个空间而不深入单条线索，浮现 open decisions 与现在可开始的 first steps。**如果没有 fog**，说明路径已经清晰，不需要 map；停止并建议直接走 [nk-plan](../../nk-plan/SKILL.md)。
3. **Create the map**（`wayfinder:map`）：填好 Destination 与 Notes，Decisions so far 留空，fog 勾勒进 **Not yet specified**。
4. **Create the tickets you can specify now** 作为 child issues，然后第二遍再 wire blocking edges（issues 需要编号后才能互相引用）。现在还说不清的留在 **Not yet specified**。
5. **按依赖启动 research。** 仅对相互独立、可认领的研究，在客户端支持且允许委派时并行派发，否则主会话内联处理。已完成的研究逐项记录答案并维护 map；进行中与未启动项如实汇报。主会话回传按 [`../../conventions/subagent-results.md`](../../conventions/subagent-results.md)，保留结论、证据与 ticket 链接；临时路径不替代 ticket 所需的持久研究成果。
6. 汇报 map 与研究状态，本轮结束；已有继续授权则进入下一轮，不要求新会话。

## Work through the map（用户带 map URL 或编号调用）

1. 加载 **map**：低分辨率全局视图，不逐个读 ticket body。
2. 选 ticket：用户点名就用它；未点名时由你按序拿第一个 frontier ticket。先 claim 再开工。
3. Resolve it：按需 **zoom**——只在需要时读相关或已关闭 ticket 的完整内容（含 resolution comments）；按本次任务读取 Notes 指向的资料，使用技能须遵守其调用边界与已有授权。Prototype 类 ticket 构建廉价粗糙的具体产物（outline、rough take、stub）辅助讨论，作为 asset 链接。
4. 记录 resolution：答案作为 **resolution comment** 发布，**close** issue，向 map 的 Decisions so far 追加一行 gist 与链接。
5. 维护 map：把答案已经说清的 fog 升级成新 tickets（create-then-wire），并从 **Not yet specified** 清掉每个已升级条目；发现出界的 ticket 按 Out of scope 规则处理；答案使其他 tickets 失效时更新或说明原因后关闭，保留历史。

完成维护后返回入口的“收敛并交接 Plan”，检查是否足以规划；不以 open tickets 或 frontier 为空替代完成判断。
