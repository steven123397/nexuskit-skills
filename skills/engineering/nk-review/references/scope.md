# 范围判定（审什么）

第 1 步读取本文件。目标是解析出**被审 diff**：基线 ref、文件清单、带上下文的 diff 文本，以及供编队使用的范围信号。解析不出来就早停，不带着半个 diff 进入编队。

## 一、接收范围与审查对象

调用方已给出明确的单元、修复或针对性复核范围时，检查所给材料是否可读并对应同一快照，直接复用，不重新寻找分支基线或扩大到整分支。工作区范围须包含实际 diff 和文件内容或指纹；材料缺失、版本不一致时交回调用方补齐。调用方指定的新文件按全文纳入，外来改动不混入。以下解析只用于尚未定界的手动调用。

按用户输入分流；逐条运行 Git 命令，检查结果后再决定下一步。

### 1. 空参数（默认：版本层面审查）

审当前分支相对基线分支的全部改动（已提交 + 已暂存 + 未暂存一起）：

依次运行以下命令；第一条成功后，将其输出的完整提交哈希作为后续 `<base-sha>`，不使用 shell 变量赋值拼接：

```text
git merge-base HEAD <base-ref>
git diff --name-only <base-sha>
git diff -U10 <base-sha>
git ls-files --others --exclude-standard
```

- `<base-ref>` 的确定顺序：目标项目工作流文档规定的基线分支 > 当前分支的 upstream > 远端默认分支（`origin/main` / `origin/master`）> 本地 `main` / `master`。
- `git diff <base-sha>`（不带 `..HEAD`）对 merge-base 与工作树求 diff，三种状态的改动都覆盖到。
- 无法解析出基线时停下说明，不要把范围悄悄退化成"只看未提交改动"——那会漏掉分支上已提交的工作。按 [`../../conventions/decision-autonomy.md`](../../conventions/decision-autonomy.md) 询问用户审查对象；无法取得答案则报告范围未确定，不自行改换审查对象。

### 2. 指定基线 ref

用户给了 commit、分支、tag（"review since X"）：先 `git rev-parse <ref>` 确认可解析，再单独运行 `git merge-base HEAD <ref>`；成功时使用输出哈希，失败时使用已解析的 ref 作为基线，产出同上。**diff 为空且没有明确纳入的新文件时在此报告无可审变更并结束**，不要进入编队后才发现无事可审。同时用 `git log <ref>..HEAD --oneline` 记录提交清单，供意图摘要使用。

### 3. 指定文件或路径

用户点名文件/目录：diff 限定到这些路径（`git diff -U10 <base-sha> -- <paths>`）；其中未跟踪的新文件按全文阅读。审查结论只对这些路径负责，在覆盖说明中写明"范围为用户指定路径"。

### 4. 未提交改动

用户明确只看手头改动：`git diff -U10 HEAD`（含暂存区），已暂存的新文件也由该 diff 覆盖；另列 `git ls-files --others --exclude-standard`，按下述未跟踪文件规则处理。

### 附：PR 编号或 URL（可选路径）

项目走 PR 流程时，PR 编号/URL 也可作为审查对象：用 `gh pr view <n> --repo <owner/repo> --json url,state,title,body,baseRefName,baseRefOid,headRefName,headRefOid,mergeCommit,mergedAt,files,reviews,comments` 与 `gh pr diff <n> --repo <owner/repo>` 只读取数，**不切换分支、不 checkout**。记录 PR 身份、确切 base/head SHA 和实际差异起点；取数期间 head 变化时重新定界，不混合不同快照。只有本地 HEAD 与被审快照完全相同且涉及文件无工作区改动时，才可用本地内容补证；否则用对应版本的文件或 diff，不能拿维护者 main 的内容代替。

已关闭/已合并的 PR 不默认重审；用户或调用方明确要求合并后补审、针对性复核时，核实合并结果及请求范围，走常规或原审查路径，不能称为 pre-merge。PR head 与实际合入内容不同时，以请求指定的合并结果定界；无法取得对应内容则报告覆盖缺口。明显的琐碎自动 PR（锁文件、版本号 chore）向用户确认后跳过。

## 二、未跟踪文件

调用方或用户明确纳入的未跟踪文件按全文审查；其余未跟踪文件排除并列入覆盖说明，不自动暂存。

## 三、范围信号（路径分类规则）

以下规则转写自原辅助脚本的确定性逻辑，由 Agent 按路径模式直接判定，供编队使用：

**测试文件识别**（供测试风险判定，不用于扣减行数）：`tests?/`、`spec/`、`__tests__/` 目录；`*._-test / *._-spec / *.test.* / *.spec.*` 后缀；`test_*.py`、`conftest.py`；Java/C#/Scala/Swift/Kotlin 的 `*Test.*` / `*Tests.*` / `*Spec.*` 类文件（大小写敏感，`Contest.java` 这类不算）。

**路径信号 → 编队提示**（信号是提示，不是自动派发决定）：

| 信号 | 路径模式（不区分大小写） | 提示的 persona |
| :-- | :-- | :-- |
| 迁移 | `db/migrate/`、`schema.rb/sql`、`/migrations?/`、alembic/flyway/liquibase | data-migration（+ 风险高时 deployment-verification） |
| 前端 | `.tsx/.jsx/.vue/.svelte/.css/.scss`、`/components?/`、stimulus/turbo | julik-frontend-races（有异步 UI 行为变化时） |
| API | `/routes?/`、`/controllers?/`、`/api/`、`/serializers?/`、`.proto`、openapi | api-contract |
| iOS | `.swift`、`.pbxproj`、`.entitlements`、`.xcconfig` | swift-ios |
| Agent 界面 | `/skills?/`、`/agents?/`、`/prompts?/`、`/tools?/`、`SKILL.md`、`AGENTS.md` 等指令文件 | agent-native、project-standards |

**静默放行守卫（无论改动多小都触发 adversarial）**：CI/CD 与门禁类路径——`.github/workflows/`、`.gitlab-ci.yml`、`.circleci/`、`Jenkinsfile`、`.buildkite/` 等。这类改动本身是"验证机制"，风险不在爆炸半径而在保真度：它可能在真实产物已坏时照样放行。

**编队依据**：将结构变化、行为变化与验证机制的具体 diff 证据交给 [select-and-route.md](select-and-route.md) 判定，不计算可执行行数，也不因改动少而豁免风险角色。

## 四、规范文件映射（供 project-standards）

枚举被审版本中的 `CODING_STANDARDS.md`、`CLAUDE.md`、`AGENTS.md`（任意深度），保留其目录是被改文件祖先的文件：根级文件管整个仓库，`skills/AGENTS.md` 只管 `skills/` 之下。

- `CODING_STANDARDS.md` 是指定的准则来源：一个被改文件有它管辖时，不再用指令类文件（`CLAUDE.md`/`AGENTS.md`）评它；任何文件不同时被两类准则评判。
- 没有准则文件管辖某些被改文件是完整结果，不是缺口；搜索失败或范围不确定要如实记录为不确定，不记为"无准则"。
- 映射结果（哪个准则文件管哪些被改文件）传给 project-standards persona；空结果则跳过该 persona 并在覆盖说明中注明。
