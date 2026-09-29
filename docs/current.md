# 当前状态

- 所在分支：`feat/skill-deep-audit`；核对基点：`c788c13`（2026-09-29 本轮整理时 HEAD）。
- 工作范围：[技能深读计划](plans/2026-09-27-1525-test-skill-deep-audit-plan.md) U2。十八项文本重构及入口统一已完成；本次重写 ask-ljq，下一阶段 U3 统一实测。
- 本次成果：参考 ask-matt 的工作地图写法，ask-ljq 按情境推荐入口，说明主线、wayfinder 替代探索及独立工具；区分问路与执行、用户调用与内部调度，去掉重复提交/精简/审查步骤及 R1–R6 副本。
- 配套：README 同步职责和当前进度入口；插件介绍完整列出 18 个技能；清单 JSON、技能数/集合、分发路径与市场标识检查接入既有五项检查和 CI，新增 8 项回归测试。
- 验证：`python -B -X utf8 tests/run_checks.py` 五项通过；`python -B -X utf8 -m unittest discover -s tests -p test_*.py` 31 项通过；`git diff --check` 通过。主会话对照现有技能核对路由、产物交接和授权边界；未执行受测技能或插件安装。

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

#32 已关闭。#28 实现及机械验收完成，但 GitHub GraphQL / REST 关闭请求均 TLS 超时；最后一次成功读取仍为 OPEN，待网络恢复后核实并关闭，不重复实现。

## 下一步

U3：由用户统一安排独立会话沙盒实测，先核实实际加载的技能路径及已提交版本，再按真实开发场景验证；#2 客户端语言实验一并安排。本轮不自动启动沙盒执行或分支收尾。

## 工作区未提交改动

本轮 ask-ljq、README、插件介绍、检查器与回归测试、来源、Plan 与 current 同次提交，预期无残留；不自动推送。
