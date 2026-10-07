---
name: nk-wait-what
description: "User-invoked pause when the agent's explanation did not land: re-explain the goal, conclusion, reasoning, and open points in plain language with project terminology. The agent restates its own explanation instead of asking the user to restate it."
disable-model-invocation: true
---

用户没跟上你刚才的解释。暂停推进，由你重新讲清楚，不要求用户重述你的观点。

用简单直接、没有歧义的话交代：我们正在解决什么问题；刚才的结论或提议是什么；依据和关键取舍是什么；还有什么待对齐。使用项目术语表（`CONCEPTS.md`，若存在）中的规范用词，解释必要的陌生概念；需要的上下文直接从当前会话取，不重新调查。

区分已确认的事实、你的推断、待用户决定的事项。讲完停下等用户回应；无法确定用户指的是哪段解释时，先做最小澄清再讲。

本轮只解释，不重开规划、不修改产物、不撤销操作。要纠正之前的实际工作时，交给负责那项工作的入口。
