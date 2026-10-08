---
name: nk-retro
description: "Retrospective on agent working environment and collaboration: read what actually happened in a session, problem, or experience, then return actionable improvement candidates with evidence and applicability bounds. Delivers the summary in conversation by default; writes or revises OpenViking memory only on request and verifies the result. Human-triggered; day-to-day accumulation stays with OpenViking's automatic distillation."
argument-hint: "[可选：要复盘的会话、问题或经验主题；默认复盘当前会话]"
disable-model-invocation: true
---

用户主动请求的复盘入口。复盘对象是**Agent 工作环境与协作方式**——文件组织、检查、工具、指令有没有让工作更顺；产品代码质量归 `nk-review`，不由本技能重审。用户指定会话、问题或经验时按指定对象复盘；未指定时默认复盘当前会话。

## 读取真实材料

不凭印象复盘。读指定对象的原始记录：会话日志、执行记录、提交与 Issue 状态，以实际发生的内容为准。读不到的部分如实列为未覆盖，不虚构经过，也不把单一会话的观察外推成普遍结论。

## 找改进候选

沿这些方向找证据支持的候选；方向是提示，不是必须逐项回答的清单：

- **导航**：Agent 找对文件费不费劲？有没有隐藏的文件间依赖？一处导航指针（在 AGENTS.md 里指路）能救回多少来回。
- **自动检查**：Agent 犯的错有没有现有检查能接住？先读仓库自己的检查命令（脚本、CI 工作流）——已存在但没接线或静默失效的检查本身就是发现。没有护栏的仓库（pre-commit 和 CI 都没跑 lint/类型/测试）同样是发现，不是中立默认。
- **编码标准**：该给审查侧加规则吗？先给违规分类：机械违规（固定语法模式、禁用 API、导入形状、文件位置规则）交给确定性检查，按仓库现有护栏最便宜的方式接；真正的判断类问题（跨文件一致性、"贴合周边风格"）才写进文档规则。默认造检查，不写规则。
- **指令文件**：AGENTS.md（仓库或全局）是否过大，装着本该下沉为检查或标准的内容？有没有不影响任何行为的空转指令？
- **工具经济**：有没有昂贵得不成比例的工具调用、token 特别低效的 CLI 或 MCP？
- **信息可达性**：当时有 Agent 拿不到的关键信息吗？（dev server 日志没接出来、第三方服务只读访问缺失。）

标准类改进归审查侧承担——它上下文压力小、只看 diff（NK 里是 `nk-review`）。AGENTS.md 保持克制的导航指针，细则放 docs 或技能，不堆进常驻上下文。

## 交付

候选按严重度排列，每条给：证据（哪次会话、哪个动作）、建议动作、适用边界（在哪些项目或场景成立）。**区分建议与已执行修改**：本次顺手改掉的写明改了什么；还只是建议的明确标出，不冒充已落地。

只要求复盘时，总结直接返回对话，交付即结束。总结面向人，写作时调用 `nk-prose`。

## 按请求保存

需要持久保留时，把总结写入或修订到 OpenViking 的可写位置（用户根 `viking://~` 下的 memories，或共享的 `viking://resources/`），遵循其工具契约，不写托管只读目录；写入后读回验证。写什么、写到哪里按用户请求决定。

不依赖也不宣称能操控 OpenViking 内部的自动提炼或自进化——日常积累归它，显式复盘归本技能，两者互补；不恢复强制的 compound/solutions 流程。
