# context.md — 上游通用术语统一译法

重写技能时，Matt 原文反复出现的通用术语按本表翻译，保证各技能前后一致（`frontier` 在 nk-grill 与 nk-wayfinder 中同词同译即为例）。已定译法不因单份技能的措辞偏好更换；确需调整，先改本表再统一改技能。执行技能的 Agent 不需要读本文件。

## 跨技能核心术语

| 原文 | 译法 | Matt 出处 |
| --- | --- | --- |
| design tree | 设计树 | grilling；grill-me、README 复用 |
| frontier | 前沿 | grilling、wayfinder、implement-spec、to-tickets、ask-matt |
| rounds | 轮次 | grilling |
| recommended answer | 推荐答案 | grilling |
| shared understanding | 共同理解 | grilling |
| sub-agent / subagent | 子代理 | grilling、wayfinder、implement-spec、code-review、chief-of-staff |
| implementer / exploration / merger subagents | 实施子代理 / 探索子代理 / 合并子代理 | implement-spec |
| destination | 目的地 | wayfinder、ask-matt |
| fog / fog of war | 未成形的问题（特殊决定，见下） | wayfinder |
| decision tickets | 决策 tickets | wayfinder、ask-matt |
| claim | 认领 | wayfinder |
| blocked / unblocked | 被阻塞 / 依赖已满足 | wayfinder、implement-spec、to-tickets |
| tracer bullet / vertical slice | 纵向切片 | to-tickets（STE-5 定稿，不译“曳光弹”） |
| horizontal slice | 横向切片 | to-tickets |
| wide refactor | 宽范围重构 | to-tickets |
| expand–contract | 扩展–收缩 | to-tickets |
| prefactor / prefactoring | 预重构 | to-tickets |
| blast radius | 波及面 | to-tickets |
| task graph | 任务图 | implement-spec、ask-matt |
| context pointer | 上下文指针 | implement-spec、chief-of-staff |
| integration branch | 集成分支 | implement-spec |
| session | 会话 | 各技能通用 |
| module | 模块 | codebase-design（nk-codecraft） |
| interface | 接口（含调用方须知的一切，不限于类型签名） | codebase-design |
| implementation / adapter | 实现 / 适配器 | codebase-design |
| depth / deep module | 深度 / 深模块 | codebase-design |
| seam | 接缝 | codebase-design、tdd；to-spec 的“测试接口”即测试所选的接缝 |
| leverage / locality | 杠杆 / 局部性 | codebase-design |
| deletion test | 删除测试 | codebase-design |

## map 正文章节（nk-wayfinder）

| 原文 | 译法 |
| --- | --- |
| Destination | 目的地 |
| Notes | 补充说明 |
| Decisions so far | 已定决策 |
| Not yet specified | 未成形 |
| Out of scope | 不在范围内 |

## spec 模板章节（nk-to-spec）

| 原文 | 译法 |
| --- | --- |
| Problem Statement | 问题 |
| Solution | 方案 |
| User Stories | 使用场景与预期行为（NK 整体替换，非翻译） |
| Implementation Decisions | 实现决定 |
| Testing Decisions | 测试决定 |
| Out of Scope | 不在范围内 |
| Further Notes | 补充说明 |

## ticket 模板章节（nk-to-tickets，STE-5 定稿）

| 原文 | 译法 |
| --- | --- |
| Parent | 所属 spec |
| What to build | 交付什么 |
| Acceptance criteria | 验收条件 |
| Blocked by | 依赖（Linear 原生阻塞关系承载，正文不重复） |

## 固定短语

| 原文 | 译法 |
| --- | --- |
| chart the map / work through the map | 建立 map / 处理 map |
| plan, don't do | 规划而非执行 |
| red → green（red before green） | 先见失败再实现 |
| refer by name | 用名称引用 |
| index, not a store | 索引，不存正文 |

## 保留英文不译

spec、ticket、issue、PR、map（wayfinder 的 `wayfinder:map` 索引 issue）、wayfinder 四种 ticket 类型 Research / Prototype / Grilling / Task（与 `wayfinder:*` 标签及技能入口 nk-research、nk-prototype、nk-grill 对齐；Task 由 Agent 直接处理）、HITL（human in the loop）、AFK（away from keyboard）。正文首次出现时可加中文括注，之后直接用英文。

## 已定的特殊决定

- **map 保留英文**：指 Linear 中标记 `wayfinder:map` 的索引 issue，与 spec、ticket、issue 同属跟踪器产物名；目的地、前沿仍译中文。
- **fog of war 不直译比喻**：迷雾一类词在中文里生硬。按概念直述为**未成形的问题**——能感觉到、但问题本身还没长成形、暂时无法准确表述的工作；判断标准是“现在能不能把问题说清楚”，与 ticket（说得清、还没答）相对。
- **前沿**在 nk-grill（前提已确定、现在就能问的决策集合）与 nk-wayfinder（依赖已满足且未被接手的 open tickets）中同词同译；后续重写 implement-spec / to-tickets（nk-odyssey、nk-to-tickets）时沿用。
- ready-for-agent 标签体系不沿用，NK 用 Linear 项目已有标签与状态。
- User Stories 换成“使用场景与预期行为”是模板替换，不按原文翻译。

## 参考译文

- [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN)：Matt skills 的社区中文直译版（4.6k stars，按内容刷新同步上游，译文与 NK 采用的 `6fd9479` 期一致），本地克隆在 `D:/codex_project/upstreams/mattpocock-skills-zh-CN/`。其策略是保留英文术语的混排直译——fog、map、destination、frontier、design tree 全部不译——比 NK 的全中文本地化保守，只能作句子级参考，不作译法依据。可借鉴点：fog-or-ticket 测试译作“现在能不能把问题说清楚”，与本表判断标准一致；graduates 译作“升级”；共同理解、推荐答案与 nk-grill 既有译法相同。

## CE 派生术语（nk-review）

| 原文 | 译法 | 出处 |
| --- | --- | --- |
| reviewer | 保留英文 | ce-code-review（nk-review） |
| finding | 发现 | ce-code-review（nk-review） |
| baseline | 基线 | ce-code-review（nk-review） |
| intent / intent summary | 意图摘要 | ce-code-review（nk-review） |

## 待定（重写对应技能时定稿）

- writing-for-agents 的 leading word（暂记：主导词）。
- nk-debug 等 CE 派生技能的其余通用术语，重写时继续并入上表。
