---
description: 项目首次接入 NexusKit — 确认规则文件、产物落点、外置工具与子智能体模型，幂等写入项目约定
disable-model-invocation: true
---

在目标仓库首次启用 NexusKit 时运行一次，把仓库变成"体系就绪"状态：后续技能知道 idea、决策、规格、task 分别放在哪，子智能体按什么模型派发。全程幂等，可重复运行；已存在且一致的条目跳过，不覆盖既有内容。

**完成标志：** 选定的规则文件包含「项目约定」小节，七项决策均已明确，用户知道哪些技能会读它。
**工作原则：** 先探测再提问；探测只用于给推荐，不代替用户决定；只改规则文件；不预建空目录；不提交。

---

## 执行步骤

### 1. 探测现状

只读，不发问，不假设：

- **规则文件**：根目录 `AGENTS.md`、`CLAUDE.md` 是否存在；是否已有「项目约定」小节或等价内容。
- **现有产物**：`docs/ideas/`、`docs/adr/`、`SPEC.md`、`docs/SPEC.md`、`spec/`、`tasks/plan.md`、`tasks/todo.md` 各自是否存在。
- **外置工具信号**：MCP 工具表或 `.mcp.json` 中是否出现 Linear 等 tracker；`openspec/` 目录或配置；`bd`/beads 配置；`git remote -v` 与 `gh --version`。
- **模型覆盖**：项目 `.claude/agents/` 或用户 `~/.claude/agents/` 是否已有五个 agent 的同名定义。
- **多模块信号**：`pnpm-workspace.yaml`、`package.json` 的 `workspaces`、多个 `packages/*/src`。

用两行汇报发现：一行已有产物，一行将采用的推荐值。

探测结果**只影响推荐值**。即使发现 Linear MCP、OpenSpec 目录或 beads 已安装，也必须询问这个项目实际要用哪一个——全局装了不代表本项目要用，不要直接采用。

### 2. 逐项确认

一次问一项，每项给出推荐答案和可用的默认值；用户接受推荐即可继续。**默认七项都要问**，不能因为探测有结果就跳过；只有 A 项在仅存在一个规则文件时可直接采用并说明。

**A. 规则文件**
- 只有一个存在：使用它，告知用户，不再提问。
- 两个都存在：问改哪一个；并问未选中的那个是否加一行指向被选中的文件。
- 都不存在：问新建哪一个，不代选。

**B. idea 存放位置**（推荐 `docs/ideas/`，一个想法一个文件）

**C. 决策记录位置**（推荐 `docs/adr/`，编号递增，不删旧）

**D. spec 存放位置与外置工具**
推荐单份 `SPEC.md`；多模块用 `spec/SPEC-<id>.md` + `spec/capability-map.md`。问是否使用 OpenSpec 等外置规格系统（默认否）。选外置时记录工具名与位置；该工具是唯一来源，不另建本地副本。

**E. task 存放位置与外置工具**
推荐 `tasks/plan.md` + `tasks/todo.md`，plan 格式遵循 planning-and-task-breakdown。问是否使用 GitHub Issues、Linear、beads 等外置 tracker（默认否）。选外置时记录工具与项目/工作区；同样只保留一份来源。

**F. 子智能体模型**
推荐 `code-reviewer`、`security-auditor` 用 opus；`doubt-challenger`、`test-engineer`、`web-performance-auditor` 用 sonnet。

**G. 模型覆盖写在哪**
- 推荐：不改任何文件；把模型选择写进「项目约定」，以后派发子智能体时显式传 `model`。优先级最高，插件更新时提示词不会被冻结。
- 项目级覆盖：把五个 agent 的完整定义复制到 `.claude/agents/` 并改 `model`，从此提示词随项目冻结。
- 用户级覆盖：同上，写到 `~/.claude/agents/`，影响该用户的所有项目。

用户回答"我不知道"时，按推荐值继续，并说明后续可以改。

### 3. 展示草稿并确认

把要写入的「项目约定」小节完整展示给用户，标明哪些行来自探测、哪些来自回答。让用户修改后再落盘。不要边问边写。

草稿使用中性标题 `## 项目约定`，每项一行，不写日期，不写"本次初始化"之类的流水账：

```markdown
## 项目约定

- idea：`docs/ideas/`，一个想法一个文件
- 决策记录：`docs/adr/`，编号递增，不删旧
- 规格：`SPEC.md`；多模块用 `spec/SPEC-<id>.md` + `spec/capability-map.md`；外部工具：无
- task：`tasks/plan.md` + `tasks/todo.md`，格式遵循 planning-and-task-breakdown；外部工具：无
- 子智能体模型：派发时显式传 `model` —— code-reviewer、security-auditor 用 opus；doubt-challenger、test-engineer、web-performance-auditor 用 sonnet
- 以上文件在第一次真正产出时创建，不预建空目录
```

按回答替换路径与外部工具；选了外部工具就把"无"换成工具名和位置，并去掉不再适用的本地路径。用户选择项目级或用户级模型覆盖时，把模型行改为"覆盖文件：`.claude/agents/`（项目级）"或"`~/.claude/agents/`（用户级）"。

### 4. 写入

- 只改第 2 步选定的规则文件。
- 已有 `## 项目约定` 小节：逐行比对，缺失的补上，相同的跳过；与现有内容冲突时报告并询问，不静默覆盖。
- 没有该小节：追加到文件末尾，不改动其他内容。
- 不预建 `docs/ideas/`、`docs/adr/`、`spec/`、`tasks/` 等目录；不创建 `CONCEPTS.md`。
- 不暂存、不提交。

### 5. 收尾

列出本次写入、更新和跳过的条目。说明谁会读这些约定：

- `/nk-spec` 与 `spec-driven-development` 按规格位置和外部工具产出
- `/nk-plan` 与 `planning-and-task-breakdown` 按 task 位置和外部 tracker 拆分
- `/nk-build` 按规格位置查找 spec
- `/nk-ship`、`/nk-review`、`/nk-test` 等派发子智能体时按模型行传参

提醒用户审阅 `git diff` 后自行提交。

---

## 边界

- 不迁移既有产物，不安装外置工具，不改项目代码。
- 重复运行时只报告现状；已存在且一致的条目跳过，不产生改动。
- 不写 `CONCEPTS.md`，不建空目录，不提交。