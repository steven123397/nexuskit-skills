# 实施底线片段（维护源）

<!-- fragment: work/verification -->
未在终端实际运行的测试、检查或走查，不记为通过；无法运行的项目明确标为“未验证”。
<!-- /fragment -->

<!-- fragment: work/settled-decisions -->
Plan 或需求中已标注为用户敲定的决定，执行时不得擅自推翻；若事实证明不可行或有破坏性，停下报告证据。
<!-- /fragment -->

<!-- fragment: work/escalate -->
只有范围外溢、不可逆或破坏外部契约、用户可见行为分歧、安全权限变更、或外部硬阻断需要向用户确认；局部、可逆、有惯例的实现细节由 Agent 自行决定并说明理由。
<!-- /fragment -->

<!-- fragment: work/subagents -->
子代理不提交 Git；返回结果不触发提交。主会话核对并整合实际改动，亲自验证待交付状态后，按已验证的交付变化调用 [/nk-commit](../nk-commit/SKILL.md)。
<!-- /fragment -->
