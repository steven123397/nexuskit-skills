# 当前状态

- 所在分支：`feat/skill-deep-audit`；核对基点：`b613519`（2026-09-29 本轮整理时 HEAD）。
- 工作范围：[技能深读计划](plans/2026-09-27-1525-test-skill-deep-audit-plan.md) U2。前十三项已处理；本次交付 nk-to-issue，下一项 nk-wait-what。
- 本次成果：to-issue 保持单文件与自然语言调用，支持当前会话及授权后的嵌入调用；复用证据、补缺、查重、创建/更新后返回，不修复或扩大实施范围。
- 相关边界：模型选中技能不等于外部写入授权；既有 Issue 可补充增量，历史否决核对当前条件；网络故障不自动创建平行 backlog。work / debug / close 接口、路由及共享约定同步。
- 验证：`python -B -X utf8 tests/run_checks.py` 五项通过；`python -B -X utf8 -m unittest discover -s tests -p test_*.py` 23 项通过；`git diff --check` 通过。主会话已核对调用授权、证据复用、更新/查重分支、失败出口与 Issue 范围，未执行受测技能。

## 接手依据与边界

先读 [组织范式](solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)、Plan 的逐技能顺序及联合设计，按需读 [来源与取舍](skill-sources.md)。当前技能与用户后续决定优先于历史来源描述。

- 主流程直接写执行顺序；阶段材料连续可读，条件分支返回入口，共享方法按需复用。精简不删质量要求，不以文件数或字节减少证明实际收益。
- review 常规路径保持 CE 风险编队、simplify 与独立 validator；新增 pre-merge 是 NK 的组合检查，不替代缺失的单元审查或必要验证。close 发起它但不承担产品修复。
- work 修复查证成立的单元内问题，范围外阻断交给用户；debug 修复查证成立的问题。修后针对性验证与复核，复用有效证据。
- ideate、brainstorm、plan 保留无子代理时的内联路径，不把内联称为独立核实。grill 仅由用户主动召唤；共识不等于写入、规划或实施授权。
- 所有提交经 nk-commit，current 随完整交付按需一起维护；同一交付遗漏补记按 R3 核实后 amend。handoff 仅显式调用。ideate 不自动提交或维护 current；合格需求/实施 Plan 交给 nk-commit，实施仍须授权。

## 阻断与已知缺口

无编辑阻断；用户已授权提交本轮重构，不执行本仓分支收尾。全部技能重构后才由用户统一安排独立会话沙盒实测，本会话不执行受测技能。提交钩子同步、机械检查和 Issue 关闭均不代表行为验证。

#15、#16、#18 已关闭；#13 已关闭；#20 的 init 与 to-issue 部分已处理并回写，to-issue 的“必须手动”旧前提按最新决定作废，仅余 wayfinder，仍开放。真实效果仍纳入 U3。#2 的客户端语言实验保留。历史 Issue 处置见 Plan，#21 不新增 reference 总量硬阈值，#40 保持否决。

PyYAML 检查依赖已在 tests/requirements.txt 声明并接入 CI；新环境先安装依赖。外部 quick_validate 字段限制按 AGENTS.md 处理，不改有效字段或外部安装文件。

## 下一步

下一项 nk-wait-what；#20 的 wayfinder 部分留待其节点。全部技能完成后进入 U3。

## 工作区未提交改动

本轮 to-issue、调用方、共享约定、路由、来源、检查登记、Plan 与 current 同次提交，预期无残留；不自动推送。未执行受测技能或真实落档测试。
