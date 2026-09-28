# NexusKit 体系架构立项与设计构想 (Ideation RFC)

> **Document Version:** 2.1.0
> **Date:** 2026-09-28（初版立项：2026-09-25）
> **Status:** Approved — 技能迭代与逐项审查中
> **Author:** steven123397（设计评审：Claude）

v2.0 相对 v1.0 的主要变化：从"固定流水线"改为"按场景取用的工具箱"；Issue 的职责收窄到跨 plan 的事务；新增产物生命周期、`current.md` 入口约定、提交节奏规则、术语维护时机；ADR 并入 `solutions/`；新增实施方法一章。

v2.1 将 nk-work 的组织方式纳入 D12，更新单元边界与子代理提交规则，纠正规则下沉、打包、加载方式等过时表述。本文保留立项背景与历史阶段；当前进度以 [current.md](../current.md) 为入口，执行细则以技能和共享约定为准，设计理由见 [nk-work 范式决定](../solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)。review 的触发安排留待审查该技能时决定。

---

## 一、背景

实战验证基地：paper-30min（私有仓库，先后完整运行过 Matt 体系与 CE 体系）。

参考源：
* **Matt Pocock Skills**：[mattpocock/skills](https://github.com/mattpocock/skills)（2026-08 本地备份）
* **Compound Engineering (CE)**：[EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)（本地安装）
* **Ponytail**（2026-09-28 补充）：本地 `D:/codex_project/upstreams/ponytail`，快照 `e3ba2aa`；吸收“更少自维护代码满足同一需求”的理念，来源与未采纳部分见 [skill-sources.md](../skill-sources.md)。

NexusKit 是一套**个人体系**：用户画像是个人项目、同时使用多种 Agent（Claude Code / Codex / Antigravity 等）、不强制走 PR、中文协作。参考源是素材库，不要求与上游保持同步。

---

## 二、两套体系的得失（基于 paper-30min 实证）

以下是立项时对本地使用版本的观察，保留用于解释取舍；不作为上游当前版本的能力清单。

### CE

**优势**
* `ideate → brainstorm → plan` 层次清楚，抓大放小，不纠缠细节。
* `ce-compound` 把非显而易见的因果沉淀进 `solutions/`，解决跨会话失忆。
* 技能文本打磨得细，边界情况考虑周全（代价是很重：`ce-plan` 连同 references 约 3500 行）。

**问题**
1. **主会话上下文膨胀**：`ce-work` 倾向由一个主对话承包整份 plan，上下文飙升后注意力漂移。
2. **产物无生命周期**：plan、review 写成本地 Markdown 后没有归宿（paper-30min 一天内产生 5 份 `docs/reviews/`）。
3. **术语表只在 compound 时生长**：`ce-brainstorm` 只把 `CONCEPTS.md` 当冲突检查读，从不写；新术语恰恰诞生在 brainstorm/plan 阶段。paper-30min 迁移到 CE（`56dc422`）后 `CONCEPTS.md` 再无改动。
4. **无提交节奏约束**：常见"代码提交后再为 `current.md` 小改单独提交一次"（见 `54849fd`、`0e05c8d`、`9f32bdf`、`894f51a`、`5df3454`）。

### Matt

**优势**
* 一个任务对应一个干净的新会话，上下文始终在最佳区间。
* 用 GitHub Issues 管理任务与阻塞关系，状态更新不产生 commit。
* `wayfinder`：面对超大未知目标时用探针逐步驱散迷雾。
* `domain-modeling`：术语一经敲定立即写入术语表。
* `tdd`：测试先行的纪律。

**问题**
1. **`grill` 盘问繁琐**：把大量可推断的细节抛回给人，违背分担认知负荷的初衷。
2. **同样存在产物堆积**：Matt 时期留下 11 份 `docs/draft/*-walkthrough.md`、大量 `docs/background/` 与每份仅 7 行的 ADR，最终在 `56dc422` 统一清理。**堆积是生命周期问题，不是哪套体系独有的问题。**
3. **缺少跨会话的长期知识沉淀**。

---

## 三、设计决定

| # | 决定 | 要点 |
| :-- | :-- | :-- |
| D1 | **工具箱，不是流水线** | 正式支持整套安装，任意技能都可作为工作入口；不表示单技能可独立安装。README 按场景路由，不规定每个版本必经的技能链。 |
| D2 | **`docs/current.md` 是跨会话入口** | 新会话从这里进入。只记当前能力、验证结果、阻断项、下一步、所在分支；不记操作流水。 |
| D3 | **所有产物都有生命周期** | 每类产物诞生时就确定终点（见第四章）。清理挂在"版本收尾"上，不挂在 PR 上；PR 可选。 |
| D4 | **plan 与审查记录"活时在本地，死后从 main 消失"** | 执行期留在版本分支、随代码一起修改提交；收尾时提炼长期价值后删除，git 历史保留原文。 |
| D5 | **Issue 负责跨 plan 的事务** | 待办、疑难缺陷、推迟的工作、wayfinder 探针。plan 内部的实施单元不拆 Issue，靠 plan + `current.md` 接力。不设 plan→Issue 的转换技能（长期挂起由 `nk-close` 覆盖，并行认领按 YAGNI 不建）；Issue 格式由 `conventions/issue-writing.md` 统一约定，开发中冒出的 bug/需求由 `nk-to-issue` 核实分析后落档。 |
| D6 | **不强制盘问；术语即时写入** | 以 CE 的 ideate/brainstorm 为主体。Agent 对可逆、局部、有惯例的事自行决定；范围变化、不可逆、数据/API 契约等分歧按共享约定确认。`nk-grill` 已作为用户主动选择的压力测试工具补入，不是必经环节。术语在 brainstorm/plan 中敲定即写，格式由 `concepts-vocabulary.md` 持有。 |
| D7 | **ADR 并入 `solutions/`** | 取消 `docs/adr/`，"决策"作为 solution 的一种类型。入选门槛沿用 Matt 三条：难以撤回、无背景会困惑、确有取舍。D4 删除 plan 后，决策理由需要去处，这正是收尾时提炼的主要内容。 |
| D8 | **自主体系，审慎派生** | 以 CE/Matt 等材料为起点，按自身场景改写；吸收 Ponytail 的减少自维护代码理念，不照搬其运行机制。来源与取舍集中记录于 `docs/skill-sources.md`，不维护上游同步机制。删减原则见第七章。 |
| D9 | **提交节奏规则** | 见第五章。 |
| D10 | **任务粒度按实现内容切** | 以明确目标、依赖、文件范围和可验证的完成条件切分单元；不以 Token 数或模型估计的上下文余量决定执行边界。一次 nk-work 调用只完成一个已确认单元，完成或形成不可自行解除的阻断后交接，不自动顺延。 |
| D11 | **不为子代理建通用编排层** | nk-work 中，客户端支持且指令允许时，由 Agent 自主决定是否委派；不以用户点名为前提，也不强制派发。子代理不提交，主会话核对、整合并亲自验证，按完整交付变化提交。不同技能可保留必要的结果字段或格式；不为所有技能增加统一调度脚本或 return-to-caller 返回协议。 |
| D12 | **执行规则就近读取，共享规则单源维护** | 以 nk-work 为范式：入口组织主流程与短底线，完整执行方法和条件分支按使用时机拆分，本地执行 reference 优先保持叶子结构。短底线允许受控复制并检查一致性；理由与来源留在维护者文档。公开技能入口仍可协作，整套安装不变。详见 [设计决定](../solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)。 |

---

## 四、产物与生命周期

| 产物 | 位置 | 生命周期 |
| :-- | :-- | :-- |
| Plan（目标、范围、关键决策、实施单元、变更记录） | 版本分支 `docs/plans/` | 执行中直接修改，与代码同一提交；版本收尾时提炼后删除 |
| 审查记录（待修清单、收敛结论） | 版本分支 `docs/reviews/` | 同上；遗留项转 Issue 或 `current.md` 阻断项 |
| 进度、阻断项、下一步 | `docs/current.md` | 常驻，在交接点覆盖更新 |
| 待办、疑难缺陷、推迟项、探针 | GitHub Issues（无远端时退化为 `docs/backlog.md`） | 关闭即结束 |
| 踩坑因果、决策理由 | `docs/solutions/` | 长期保留；由 `nk-compound` 审计模式维护过期条目 |
| 领域术语 | `CONCEPTS.md` | 长期保留；由 `nk-compound` 审计模式维护 |
| 项目特有流程（分支、发布、签名等） | 项目自己的工作流文档，由 `AGENTS.md` 指向 | 项目自行维护；技能读取、不内置 |
| PR 描述 | 可选 | 有 PR 时收尾步骤写摘要，没有就跳过 |

**执行中新发现的分流规则**
* 影响当前 plan 的范围或做法 → 改 plan，末尾加一行变更记录，随代码提交。
* 与当前 plan 无关的需求或疑难缺陷 → 开 Issue。
* 小缺陷 → 随当前实施单元修复并验证。

**版本收尾**（`nk-close`）依次完成：遗留项转移 → 提炼 solutions/术语 → 删除 plans 与 reviews → 更新 `current.md` 为合并后仍准确的状态 → 单个收尾提交 →（可选）写 PR 摘要。

---

## 五、提交节奏规则

提交以“一个经过验证的变化”为单位，实现、测试和配套文档一并交付。进度由提交及其证据体现，不为标记完成而修改 Plan；`current.md` 不作实时进度日志。

R1–R6 的完整规则、amend 条件和纯文档提交例外及提交操作统一由 [nk-commit](../../skills/nk-commit/SKILL.md) 持有。此处不再维护另一份节奏规则；旧版“纯文档提交只允许两个时刻”不能覆盖现有规划与知识库维护等具体条件。

通用执行底线：
* 未运行的测试或走查不记为通过。
* 子代理返回结果不触发提交。主会话核对并整合实际改动，验证待交付状态后，按交付变化提交；多个代理可共同贡献一个提交。

---

## 六、技能清单

“阶段”保留初始建设时的归属，不表示这些技能已通过真实执行验收；当前审查安排从 [current.md](../current.md) 进入。

| 技能 | 用途 | 主要来源 | 阶段 |
| :-- | :-- | :-- | :-- |
| `nk-work` | 认领一个实施单元或 Issue，测试先行实现、验证、按 R1 提交 | CE `ce-work` + Matt `tdd`/`implement` | P1 |
| `nk-commit` | 提交信息 + 提交节奏规则的唯一持有者 | CE `ce-commit` | P1 |
| `nk-handoff` | 会话结束：更新 `current.md`，按 R4 提交；接手时读取 | CE `ce-handoff` + Matt `handoff` | P1 |
| `nk-brainstorm` | 澄清要做什么、范围与边界；术语即时写入 | CE `ce-brainstorm` + Matt `domain-modeling` | P2 |
| `nk-grill` | 用户主动选择的计划、决策或想法压力测试 | Matt `grilling`（具体取舍见来源记录） | 后续补入 |
| `nk-plan` | 技术方案与实施单元；plan 落在版本分支 | CE `ce-plan` | P2 |
| `nk-ideate` | 基于代码现状发散并筛选改进方向 | CE `ce-ideate` | P2 |
| `nk-close` | 版本收尾（第四章流程） | 新增 | P3 |
| `nk-compound` | 沉淀 solution（含决策类型）与术语；通过审计模式维护既有知识 | CE `ce-compound` / `ce-compound-refresh` + Matt ADR 门槛 | P3 |
| `nk-debug` | 先建立可快速变红的复现，再做因果排错 | CE `ce-debug` + Matt `diagnosing-bugs` | P4 |
| `nk-review` | 代码审查；结果写版本分支 `docs/reviews/` | CE `ce-code-review` + Matt `code-review` | P4 |
| `nk-simplify` | 交付后精简 | CE `ce-simplify-code` | P4 |
| `nk-wayfinder` | 超大未知目标的决策地图与探针（Issue 承载） | Matt `wayfinder` | P5 |
| `nk-to-issue` | 核实并分析开发中冒出的 bug/新需求，落档为可接手的 Issue | Matt `triage`（核实与 brief） | P5 |
| `nk-wizard` | 生成引导人完成手动操作的交互脚本 | Matt `wizard` | P5 |
| `nk-wait-what` | 暂停发散，重新梳理上下文 | Matt `wait-what` | P5 |
| `nk-init` | 目标仓库首次启用 NexusKit 的初始化 | 新增（灵感源自 Matt `setup-matt-pocock-skills`） | P6 |
| `nk-ask-ljq` | 场景路由器：当前情境该用哪个技能/流程（名字含作者缩写，个人元素） | Matt `ask-matt` | P6 |

初始技能建设已完成；当前仍在逐项审查和修改。文件已存在、机械检查通过与真实客户端验收是不同状态，不用“已实现”代替全部验收通过。

---

## 七、派生与删减原则

减重同时考虑注入体量、实际读取路径和执行动作。仅将内容移入 references，或将检查压成一句口号，并不能证明成本下降。具体客户端的加载效果仍需实际验证。

1. **入口能直接指导执行**：SKILL.md 保留流程、短底线、条件分支与结束条件；不要求所有实质规则下沉。
2. **按使用时机拆分**：同一路径连续使用的方法可放在一个完整 reference；条件分支由入口显式加载，优先保持本地执行 reference 为叶子，避免按章节号递归拼装规则。
3. **共享规则单源维护**：短底线允许在入口保留受控副本并检查一致性；长方法不无差别复制。资料链接与公开技能入口仍可保留，不将“叶子材料”误解为禁止全部链接。
4. **质量要求逐项核对**：保留 / 改写 / 删除均应有理由；不能因精简而丢失真实调用链、测试发现、集成风险、构建检查、外部状态与验收证据。拿不准时先厘清职责与使用时机，不机械下沉。
5. **更少自维护代码满足同一需求**：先理解现状，复用既有实现和原生能力，再新增必要实现；不以删行数、单行表达式或缩减已定需求为目标。
6. **执行约束清晰可判定**：单元边界、交接条件和提交单位直接说明；不依赖模型估计上下文占用，不把子代理结束与提交绑定。委派遵守客户端能力、用户与项目限制。
7. **文案直接，理由另存**：开头说明适用场景与动作，长条件拆句；来源与取舍集中放在 `docs/skill-sources.md`，长期决策进 `docs/solutions/`，不要求运行技能时阅读维护史。

以上是 nk-work 已采纳的范式，后续随逐技能审查应用。它不宣告整仓完成迁移，也不预先确定 review 的触发安排。具体取舍与证据边界见 [设计记录](../solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)。

---

## 八、实施与验证

### 当前迭代方式

- 当前逐技能深读、修改与外部实跑安排由 [current.md](../current.md) 指向的计划维护，本 RFC 不复制进度或问题清单。
- 本轮对话负责文档修改、机械检查和反馈核对；实际技能执行由用户另行安排独立会话。遵循当前计划，不把静态阅读或模拟记为技能实跑。
- 后续整理以 nk-work 范式为参考，逐项核对动作与质量要求。跨技能规则、来源与消费端随改动同步维护，不因目录看起来整齐就认定迁移完成。
- 来源取舍写入 [skill-sources.md](../skill-sources.md)，长期设计决定进入 [solutions/](../solutions/)。不再把每个技能新建简报或固定由某个客户端审核作为本轮必经步骤。

### 共享维护与分发

共享约定已位于 `skills/conventions/`，包含产物、提交、术语、Plan 格式及共享角色方法等内容。正式支持整套安装；平级分发布局继续有效，详见 [分发决定](../solutions/architecture-decisions/2026-09-26-distribution-layout.md)。

nk-work 的四段短底线在维护时同步到入口，由一致性检查约束。其他共享规则仍按当前技能的使用路径消费，后续逐步审查；这不是全仓生成系统，也不代表 conventions 只剩维护用途。

正式加载使用安装快照，不直接消费开发目录。试用未发布改动时按根目录 [AGENTS.md](../../AGENTS.md) 重装本地插件或建立临时 junction。安装快照不会因仓库修改而自动刷新；采用临时 junction 时须核对实际指向路径。验证前确认客户端读到的版本，不能假设沙盒已读取本轮文案。

### 验证层次

1. **内容核对**：比较改动前后的目标、条件、动作、质量要求、产物接口与结束条件，检查是否遗漏或冲突。
2. **机械检查**：修改技能或约定后运行 `python -B -X utf8 tests/run_checks.py`；涉及检查逻辑时运行对应测试，当前回归入口为 `python -B -X utf8 -m unittest discover -s tests -p 'test_*.py'`；同时检查 `git diff --check`。
3. **真实执行**：由独立会话在沙盒中执行实际任务，核对所用版本、触发路径、读取过程、产物和验证证据。机械检查不代替这层验收。
4. **目标项目迁移**：单独制定迁移方案，处理既有产物、项目指令、CE 的停用或并存、跨客户端接手及回退方案。本文不宣称 paper-30min 已完成迁移验收。

### 初始阶段路线图（历史）

以下保留立项时的建设顺序，便于解释各技能的来源；它不是当前待办，也不作为验收通过记录。

| 阶段 | 原始建设范围 |
| :-- | :-- |
| P0 | 共享约定 |
| P1 | nk-work、nk-commit、nk-handoff |
| P2 | nk-brainstorm、nk-plan、nk-ideate |
| P3 | nk-close、nk-compound |
| P4 | nk-debug、nk-review、nk-simplify |
| P5 | nk-wayfinder、nk-to-issue、nk-wizard、nk-wait-what |
| P6 | nk-init、nk-ask-ljq |

原路线图中的“写简报 → Claude 评审 → 编写 → 成稿评审 → 单元验证”是初始建设方法；“全部完成后再迁移、最后打包”也属于当时的排期。现在已有分发形态，正在按审计计划迭代，不再按该历史排期安排当前工作。

---

## 九、问题与决策边界

1. **技能语言与触发效果**：继续由现行审计计划与关联 Issue 跟踪，凭真实客户端证据判断；此处不沿用旧版“v1.1.0 处理”的排期，也不推断外部 Issue 的最新状态。
2. **知识审计形态**：已定为 nk-compound 的审计模式，不再待选独立 refresh 技能。
3. **共享约定如何分发与消费**：整套平级分发继续有效；nk-work 的运行时规则组织按 D12 调整。后续技能随审查迁移，不预设全面内联或移除 conventions。
4. **开发目录如何加载**：采用安装快照；临时 junction 是开发试用选项，不是正式加载模型。
5. **review 的触发安排**：用户指定留到修改 nk-review 时再讨论。本轮不确定每单元审查、阶段审查或 Plan 完成后审查的固定安排。
6. **nk-work 范式的运行效果**：设计已采纳，实际读取与完成质量仍需独立执行证据；当前没有客户端对照实验结论。
