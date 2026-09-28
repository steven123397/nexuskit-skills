---
title: "技能逐个重构、深读审计与微项目实跑 - Plan"
type: test
date: 2026-09-27
plan_contract: nk-plan/v1
product_contract_source: nk-plan
topic: skill-deep-audit
---

# 技能逐个重构、深读审计与微项目实跑

**当前位置：U2，`nk-work` 试点与 `nk-commit` 首轮重构已提交；`nk-commit` 的 current 归属调整和 `nk-handoff` 简化已获用户确认，本次一并交付。下一项为 `nk-debug`。** 2026-09-28 用户确认按依赖关系调整重写顺序；`nk-work` 及配套范式已提交为 `1dc57bd`，机械检查通过，真实客户端执行效果仍待验证。此前的深读与跨技能修改继续保留，不把它们视为其他技能已经完成重构。

**推进方式：逐技能深读、重构，并处理关联 Issue。** GitHub Issues 是唯一问题清单；本计划记录重构顺序与任务范围，不另设问题编号或复制 Issue 验收要求。问题详情、讨论和完成状态以对应 Issue 为准；只有取得所需证据并满足验收后才关闭。

## 重构顺序与关联 Issue

先整理 work 直接依赖的提交与交接，再处理调试和质量保障；随后从 Plan 消费契约向需求与发想上游整理，最后处理沉淀、收尾与辅助入口。先按此顺序完成全部技能重写及机械检查，再统一进入沙盒实际测试；沙盒测试按真实开发场景的依赖安排，不要求沿用重构顺序。

同一 Issue 出现在多个节点时，处理当前技能涉及的部分，全部验收满足后才关闭。既有 #1 方案 C 与 #3 整体处置继续按原范围核对，不因重排遗漏跨技能消费端；#2 的触发证据贯穿相关技能。已拆分的 #8、#10 不再作为待办；#9 在相关节点回归。下表保留原有关联，不代表本次重新核实了远端 Issue 状态。

| 顺序 | 技能 | 重构重点 | 关联 Issue / 既有安排 |
| :-- | :-- | :-- | :-- |
| 1 | `nk-work` | 试点重构基本完成（1dc57bd）；保留单单元边界，真实执行效果待验证 | [#3](https://github.com/steven123397/nexuskit-skills/issues/3)：Fresh Worker、输出体量、返回行；核对项目指导持续维护 |
| 2 | `nk-commit` | 首轮已提交；current 随提交维护及 R1–R6 调整已确认 | [#11](https://github.com/steven123397/nexuskit-skills/issues/11)，回归已修复的 [#9](https://github.com/steven123397/nexuskit-skills/issues/9) |
| 3 | `nk-handoff` | 四步流程及显式调用已确认；字段由 current 契约持有 | [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#19](https://github.com/steven123397/nexuskit-skills/issues/19)，回归 [#9](https://github.com/steven123397/nexuskit-skills/issues/9) |
| 4 | `nk-debug` | 保持因果调查与修复关卡，处理对 nk-work 私有 reference 的依赖 | 修复微项目预留 bug；核对已定共享规则在调试场景的适用性 |
| 5 | `nk-simplify` | 集中行为保持与精简方法，明确角色材料的加载条件和结果回收 | [#3](https://github.com/steven123397/nexuskit-skills/issues/3)、[#30](https://github.com/steven123397/nexuskit-skills/issues/30) 的使用端；实施后精简；[#34](https://github.com/steven123397/nexuskit-skills/issues/34)：已定决策的消费端 |
| 6 | `nk-review` | 整理审查范围、角色选择、输出及修复接口；到此讨论审查触发安排 | [#1](https://github.com/steven123397/nexuskit-skills/issues/1)、[#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#14](https://github.com/steven123397/nexuskit-skills/issues/14)、[#22](https://github.com/steven123397/nexuskit-skills/issues/22)、[#23](https://github.com/steven123397/nexuskit-skills/issues/23)、[#31](https://github.com/steven123397/nexuskit-skills/issues/31)，回归 [#9](https://github.com/steven123397/nexuskit-skills/issues/9) |
| 7 | `nk-plan` | 按规划阶段组织材料，明确 Plan 生产契约及 work 所需字段 | [#1](https://github.com/steven123397/nexuskit-skills/issues/1)、[#3](https://github.com/steven123397/nexuskit-skills/issues/3)、[#12](https://github.com/steven123397/nexuskit-skills/issues/12)、[#17](https://github.com/steven123397/nexuskit-skills/issues/17)、[#21](https://github.com/steven123397/nexuskit-skills/issues/21)、[#23](https://github.com/steven123397/nexuskit-skills/issues/23)、[#24](https://github.com/steven123397/nexuskit-skills/issues/24)、[#25](https://github.com/steven123397/nexuskit-skills/issues/25)；核对 [#30](https://github.com/steven123397/nexuskit-skills/issues/30) 的使用端；[#33](https://github.com/steven123397/nexuskit-skills/issues/33)、[#34](https://github.com/steven123397/nexuskit-skills/issues/34)、[#35](https://github.com/steven123397/nexuskit-skills/issues/35)、[#36](https://github.com/steven123397/nexuskit-skills/issues/36)：产物复用、已定决策、重对齐与授权 |
| 8 | `nk-brainstorm` | 整理需求对齐主流程、条件研究与规划交接，保留已有有效修改 | [#1](https://github.com/steven123397/nexuskit-skills/issues/1)、[#12](https://github.com/steven123397/nexuskit-skills/issues/12)、[#23](https://github.com/steven123397/nexuskit-skills/issues/23)、[#25](https://github.com/steven123397/nexuskit-skills/issues/25)：副本边界、读取复用与综述摘要；[#3](https://github.com/steven123397/nexuskit-skills/issues/3) 的证据交接消费端；[#33](https://github.com/steven123397/nexuskit-skills/issues/33)、[#34](https://github.com/steven123397/nexuskit-skills/issues/34)、[#36](https://github.com/steven123397/nexuskit-skills/issues/36)：产物复用、已定决策与授权；[#37](https://github.com/steven123397/nexuskit-skills/issues/37)、[#38](https://github.com/steven123397/nexuskit-skills/issues/38)、[#39](https://github.com/steven123397/nexuskit-skills/issues/39)：视觉提问、规模分级与扫描 |
| 9 | `nk-grill` | 明确质疑范围、停止条件与返回原流程的接口 | [#29](https://github.com/steven123397/nexuskit-skills/issues/29)、[#30](https://github.com/steven123397/nexuskit-skills/issues/30)；[#34](https://github.com/steven123397/nexuskit-skills/issues/34)：一次质疑的衔接 |
| 10 | `nk-ideate` | 整理不同发想路径、研究材料及证据交接，保留已有有效修改 | [#3](https://github.com/steven123397/nexuskit-skills/issues/3)：非软件路径重复、数量口径、证据交接与输出体量；[#36](https://github.com/steven123397/nexuskit-skills/issues/36)：明确授权后的续作 |
| 11 | `nk-compound` | 区分沉淀与审计路径，收拢知识产物规则及提交边界 | [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#15](https://github.com/steven123397/nexuskit-skills/issues/15) |
| 12 | `nk-close` | 按收尾场景组织验收、知识维护与发布分支，复用已整理的公开入口 | [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#16](https://github.com/steven123397/nexuskit-skills/issues/16)、[#18](https://github.com/steven123397/nexuskit-skills/issues/18)；先在沙盒验证收尾，主仓库分支最后收尾 |
| 13 | `nk-init` | 保持最小初始化，核对首次接入与后续维护的职责边界 | 已读，显式首次接入已有外部证据；关联 [#13](https://github.com/steven123397/nexuskit-skills/issues/13)、[#20](https://github.com/steven123397/nexuskit-skills/issues/20)、[#27](https://github.com/steven123397/nexuskit-skills/issues/27) 尚待处理，不视为完成 |
| 14 | `nk-to-issue` | 整理 Issue 写入、生命周期及无远端降级路径 | [#20](https://github.com/steven123397/nexuskit-skills/issues/20)；验证 Issue 闭环及无远端降级 |
| 15 | `nk-wait-what` | 整理重对齐步骤、已有产物有效性及后续返回条件 | 真实重对齐场景；历史模拟观察仅作核实线索；[#35](https://github.com/steven123397/nexuskit-skills/issues/35)：重对齐后的产物有效性 |
| 16 | `nk-wayfinder` | 整理决策地图、Issue 关联与按需材料 | [#20](https://github.com/steven123397/nexuskit-skills/issues/20)；有远端的决策地图与 Issue 链路 |
| 17 | `nk-wizard` | 整理手动操作步骤、观察证据与人机交接 | 手动操作流程；补齐本技能的阅读与实际验证 |
| 18 | `nk-ask-ljq` | 最后统一入口引导，并同步 README 与插件介绍 | 已读；按用户决定，其余技能整理完后再统一修订，关联 [#11](https://github.com/steven123397/nexuskit-skills/issues/11)、[#26](https://github.com/steven123397/nexuskit-skills/issues/26)、[#28](https://github.com/steven123397/nexuskit-skills/issues/28) 与入口文案；[#32](https://github.com/steven123397/nexuskit-skills/issues/32)：入口中的提交步骤 |

第 18 项完成入口统一后，进入 U3 统一开展沙盒实际测试，核对全部 Issue 验收与外部证据，再做主仓库分支收尾。前面节点的未完成项保留在原行和对应 Issue，不另建收尾待办。

## 逐技能重构任务

以 [nk-work 技能组织范式](../solutions/architecture-decisions/2026-09-28-skill-execution-locality.md) 为依据，每次只重构当前技能，必要时同步其共享维护源与直接消费端：

1. **盘点现状**：读取入口及实际执行依赖，列出输入、主要动作、条件分支、产物、停止条件和必须保留的质量要求。
2. **按使用时机重组**：入口安排流程与加载条件；同一阶段连续需要的方法放在完整材料中；条件材料读完返回主流程，不递归拼装必需规则。不照搬 nk-work 的文件数量，不为拆分而拆分。
3. **核对共享与接口**：短且稳定的必需底线可采用受控副本；完整共享方法按需读取；跨技能通过公开入口协作，写清必要输入与返回或结束边界。格式消费端只保留所需内容，修改格式时核对生产方与消费方。
4. **保留行为与质量**：逐项对照重构前后的动作和约束，避免把具体方法压成口号。非代码验证保持现有力度，不额外增加通用检查清单；不借重构擅自改动已定需求或执行策略。
5. **同步与验证**：更新来源说明、失效引用和受影响的检查配置，运行机械检查后与用户核对改动；全部技能重写完成后，真实技能执行由用户统一安排独立会话。提交按已验证的交付变化划分，不因重构顺序调整批量改写后续技能。

“重构基本完成”表示本技能组织方式已调整、必要要求已核对、机械检查通过；“行为验收完成”还需真实执行证据。二者分别判断，机械检查不自动关闭需要实跑证据的 Issue。

## Goal Capsule

完成 18 个技能的深读、按新范式重构和外部实跑，在 `feat/skill-deep-audit` 分支处理完本轮遗留 Issue；重点减少逻辑赘余、规则复述、重复读取和无必要的交互。

## Product Contract

### Requirements

- R1：按上述顺序深读并重构技能正文、按需引用和共享约定，检查职责边界、读取成本、触发与实际行为。
- R2：全部技能重写完成后，统一用仓库外的 notes CLI 沙盒承载真实开发测试；保留现有远端，无远端路径另用独立夹具验证。
- R3：小调整直接修；重要新问题记录到 Issue，核心方法变化先讨论，不用计划制造另一套问题追踪。
- R4：验证记录只保留沙盒实际执行效果及证据边界；已提交成果看 Git，问题及修复状态看 GitHub Issues，不另记审核流水账。
- R5：[#2](https://github.com/steven123397/nexuskit-skills/issues/2) 区分显式调用与自动触发，凭真实客户端证据决定语言策略；模拟不能替代证据。
- R6：本轮遗留问题按拆分后的 GitHub Issues 逐项处理；可选增强明确采纳或否决，跨技能项验收完整后关闭。
- R7：实际技能执行由用户另行安排独立会话。本对话负责修改质量、机械检查、提示词交流和只读核对反馈，不执行受测技能；可按任务独立性和客户端能力选择是否委派子代理，主会话负责整合与核验。
- R8：减重以减少实际读取与动作负担为目标，不能只移进 references 或缩短文字；保留必要的行为边界与验证。

### 已定边界

正式支持整套安装，保留任意技能作为工作入口。`nk-init` 保持最小初始化，后续维护由共享约定及 work/close 承接。`nk-ask-ljq` 最后修订，必要时重写。用户负责语义和行为判断，本对话负责改动一致性、引用、来源说明和检查质量。用户已确定先完成全部重写，再统一进入沙盒实际测试；重写阶段不逐技能安排实跑。

## Planning Contract

- 重构顺序按上表的技能依赖关系推进；每次聚焦一个技能，跨技能规则变动同步直接消费端。全部重写完成后才统一安排外部验证，按真实开发场景组织，不把重构顺序强加到实跑流程。
- 沙盒为 `D:/codex_project/nexuskit-audit-sandbox`，独立 Git 仓库；其 `.agents` 按用户脚本同步本项目本分支的最新提交，未提交改动尚未同步。
- 验证提示词先与用户交流，保持自然开发请求，不塞入预期答案或冗长测试脚本。收到反馈或准备下一轮时，只读核对沙盒版本、改动和产物。
- [沙盒执行效果](../reviews/feat-skill-deep-audit.md) 只记录实际运行；历史疑点去重后转 Issue。current 随 nk-commit 的交付提交按需更新，不作实时流水账。

## Implementation Units

- **U1：沙盒准备。** 已完成骨架与远端配置；外部 nk-init 首次接入已核对。
- **U2：逐技能重构与机械检查。** 按上表及“逐技能重构任务”推进，下一项为 nk-debug。每次核对当前技能和关联 Issue，修改后完成内容核对、来源同步与机械检查；不安排逐技能沙盒实跑。全部技能重写及入口统一完成后进入 U3。
- **U3：统一沙盒实测与收口。** 确认沙盒加载全部重写后的已提交版本，由用户安排独立会话按真实开发场景测试；核对触发、读取路径、产物、验证证据和关联 Issue 验收。实测发现的问题修复后重跑受影响场景，满足验收再关闭 Issue。全部通过后汇总用户确认并收尾；必要长期结论进既有经验库，不再建立成果流水账。

## Verification Contract

- 重构后核对主流程、条件加载、公开接口和质量要求的保留情况；来源与直接消费端同步，不以文件数或字节减少量判定完成。
- 修改技能或共享约定后运行 `python -X utf8 tests/run_checks.py`，五项全绿；改动通过 `git diff --check`。
- 统一实测的进入条件：18 个技能重写及入口统一完成，相关改动已提交，机械检查通过，并核对沙盒实际加载版本；快照同步本身不算实际测试。
- 机械检查不等于行为验证。真实触发、调用路径、实际读取量以外部会话和沙盒证据为准；没有证据不记为通过。
- 外部 init 证据目前仅覆盖已有项目、有远端的显式首次接入；其他路径和本轮技能修改的行为仍需验证。

## Definition of Done

18 个技能均完成深读、按新范式重构、真实执行与效果记录，本轮遗留 Issue 全部取得最终处置并满足验收；必要检查通过，汇总结论经用户确认。分支收尾时提炼并清理短期审计产物。

2026-09-28 决策调整：current 的维护归 nk-commit，每次提交前核对并按需与交付同次入库；nk-handoff 仅限用户显式调用，不根据自然语言或技能结束自动触发。Plan 达到交付标准后提交，移除依赖交接入库的旧限制；ideate 只写入记录，用户需要时自行调用 nk-commit。
