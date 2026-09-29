# 沉淀模式细则

## 1. 定位与采样

**定位本次结论**：以当前会话的排查过程、失败尝试、修复验证、已采纳决定与实践证据为主。需要补充事实时用 `git log`、`git diff` 核对关联提交与改动；不默认搜索历史会话。明确复盘指定历史材料时由入口先走 retro，再将合格结论交到这里。

**一次一条**：一个会话产出多条经验时分多次运行。交叉引用在草稿之间缝合，会把"第 3 条"这类草稿编号泄漏进成文。

**语料优先采样**：写 frontmatter 前先看 `docs/solutions/` 既有条目——目录优先沿用，`component`、`root_cause`、`tags` 优先复用既有拼写。规则见 [`../../conventions/solution-schema.md`](../../conventions/solution-schema.md) 第二章，此处不重述。

**重叠判定**：检索同问题域的既有条目，按问题陈述、根因、方案、引用文件、预防规则五个维度评估：

| 重叠 | 动作 |
| :-- | :-- |
| 高（基本相同的问题与方案） | 更新既有条目：保留路径与 frontmatter 结构，更新正文、示例与预防建议；不建新文档 |
| 中（同域，不同角度/根因/方案） | 正常新建；在汇报中标注为审计候选 |
| 低/无 | 正常新建 |

更新而非重复新建的原因：两份描述同一问题的文档必然逐渐漂移；新上下文更新鲜，并入既有条目。

**文件名**：`[problem-slug].md`，不加日期后缀（`date` frontmatter 字段即创建日期）。写前确认目标路径不存在；已存在且覆盖同一问题则走更新，不同问题则换明确的 slug，不覆盖。

## 2. 编写

模板与字段以 [`../../conventions/solution-schema.md`](../../conventions/solution-schema.md) 第三、四章为准。写作纪律：

- **行为断言先读源码**：断言代码行为（枚举值、状态语义、限制、默认值）前，读当前树的定义行并在文中标注 `file:line`；无法核实的断言软化或注明"按本次会话结论"，不写成事实。
- **合并状态引用 PR 编号而非裸 SHA**：SHA 会被 rebase/squash 重写；"已在 X 修复"要求修复在当前树可达，否则写为待定（如"已在 #123 打开，本文撰写时未合并"）。
- **流程复盘线**：工作流/协作过程本身的问题用 `workflow_issue`（Knowledge 轨），正文同样走模板：当时怎么卡住、根因在流程哪个环节、以后怎么防。
- **可检索性**：标题使用未来任务会出现的模块、症状或决定名称；`component`、`module`、`tags` 沿用项目术语。Knowledge 写明 `applies_when`，Bug 保留具体错误或症状。检查这些信息能否对应真实查询，不用泛称标题、同义标签堆砌或另建强制索引。

## 3. 可选增强评审（按 problem_type 映射）

支持子代理的客户端仅读取下表选中的共享方法，连同该行目的及本节返回要求初始化通用子代理；不支持时在主会话内联评审。派发时同时传入选中方法的绝对路径，供子代理解析相对引用。评审只针对文档与示例，不修改产品代码；无收益则跳过本阶段。

| problem_type / 情形 | 共享方法 | 文档评审目的 |
| :-- | :-- | :-- |
| `performance_issue` | [performance-oracle](../../conventions/agents/performance-oracle.md) | 核实瓶颈类型、修复原理、测量证据和扩展假设，补充复发监控建议；不提出无关优化。 |
| `security_issue` | [security-sentinel](../../conventions/agents/security-sentinel.md) | 核实漏洞类别、利用路径、修复效果、残余限制和预防办法；不扩展为全仓安全审计。 |
| `database_issue` | [data-integrity-guardian](../../conventions/agents/data-integrity-guardian.md) | 核实受影响的不变量、修复如何保护它、验证证据、回滚或迁移限制及复用前提。 |
| 反复出现 / 疑似反模式 | [pattern-recognition-specialist](../../conventions/agents/pattern-recognition-specialist.md) | 说明导致或避免问题的模式、其他出现位置、识别方法及经验可推广的边界。 |
| 需要业界实践佐证 | [best-practices-researcher](../../conventions/agents/best-practices-researcher.md) | 补充预防指引、权威引用、准确术语与取舍，纠正过度泛化，使经验可复用。 |
| 需要框架/库官方文档佐证 | [framework-docs-researcher](../../conventions/agents/framework-docs-researcher.md) | 用官方依据核实经验原理、版本限制和术语；补充能验证、限定或改善结论的引用。 |

按 [`../../conventions/subagent-results.md`](../../conventions/subagent-results.md) 直接返回紧凑的文档修订建议、证据、适用限制和预防要点；只评估当前经验，不额外生成全仓审计报告。

评审发现由主会话裁决并落到文档；子代理不直接改知识库文件。

## 4. 返回入口

返回条目路径、类型、证据与验证边界、重叠处理、已采纳的增强意见，以及术语和定向审计信号。增强修改完成后回到入口，统一处理术语、可见性、最终两项自检、提交与报告；本材料不自行收尾。

术语涉及行为规则（生命周期、状态流转）时，返回当前源码依据；需 Fold / Retire / Scrub 时只报告审计信号，不在沉淀中执行。
