---
name: nk-wait-what
description: "User-invoked pause asking the agent to re-explain its last unclear message with context and plain project terminology. 仅用户主动调用：没跟上、请 Agent 重新解释、wait what。"
disable-model-invocation: true
---

# /nk-wait-what

用户没跟上你刚才的解释。暂停推进，由你重新说清楚，不要求用户重述你的观点。

用简单直接、没有歧义的话交代：我们正在解决什么；刚才的结论或提议是什么；依据和关键取舍是什么；还有什么需要对齐。复用已有上下文，使用 `CONCEPTS.md`（若存在）中的规范术语，并解释必要的陌生概念。

区分已确认事实、你的推断和待用户决定的事项。解释后停下等用户回应；仅在无法确定所指内容时做最小澄清。不自动重开规划、修改产物、撤销操作或调用其他技能；后续明确纠正交给负责该工作的流程承接。
