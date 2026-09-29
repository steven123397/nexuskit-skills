# 当前状态

- 所在分支：`feat/skill-deep-audit`；核对基点：`c3bea7c`（2026-09-29 本轮整理时 HEAD）。
- 工作范围：[技能深读计划](plans/2026-09-27-1525-test-skill-deep-audit-plan.md) U2。前十二项完成；nk-close 与 review 合并前路径已获用户审阅，随本次提交入库。
- 本次成果：close 协调轻量合并前检查、遗留承接、compound 沉淀、清理与统一提交；review 新增 pre-merge，默认主会话、最多两个只读专项代理，不自动调用 simplify 或 validator。
- 共享规则：生命周期约定保留归属与责任，执行顺序归 close；发想三类状态、共享消费者、长期引用及未提交证据均有保全规则。发布日独立加载，release notes 提交后才创建已授权 tag。
- 验证：`python -B -X utf8 tests/run_checks.py` 五项通过；`python -B -X utf8 -m unittest discover -s tests -p test_*.py` 14 项通过；两个本轮入口 PyYAML 解析通过；`git diff --check` 通过。主会话已核对两条审查路径隔离、代理上限、产物矩阵与 Issue 范围，未执行受测技能。

## 接手依据与边界

先读 [组织范式](solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)、Plan 的逐技能顺序及联合设计，按需读 [来源与取舍](skill-sources.md)。当前技能与用户后续决定优先于历史来源描述。

- 主流程直接写执行顺序；阶段材料连续可读，条件分支返回入口，共享方法按需复用。精简不删质量要求，不以文件数或字节减少证明实际收益。
- review 常规路径保持 CE 风险编队、simplify 与独立 validator；新增 pre-merge 是 NK 的组合检查，不替代缺失的单元审查或必要验证。close 发起它但不承担产品修复。
- work 修复查证成立的单元内问题，范围外阻断交给用户；debug 修复查证成立的问题。修后针对性验证与复核，复用有效证据。
- ideate、brainstorm、plan 保留无子代理时的内联路径，不把内联称为独立核实。grill 仅由用户主动召唤；共识不等于写入、规划或实施授权。
- 所有提交经 nk-commit，current 随完整交付按需一起维护；同一交付遗漏补记按 R3 核实后 amend。handoff 仅显式调用。ideate 不自动提交或维护 current；合格需求/实施 Plan 交给 nk-commit，实施仍须授权。

## 阻断与已知缺口

无编辑阻断；用户已授权提交本轮重构，不执行本仓分支收尾。全部技能重构后才由用户统一安排独立会话沙盒实测，本会话不执行受测技能。提交钩子同步、机械检查和 Issue 关闭均不代表行为验证。

前轮 #15 已关闭；本轮 #16、#18 已按文本修复关闭。真实效果仍纳入 U3。#2 的客户端语言实验保留。历史 Issue 处置见 Plan，#21 不新增 reference 总量硬阈值，#40 保持否决。

PyYAML 已可用；全仓 frontmatter 检查仍为基础检查，真正解析由 #13 跟踪。外部 quick_validate 字段限制按 AGENTS.md 处理，不改有效字段或外部安装文件。

## 下一步

按用户要求保留其调整后的 nk-init 主体，只处理相关 #13、#20；#20 跨技能部分按实际范围收口。全部技能完成后进入 U3。

## 工作区未提交改动

本轮 close / review、共享规范、CONCEPTS、README、来源、检查登记、Plan 与 current 同次提交，预期无本轮残留。新增 closure、release-day、pre-merge 材料，旧 harvest 方法迁入 closure 后删除；未运行 nk-close、nk-review 或实际技能测试。
