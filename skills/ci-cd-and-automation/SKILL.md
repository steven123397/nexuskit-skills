---
name: ci-cd-and-automation
description: Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies.
---

# CI/CD and Automation

## 概览

把质量门禁自动化，确保任何变更在通过测试、lint、类型检查和 build 之前都无法进入生产环境。CI/CD 是落地其他所有 skill 纪律的强制执行机制——它能拦住人类和 agents 容易遗漏的问题，而且对每一次变更都会一视同仁地严格执行。

**质量左移（Shift Left）：** 尽可能在 pipeline 的更早阶段就把问题拦下来。在 lint 阶段揪出的 bug 只需几分钟就能修好；同一个 bug 放到生产环境才暴露，排查代价就是按小时算。把检查尽量往前挪：先做静态分析再跑测试，先过测试再上 staging，先验证 staging 再进 production。

**小步快跑更安全（Faster is Safer）：** 缩小单次发布规模、提高发布频次反而是在降低风险，而不是推高风险。一次只带 3 个改动的部署，比塞了 30 个改动的部署好排查得多；频繁发布也会反过来建立起对发布流程本身的信心。

## 何时使用

- 为新项目搭建 CI pipeline
- 新增或修改自动化检查项
- 配置部署 pipelines
- 需要让某类变更自动触发校验流程时
- 排查 CI 失败（failure）

## 质量门禁 Pipeline

每个变更在合并前都要经过以下门禁：

```
Pull Request Opened
    │
    ▼
┌─────────────────┐
│   LINT CHECK     │  eslint, prettier
│   ↓ pass         │
│   TYPE CHECK     │  tsc --noEmit
│   ↓ pass         │
│   UNIT TESTS     │  jest/vitest
│   ↓ pass         │
│   BUILD          │  npm run build
│   ↓ pass         │
│   INTEGRATION    │  API/DB tests
│   ↓ pass         │
│   E2E (optional) │  Playwright/Cypress
│   ↓ pass         │
│   SECURITY AUDIT │  npm audit
│   ↓ pass         │
│   BUNDLE SIZE    │  bundlesize check
└─────────────────┘
    │
    ▼
  Ready for review
```

**任何门禁都不能跳过。** 如果 lint 失败，就去修 lint，不要关掉规则；如果测试失败，就去修代码，不要跳过测试。

## GitHub Actions 配置

### 基础 CI Pipeline

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type check
        run: npx tsc --noEmit

      - name: Test
        run: npm test -- --coverage

      - name: Build
        run: npm run build

      - name: Security audit
        run: npm audit --audit-level=high
```

### 包含数据库集成测试

```yaml
  integration:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: testdb
          POSTGRES_USER: ci_user
          POSTGRES_PASSWORD: ${{ secrets.CI_DB_PASSWORD }}
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - run: npm ci
      - name: Run migrations
        run: npx prisma migrate deploy
        env:
          DATABASE_URL: postgresql://ci_user:${{ secrets.CI_DB_PASSWORD }}@localhost:5432/testdb
      - name: Integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://ci_user:${{ secrets.CI_DB_PASSWORD }}@localhost:5432/testdb
```

> **注意：** 即使是仅供 CI 使用的测试数据库，也必须用 GitHub Secrets 来存放凭据，不要硬编码在配置里。这不仅能养成好习惯，也能避免测试凭据在其他场景下被误复用。

### E2E Tests（端到端测试）

```yaml
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - run: npm ci
      - name: Install Playwright
        run: npx playwright install --with-deps chromium
      - name: Build
        run: npm run build
      - name: Run E2E tests
        run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
```

## 将 CI 失败结果反馈给 Agents

CI 搭配 AI agents 的威力在于形成反馈闭环。当 CI 失败时：

```
CI fails
    │
    ▼
Copy the failure output
    │
    ▼
Feed it to the agent:
"The CI pipeline failed with this error:
[paste specific error]
Fix the issue and verify locally before pushing again."
    │
    ▼
Agent fixes → pushes → CI runs again
```

**关键模式：**

```
Lint failure → Agent runs `npm run lint -- --fix` and commits
Type error  → Agent reads the error location and fixes the type
Test failure → Agent follows debugging-and-error-recovery skill
Build error → Agent checks config and dependencies
```

## 部署策略

### Preview Deployments（预览部署）

每个 PR 都会获得一个 preview deployment（预览部署），便于人工测试验证：

```yaml
# Deploy preview on PR (Vercel/Netlify/etc.)
deploy-preview:
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request'
  steps:
    - uses: actions/checkout@v4
    - name: Deploy preview
      run: npx vercel --token=${{ secrets.VERCEL_TOKEN }}
```

### Feature Flags（功能开关）

Feature flags 将“部署（deploy）”与“发布（release）”解耦。把尚未完工或存在风险的功能藏在 flags 后面上线，这样你就能：

- **代码先上线但暂不启用。** 尽早合入 main，等条件成熟再开启。
- **无需重新部署即可回滚。** 直接关掉 flag，而不是回滚代码再重新发布。
- **灰度（Canary）放量新功能。** 先对 1% 用户启用，再到 10%，最后放量到 100%。
- **开展 A/B tests。** 对比开启与关闭该功能时的真实表现。

```typescript
// Simple feature flag pattern
if (featureFlags.isEnabled('new-checkout-flow', { userId })) {
  return renderNewCheckout();
}
return renderLegacyCheckout();
```

**Flag 生命周期：** Create → Enable for testing → Canary → Full rollout → Remove the flag and dead code。长期留存的 flags 会演变成技术债，因此在创建之初就应该设定好清理日期（cleanup date）。

### 分阶段发布

```
PR merged to main
    │
    ▼
  Staging deployment (auto)
    │ Manual verification
    ▼
  Production deployment (manual trigger or auto after staging)
    │
    ▼
  Monitor for errors (15-minute window)
    │
    ├── Errors detected → Rollback
    └── Clean → Done
```

### 回滚计划

每次部署都应该可回滚：

```yaml
# Manual rollback workflow
name: Rollback
on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to rollback to'
        required: true

jobs:
  rollback:
    runs-on: ubuntu-latest
    steps:
      - name: Rollback deployment
        env:
          VERSION: ${{ inputs.version }}
        run: |
          # Deploy the specified previous version. Pass the input through env,
          # never interpolate it into the script (shell injection).
          npx vercel rollback "$VERSION"
```

## 环境管理

```
.env.example       → Committed (template for developers)
.env                → NOT committed (local development)
.env.test           → Committed (test environment, no real secrets)
CI secrets          → Stored in GitHub Secrets / vault
Production secrets  → Stored in deployment platform / vault
```

CI 绝不应持有生产环境 secrets。务必为 CI 测试单独配置隔离的 secrets。

## CI 之外的自动化

### Dependabot / Renovate

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly
    open-pull-requests-limit: 5
```

### Build Cop 角色

指定专人负责维护 CI 绿灯状态。当构建失败时，由 Build Cop 负责修复或回滚，而不是被动等待引发故障的提交者来处理。这能避免所有人都指望“别人会去修”，从而让破损的构建状态不断累积。

### PR 检查（PR Checks）

- **强制评审（Required reviews）：** 合并前至少需要 1 个 approval
- **强制状态检查（Required status checks）：** 合并前 CI 必须全部通过
- **分支保护（Branch protection）：** 禁止向 main 强推（force-push）
- **自动合并（Auto-merge）：** 如果所有检查通过且审批完成，自动合并

## CI 优化

当 pipeline 超过 10 分钟时，按影响从大到小应用这些策略：

```
Slow CI pipeline?
├── Cache dependencies
│   └── Use the setup-node cache option (or actions/cache) for the package manager cache, not node_modules
├── Run jobs in parallel
│   └── Split lint, typecheck, test, build into separate parallel jobs
├── Only run what changed
│   └── Use path filters to skip unrelated jobs (e.g., skip e2e for docs-only PRs)
├── Use matrix builds
│   └── Shard test suites across multiple runners
├── Optimize the test suite
│   └── Remove slow tests from the critical path, run them on a schedule instead
└── Use larger runners
    └── GitHub-hosted larger runners or self-hosted for CPU-heavy builds
```

**示例：缓存和并行**
```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22', cache: 'npm' }
      - run: npm ci
      - run: npm run lint

  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22', cache: 'npm' }
      - run: npm ci
      - run: npx tsc --noEmit

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22', cache: 'npm' }
      - run: npm ci
      - run: npm test -- --coverage
```

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “CI 太慢了” | 去优化 pipeline（见「CI 优化」一节），不要跳过它。5 分钟的 pipeline 能帮你省下几小时的排障时间。 |
| “这个变更很小，跳过 CI” | 小改动照样会把构建搞挂，而且小改动跑 CI 本来也很快。 |
| “测试不稳定，重跑就行” | 不稳定的测试（flaky tests）会掩盖真实 bug，并持续浪费所有人的时间。必须从根源修掉这种不稳定性。 |
| “以后再加 CI” | 没有 CI 兜底的项目迟早会积累大量破损状态。从第一天起就配好它。 |
| “手动测试就够了” | 手动测试既不可扩展，也无法稳定复现。凡是能自动化的检查都应自动化。 |

## 危险信号

- 项目中没有 CI pipeline
- 对 CI 失败视而不见或直接静音屏蔽
- 为了让 pipeline 变绿，直接在 CI 里禁用测试
- 没在 staging 验证就直发 production
- 没有回滚（rollback）机制
- 把 secrets 直接写死在代码或 CI 配置文件中（而非存入 secrets manager）
- CI 耗时很长却没有任何优化投入

## 验证

设置或修改 CI 后：

- [ ] 所有质量门禁均已配置到位（lint、类型检查、测试、build、安全审计）
- [ ] Pipeline 在每次发起 PR 及推送（push）到 main 时都会运行
- [ ] 检查失败会阻塞合并（已配好 branch protection）
- [ ] CI 结果能够闭环反馈回开发流程
- [ ] Secrets 统一存放在 secrets manager 中，而非硬编码进代码
- [ ] 部署流程配备了可靠的回滚（rollback）机制
- [ ] 完整测试套件在 pipeline 中能在 10 分钟内跑完
