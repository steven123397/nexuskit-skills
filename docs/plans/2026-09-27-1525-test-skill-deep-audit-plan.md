---
title: "技能逐个深读审计与微项目实跑 - Plan"
type: test
date: 2026-09-27
plan_contract: nk-plan/v1
product_contract_source: nk-plan
topic: skill-deep-audit
---

# 技能逐个深读审计与微项目实跑

**当前位置：第 3–4 步，`nk-ideate` / `nk-brainstorm`。** 两轮静态审核已有修改，第二轮尚未提交；用户已指定跨全部技能完成 #1 方案 C 与 #3 的整体处置，再回到阅读顺序及其余 Issue；不把这些跨技能改动分散到后续节点。本轮审核及关联 Issue 与用户看完前不再提交。

**推进方式：按阅读顺序，读到哪个技能，就处理关联 Issue。** GitHub Issues 是唯一问题清单；已修改项评论说明，沙盒验证满足该项验收后直接关闭；本计划只保留阅读顺序和关联编号，不再另设问题编号、待办分类或重复验收清单。问题详情、讨论和完成状态以对应 Issue 为准。

## 阅读顺序与关联 Issue（原附录 A.1）

同一 Issue 出现在多个节点时，只处理当前技能涉及的部分，后续读到相关技能再核对；全部验收满足后才关闭。[#1](https://github.com/steven123397/nexuskit-skills/issues/1) 的共享提示词和 [#2](https://github.com/steven123397/nexuskit-skills/issues/2) 的触发证据贯穿相关技能，不另排一轮阅读。已拆分的 [#8](https://github.com/steven123397/nexuskit-skills/issues/8)、[#10](https://github.com/steven123397/nexuskit-skills/issues/10) 不再作为待办；[#9](https://github.com/steven123397/nexuskit-skills/issues/9) 已修复，仅在相关节点回归。

| 顺序 | 阅读技能 | 关联 Issue / 当前安排 |
| :-- | :-- | :-- |
| 1 | `nk-init` | 已读，显式首次接入已有外部证据；关联 [#13](https://github.com/steven123397/nexuskit-skills/issues/13)、[#20](https://github.com/steven123397/nexuskit-skills/issues/20)、[#27](https://github.com/steven123397/nexuskit-skills/issues/27) 尚待处理，不视为完成 |
| 2 | `nk-ask-ljq` | 已读；按用户决定，全部技能读完后再统一修订，关联 [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#26](https://github.com/steven123397/nexuskit-skills/issues/26)、[#28](https://github.com/steven123397/nexuskit-skills/issues/28) 与入口文案；[#32](https://github.com/steven123397/nexuskit-skills/issues/32)：入口中的提交步骤 |
| **3** | **`nk-ideate`（当前）** | **[#3](https://github.com/steven123397/nexuskit-skills/issues/3)：非软件路径重复、数量口径、证据交接与输出体量**；[#36](https://github.com/steven123397/nexuskit-skills/issues/36)：明确授权后的续作 |
| **4** | **`nk-brainstorm`（当前）** | **[#1](https://github.com/steven123397/nexuskit-skills/issues/1)、[#12](https://github.com/steven123397/nexuskit-skills/issues/12)、[#23](https://github.com/steven123397/nexuskit-skills/issues/23)、[#25](https://github.com/steven123397/nexuskit-skills/issues/25)：副本边界、读取复用与综述摘要；[#3](https://github.com/steven123397/nexuskit-skills/issues/3) 的证据交接消费端**；[#33](https://github.com/steven123397/nexuskit-skills/issues/33)、[#34](https://github.com/steven123397/nexuskit-skills/issues/34)、[#36](https://github.com/steven123397/nexuskit-skills/issues/36)：产物复用、已定决策与授权；[#37](https://github.com/steven123397/nexuskit-skills/issues/37)、[#38](https://github.com/steven123397/nexuskit-skills/issues/38)、[#39](https://github.com/steven123397/nexuskit-skills/issues/39)：视觉提问、规模分级与扫描 |
| 5 | `nk-grill` | [#29](https://github.com/steven123397/nexuskit-skills/issues/29)、[#30](https://github.com/steven123397/nexuskit-skills/issues/30)；[#34](https://github.com/steven123397/nexuskit-skills/issues/34)：一次质疑的衔接 |
| 6 | `nk-plan` | [#1](https://github.com/steven123397/nexuskit-skills/issues/1)、[#3](https://github.com/steven123397/nexuskit-skills/issues/3)、[#12](https://github.com/steven123397/nexuskit-skills/issues/12)、[#17](https://github.com/steven123397/nexuskit-skills/issues/17)、[#21](https://github.com/steven123397/nexuskit-skills/issues/21)、[#23](https://github.com/steven123397/nexuskit-skills/issues/23)、[#24](https://github.com/steven123397/nexuskit-skills/issues/24)、[#25](https://github.com/steven123397/nexuskit-skills/issues/25)；核对 [#30](https://github.com/steven123397/nexuskit-skills/issues/30) 的使用端；[#33](https://github.com/steven123397/nexuskit-skills/issues/33)、[#34](https://github.com/steven123397/nexuskit-skills/issues/34)、[#35](https://github.com/steven123397/nexuskit-skills/issues/35)、[#36](https://github.com/steven123397/nexuskit-skills/issues/36)：产物复用、已定决策、重对齐与授权 |
| 7 | `nk-work` | [#3](https://github.com/steven123397/nexuskit-skills/issues/3)：Fresh Worker、输出体量、返回行；核对项目指导持续维护 |
| 8 | `nk-commit` | 随 work 阅读；[#11](https://github.com/steven123397/nexuskit-skills/issues/11)，回归已修复的 [#9](https://github.com/steven123397/nexuskit-skills/issues/9) |
| 9 | `nk-to-issue` | [#20](https://github.com/steven123397/nexuskit-skills/issues/20)；验证 Issue 闭环及无远端降级 |
| 10 | `nk-debug` | 修复微项目预留 bug；核对已定共享规则在调试场景的适用性 |
| 11 | `nk-simplify` | [#3](https://github.com/steven123397/nexuskit-skills/issues/3)、[#30](https://github.com/steven123397/nexuskit-skills/issues/30) 的使用端；实施后精简；[#34](https://github.com/steven123397/nexuskit-skills/issues/34)：已定决策的消费端 |
| 12 | `nk-wait-what` | 真实重对齐场景；历史模拟观察仅作核实线索；[#35](https://github.com/steven123397/nexuskit-skills/issues/35)：重对齐后的产物有效性 |
| 13 | `nk-review` | [#1](https://github.com/steven123397/nexuskit-skills/issues/1)、[#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#14](https://github.com/steven123397/nexuskit-skills/issues/14)、[#22](https://github.com/steven123397/nexuskit-skills/issues/22)、[#23](https://github.com/steven123397/nexuskit-skills/issues/23)、[#31](https://github.com/steven123397/nexuskit-skills/issues/31)，回归 [#9](https://github.com/steven123397/nexuskit-skills/issues/9) |
| 14 | `nk-compound` | [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#15](https://github.com/steven123397/nexuskit-skills/issues/15) |
| 15 | `nk-close` | [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#16](https://github.com/steven123397/nexuskit-skills/issues/16)、[#18](https://github.com/steven123397/nexuskit-skills/issues/18)；先在沙盒验证收尾，主仓库分支最后收尾 |
| 16 | `nk-handoff` | [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#19](https://github.com/steven123397/nexuskit-skills/issues/19)，回归 [#9](https://github.com/steven123397/nexuskit-skills/issues/9) |
| 17 | `nk-wayfinder` | [#20](https://github.com/steven123397/nexuskit-skills/issues/20)；有远端的决策地图与 Issue 链路 |
| 18 | `nk-wizard` | 手动操作流程；补齐本技能的阅读与实际验证 |

全部读完后，回到第 2 步修订 `nk-ask-ljq`、README 与插件入口介绍，核对全部 Issue 的验收及外部证据，再做分支收尾。前面节点留下的未完成项保留在原行和对应 Issue，不另建收尾待办。

## Goal Capsule

完成 18 个技能的深读和外部实跑，在 `feat/skill-deep-audit` 分支处理完本轮遗留 Issue；重点减少逻辑赘余、规则复述、重复读取和无必要的交互。

## Product Contract

### Requirements

- R1：按上述顺序审核技能正文、按需引用和共享约定，检查职责边界、读取成本、触发与实际行为。
- R2：用仓库外的 notes CLI 沙盒承载真实开发过程；保留现有远端，无远端路径另用独立夹具验证。
- R3：小调整直接修；重要新问题记录到 Issue，核心方法变化先讨论，不用计划制造另一套问题追踪。
- R4：验证记录只保留沙盒实际执行效果及证据边界；已提交成果看 Git，问题及修复状态看 GitHub Issues，不另记审核流水账。
- R5：[#2](https://github.com/steven123397/nexuskit-skills/issues/2) 区分显式调用与自动触发，凭真实客户端证据决定语言策略；模拟不能替代证据。
- R6：本轮遗留问题按拆分后的 GitHub Issues 逐项处理；可选增强明确采纳或否决，跨技能项验收完整后关闭。
- R7：实际技能执行由用户另行安排独立会话。本对话负责修改质量、机械检查、提示词交流和只读核对反馈，不执行受测技能、不派发子代理。
- R8：减重以减少实际读取与动作负担为目标，不能只移进 references 或缩短文字；保留必要的行为边界与验证。

### 已定边界

正式支持整套安装，保留任意技能作为工作入口。`nk-init` 保持最小初始化，后续维护由共享约定及 work/close 承接。`nk-ask-ljq` 最后修订，必要时重写。用户负责语义和行为判断，本对话负责改动一致性、引用、来源说明和检查质量。

## Planning Contract

- 阅读顺序沿一次功能开发展开，外部验证随阅读推进；一般不提前展开后续节点；用户指定的 #1 全体系迁移与 #3 整体处置先完成。
- 沙盒为 `D:/codex_project/nexuskit-audit-sandbox`，独立 Git 仓库；其 `.agents` 按用户脚本同步本项目本分支的最新提交，未提交改动尚未同步。
- 验证提示词先与用户交流，保持自然开发请求，不塞入预期答案或冗长测试脚本。收到反馈或准备下一轮时，只读核对沙盒版本、改动和产物。
- [沙盒执行效果](../reviews/feat-skill-deep-audit.md) 只记录实际运行；历史疑点去重后转 Issue。当前会话持续执行本计划，不高频更新 current.md。

## Implementation Units

- **U1：沙盒准备。** 已完成骨架与远端配置；外部 nk-init 首次接入已核对。
- **U2：按阅读顺序推进。** 当前第 3–4 步。每次只讨论当前技能和关联 Issue，修改、检查后交流外部验证；只在验证记录中记录实际运行效果、可取得的读取成本及证据边界。
- **U3：完成收口。** 全部技能读完后修订引导入口，核对 Issue 验收与沙盒执行证据；必要长期结论进既有经验库，不再建立成果流水账。

## Verification Contract

- 修改技能或共享约定后运行 `python -X utf8 tests/run_checks.py`，五项全绿；改动通过 `git diff --check`。
- 机械检查不等于行为验证。真实触发、调用路径、实际读取量以外部会话和沙盒证据为准；没有证据不记为通过。
- 外部 init 证据目前仅覆盖已有项目、有远端的显式首次接入；其他路径和本轮技能修改的行为仍需验证。

## Definition of Done

18 个技能均完成阅读、真实执行与效果记录，本轮遗留 Issue 全部取得最终处置并满足验收；必要检查通过，汇总结论经用户确认。分支收尾时提炼并清理短期审计产物。
