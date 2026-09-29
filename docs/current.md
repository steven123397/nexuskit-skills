# 当前状态

- 所在分支：`feat/skill-deep-audit`；核对基点：`7d5342c`（2026-09-29 本轮整理时 HEAD）。
- 工作范围：[技能深读计划](plans/2026-09-27-1525-test-skill-deep-audit-plan.md) U2。前十七项已处理；本次联合交付 wayfinder、wizard、wait-what，最后一项 ask-ljq。
- 本次成果：wayfinder 保留决策地图探索，经 nk-plan 公开入口形成统一 Plan，补齐消费端承接；每轮维护后可同会话续作，不从 ticket 直接实施。三个技能均明确用户主动调用。
- 相关边界：wizard 按目的地保存值、限定范围，模板有跳过项时显示未完成；wait-what 由 Agent 重新解释。Tracker 明确认领非原子锁、完整查询与并发合并，HITL 未解决不伪造答案。
- 验证：`python -B -X utf8 tests/run_checks.py` 五项通过；Git Bash `bash -n skills/nk-wizard/assets/template.sh` 通过；`git diff --check` 通过。主会话已核对输入、交接、完成条件及失败出口；未运行交互向导或受测技能。检查器未修改，既有 23 项测试结果不冒充本轮重跑。

## 接手依据与边界

先读 [组织范式](solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)、Plan 的逐技能顺序及联合设计，按需读 [来源与取舍](skill-sources.md)。当前技能与用户后续决定优先于历史来源描述。

- 主流程直接写执行顺序；阶段材料连续可读，条件分支返回入口，共享方法按需复用。精简不删质量要求，不以文件数或字节减少证明实际收益。
- review 常规路径保持 CE 风险编队、simplify 与独立 validator；新增 pre-merge 是 NK 的组合检查，不替代缺失的单元审查或必要验证。close 发起它但不承担产品修复。
- work 修复查证成立的单元内问题，范围外阻断交给用户；debug 修复查证成立的问题。修后针对性验证与复核，复用有效证据。
- ideate、brainstorm、plan 保留无子代理时的内联路径，不把内联称为独立核实。grill 仅由用户主动召唤；共识不等于写入、规划或实施授权。
- 所有提交经 nk-commit，current 随完整交付按需一起维护；同一交付遗漏补记按 R3 核实后 amend。handoff 仅显式调用。ideate 不自动提交或维护 current；合格需求/实施 Plan 交给 nk-commit，实施仍须授权。

## 阻断与已知缺口

无编辑阻断；用户已授权提交本轮重构，不执行本仓分支收尾。全部技能重构后才由用户统一安排独立会话沙盒实测，本会话不执行受测技能。提交钩子同步、机械检查和 Issue 关闭均不代表行为验证。

#15、#16、#18、#13、#20 已关闭；#20 的 init、to-issue 与 wayfinder 文本冲突均已处理。to-issue 的“必须手动”旧前提按最新决定作废。真实效果仍纳入 U3。#2 的客户端语言实验保留。历史 Issue 处置见 Plan，#21 不新增 reference 总量硬阈值，#40 保持否决。

PyYAML 检查依赖已在 tests/requirements.txt 声明并接入 CI；新环境先安装依赖。外部 quick_validate 字段限制按 AGENTS.md 处理，不改有效字段或外部安装文件。

## 下一步

最后核对并讨论 nk-ask-ljq：参考路径去除重复提交/精简/审查暗示，呈现 wayfinder 替代路线，统一 README 与插件介绍；处理 #28 与 #32。全部技能完成后进入 U3。

## 工作区未提交改动

本轮三个手动技能、nk-plan 承接、来源、Plan 与 current 同次提交，预期无残留；不自动推送。ask-ljq 仅核对，尚未修改；未执行受测技能或真实落档测试。
