# AGENTS.md

本仓库是 NexusKit（`nk-*`）技能体系的开发目录。技能与共享约定位于 [`skills/`](skills/)（`skills/nk-*` + `skills/conventions/`）。

**加载模型：本仓库是半成品工作区，不直接作为技能加载源。** 各客户端通过发布形态消费成品——Kimi Code 插件、Codex 插件、`npx skills add`（见 [`README.md`](README.md) 安装节）。开发期想让客户端立即试用未发布改动时，手动重装本地插件（`/plugins install D:\codex_project\nexuskit`）或在 `~/.agents/skills/` 建临时 junction（用 PowerShell `New-Item -ItemType Junction`；删除用 `[IO.Directory]::Delete()`，勿用 `Remove-Item -Recurse`）。

## 维护者入口

- **[`docs/current.md`](docs/current.md)**：仓库当前状态、验证结果、下一步——新会话先读它。
- **[`docs/solutions/`](docs/solutions/)**：经验与决策库（长期资产）；沉淀与审计规则见 `skills/conventions/solution-schema.md`。
- 涉及设计取舍、非琐碎实现或排障时，按主题、模块或症状定向检索 `docs/solutions/`；已有适用结果直接复用，只精读相关条目。无匹配照常推进，不因此触发沉淀或审计。交接相关经验时带上来源路径、适用条件、关键约束及验证影响；存疑或已取代条目先核实现状。
- **[`CONCEPTS.md`](CONCEPTS.md)**：领域术语表（分支收尾、容器中立认领、前沿轮次等体系术语的唯一真实来源）；维护规则见 `skills/conventions/concepts-vocabulary.md`。
- **[`docs/skill-sources.md`](docs/skill-sources.md)**：每个技能的上游来源与取舍理由（维护者向；执行技能的 Agent 不需要读）。
- **[`conventions/`](skills/conventions/)**：共享约定的维护源（提交节奏、产物生命周期、术语、plan 格式等）。一般按需引用；每次必需的短底线可按 nk-work 范式同步到入口，并校验副本一致性，不维护未经核对的改写副本。
- **[技能组织范式](docs/solutions/architecture-decisions/2026-09-28-skill-execution-locality.md)**：以 nk-work 为例，说明主流程、完整执行材料、条件分支和共享维护源的边界；后续逐技能整理时参考。
- **[`docs/ideation/nexuskit-framework-ideation.md`](docs/ideation/nexuskit-framework-ideation.md)**：体系设计 RFC（D1–D12 设计决定、历史阶段路线图）。
- **[`README.md`](README.md)**：按场景选用技能的路由表。
- **[设计对话转录](docs/case-studies/2026-09-25-design-dialogue-transcript.md)**：追溯立项取舍时按需查阅的历史材料，不是当前执行规则，不要求技能或新会话全文加载；当前规则以技能、共享约定与已采纳设计决定为准。

## 改动规则

- 修改任何 `skills/nk-*/` 或 `skills/conventions/` 后，运行 `python tests/run_checks.py`，五项检查（链接、引用、字节上限、共享方法及调用关系、frontmatter YAML 解析/重复键与 name/目录同名）必须全绿；CI 会在推送时复跑。首次运行先安装 `python -m pip install -r tests/requirements.txt`。
- **新增技能目录不建加载链接**：发布模型下各客户端消费的是安装快照（见头部加载模型），仓库内改动不直接影响线上；需要即时试用时按头部说明重装本地插件或建临时 junction。
- 所有提交通过 [`nk-commit`](skills/nk-commit/SKILL.md)，提交节奏由该入口统一持有：一个经过验证的变化一次提交，提交前按需同步 current 并一起入库；中途状态默认暂留，显式现场保存按入口规则处理。
- `docs/skill-sources.md` 随技能的新建/修改同步更新；技能的 `SKILL.md` 正文不写来源备注。
- 技能 frontmatter 的 `description` 统一用英文，按当前职责说明适用场景、主要产物及必要的调用边界，不追加中文关键词；正文语言不受此规则影响。这是维护者选定的统一策略，不宣称英文触发效果已经实验验证。

- **校验器适用范围**：本仓库的机械检查入口是 `python tests/run_checks.py`，frontmatter 使用 PyYAML SafeLoader 加重复键拒绝，核对 name/description 为非空字符串及 name 与目录同名，不限制可选字段。合法 YAML 注释不视为语法错误。外部 skill-creator 的 `quick_validate.py` 字段白名单不含本仓库使用的 `argument-hint`、`disable-model-invocation`；不应为通过它删除有效字段或修改外部安装文件。缺少 `yaml` 时按 tests/requirements.txt 安装依赖；YAML 通过不代表客户端支持全部字段，也不代表真实技能执行通过。
