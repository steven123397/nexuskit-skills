# 规划研究员的任务说明

选定研究员后，仅读取下面对应的共享方法，连同该行任务目的、规划上下文和当前阶段的结果要求派发。同时传入选中方法的绝对路径，供子代理解析相对引用。未列出的本技能专用角色仍在 `agents/`，不预读整库。不支持子代理时，主会话按相同方法内联完成。

| 共享方法 | 本技能的任务目的 |
| :-- | :-- |
| [best-practices-researcher](../../conventions/agents/best-practices-researcher.md) | 提炼实现约束、推荐与反模式、验证要求及影响顺序或范围的取舍；只保留改变 plan 的证据，必要示例紧凑并贴合仓库。 |
| [data-integrity-guardian](../../conventions/agents/data-integrity-guardian.md) | 识别迁移安全、事务边界、一致性不变量、隐私约束、回滚、回填或双写及验证查询；优先影响实施顺序和验收的风险。 |
| [data-migration-reviewer](../../conventions/agents/data-migration-reviewer.md) | 形成 expand/contract 顺序、回填与分批、双写窗口、部署风险、回滚、schema 工件、验证和监控要求。仅在有真实 diff 与基准时检查漂移；返回规划建议，不输出审查 JSON。 |
| [deployment-verification-agent](../../conventions/agents/deployment-verification-agent.md) | 形成上线前检查、部署顺序、验证查询、监控、回滚、责任与停止/继续条件。没有 diff 时依据拟议变更分析，不假装已经审查实现。 |
| [framework-docs-researcher](../../conventions/agents/framework-docs-researcher.md) | 核实具体版本的行为、支持的 API、迁移约束、集成方式、破坏性变化和测试影响，优先会改变技术做法或顺序的官方依据。 |
| [learnings-researcher](../../conventions/agents/learnings-researcher.md) | 检索全部经验类型，提炼约束、顺序风险、可用模式、失败先例、验证影响及实施前应读的经验；不只查架构或规划文档。 |
| [pattern-recognition-specialist](../../conventions/agents/pattern-recognition-specialist.md) | 寻找可沿用的模式、反模式与重复风险、命名和边界约定及参照文件，帮助实施者选定做法。 |
| [performance-oracle](../../conventions/agents/performance-oracle.md) | 识别瓶颈、扩展风险、数据量假设、缓存与分批需求、性能剖析和基准策略，优先会改变范围、顺序或验收的内容。 |
| [security-sentinel](../../conventions/agents/security-sentinel.md) | 形成威胁模型、敏感边界、认证授权与隐私控制、测试和发布防护要求，优先会改变设计、范围、顺序或验收的可信风险。 |
| [web-researcher](../../conventions/agents/web-researcher.md) | 寻找当前权威文档、实现取舍、生态选项、版本行为、集成与迁移限制；优先改变实现决定的依据，市场与灵感仅在影响范围或做法时纳入。 |

## 返回方式

阶段 1 需要保留长材料时写到调用方指定的绝对路径，只返回关键结论、重要反证、限制和路径（通常 3–5 行，不为行数删掉阻断）；短结果直接返回并说明未另建报告。工具不可用或失败直接报告，不伪造文件。阶段 5.3 的章节深化按 [deepening-workflow.md](deepening-workflow.md) 的直接/文件模式返回，不额外生成另一份报告。

结果围绕会改变规划的约束、依据、建议、验证和未决问题组织，不要求每个角色写一套固定栏目。经验检索保留来源、适用条件和已淘汰方案；迁移分析保留顺序、验证、回滚和开工前问题；部署分析覆盖检查、监控、责任与停止条件。SQL 等证据仅在所选阶段允许时给出，深化阶段仍遵守不写实现代码与命令的要求。

网络调研的研究价值、来源和体量按 [网络调研摘要](../../conventions/research-digest.md)；其研究目的仍由上面的规划调用说明限定。
