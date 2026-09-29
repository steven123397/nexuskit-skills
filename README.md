# NexusKit (`nk-*`)

> 面向 AI 编程 Agent 的个人工程技能体系。
> 取 **Compound Engineering (EveryInc)** 的规划严谨性与知识沉淀，取 **Matt Pocock Skills** 的任务边界、测试先行与术语维护，按个人项目、多 Agent 协作的实际画像重新组织。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Prefix: nk-](https://img.shields.io/badge/Prefix-nk--*-brightgreen.svg)](#)

当前正式版：[v0.2.0](docs/releases/v0.2.0.md)。本轮技能重构与 U3 沙盒验收已完成，基本使用和触发流程通过维护者验收；接下来在 paper30min 实际开发中使用，内容、方法论及其他问题在 v0.2.x 中逐步修复。v0.3.0 仅有初步构想，暂不启动新一轮大迭代。实测范围见 [验证记录](docs/reviews/feat-skill-deep-audit.md)。

---

## 背景

两套体系都在实战项目（paper-30min，私有仓库）中完整运行过：

* **Matt Pocock Skills**（[mattpocock/skills](https://github.com/mattpocock/skills)，2026-08 本地备份）
* **Compound Engineering**（[EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)，v3.28.2）

| 维度 | Matt | CE | NexusKit |
| :-- | :-- | :-- | :-- |
| 上下文管理 | 一个任务一个新会话 | 主对话承包整份 plan，上下文膨胀 | 新会话 + `current.md` 入口 + 单个实施单元 |
| 需求对齐 | `grill` 盘问繁琐 | ideate/brainstorm 节奏合适 | 采用 CE 方式，去掉默认强制盘问；保留用户主动调用的 `/nk-grill` 严格对齐 |
| 产物管理 | walkthrough、ADR 等本地文件堆积 | plan、review 本地文件堆积 | 每类产物有明确终点，分支收尾时统一清理 |
| 知识沉淀 | 术语即时维护，缺少经验库 | `solutions/` 经验库，术语只在 compound 时生长 | `solutions/`（含决策类型）+ 术语在规划中即时写入 |
| 提交节奏 | 无约束 | 无约束 | 统一入口，按完整交付提交并携带现状 |

完整设计见 [NexusKit 架构设计 RFC](docs/ideation/nexuskit-framework-ideation.md)。

---

## 核心约定

1. **工具箱，不是流水线**：整套安装后，任意技能都可作为工作入口，按场景选取；这不表示支持单技能安装。
2. **`docs/current.md` 是跨会话入口**：记录当前能力、验证结果、阻断项、下一步与所在分支。
3. **产物有生命周期**：Plan 与审查记录在工作分支上演进，收尾时承接长期价值再清理已消费产物，其他活跃工作仍引用的材料保留；Issue 承载待办、缺陷与探针，也承载 wayfinder 的探索地图与决策 tickets。
4. **知识双轨**：踩坑因果与决策理由进 `docs/solutions/`，领域术语进 `CONCEPTS.md`。
5. **提交节奏**：所有提交统一经过 [nk-commit](skills/nk-commit/SKILL.md)，由它核对交付范围、证据并按需同步 current。work / debug 已调度提交，无需再补跑；显式保存未完成现场才调用 handoff。
6. **项目流程归项目**：分支、发布、签名等项目特有约定写在项目自己的工作流文档中，技能读取而不内置。

---

## 按场景选用

| 场景 | 技能 |
| :-- | :-- |
| 不确定该用哪个 | `/nk-ask-ljq` |
| 在新仓库首次启用本体系 | `/nk-init`（仅手动调用） |
| 想找改进方向 | `/nk-ideate` |
| 有想法，要明确做什么、做到哪 | `/nk-brainstorm` |
| 想让 Agent 详细追问，严格对齐设计、决策或想法 | `/nk-grill`（仅手动调用） |
| 需求明确，要设计怎么做 | `/nk-plan` |
| 实现一个实施单元或 Issue | `/nk-work` |
| 提交交付成果 | `/nk-commit` |
| 显式保存未完成现场 | `/nk-handoff`（仅手动调用） |
| 排查缺陷或异常 | `/nk-debug` |
| 审查代码 | `/nk-review` |
| 只检查累计成果能否一起交付 | `/nk-review pre-merge`（主会话为主，最多两个专项子代理） |
| 手动分析代码精简机会 | `/nk-simplify` |
| 沉淀经验、记录决策，或明确要求协作复盘 / 知识审计 | `/nk-compound` |
| 分支收尾 | `/nk-close`（仅手动调用；含轻量合并前检查、提炼和清理） |
| 目标巨大、未知太多，无法直接写 Plan | `/nk-wayfinder`（仅手动调用；探索后交给 nk-plan） |
| 开发中冒出 bug 或新需求，在当前会话先记下来、不展开实施 | `/nk-to-issue` |
| 引导人完成一系列手动操作 | `/nk-wizard`（仅手动调用） |
| 没跟上 Agent 的解释，请它补上下文重讲 | `/nk-wait-what`（仅手动调用） |

常见路线是：可选 ideate → brainstorm 的需求阶段 Plan → nk-plan 补全同一份 Plan → nk-work 逐单元交付 → 用户调用 nk-close。已有清楚请求或 Plan 可从中间进入；wayfinder 是替代探索路线，同样交给 nk-plan 形成标准 Plan。

“按 Plan 实现 U2”交给 nk-work 即可：它调度验证、常规 review（含精简分析与独立复核）、问题处理及 nk-commit，不需要用户再串行调用这些技能。close 的 pre-merge 检查关注累计成果，收尾不自动合并或发布。详细选路见 [ask-ljq](skills/nk-ask-ljq/SKILL.md)。当前维护进度与未验证项见 [docs/current.md](docs/current.md)。

---

## 命令书写约定

面向不同客户端的通用 Git 探针逐条执行，观察结果后再决定下一条；不使用 shell 赋值、管道或 `&&` / `||` 拼接作为跨平台默认写法，`'@{u}'` 等 revision 参数须正确引用。明确标注 Bash / Git Bash 等运行环境的脚本和示例可以使用该 shell 语法，不直接复制到 PowerShell。本约定约束命令书写，不要求把明确的平台脚本改成多客户端变体。

## 安装

正式支持整套安装，任意技能都可以作为工作入口。仓库布局：技能与共享约定都在 [`skills/`](skills/) 下（`skills/nk-*` + `skills/conventions/`；`conventions` 是共享约定与角色方法参考库，不是可执行技能，但必须以同名目录与 `nk-*` 平级安装，技能正文里的 `../conventions/` 引用才能解析）。

### Kimi Code 插件

```
/plugins install https://github.com/steven123397/nexuskit-skills
```

清单为 `.kimi-plugin/plugin.json`（`skills: "./skills/"`，整树随插件分发；与根目录 `kimi.plugin.json` 二选一，本仓库用目录形态）。安装后 `/reload` 或开新会话生效。

### Codex 插件

Codex 通过"市场"机制安装（清单在 [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json)，仓库即单插件市场）：

**Codex App**：侧边栏 **Plugins** → **Create** 旁的箭头 → **Add marketplace** → Source 填 `steven123397/nexuskit-skills`、Git ref 填 `main`、Sparse paths 留空 → Add marketplace → 搜索 **NexusKit** 安装 → 重启 Codex。

**Codex CLI**：

```bash
codex plugin marketplace add steven123397/nexuskit-skills
codex plugin add nexuskit@nexuskit-skills
```

装完重启 Codex。

### npx（skills CLI）

```
npx skills add steven123397/nexuskit-skills
```

安装时选择整套技能（交互多选时全选，或 `--all`），并保留 `.agents/skills/conventions/` 与 `nk-*` 平级。`conventions/agents/` 中的共享角色方法随该目录安装，各技能只按需读取选中的文件。单选某个技能不属于本项目支持的安装形态；安装后仍可从任意技能开始工作。

---

## 许可证

[MIT](LICENSE)。本体系部分技能派生自 mattpocock/skills 与 EveryInc/compound-engineering-plugin（均 MIT），归属声明见 [NOTICE](NOTICE)。
