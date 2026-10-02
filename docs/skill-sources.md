# 技能来源映射

维护者向索引：只记录 NexusKit（NK）具体部分对应的上游材料。来源表示方法借鉴或改写，不表示整份技能照搬；NK 自有流程标为原创。执行技能的 Agent 不需要读本文件。

上游定位简称（下文路径相对对应仓库根目录）：

- **CE**：`D:/codex_project/upstreams/compound-engineering-plugin/`。
- **Matt**：`D:/codex_project/upstreams/matt-pocock-skills/`。
- **Ponytail**：`D:/codex_project/upstreams/ponytail/`。

以上目录为维护者的本地只读克隆，未随 NK 分发；路径用于定位现有材料，不将当前上游 HEAD 当作当初采用的版本。归属和许可证见 [NOTICE](../NOTICE)。下文 NK 的 `references/`、`SKILL.md` 相对该节技能目录。

## nk-ask-ljq

- [入口](../skills/nk-ask-ljq/SKILL.md) 的场景推荐、主线与独立工具地图：Matt `skills/engineering/ask-matt/SKILL.md` 的 `The main flow: idea → ship`、`On-ramps`、`Standalone`。
- NK 技能路线、执行授权与外部 PR 指引、维护者个人留言：NK 原创。

## nk-brainstorm

- [入口](../skills/nk-brainstorm/SKILL.md)、`references/phase-0.md`、`evidence.md`、`dialogue.md`、`approaches.md` 的定界、侦察与声明核实、产品压力测试、对话及方案比较：CE `skills/ce-brainstorm/SKILL.md` 的 `Execution Flow`，及 `references/phase-0.md`、`dialogue.md`、`product-pressure-test.md`、`model-tiers.md`、`approaches.md`。
- `references/sections.md` 的 Product Contract 与 Ready for Planning Check，以及 `blindspot-pass.md`、`visual-probes.md`、`universal-brainstorming.md`：CE `skills/ce-brainstorm/references/brainstorm-sections.md`、`plan-write.md` 及后三个同名文件。
- `references/dialogue.md` 的术语质疑与场景压力测试：Matt `skills/engineering/domain-modeling/SKILL.md` 的 `During the session`；上下文充分时直接综合：Matt `skills/engineering/to-spec/SKILL.md` 开头的“不访谈，综合已有上下文”。
- 需求阶段 Plan、R-ID、与 plan 的证据交接及提交接口：NK 原创；共享术语与综述方法见 conventions。

## nk-close

- [PR 描述](../skills/nk-close/references/pr-description.md) 的行为变化优先、按决策成本定长度、真实验证与项目模板优先：CE `skills/ce-commit-push-pr/references/pr-description-writing.md`。
- [入口](../skills/nk-close/SKILL.md)、`references/closure.md`、`release-day.md` 的分支交付确认、材料处置、发布收尾与已合并外部 PR 路径：NK 原创。

## nk-commit

- [入口](../skills/nk-commit/SKILL.md) 的状态与风格检查、按逻辑变化提交、具名路径暂存、提交消息文件及提交后核对：CE `skills/ce-commit/SKILL.md` 的 `Context`、`Workflow`。
- R1–R6 提交节奏、current 归属、验证与审查证据、amend 条件：NK 原创。
- 中文提交文案的类型、动宾主题、动机与不兼容标记：原来源记录归于本地 `C:/Users/29617/.codex/skills/chinese-commit-conventions/SKILL.md`；该文件现已不存在，无法核对具体章节。

## nk-compound

- [沉淀](../skills/nk-compound/references/capture.md) 的语料检索、研究、成文、增强与可发现性：CE `skills/ce-compound/SKILL.md`，及 `references/assembly.md`、`research.md`、`enhancement.md`、`grounding-validation.md`、`refresh-and-discoverability.md`。
- `references/audit.md` 的范围、分类、调查与处置：CE `skills/ce-compound-refresh/references/scope.md`、`classify.md`、`investigate.md`、`per-action-flows.md`、`worth-audit.md`。
- `references/frontmatter-checklist.md`、`claims-checklist.md`：CE `skills/ce-compound/scripts/validate-frontmatter.py`、`validate-doc-claims.py`，由脚本校验改为人工清单。
- `references/retro.md` 的六类协作复盘视角：Matt `skills/in-progress/retro/SKILL.md` 的 `Steps` 第 3 步；决策三门槛：Matt `skills/engineering/domain-modeling/ADR-FORMAT.md` 的 `When to offer an ADR`。
- [入口](../skills/nk-compound/SKILL.md) 的沉淀/审计合并、授权与提交接口、显式复盘路由：NK 原创；知识格式见 conventions。

## nk-debug

- [入口](../skills/nk-debug/SKILL.md)、`references/investigate.md`、`fix.md`、`investigation-techniques.md`、`defense-in-depth.md`：CE `skills/ce-debug/SKILL.md` 的 `Execution Flow` 及 `references/` 下同名文件；就近合入的反模式源于 `references/anti-patterns.md`。
- `references/reproduction.md` 的反馈回路、收紧复现与最小化，以及调查中的可检验预测：Matt `skills/engineering/diagnosing-bugs/SKILL.md` 的 `Phase 1: Build a feedback loop`、`Phase 2: Reproduce + minimise`、`Phase 3: Hypothesise`、`Phase 4: Instrument`。
- 仅诊断出口、修复授权承接、nk-review/nk-commit 接口：NK 原创。

## nk-grill

- [入口](../skills/nk-grill/SKILL.md) 的设计树、前沿轮次、推荐答案与 Agent 事实查证：Matt `skills/productivity/grilling/SKILL.md` 正文。
- 显式调用、复用与局部重开已定决策、暂停与共识汇报、行动授权边界：NK 原创。

## nk-handoff

- [入口](../skills/nk-handoff/SKILL.md) 的现场总结、下一步与接手材料：CE `skills/ce-handoff/SKILL.md` 的 `Create`；按接手用途总结、不重复已有产物、脱敏：Matt `skills/productivity/handoff/SKILL.md` 正文。
- 单例 `docs/current.md`、显式调用与提交委托：NK 原创。

## nk-ideate

- [入口](../skills/nk-ideate/SKILL.md) 的定界、扎根、拆轴、六视角发散、候选预算与独立核查裁定：CE `skills/ce-ideate/SKILL.md`，及 `references/scope-gates.md`、`grounding.md`、`decomposition.md`、`divergent-ideation.md`、`post-ideation-workflow.md`。
- `references/user-research-artifacts.md`、`web-research-cache.md`、`issue-intelligence.md`、`ideation-sections.md`、`universal-ideation.md`、`agents/issue-intelligence-analyst.md`：CE `skills/ce-ideate/references/` 下对应同名材料。
- NK 产物位置与生命周期、向 brainstorm 交接证据、共享研究方法调用：NK 原创适配；角色来源见 conventions。

## nk-init

- [入口](../skills/nk-init/SKILL.md) 的探测、呈现确认、幂等写入骨架与已知答案不再询问：Matt `skills/engineering/setup-matt-pocock-skills/SKILL.md` 的 `Process` 下 `Explore`、`Present findings and ask`、`Confirm and edit`。
- 项目知识入口、`docs/current.md`、本地 backlog 与 nk-commit 接口：NK 原创。

## nk-plan

- [入口](../skills/nk-plan/SKILL.md)、`references/research.md`、`output-contracts.md`、`structure.md`、`final-review.md`、`deepening-workflow.md`、`approach-altitude.md`、`universal-planning.md`：CE `skills/ce-plan/SKILL.md` 及 `references/` 下同名文件，章节组成另见 `plan-sections.md`；`references/phase-0.md` 对应上游 `intake.md`、`resume.md`、`output-mode.md`。
- `references/self-review.md` 的连贯性、可行性与条件审阅视角：CE `skills/ce-doc-review/references/persona-selection.md` 及 `references/personas/` 的 coherence、feasibility、scope、security、design、product、adversarial 角色，NK 改为写后自检。
- `references/design-alternatives.md`：Matt `skills/engineering/codebase-design/DESIGN-IT-TWICE.md` 的 `Process`；深化中的依赖分类：同目录 `DEEPENING.md` 的 `Dependency categories`、`Seam discipline`。
- `references/agents/` 的五个本地规划角色：CE `skills/ce-plan/references/agents/` 下同名文件；其他复用角色见 conventions。
- R-ID/U-ID、实施单元交付契约、wayfinder 输入、提交与 work 接口：NK 原创。

## nk-review

- [入口](../skills/nk-review/SKILL.md)、`references/scope.md`、`select-and-route.md`、`reviewer-prompt.md`、`validate.md` 的意图、范围、风险编队、叶子审查与独立复核：CE `skills/ce-code-review/references/intent-and-plan.md`、`scope.md`、`diff-scope.md`、`select-and-route.md`、`dispatch-reviewers.md`、`subagent-template.md`、`validator-batch-template.md`、`finish-review.md`。
- `references/personas/` 的风险角色：CE `skills/ce-code-review/references/personas/` 下同名文件；共享经验、迁移、部署角色见 conventions。
- maintainability 的“可删除内容、替代能力及等价依据”：Ponytail `skills/ponytail-review/SKILL.md` 的 `Format` 分类；NK 增加证据与行为保持条件。
- `references/pre-merge.md`、`entry-format.md`，外部 PR 的 base/head、修订复核、合并前确认与报告生命周期：NK 原创；常规流程显式调用 nk-simplify。

## nk-simplify

- [入口](../skills/nk-simplify/SKILL.md) 的三个分析视角与 `references/personas/` 三个角色：CE `skills/ce-simplify-code/SKILL.md` 及 `references/personas/code-reuse-reviewer.md`、`code-quality-reviewer.md`、`efficiency-reviewer.md`。
- 删减优先、复用仓库/标准库/原生能力：Ponytail `skills/ponytail/SKILL.md` 的 `The ladder`，及 `skills/ponytail-review/SKILL.md` 的 `Format`。
- 默认分析、修复授权、review 嵌入接口与行为等价证据：NK 原创适配。

## nk-to-issue

- [入口](../skills/nk-to-issue/SKILL.md) 的事实核实、已有实现与历史否决检查、已知与缺口表达：Matt `skills/engineering/triage/SKILL.md` 的 `Triage a specific issue or PR` 第 1、3 步、`Needs-info template`、`Resuming a previous session`。
- 授权后在当前任务建票/更新、本地 backlog、失败去重与调用方接口：NK 原创；条目契约见 conventions。

## nk-wait-what

- [入口](../skills/nk-wait-what/SKILL.md) 的重新解释、补上下文、简单语言与项目术语：Matt `skills/productivity/wait-what/SKILL.md` 正文。
- 中文表达适配、`CONCEPTS.md`、不清楚处与待对齐项的汇报：NK 原创适配。

## nk-wayfinder

- [入口](../skills/nk-wayfinder/SKILL.md)、`references/modes.md`、`ticket-types.md`、`fog-and-scope.md` 的 Map、票种、依赖、迷雾与逐票探索：Matt `skills/engineering/wayfinder/SKILL.md` 的 `The Map`、`Ticket Types`、`Fog of war`、`Invocation`。
- `references/tracker-operations.md` 的 GitHub 分页、认领与失败处理，探索结果经 nk-plan 汇合：NK 原创适配。

## nk-wizard

- [入口](../skills/nk-wizard/SKILL.md) 的分阶段人工向导与 [Bash 模板](../skills/nk-wizard/assets/template.sh)：Matt `skills/engineering/wizard/SKILL.md` 与同目录 `template.sh`。
- Git Bash 说明、跳过项不算全部完成、目的地与凭据边界、静态验证及提交接口：NK 原创适配。

## nk-work

- [入口](../skills/nk-work/SKILL.md)、`references/intake.md`、`tdd-loop.md`、`ui-work.md`、`non-code.md`、`subagents.md` 的承接、真实调用链与实施循环、UI/非代码检查、委派与验收：CE `skills/ce-work/SKILL.md`，及 `references/input-triage.md`、`work-intake.md`、`implementation-loop.md`、`non-code-execution.md`、`execution-strategy.md`、`agents/implementation-worker.md`。
- `references/tdd-loop.md` 的测试反馈循环、测试 seam 与反模式：Matt `skills/engineering/tdd/SKILL.md` 的 `What a good test is`、`Seams: where tests go`、`Anti-patterns`、`Rules of the loop`；持续类型检查、局部/完整测试及完成后审查：`skills/engineering/implement/SKILL.md` 正文。
- 方案选择中的理解真实流程、优先既有能力与根因修复：Ponytail `skills/ponytail/SKILL.md` 的 `The ladder`、`Rules`。
- current 接手、一次一个已确认单元、`references/out-of-repo-state.md` 的真实外部状态证据、审查与提交接口：NK 原创适配。

## conventions

- [共享角色](../skills/conventions/agents/) 中的 best-practices-researcher、framework-docs-researcher、data-integrity-guardian、pattern-recognition-specialist、performance-oracle、security-sentinel、learnings-researcher、web-researcher：CE `skills/ce-plan/references/agents/` 下同名文件；前六个方法也见 `skills/ce-compound/references/agents/`，learnings/web 也见 `skills/ce-ideate/references/agents/`。
- 共享 data-migration-reviewer、deployment-verification-agent：CE `skills/ce-code-review/references/personas/` 下同名文件；NK 分离方法与调用方输出契约。
- [solution-schema.md](../skills/conventions/solution-schema.md) 的双轨分类、YAML 元数据与语料优先：CE `skills/ce-compound/references/schema.yaml`、`yaml-schema.md`、`assets/resolution-template.md`；架构决策三门槛：Matt `skills/engineering/domain-modeling/ADR-FORMAT.md` 的 `When to offer an ADR`。
- [concepts-vocabulary.md](../skills/conventions/concepts-vocabulary.md) 的术语维护与即时记录：CE `skills/ce-compound/references/concepts-vocabulary.md`、`skills/ce-compound-refresh/references/concepts-vocabulary.md`；Matt `skills/engineering/domain-modeling/SKILL.md` 的 `During the session`。
- [settled-decisions.md](../skills/conventions/settled-decisions.md)、[scope-synthesis.md](../skills/conventions/scope-synthesis.md)：CE `skills/ce-brainstorm/references/settled-decisions.md`、`synthesis-summary.md` 与 `skills/ce-plan/references/` 下同名文件，NK 改为跨技能维护源。
- [plan-format.md](../skills/conventions/plan-format.md) 的产品/技术章节与测试场景：CE `skills/ce-brainstorm/references/brainstorm-sections.md`、`skills/ce-plan/references/plan-sections.md`；NK 的阶段、R-ID/U-ID 和单元契约为原创。
- artifact-lifecycle、current-md、issue-writing、decision-autonomy、resource-loading、subagent-results、research-digest、work-guardrails，以及入口短片段与跨技能接口：NK 原创适配。
