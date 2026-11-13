---
name: constraint-driven-development
description: Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which dimensions matter, supplies sane default thresholds when they have no number in mind, records everything in CONSTRAINTS.md, and watches the diff for a weakened bar — new @ts-ignore or eslint-disable suppressions, skipped or deleted tests, assertions stripped out, unimplemented stubs, thresholds edited down. Use when no quality bar is written down, when the user says "set up constraints" or "define our standards", when the user wants dimensions they care about — accessibility, web performance, coverage — set up as enforced constraints, when an agent keeps silencing checks or skipping tests to get to green, when you need a coverage or performance threshold and don't know what number to pick, or when an agent writes more code than anyone will read.
---

# Constraint-Driven Development

## 概览

本技能包里的其他 skill 描述的是“好代码”长什么样：`code-review-and-quality` 给出五个维度，`test-driven-development` 给出一个开发循环，`security-and-hardening` 给出一份威胁清单。但这些规范都只停留在说明文字里，agent 读完可能照做也可能不照做，而且没有任何一条能延续到当前会话结束之后。

这个 skill 产出的是另一回事：一份属于**本项目**的质量基线书面记录——带有明确数值，能跨对话持久存在，并且可以被自动化检查。

背后的原因很现实。当你自己亲手写代码时，靠通读代码就能判断它好不好。但一个 agent 一个下午写出的代码，就已经超过你一整周能逐行审完的体量，于是“质量判断”不得不从你的脑子里，挪到围绕开发循环自动运行的检查上。这些检查必须真实存在，必须用上你亲手定下的数值，而且触发点必须离编码现场足够近，好让 agent 自己就能把产出改合格。

Spec-driven development 说清楚要构建什么。Test-driven development 证明它能工作。Constraint-driven development 定义“好到可以发布”意味着什么——在任何人在 pull request 里为此争吵之前。

## 何时使用

在以下情况应用这个 skill：

- 启动一个项目或一个重要功能，而没有任何质量线被写下来
- 用户要求 "set up constraints"、"add quality gates"、"define our standards" 或 "stop the agent shipping junk"
- Agent 产出的代码体量已经没人能逐行审阅了
- CI 有检查，但没人说得清哪些会阻塞合并、哪些只是摆设
- 覆盖率、性能或无障碍性的数字在每个 PR 上被争论，而不是被一次性决定
- 你正准备运行 `/nk-build auto` 或任何自主循环，而它和 main 之间唯一的屏障是一套 agent 自己写的测试

**何时不要使用：**

- 项目已经有 `CONSTRAINTS.md` 而用户并不想改它——去读它并遵循它
- 一次性脚本、spike、用完即弃的原型
- 用户现在就要 code review（`code-review-and-quality`）或要搭 CI pipeline（`ci-cd-and-automation`）
- product-market fit 之前的代码，预期寿命两周——下面的 floor 仍然值得，其余的不值得

## 加载约束

这场访谈需要真人用户在线参与交互。**不要在非交互上下文中运行它**（如 CI、`/loop` 或无人值守的自主运行）。如果你正处于这类环境中且项目尚无约束，请直接套用下方的 Floor 基线，注明你这么做了，并把其余待定项标记出来交由人工处理。

## 流程

### Step 1: 先检测，再提问

能读到的东西绝不要问。在第一个问题之前，先收集：

| 看什么 | 去哪看 |
|------|---------------|
| 语言与技术栈 | `package.json`、`pyproject.toml`、`go.mod`、`Cargo.toml` |
| 测试 runner | dev 依赖、`test` script、已有的测试文件 |
| 已有的 linter | `eslint.config.*`、`biome.json`、`.ruff.toml` |
| 当前覆盖率 | `coverage/` 输出，或把套件跑一遍 |
| CI | `.github/workflows/`、`.gitlab-ci.yml` |
| Agent harness | `.claude/`、`.codex/`、`AGENTS.md` |

用两行汇报你发现的东西，然后只问剩下的。

### Step 2: 四个问题，每个都带默认值

遵循 `interview-me` 的一次一问纪律，只有一个变化：这里的每个问题都有默认值，所以 "I don't know" 也是一个完整的答案，并且仍能产出可用的配置。

```
Q1: Beyond the floor, which of these do you want enforced?
    (a) Test coverage on new code
    (b) Security scanning
    (c) Performance budgets
    (d) Accessibility
    (e) Architecture boundaries
GUESS: (a) and (b) — you have a test runner already and you're handling user input.
DEFAULT if unsure: (a) and (b).
Say what each pick costs: (c) and (d) need a running URL, (e) needs a rules file written.
```

```
Q2: When a check fails while the agent is mid-task, should it block or warn?
GUESS: Block. You're running agents unattended and a warning nobody reads is a warning.
DEFAULT if unsure: Block on the floor, warn on everything else for the first two weeks.
```

```
Q3: Do you have target numbers in mind, or should I measure where you are today and hold that line?
GUESS: Measure. Most teams don't have a number, and an invented one gets ignored.
DEFAULT if unsure: Measure and hold. See "Ratchets" below.
```

```
Q4: What's the slowest check you'll tolerate before the agent hands work back?
GUESS: About 90 seconds. Longer and you'll stop running it.
DEFAULT if unsure: 90 seconds at task end, unlimited in CI.
```

最多问四个问题就停。一场扯上十二个问题的访谈，只会换来一份没人看得懂的配置，以及一个后悔开启这场对话的用户。

### Step 3: 写出 CONSTRAINTS.md

整个仓库根目录只放这一个文件。无论哪种 harness 上的哪个 agent 都能直接读取它；只要它有变动，改动就会直接出现在代码 review 中——这正是它本该接受审视的地方。

```markdown
# Constraints

Last reviewed: 2026-08-08 by @addy

## Floor (always enforced, no setup required)

- No new suppression comments: `@ts-ignore`, `eslint-disable`, `# noqa`, `# type: ignore`
- No unimplemented stubs: `throw new Error("Not implemented")`, empty `catch {}`
- No skipped or deleted tests without a reason in the commit message
- No secrets in source
- This file does not get weakened to make a change pass

## Enforced with numbers

| Dimension | Rule | Checked by | Runs at |
|-----------|------|-----------|---------|
| Types | Zero type errors | `tsc --noEmit` | every edit |
| Lint | Zero errors from our config | `biome check` | every edit |
| Secrets | No secrets in source | `gitleaks dir . --redact` | every edit |
| Coverage | Changed lines ≥ 80% covered | `vitest run --coverage` + git diff | task end, CI |
| Security: code | Nothing at high or above | `npm run check:security` | CI |
| Security: deps | Nothing at high or above | `osv-scanner scan source -r .` | CI |
| Accessibility | Zero critical or serious | `npm run check:a11y` | preview deploy |
| Performance | LCP ≤ 2500ms, CLS ≤ 0.1 | `lighthouse $PREVIEW_URL --output=json` | preview deploy |

Every row names the command that produces the verdict. A dimension with a
number and no command in this column is an aspiration, not a constraint.

## Measured, not yet enforced

| Metric | Today | Direction |
|--------|-------|-----------|
| Project coverage | 62.4% | must not fall |
| Bundle size (main) | 184 kB | must not grow |

## Exceptions

| ID | Rule | Path | Reason | Owner | Expires |
|----|------|------|--------|-------|---------|
| W1 | `no-explicit-any` | `src/legacy/**` | Rewrite tracked in ENG-441 | @addy | 2026-11-01 |
```

然后在项目的 agent 规则文件（`AGENTS.md` / `CLAUDE.md`）里加一行：`Read CONSTRAINTS.md before writing code. Do not weaken it to make a change pass.`

### Step 4: 为每个维度安装它需要的东西

选定一个维度，就意味着必须装上对应的检查工具。不要只给用户留下一串数字却不配落地机制，也不要在明明有业界事实标准工具的情况下，自己凭空造一个 checker——上表所列的工具之所以入选，是因为它们的规则格式与阈值标准正是整个生态共同对齐的准绳，这样团队原有的配置也能继续生效。

| 维度 | 工具 | 安装 | 运行 | 拦截条件 |
|-----------|------|---------|-----|---------|
| 类型 (TS) | tsc | 已内置 | `tsc --noEmit` | 任何错误 |
| 类型 (Python) | mypy | `pip install mypy` | `mypy .` | 任何错误 |
| Lint | 你已有的配置 | 已内置 | `eslint .` / `biome check` / `ruff check` | 任何错误 |
| 覆盖率 (JS) | 你的 test runner | Vitest：`npm i -D @vitest/coverage-v8`；Jest：已内置 | `vitest run --coverage`（或 `jest --coverage`） | 变更行的覆盖率 |
| 覆盖率 (Python) | pytest-cov | `pip install pytest-cov` | `pytest --cov --cov-report=lcov` | 同上 |
| Security: 代码 | Semgrep | `pipx install semgrep` | `npm run check:security`（见下） | high 或 critical，含旧版 `ERROR` |
| Security: secrets | gitleaks | `brew install gitleaks`（macOS）/ `scoop install gitleaks`（Windows） | `gitleaks dir . --redact --no-banner` | 任何 finding |
| Security: 依赖 | osv-scanner | `brew install osv-scanner`（macOS）/ `scoop install osv-scanner`（Windows） | `osv-scanner scan source -r .` | high 及以上 |
| 性能: 页面 | Lighthouse | `npm i -D lighthouse` | `lighthouse $URL --output=json --quiet` | LCP、CLS、performance score |
| 性能: bundle | size-limit | `npm i -D size-limit` | `size-limit --json` | 每个 entry 的字节预算 |
| 无障碍性 | axe-core | `npm i -D @axe-core/cli` | `npm run check:a11y`（见下） | critical 或 serious 为零 |
| 架构 | dependency-cruiser | `npm i -D dependency-cruiser` | `depcruise --validate src` | 任何违规 |
| 断言质量 | Stryker | `npm i -D @stryker-mutator/core` | `stryker run --mutate <changed files>` | mutation score |

跳过下面五件事，它们会反咬你一口：

1. **gitleaks 的 `--redact` 不是可选的。** 没有它，被匹配到的 secret 会落入 agent 的 transcript——这正是泄露的 key 进入日志、summary 或 commit message 的路径。报告规则和位置，绝不报告值。
2. **Lighthouse 和 axe 需要一个 URL。** 它们只能对运行中的应用生效，所以它们属于 runtime 阶段，对准一个 preview deploy 或你先启动的本地 server。如果项目没有可访问的 URL——CLI、库、桌面应用——说清楚，然后砍掉这个维度，而不是发明一个跑不起来的检查。
3. **把贵的检查限定在 diff 上。** 对整个仓库跑 `stryker run --mutate` 要几个小时，然后就会被人关掉；只跑一次变更触及的文件不到一分钟。Semgrep 也一样，它接受一个路径列表。
4. **覆盖率不需要第二次 test run。** 读你的套件已经在写的 lcov，把它和 `git diff` 求交集。为了拿一个数字而把套件跑两遍，是让人最快开始憎恨这件事的办法。
5. **Semgrep 注册表中的规则可以免费运行，但二次分发前请先核对许可证条款。** 如果法务团队对此敏感，`opengrep` 是现成的可无缝替换的 drop-in fork，沿用相同的规则格式与 JSON 输出。

`semgrep scan` 和 `axe` 在发现 findings 时仍可能以 0 退出；把 [scripts/quality-gate.mjs](scripts/quality-gate.mjs) 复制到项目的 `scripts/` 目录，用它在这些阈值上执行拦截。把 scanner 放在 `&&` 之前，这样扫描失败会中止命令。

把每一个都加进项目自己的 script，让它在没有 agent 的情况下也可复现：

```json
{
  "scripts": {
    "check:fast": "tsc --noEmit && eslint . && gitleaks dir . --redact --no-banner",
    "check:task": "npm run check:fast && vitest run --coverage",
    "check:security": "semgrep scan --config p/default --strict --json > semgrep-results.json && node scripts/quality-gate.mjs semgrep semgrep-results.json",
    "check:a11y": "axe \"$PREVIEW_URL\" --tags wcag2a,wcag2aa,wcag21aa --stdout > axe-results.json && node scripts/quality-gate.mjs axe axe-results.json",
    "check:full": "npm run check:task && npm run check:security && osv-scanner scan source -r ."
  }
}
```

这个映射比工具本身更重要。`check:fast` 是每次编辑之后运行的，`check:task` 是 agent 自以为完成时运行的，`check:full` 在 CI 里运行。在 preview 可访问之后再跑 `check:a11y`，并设置 `PREVIEW_URL`（示例使用 POSIX shell 语法）。

在对外宣称某一行约束“已被强制执行”之前，务必拿一条已知违规样本和一条干净对照样本，跑一遍它真正的 CI 命令。确认触发违规时命令退出失败、干净对照样本能通过，且 scanner 自身报错时命令也会跟着失败。带有严重度阈值时，再确认低于阈值的 finding 确实能放行。每个维度都要这样逐一验证，包括覆盖率和 Lighthouse：光会生成报告，并不代表 `CONSTRAINTS.md` 里定下的那个数字真的起了强制约束作用。

这些命令此时会同时出现在两处——`CONSTRAINTS.md` 的 `Checked by` 列，以及这些 scripts 里。`CONSTRAINTS.md` 才是权威来源：它不仅记录命令，还连带写明了每条规则背后的理由，而且每次变更都会进入代码 review。那些 scripts 只是必须与它保持一致的便捷封装，绝不是第二个权威来源；一旦发生漂移，以文件为准。

### Step 5: 把它接到生命周期上

最常见也最致命的一个错误，就是在所有时机都跑全套检查。会拖慢 agent 节奏的检查迟早会被人关掉；而一个已经被人关掉的 gate 比根本没有 gate 更糟，因为它会让人误以为质量红线依然存在。

| 阶段 | 命令 | 运行什么 | 预算 |
|-------|---------|-----------|--------|
| BUILD | `/nk-build` | 类型、lint、secrets、floor | 5 秒内，只查变更文件 |
| VERIFY | `/nk-test` | 相关测试、变更行的覆盖率 | 90 秒内 |
| REVIEW | `/nk-review` | 全部，外加下面的 guards | 以分钟计 |
| SHIP | `/nk-ship` | 方向检查，不许回退 | CI |

两条让这件事保持在可忍受范围内的规则：

1. **限定到 diff。** 检查这次变更触及的行，而不是整个仓库。变更行的覆盖率是 agent 能推动的数字；项目覆盖率是它继承来的数字。
2. **成本决定位置。** 任何超过几秒钟的东西都要挪出编辑循环。对整个仓库做 mutation testing 要几个小时；对变更触及的文件做，不到一分钟——这就是“人们会运行的检查”和“人们不会运行的检查”之间的差别。

### Step 6: 守护质量线本身

总会有人指出：如果 agent 既写代码又写检查，那检查证明不了什么。这个说法对一半，而且值得围绕它做工程。

Agent 不会精心构造巧妙的漏洞。它们撞上一个红色检查，然后走通往绿色的最便宜的路。在 review 时盯住 diff 里的这五个动作：

1. **阈值动了。** 预算被调低，severity 被降级，某个检查被移出快速阶段。把 `CONSTRAINTS.md` 与它在 branch 起点处的状态做对比。
2. **测试变简单了。** 加了 `.skip`，删了测试文件，从留下的测试里抽走了断言。
3. **checker 被静默了。** 新增了 `@ts-ignore` 或 `eslint-disable`。尤其要重点盯防这四种抑制注释，因为它们会直接关掉你最依赖的防线：`istanbul ignore` 把代码从覆盖率分母里剔除而非真正去测它，`Stryker disable` 藏起原本已存活的 mutant，`nosemgrep` 和 `gitleaks:allow` 干的则是把安全 scanning finding 压下去的同一件事。
4. **工作没做完。** 一个直接抛异常的 stub、一个把失败静默吞掉的空 `catch`，或者本该写实现的位置上只占着一个 `TODO`。
5. **私自新增了例外。** Exceptions 表里多了一行没人讨论并批准过的记录。

以上检查都不需要 `git diff` 之外的任何工具。收紧质量线应当安静放行；放松或绕过质量线则应当响亮告警。

与带数字指标的维度不同，floor 并没有统一公认的业界事实标准工具，因此每当要求 agent 执行 floor 检查时，它们往往倾向于从零自写一个 checker，结果两个 agent 就能写出两套不一致的脚本。这五项检查的参考实现已随本 skill 一并提供，见 [references/floor-guard.md](references/floor-guard.md)（按 diff 作用域运行，返回退出码 `0`/`1`/`2`，匹配模式可按技术栈调整）。请直接复用它，而不要重新造轮子——原因与每个维度都指名标准工具完全一致：让检验机制在每次运行、每个技术栈之间保持一致。

**不同检查“循环自证”的程度并不相同。** 拿一个问题给它们排个序：agent 能不能写一段根本跑不通的烂代码，却依然让这项检查通过？

- **External（外部基准）** —— `axe-core` 内置的是 WCAG 规范，`osv-scanner` 查的是公开漏洞库，Lighthouse 实测的是真实浏览器表现。在这些外部硬标准面前，agent 讨不到半点便宜。
- **Project（项目规范）** —— 你们自己的 lint 规则、架构分层边界。配置文件由人工掌控。
- **Suite（测试套件）** —— 你们自己写的测试。它日常最有价值，却也是唯一真正存在“自己证明自己（循环自证）”风险的一类。

完全由第三种构成的质量防线，价值远低于至少包含一项外部独立校验基准（outside opinion）的质量体系。请确保检查清单里至少存在一项外部约束。

### Step 7: 没有数字时用 Ratchet（棘轮）

在一个 62% 的代码库上设 80% 覆盖率，你会得到一个永远红色的 build，然后是一个学会无视红色 build 的团队。

另一种做法不需要任何决策：记录你现在在哪里，然后拒绝变差。把它放进 "Measured, not yet enforced" 表，带上今天的数字和一个方向。每次检查都对照记录值，而不是对照愿景。当数字变好时，更新它；当它下滑时，那就是 finding。

这也恰好回应了业界对模型训练机制的一个合理质疑：模型在训练中因“通过测试”而获得奖励，这种信号几秒钟内就能完成评估；可架构腐坏往往几个月后才会显形，永远传导不到模型权重上。一个 ratchet 棘轮检查正是那项缺失的惩罚机制，直接钉在构建流水线一眼就能拦住的位置。

## 合理默认值

当用户没有意见时，用这些。它们的选取标准是：多数代码库在第一天就能满足。

| 约束 | 默认值 | 为什么是这个数字 |
|------------|---------|-----------------|
| 变更行的覆盖率 | ≥ 80% | 高到足以逼出一个测试，低到足以放过一行配置 |
| 项目覆盖率 | 今天的值，不许下降 | 采纳它不需要争论 |
| Mutation score（如果用） | 起步 ≥ 60% | 对一个从没被 mutate 过的套件这是典型值；80% 是成熟态 |
| 依赖漏洞 | high 及以上不许有 | 低于那个的多半是噪音 |
| LCP | ≤ 2500 ms | Core Web Vitals 的 "good" 阈值 |
| CLS | ≤ 0.1 | 同上 |
| 无障碍性 | axe 的 critical 或 serious 违规为零 | moderate 和 minor 级别问题通常存在视场景商榷的余地 |
| 例外有效期 | 90 天 | 足够排期修复，也不至于久到被人遗忘 |
| Ratchet 容差 | 0.5% | 在无关文件变动轻微拉动数字时吸收正常波动 |

把数字和理由一起说出口。一个没有依据的阈值会被下一个撞上它的人删掉。

## 升级路径

约束的落地有三档逐步加码的执行硬度，从第一档起步即可。

1. **仅书面约定。** `CONSTRAINTS.md` 存在且 agent 会读取它。零接入成本，能防住非故意的疏漏，依赖 agent 自觉遵守。
2. **脚本化。** 配一个 `npm run check`（或 `make check`）来运行快速检查，接入 agent 的 post-edit hook 和你的 CI 流水线。结果确定，无需引入新依赖。
3. **工具化。** 上专门的 runner，统一处理 diff scoping、性能预算、ratchet 和 guard 检查。当配置复杂到一个 shell script 装不下时再启用它。[references/floor-guard.md](references/floor-guard.md) 里的 floor-guard 参考实现，就是这一层里 guard 检查那一半的起点。

多数项目止步于第 2 档就够了。只有当你要维护超过大约三十行跑检查的 shell 脚本时，再升级到第 3 档。

**第一次运行可以只有 floor。** Floor guard 只针对 diff、不需要安装任何额外工具，所以第一天就能直接启用 floor，再随着每个工具的安装逐个补上带数字指标的维度——不必非得在第一次 commit 受保护之前把所有 checker 全部搭齐。需要按机器级全局安装的安全工具（gitleaks、osv-scanner）如果不想装进开发笔记本里，也可以只在 CI 中运行；在 `Runs at` 列里明确声明每个维度具体跑在哪里。

## 常见合理化借口

| 合理化借口 | 现实 |
|--------|---------|
| "等代码稳定了我们再加约束" | 代码在变动演进期被纵容出的任何形态，最终都会跟着一起固化下来 |
| "测试就是我们的约束" | 你自己写的测试只能证明你和自己意见一致；它们对变更代码的覆盖率、依赖风险或 bundle 增长什么都没说 |
| "我们达不到 80% 覆盖率" | 那就别设 80%。设今天的数字并守住它 |
| "这会让 agent 变慢" | 只有当你把慢检查放进快速循环时才会。那是放置错误，不是反对约束的论据 |
| "我会记得我们的标准是什么" | Agent 不会，而它正在写大部分代码 |
| "约束会挡住我们发布" | 一个带 owner 和日期的例外能放行你。删掉约束则永远放行所有人 |

## 危险信号

如果你注意到这些，停下来重新考虑：

- 访谈超过了四个问题，或产出了一份用户自己解释不了的配置
- 设了一个代码库今天就不达标的预算，且没有达标的计划
- 一个维度带着数字写进了 CONSTRAINTS.md，背后却没有工具
- 明明存在业界事实标准的 checker，你却手工自造了一个，导致团队已有的配置被无视
- 每个约束都靠项目自己的测试套件自查，没有任何外部独立校验基准
- `CONSTRAINTS.md` 和那个尚未达标的功能出现在同一个 commit 里
- 一个例外没有 owner，或到期日在一年以上
- Agent 提议放松阈值而不是修代码
- 慢检查落进了编辑循环，有人已经开始传 `--no-verify`
- 自从 `CONSTRAINTS.md` 写下后就没人打开过它

## 验证

当以下条件满足时，说明本 skill 被正确应用：

- [ ] `CONSTRAINTS.md` 存在，其中每个数字都有陈述的理由
- [ ] Floor 被强制执行，并且在当前代码库上无需任何改动即可通过
- [ ] 用户挑选的每个维度都有安装好的工具和今天就能运行的命令
- [ ] 每条约束都写明它运行在哪，且快速阶段保持在几秒之内
- [ ] 至少一条约束是外部的（不由本项目自己的测试裁决）
- [ ] 仅测量的指标记录了今天的值和一个方向
- [ ] 例外有 owner 和到期日
- [ ] `AGENTS.md` 或 `CLAUDE.md` 指向这个文件
- [ ] 在当前分支上试运行一次，没有出现用户未曾认可的失败项
- [ ] 每条被强制执行的命令都在故意违规和 scanner 报错时失败、在干净对照上通过，并保持约定的严重度阈值

## 另见

- `interview-me` —— 本 skill 的 intake 借用的一次一问纪律
- `code-review-and-quality` —— 如何 review；本 skill 决定 review 执行什么
- `ci-cd-and-automation` —— 搭建这些约束运行其中的 pipeline
- `test-driven-development` —— 覆盖率和 mutation 约束所度量的那个套件
- `security-and-hardening` —— security 维度应当包含的内容
- `performance-optimization` —— 性能数字的来源
