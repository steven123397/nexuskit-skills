---
name: nk-handoff
description: "Only when explicitly invoked by the user, save an unfinished work checkpoint with current progress, evidence, blockers, and next steps in docs/current.md through nk-commit. Not an automatic end-of-session step or a follow-up required after normal delivery commits."
disable-model-invocation: true
---

# /nk-handoff

本技能保存尚未形成交付的现场，由 nk-commit 处理入库。交接让下一位能定位现状、遗留与下一步，不复述整段对话。

## 1. 核对现场与已有记录

先读已有 `docs/current.md`（若有），结合本会话的交付、用户决定和验证证据核对现状。检查当前分支、HEAD 及 `git status --short --untracked-files=all`；无初始提交时如实记录，不虚构基点。必要时按已知提交查 Git 记录，不扫描完整历史，不以有无 U-ID 判断是否属于本会话。

区分本次遗留与外来改动，覆盖代码、配置、规划、审查及知识工件；不确定归属时保持原样并说明。用户指定的交接关注点优先，但不能掩盖已知阻断。复用已有验证证据，不因交接重跑测试。

## 2. 更新并检查交接文件

读取 [current.md 格式契约](../conventions/current-md.md)，按其中字段更新目标仓库的单例文件；规则已完整在上下文中且未变时复用。保留仍有效的阻断、决定与遗留，删除有事实依据判定失效的内容，不因本会话未提及而丢弃。

检查事实与证据是否对应、引用路径是否有效、下一步是否可定位；未确认的状态明确标注。核对提交后仍将留在工作区的内容，避免将本次即将入库的文档误记为待接手的半成品。检查 `AGENTS.md` 或等价入口是否指向 `docs/current.md`，缺失时只补必要指引，不顺带初始化其他知识目录。

## 3. 委托提交

将交接场景、明确文件范围、已有证据，以及本会话相关交付的归属和已知发布情况交给 [nk-commit](../nk-commit/SKILL.md)。提交方式与时机由其决定，本技能不重复 amend 算法。

范围包括交接文件、必要的入口指引，以及归属明确、符合提交条件且约定随本次交接入库的文档工件，例如规划、术语、审查记录和知识沉淀。未完成的产品改动与外来文件保持原样；不为让工作区干净而一并提交。

## 4. 汇报并结束

简述交付、阻断或待确认事项、遗留文件及下一步指针；采用 nk-commit 返回的真实提交结果。文件已更新但提交失败时，明确“已写入，未入库”及原因，不声称交接全部完成；无新增变化则如实说明。

最终提交哈希只在汇报中给出，不回写 current 追逐新的 HEAD。结束本次调用，不自动开始下一单元。
