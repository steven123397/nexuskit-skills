# 编队与路由（选哪些 reviewer）

编队时读取本文件。reviewer 的共享方法路径和本次审查目的见 [reviewer-prompt.md](reviewer-prompt.md)；其他角色在 `personas/`。这些是提示词资产，不是可按名调用的 Agent：读取文件内容，用它初始化一个通用子代理。必须通过子代理执行，容量有限时分批；不可用时报告未完成。simplify 的三个角色由其公开入口提供，不在本表重复维护。

## 选择层次

**常驻（必选）**：`correctness-reviewer`。

**规范条件**：`project-standards-reviewer` —— 范围判定阶段的规范文件映射非空时运行；映射为空则跳过并在覆盖说明中注明（该 persona 不允许臆造准则）；搜索失败或不确定时照常运行并说明不确定性。

**通用条件**：

- `testing-reviewer` —— 测试文件、测试基础设施、mock、fixture 或测试 harness 行为有变化；或 diff 改变了有意义的运行时行为却没有相应测试工作。行为性触发需要具体 diff 证据：新增/改动的分支、状态变更、API/控制流行为、错误处理。仅因生产文件在场或非行为性编辑不选。
- `maintainability-reviewer` —— 模块职责、依赖方向、公共抽象或类型边界发生变化，存在可定位的耦合、规则漂移或契约维护风险。普通重复代码、无用包装、命名和删减建议由 simplify 分析，不因此重复派发本角色。
- `agent-native-reviewer` —— 面向 Agent 的功能或界面有变化（技能、提示词、工具、MCP、命令，或预期对 Agent 可见的产品能力）。
- `learnings-researcher` —— `docs/solutions/` 语料存在且按路径/标题的廉价搜索能找到与被改模块或模式的可信匹配；语料存在本身不足以触发。

**横切条件（按 diff 判定）**：

- `security-reviewer` —— 认证、公开端点、用户输入、权限（含控制可达性的特性开关）。
- `performance-reviewer` —— 数据库查询、数据变换、缓存、异步。
- `api-contract-reviewer` —— 路由、序列化器、类型签名、版本化；diff 改变了外部消费的契约才选，不是导出符号就选。
- `data-migration-reviewer` —— 仅当 diff 含迁移或 schema 工件（`db/migrate/*`、`schema.rb`、`structure.sql`、Alembic/Flyway/Liquibase 路径、显式回填/数据变换脚本）。模型层改动、纯查询重构、只引用列的序列化器不触发。
- `reliability-reviewer` —— 错误处理、重试、超时、后台任务。
- `adversarial-reviewer` —— 改动涉及认证/支付/持久化写入/事件发布/重试或并发语义/外部 API；或新增、改变了跨步骤状态转换、输入信任边界、资源释放/补偿路径，存在需要反例检验的不变量；或改动本身是**静默放行验证机制**（CI/CD 门禁、合并阻断检查、构建/部署步骤、覆盖率/lint 闸门、可能掩盖生产的测试基础设施）——此时必选。选择判据一句话："这个机制出错时，是大声失败还是静默放行？"
- `previous-comments-reviewer` —— **仅 PR 审查且该 PR 已有评审评论时**适用；无 PR 或 PR 尚无反馈时跳过（没有可核对的对象，空跑也花一份子代理开销）。

**栈专属条件**：`julik-frontend-races-reviewer`（Stimulus/Turbo、DOM 事件、异步 UI 的运行时行为变化）、`swift-ios-reviewer`（Swift/SwiftUI/UIKit、entitlements、Core Data、`.pbxproj`）。触发条件是相应栈**运行时行为**的变化，不是文件扩展名；路由不到就不加载，但不从编队目录删除。

**迁移风险附加**：迁移门禁命中且改动有风险（破坏性 DDL、回填、无默认值的 NOT NULL、列改名/删除）时，加 `deployment-verification-agent`，按统一审查 JSON 返回部署就绪缺口、残余风险和测试缺口。

## 散文类改动的特判

纯说明文字不因篇幅触发 adversarial；配置或指令实际定义了上述高风险行为或验证机制时仍按行为触发。不得仅按扩展名排除运行时配置。

不使用行数阈值，也不计算“可执行改动行数”。对每个条件 reviewer，以具体文件或 diff 片段说明命中的条件与可能失败的机制；相同条件不得因 diff 长短改变判定。证据不足时先做一次定向核对，仍不确定则记录覆盖限制，不编造触发理由。

## 编队宣布

派发前用一段话向用户宣布最终编队：常驻 reviewer 直说，条件 reviewer 各给一句被选中的真实原因（实际担忧，不是命中的关键词）。这是进度通报，不是阻塞性确认。

## 关于跨模型复核

不内置跨模型对抗审查流程。若用户同时装有多个客户端，可一句话建议：把写好的审查条目交给另一个客户端复核一遍，作为独立的第二意见。
