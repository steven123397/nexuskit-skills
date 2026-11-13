---
description: 定义并执行本项目质量标准 — 访谈、合理默认值、CONSTRAINTS.md
disable-model-invocation: true
---

调用 constraint-driven-development skill。

$ARGUMENTS

不带参数时的默认行为：为本仓库设置 constraints。

1. **先检测。** 读取 package.json / pyproject.toml / go.mod、test runner、现有 lint 配置、当前覆盖率输出、CI workflows，以及正在使用的 agent 宿主环境（harness）。用两行概括你的发现。绝不询问任何你自己能直接读到的东西。

2. **访谈，最多四个问题。** 一次一个，每个问题都附上你的最佳猜测和一个可用的默认值，让用户回答“我不知道”时也能产出一份可用配置：
   - 除了底线（floor）之外还需要哪些维度（coverage、security、performance、accessibility、architecture）
   - 任务中途某项检查失败时，是阻断（block）还是警告（warn）
   - 采用目标数值，还是先测量今日基准值并守住它们
   - 把工作交还给人工之前，可容忍的最慢单次检查耗时

3. **在仓库根目录编写 CONSTRAINTS.md**，包含 Floor 部分、被强制执行的数值、仅测量类指标及其今日数值，以及一张带负责人（owner）和到期日期的例外（exceptions）表。每个数值都要写明设定理由。

4. **为每个选中的维度安装所需工具。** 一个维度有数值要求却背后没有工具支撑，那只是一纸愿望。使用事实标准工具，让现有配置继续可用：代码扫描用 Semgrep，secrets 用 gitleaks（始终带 `--redact`），依赖审计用 osv-scanner，accessibility 用 axe-core，web vitals 用 Lighthouse，bundles 用 size-limit，boundaries 用 dependency-cruiser，断言质量用 Stryker。在 CONSTRAINTS.md 中把确切命令记录在每条规则旁边。Accessibility 和 performance 需要一个可运行的 URL；如果项目没有，如实说明并舍弃该维度，而不是凭空编造检查项。把这些命令作为 check:fast / check:task / check:full 添加到 package.json。

5. **按耗时成本安排每项检查。** Types、lint 和 secrets 放在编辑循环（edit loop）里（秒级）。相关 tests 和变更行覆盖率放在任务结束时（90 秒以内）。其余全部放在 review 或 CI 中。将检查范围限定在 diff，而不是扫描整个仓库。

6. **让 agent 指向它。** 在 CLAUDE.md/AGENTS.md 中加一行，告诉 agents 阅读 CONSTRAINTS.md，且绝不允许为了让某个变更通过而弱化它。

7. **验证。** 对当前分支运行这些 constraints。如果某项失败而用户认为不合理，现在就修正该 constraint，而不是留下一个人们会学着无视的门禁。

子命令：
- `/nk-constraints check` — 对当前分支运行现有 constraints 并报告
- `/nk-constraints guard` — 在 diff 中检查被弱化的标准：调低的阈值、被跳过或删除的 tests、新增的抑制（suppression）注释、未完成的占位桩（stubs）、新增的例外（exceptions）
- `/nk-constraints ratchet` — 把今天的测量值记录为不得下降的 floor
