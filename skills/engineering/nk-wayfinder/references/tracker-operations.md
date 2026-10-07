# Tracker 操作细则（GitHub Issues + `gh`）

> 本文件定义 map、child tickets、blocking 与 frontier 在 GitHub Issues 上的物理表达。原则：优先使用 GitHub 原生关系（sub-issues、blocked-by），因为 tracker UI 会可视化它们，人类不用打开 map 也能看到哪些 ticket 可拿；原生能力不可用时退回 body 约定。

## 前置检查与 label 准备

```bash
gh repo view --json nameWithOwner   # 确认远端与 gh 可用；失败则本技能不可用
```

所需 labels：`wayfinder:map`、`wayfinder:research`、`wayfinder:prototype`、`wayfinder:grilling`、`wayfinder:task`。缺失时创建：

```bash
gh label create wayfinder:map --color 1D76DB --description "Wayfinder decision map"
gh label create wayfinder:research --color 0E8A16
# …其余类推
```

## 创建 map

```bash
gh issue create --label wayfinder:map --title "<map name>" --body-file <body>
```

body 按 SKILL.md 的 map body 模板填写。Map 的 title 就是它的 name；所有引用都用 name 加链接。

## 创建 child tickets

先建全部 tickets，拿到编号后第二遍再 wire blocking edges。

1. **优先：GitHub 原生 sub-issues。** 用 GraphQL API 把 ticket 挂为 map 的 sub-issue（`addSubIssue` mutation，需要双方的 node id）。GitHub UI 会在 map 下直接列出 tickets。
2. **退回：body 约定。** ticket body 末尾加一行 `Part of: [<map name>](<map url>)`；查询时按 label + 正文中的 map 链接过滤。

无论哪种方式，ticket 都带 `wayfinder:<type>` label，body 是 `## Question` 一节。

## Blocking

1. **优先：GitHub 原生依赖关系。** 用 REST API `POST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by`（或对应的 gh api 调用）建立 blocked-by。UI 会展示依赖，frontier 一目了然。
2. **退回：body 约定。** ticket body 加一节：

   ```markdown
   ## Blocked by

   - [ ] [<blocker ticket name>](link)
   ```

   blocker 关闭后同步勾选；查询时核对链接所指 Issue 的当前状态及关闭原因。作废或未解决的 blocker 不视为已满足，先修订依赖。

先沿用 map 已记录的约定。只有确认原生能力不支持时才退回 body 约定并记入 Notes；网络、认证或权限失败应报告阻断，不切换表示或重复创建。写入结果不明时先查询核实。

## Claim 与 frontier 查询

- **Claim**：先核对无人认领，再执行 `gh issue edit <number> --add-assignee @me` 并复查归属。它不是原子锁；发现竞争先协调，同账号多会话须用会话标识或用户分工区分，不凭 `@me` 判断独占。
- **Frontier**：open、unblocked、unclaimed 的 tickets。基础查询：

  ```bash
  gh issue list --state open --search "label:wayfinder:research OR label:wayfinder:prototype OR label:wayfinder:grilling OR label:wayfinder:task" --json number,title,body,assignees,labels
  ```

  此命令仅为候选查询，不代表完整结果。核对分页，必要时用分页 API 取全本 map 的子项与依赖；不能用默认列表长度判断无剩余工作。再过滤掉已认领和依赖未满足的项：原生依赖查 `blocked_by`，body 约定读取链接并核实当前状态。属于哪张 map 由 sub-issue 关系或 `Part of:` 行判定。

## Resolution 与关闭

```bash
gh issue comment <number> --body-file <resolution-file>
gh issue close <number>
gh issue edit <map number> --body-file <merged-map-file>
```

Resolution comment 至少包含：答案本身、关键理由、解决中产生的 assets 链接、后续 tickets 依赖的事实（凭据位置、新 URL、数据规模等）。向 map 追加时遵循 Refer by name：`[name](link) — 一行 gist`。

## 并发

多个会话可能同时处理 unblocked tickets。写 map 前重新读取最新 body，只合入本轮增量，写后复查；检测到冲突就重新合并或协调，不用旧快照覆盖他人的记录。Assignee 操作可能成功但仍有竞争，不能把命令成功当作锁成功。不要抢占他人的 ticket；无人可处理时汇报阻塞或进行中状态。
