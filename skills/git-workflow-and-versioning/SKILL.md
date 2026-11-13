---
name: git-workflow-and-versioning
description: Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in a messy working tree into clean atomic commits, opening or reviewing a pull request (PR), pushing to a remote, or when you need to organize work across multiple parallel streams. Use when cutting a release, choosing a semantic version bump, tagging, or writing a changelog. Use when asked to write a commit message or a changelog entry for a change, or to split a change into commits, even when the diff is pasted inline and the message seems easy to write from it.
---

# Git Workflow and Versioning

## 概览

Git 是你的安全网。把 commits 当作保存点，把 branches 当作沙盒，把提交历史（history）当作文档。在 AI agents 高速生成代码的当下，严谨的版本控制正是让变更保持可控、可审查、可回滚的保障机制。

## 何时使用

始终适用。所有代码变更都要经过 git。

## 核心原则

### Trunk-Based Development（推荐）

保持 `main` 始终处于可部署状态。在短生命周期的 feature branches 上工作，并在 1-3 天内合回主干。长期存在的开发分支会带来隐性成本：它们会不断分叉偏离、制造 merge conflicts，并拖慢集成节奏。DORA 研究一贯表明，trunk-based development 与高绩效工程团队高度相关。

```
main ──●──●──●──●──●──●──●──●──●──  (always deployable)
        ╲      ╱  ╲    ╱
         ●──●─╱    ●──╱    ← short-lived feature branches (1-3 days)
```

这是推荐的默认实践。采用 gitflow 或长期分支的团队，同样可以把这些原则（atomic commits、小步变更、描述清晰的 commit message）套用到自己的分支模型中——提交纪律远比具体的分支策略更重要。

- **开发分支（dev branches）也是成本。** 分支每多存活一天，就会累积多一分 merge 风险。
- **Release branches 可以接受。** 当你需要在 main 继续往前推进的同时稳定某个 release 时，可以单独维护发布分支。
- **Feature flags > 长期分支。** 优先把未完成的功能藏在 feature flags 后面先部署，而不是让它滞留在分支上好几周。

### 1. 尽早提交，经常提交

每完成一个验证通过的增量，就应该单独打一个 commit，不要把大量未提交的改动攒在一起。

```
Work pattern:
  Implement slice → Test → Verify → Commit → Next slice

Not this:
  Implement everything → Hope it works → Giant commit
```

Commits 就是保存点。只要下一个改动改坏了东西，你可以立刻退回到上一个已知正常的稳定状态。

### 2. Atomic Commits（原子提交）

每个 commit 只完成一件逻辑独立的事：

```
# Good: Each commit is self-contained
git log --oneline
a1b2c3d Add task creation endpoint with validation
d4e5f6g Add task creation form component
h7i8j9k Connect form to API and add loading state
m1n2o3p Add task creation tests (unit + integration)

# Bad: Everything mixed together
git log --oneline
x1y2z3a Add task feature, fix sidebar, update deps, refactor utils
```

### 3. 描述性消息

Commit messages 应该解释 *why*（为什么改），而不只是描述 *what*（改了什么）：

```
# Good: Explains intent
feat: add email validation to registration endpoint

Prevents invalid email formats from reaching the database.
Uses Zod schema validation at the route handler level,
consistent with existing validation patterns in auth.ts.

# Bad: Describes what's obvious from the diff
update auth.ts
```

**格式：**
```
<type>: <short description>

<optional body explaining why, not what>
```

**类型：**
- `feat` — 新功能
- `fix` — Bug 修复
- `refactor` — 既不修 bug 也不加新功能的代码重构
- `test` — 添加或更新测试
- `docs` — 仅文档变更
- `chore` — 工具链、依赖与配置调整

### 4. 保持关注点分离

不要把格式调整和行为变更混在一起，也不要把重构和新功能塞进同一次改动。每类变更都应该单独作为一个 commit，理想情况下更应该拆成单独的 PR：

```
# Good: Separate concerns
git commit -m "refactor: extract validation logic to shared utility"
git commit -m "feat: add phone number validation to registration"

# Bad: Mixed concerns
git commit -m "refactor validation and add phone number field"
```

**将重构与功能开发分开。** 重构和功能开发本质上是两笔不同的变更，应当分别提交。这样每一笔改动都更容易审查、回滚，也更容易在历史记录中追溯理解。顺手做的小幅清理（例如变量重命名）可由 reviewer 酌情决定是否允许带入功能 commit 中。

### 5. 控制变更大小

目标控制在每个 commit/PR 约 100 行左右；超过约 1000 行的变更应当拆分。大变更的具体拆分策略见 `code-review-and-quality`。

```
~100 lines  → Easy to review, easy to revert
~300 lines  → Acceptable for a single logical change
~1000 lines → Split into smaller changes
```

## 分支策略

### Feature Branches（功能分支）

```
main (always deployable)
  │
  ├── feature/task-creation    ← One feature per branch
  ├── feature/user-settings    ← Parallel work
  └── fix/duplicate-tasks      ← Bug fixes
```

- 从 `main`（或团队默认分支）拉出分支
- 保持分支短生命周期（1-3 天内合并），长期分支是隐性成本
- 合并后及时删除分支
- 对尚未完成的功能，优先使用 feature flags，而不是长期分支

### 分支命名

```
feature/<short-description>   → feature/task-creation
fix/<short-description>       → fix/duplicate-tasks
chore/<short-description>     → chore/update-deps
refactor/<short-description>  → refactor/auth-module
```

## 使用 Worktrees

需要让多个 AI agent 并行开发时，使用 git worktrees 同时运行多个分支：

```bash
# Create a worktree for a feature branch
git worktree add ../project-feature-a feature/task-creation
git worktree add ../project-feature-b feature/user-settings

# Each worktree is a separate directory with its own branch
# Agents can work in parallel without interfering
ls ../
  project/              ← main branch
  project-feature-a/    ← task-creation branch
  project-feature-b/    ← user-settings branch

# When done, merge and clean up
git worktree remove ../project-feature-a
```

收益：
- 多个 agents 可以同时推进不同功能
- 无需频繁切换分支（每个目录各自对应独立分支）
- 如果某个实验失败，直接删掉对应 worktree 即可，不会波及其他工作
- 变更在明确合并前彼此保持隔离

## 保存点模式

```
Agent starts work
    │
    ├── Makes a change
    │   ├── Test passes? → Commit → Continue
    │   └── Test fails? → Revert to last commit → Investigate
    │
    ├── Makes another change
    │   ├── Test passes? → Commit → Continue
    │   └── Test fails? → Revert to last commit → Investigate
    │
    └── Feature complete → All commits form a clean history
```

采用这种模式，哪怕出问题你最多也只会损失一个增量的工作量。万一 agent 跑偏，执行 `git reset --hard HEAD` 就能立即退回到上一个成功状态。

## 变更总结

每次修改完成后，都应提供一份结构化的变更总结。这能降低审查难度、体现范围纪律，并把非预期的改动暴露出来：

```
CHANGES MADE:
- src/routes/tasks.ts: Added validation middleware to POST endpoint
- src/lib/validation.ts: Added TaskCreateSchema using Zod

THINGS I DIDN'T TOUCH (intentionally):
- src/routes/auth.ts: Has similar validation gap but out of scope
- src/middleware/error.ts: Error format could be improved (separate task)

POTENTIAL CONCERNS:
- The Zod schema is strict — rejects extra fields. Confirm this is desired.
- Added zod as a dependency (72KB gzipped) — already in package.json
```

这种写法能及早发现错误假设，并给 reviewer 提供一张清晰的变更地图。其中 "DIDN'T TOUCH" 一节尤为关键——它证明你严守了范围纪律，没有对无关代码进行未经请求的擅自翻新。

## Pre-Commit 卫生

每次 commit 之前：

```bash
# 1. Check what you're about to commit
git diff --staged

# 2. Ensure no secrets (lists matching file names only — any output means review them)
git diff --staged -i -G'password|secret|api_key|token' --name-only

# 3. Run tests
npm test

# 4. Run linting
npm run lint

# 5. Run type checking
npx tsc --noEmit
```

用 git hooks 自动化这些检查：

```json
// package.json (using lint-staged + husky)
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md}": ["prettier --write"]
  }
}
```

## 处理生成文件

- **只有当项目预期跟踪时才 commit 生成文件**（例如 `package-lock.json`、Prisma migrations）
- **不要 commit** 构建产物（`dist/`, `.next/`）、环境文件（`.env`）或 IDE 配置（除非团队共享，否则不要提交 `.vscode/settings.json`）
- **配置好 `.gitignore`**，覆盖：`node_modules/`, `dist/`, `.env`, `.env.local`, `*.pem`

## 用 Git 调试

```bash
# Find which commit introduced a bug
git bisect start
git bisect bad HEAD
git bisect good <known-good-commit>
# Git checkouts midpoints; run your test at each to narrow down

# View what changed recently
git log --oneline -20
git diff HEAD~5..HEAD -- src/

# Find who last changed a specific line
git blame src/services/task.ts

# Search commit messages for a keyword
git log --grep="validation" --oneline
```

## 发布与版本管理

Commits 是*你*追踪变更的方式；而**版本号（version）**则是你的*使用者（consumer）*追踪变更的方式。一旦有任何外部对象开始依赖你的代码——无论是另一个团队、一个已发布的包，还是一个已部署的客户端——“main 上的最新代码（latest on main）”就不再足以回答“我跑的是哪个版本，现在升级安全吗？”这个问题。版本号和 changelog，正是用来回答这个问题的正式契约。

### 语义化版本（Semantic Versioning）

对任何有使用者的项目，按 `MAJOR.MINOR.PATCH` 规范管理版本，并让数字承载明确含义：

```
  MAJOR  breaking change — consumers must change their code to upgrade
  MINOR  new functionality, backward-compatible — safe to upgrade
  PATCH  bug fix, backward-compatible — safe to upgrade
```

版本号就是一份承诺，代码必须名副其实。只要一个所谓的 "patch" 改变了使用者原本依赖的行为，它本质上就是披着补丁外衣的 major 变更（Hyrum's Law，见 `api-and-interface-design` skill）。拿不准某个改动是否属于 breaking change 时，就按破坏性变更处理；多升一次意料之外的 major 版本，代价远比把使用方直接搞崩要低得多。

### 给 release 打 tag，并让 tag 成为唯一事实来源

Release 是代码历史中一个不可变的锚点，而不是持续移动的分支。为它打上 tag，确保任何时候都能原样复现：

```bash
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin v1.4.0
```

从 tag 派生版本号，而不是在散落各处的文件里手动修改，这样构建产物、tag 与 changelog 三者才永远不会自相矛盾。

### 维护写给人类看的 changelog

Changelog 不是 `git log`。它是面向使用者精心整理后的说明，用来回答“改了什么？与我有什么关系？”——按 `Added / Changed / Fixed / Deprecated / Removed / Security` 分类，最新版本排在最顶部，每条记录都围绕用户影响来措辞，而不是罗列内部实现机制。

```markdown
## [1.4.0] - 2025-06-12
### Added
- Bulk task import via CSV
### Fixed
- Timezone drift in recurring task due dates
### Deprecated
- `GET /v1/tasks/all` — use the paginated `GET /v1/tasks` (removal in 2.0)
```

要在做出代码改动的同一次变更里顺手写好 changelog 条目，趁着影响范围记忆犹新时记下来，而不是等到发版时再去翻 commit 考古拼凑。Breaking changes 必须附带迁移说明和弃用窗口（遵循 `deprecation-and-migration` skill）；真正执行上线发布是 `shipping-and-launch` skill 的职责，而本节提供的是作为其输入前提的版本契约。

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “功能完成后再 commit” | 单个庞大的 commit 几乎无法审查、调试或回滚。每完成一个切片就要提交一次。 |
| “消息不重要” | Commit message 本身就是文档。未来的你（以及未来的 agents）都需要靠它理解改了什么以及为什么这么改。 |
| “以后全部 squash” | 全量 squash 会抹掉开发演进的脉络。最好从一开始就写出干净的增量 commits。 |
| “分支增加开销” | 短生命周期分支几乎没有额外成本，还能防止并行工作互相冲撞。长期分支才是问题，分支应在 1-3 天内合回。 |
| “以后再拆这个变更” | 大变更更难审查、上线风险更高，也更难回滚。要在提交前拆分，而不是事后补救。 |
| “我不需要 .gitignore” | 直到把带着生产 secrets 的 `.env` 提交进了仓库才会后悔。现在就立刻配好它。 |
| “只是个小修复，patch 加一就行” | 先看使用者能观察到什么变化。只要他们依赖的行为变了，哪怕 diff 再小也属于 major 变更。 |
| “changelog 就是 commit log” | Commits 是写给你自己看的；changelog 是写给使用者看的，必须按用户影响去梳理。直接拿原始 commits 拼出来的 changelog 只会把重点淹没。 |
| “发布时再补 changelog” | 到发版时只能靠记忆回溯影响范围，而且多半已经漏掉一半细节。条目必须跟着变更一起写。 |

## 危险信号

- 累积大量未提交变更
- Commit messages 敷衍了事，像 "fix"、"update"、"misc"
- 格式调整与行为变更混在一起
- 项目中缺少 `.gitignore`
- 把 `node_modules/`、`.env` 或构建产物 commit 进了仓库
- 长期分支与 main 严重偏离分叉
- 向共享分支强推（force-push）
- 把 breaking change 混在 minor 或 patch 版本递增下发布
- Release 没有打 tag，或手动修改版本号导致与 tag 不同步
- 面向用户的 release 缺少 changelog 条目，或直接把原始 commit messages 原封不动倒进 changelog

## 验证

对每个 commit：

- [ ] 每个 commit 只做一件逻辑独立的事
- [ ] Commit message 解释了修改原因（why），并符合类型约定
- [ ] 提交前测试全部通过
- [ ] Diff 中不含 secrets
- [ ] 没有把纯格式调整混入行为变更
- [ ] `.gitignore` 已覆盖标准排除项

对每个 release（任何有使用者的发布物）：

- [ ] 版本递增与变更性质匹配：breaking → major，向后兼容的新增功能 → minor，修复 → patch
- [ ] Release 已打 tag，且版本号从 tag 派生，而非手动编辑导致不同步
- [ ] Changelog 中包含该版本的条目：经过整理、按影响分组、面向人类阅读
