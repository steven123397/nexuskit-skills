---
name: shipping-and-launch
description: Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in place before shipping. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy.
---

# Shipping and Launch

## 概览

胸有成竹地发布上线。目标不只是把代码部署出去，而是安全地部署：监控配置到位、回滚计划准备就绪，并且明确知道“成功”是什么样子。每一次上线都应该是可回滚、可观测、渐进式推进的。

## 何时使用

- 首次将功能部署到生产环境
- 向用户发布重大变更
- 迁移数据或基础设施
- 开放 beta 或抢先体验（early access）项目
- 任何存在风险的部署（也就是所有部署）

## 发布前检查清单

### 代码质量

- [ ] 所有测试通过（unit、integration、e2e）
- [ ] Build 成功且没有警告
- [ ] Lint 和类型检查通过
- [ ] 代码已 review 并获批准
- [ ] 没有残留应当在上线前解决的 TODO 注释
- [ ] 生产代码中没有 `console.log` 调试语句
- [ ] 错误处理覆盖了预期的失败模式

### 安全

- [ ] 代码或版本控制中没有 secrets
- [ ] 对应技术栈的依赖安全审计（`npm audit`、`pip-audit`、`cargo audit` 等）没有 critical 或 high 级别漏洞
- [ ] 所有面向用户的 endpoint 都有输入校验
- [ ] 认证和授权检查已到位
- [ ] 安全响应头（security headers）已配置（CSP、HSTS 等）
- [ ] 认证 endpoint 已设置 rate limiting
- [ ] CORS 已配置为具体允许的 origin（不使用通配符）

### 性能

- [ ] Core Web Vitals 在 "Good" 阈值内
- [ ] 关键路径中没有 N+1 查询
- [ ] 图片已优化（压缩、响应式尺寸、lazy loading）
- [ ] Bundle size 在预算内
- [ ] 数据库查询有合适索引
- [ ] 静态资源和重复查询已配置缓存

### 可访问性

- [ ] 所有交互元素都支持键盘导航
- [ ] 屏幕阅读器可以传达页面内容和结构
- [ ] 颜色对比度满足 WCAG 2.1 AA（文本 4.5:1）
- [ ] 模态框和动态内容的焦点管理正确
- [ ] 错误提示信息具有描述性，并与表单字段关联
- [ ] axe-core 或 Lighthouse 中没有可访问性警告

### 基础设施

- [ ] 生产环境变量已设置
- [ ] 数据库 migration 已应用（或已准备好随发布安全应用）
- [ ] DNS 和 SSL 已配置
- [ ] 静态资源 CDN 已配置
- [ ] 日志记录（logging）和错误上报（error reporting）已配置
- [ ] Health check endpoint 已存在且能正常响应

### 文档

- [ ] README 已更新所有新增的 setup 要求
- [ ] API 文档保持最新
- [ ] 所有架构决策均已编写 ADR
- [ ] Changelog 已更新
- [ ] 面向用户的文档已更新（如适用）

## Feature Flag 策略

通过 feature flags 上线，将“部署”与“发布”解耦：

```typescript
// Feature flag check
const flags = await getFeatureFlags(userId);

if (flags.taskSharing) {
  // New feature: task sharing
  return <TaskSharingPanel task={task} />;
}

// Default: existing behavior
return null;
```

**Feature flag 生命周期：**

```
1. DEPLOY with flag OFF     → Code is in production but inactive
2. ENABLE for team/beta     → Internal testing in production environment
3. GRADUAL ROLLOUT          → 5% → 25% → 50% → 100% of users
4. MONITOR at each stage    → Watch error rates, performance, user feedback
5. CLEAN UP                 → Remove flag and dead code path after full rollout
```

**规则：**
- 每个 feature flag 都必须明确指定 owner 和过期清理日期
- 全量发布后 2 周内清理掉 flags
- 不要嵌套使用 feature flags（否则会产生指数级增长的组合）
- 在 CI 中测试 flag 的两种状态（on 和 off）

## 分阶段发布

### 发布序列

```
1. DEPLOY to staging
   └── Full test suite in staging environment
   └── Manual smoke test of critical flows

2. DEPLOY to production (feature flag OFF)
   └── Verify deployment succeeded (health check)
   └── Check error monitoring (no new errors)

3. ENABLE for team (flag ON for internal users)
   └── Team uses the feature in production
   └── 24-hour monitoring window

4. CANARY rollout (flag ON for 5% of users)
   └── Monitor error rates, latency, user behavior
   └── Compare metrics: canary vs. baseline
   └── 24-48 hour monitoring window
   └── Advance only if all thresholds pass (see table below)

5. GRADUAL increase (25% -> 50% -> 100%)
   └── Same monitoring at each step
   └── Ability to roll back to previous percentage at any point

6. FULL rollout (flag ON for all users)
   └── Monitor for 1 week
   └── Clean up feature flag
```

### 发布决策阈值

用以下阈值判断每个阶段应该继续推进、暂停调查，还是回滚：

| 指标 | 继续推进（green） | 暂停并调查（yellow） | 回滚（red） |
|--------|-----------------|-------------------------------|-----------------|
| Error rate | 与基线偏差在 10% 以内 | 高于基线 10-100% | 超过基线 2 倍（>2x） |
| P95 latency | 与基线偏差在 20% 以内 | 高于基线 20-50% | 高于基线 50% 以上 |
| Client JS errors | 未出现新的错误类型 | 新错误出现在 <0.1% 的 sessions 中 | 新错误出现在 >0.1% 的 sessions 中 |
| Business metrics | 持平或正向 | 下降 <5%（可能是正常波动噪声） | 下降 >5% |

### 何时回滚

如果出现以下情况，立即回滚：
- Error rate 增加到超过基线的 2 倍
- P95 latency 上升超过 50%
- 用户上报的问题激增
- 检测到数据完整性问题
- 发现安全漏洞

## 监控和可观测性

### 监控什么

```
Application metrics:
├── Error rate (total and by endpoint)
├── Response time (p50, p95, p99)
├── Request volume
├── Active users
└── Key business metrics (conversion, engagement)

Infrastructure metrics:
├── CPU and memory utilization
├── Database connection pool usage
├── Disk space
├── Network latency
└── Queue depth (if applicable)

Client metrics:
├── Core Web Vitals (LCP, INP, CLS)
├── JavaScript errors
├── API error rates from client perspective
└── Page load time
```

### Error Reporting（错误上报）

```typescript
// Set up error boundary with reporting
class ErrorBoundary extends React.Component<React.PropsWithChildren> {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    // Report to error tracking service
    reportError(error, {
      componentStack: info.componentStack,
      userId: getCurrentUser()?.id,
      page: window.location.pathname,
    });
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback onRetry={() => this.setState({ hasError: false })} />;
    }
    return this.props.children;
  }
}

// Server-side error reporting
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  reportError(err, {
    method: req.method,
    url: req.url,
    userId: req.user?.id,
  });

  // Don't expose internals to users
  res.status(500).json({
    error: { code: 'INTERNAL_ERROR', message: 'Something went wrong' },
  });
});
```

### 上线后验证

上线后的第一个小时内：

```
1. Check health endpoint returns 200
2. Check error monitoring dashboard (no new error types)
3. Check latency dashboard (no regression)
4. Test the critical user flow manually
5. Verify logs are flowing and readable
6. Confirm rollback mechanism works (dry run if possible)
```

## Error Budget 发布门禁

服务的 error budget（SLO 允许失败的请求或时间占比）决定现在发布是否安全。把它当作客观硬门禁，而不是讨价还价的筹码：

```
Budget remaining > 20%  →  Ship normally; monitor closely
Budget remaining 0–20%  →  Slow rollouts only; no high-risk changes
Budget exhausted        →  Freeze feature work; focus entirely on reliability
Budget resets           →  Resume normal pace; bake in the fix that recovered it
```

Canary 期间的高 burn rate（消耗预算的速度快于基线节奏）是上文发布决策阈值表中的**暂停（Hold）**信号：应按 error rate 升高的同等标准处理。

## 回滚策略

每次部署发生之前都需要回滚计划：

```markdown
## Rollback Plan for [Feature/Release]

### Trigger Conditions
- Error rate > 2x baseline
- P95 latency > [X]ms
- User reports of [specific issue]

### Rollback Steps
1. Disable feature flag (if applicable)
   OR
1. Deploy previous version: `git revert <commit> && git push`
2. Verify rollback: health check, error monitoring
3. Communicate: notify team of rollback

### Database Considerations
- Migration [X] has a rollback: <verified command or runbook link>
- Data inserted by new feature: [preserved / cleaned up]

### Time to Rollback
- Feature flag: < 1 minute
- Redeploy previous version: < 5 minutes
- Database rollback: < 15 minutes
```
## 另见

- 关于每笔变更在进入本清单前都要满足的项目级 Definition of Done，见 `../../references/definition-of-done.md`
- 关于发布前安全检查，见 `../../references/security-checklist.md`
- 关于发布前性能检查清单，见 `../../references/performance-checklist.md`
- 关于上线前可访问性验证，见 `../../references/accessibility-checklist.md`
- 关于告警规则及与 SLO 绑定的阈值，见 `observability-and-instrumentation`

## 常见合理化借口

| 合理化借口 | 现实 |
|---|---|
| “它在 staging 能用，production 也会能用” | Production 有截然不同的数据、流量模式和边界情况。部署后必须监控。 |
| “这个不需要 feature flags” | 每个功能都受益于应急开关（kill switch）。即使“简单”变更也可能搞出故障。 |
| “监控是额外负担” | 没有监控，就意味着你会从用户投诉而不是 dashboard 中发现问题。 |
| “以后再加监控” | 上线前就添加。你看不见的东西出了事根本没法调试。 |
| “回滚就是承认失败” | 回滚是负责任的工程实践。把坏功能留在生产环境才是失败。 |
| “Error rate 看起来正常，继续发” | 要看 burn rate，不要只看当前 error rate。消耗预算快于基线就是暂停信号，即使各项单独阈值都是 green。 |

## 危险信号

- 没有回滚计划就直接部署
- 生产环境没有监控或错误上报
- 一次性全量发布（Big-bang releases，不经 staging 验证直接全量上线）
- Feature flags 没有到期时间或 owner
- 部署后第一个小时无人盯防监控
- 生产环境配置靠人脑记忆维护，而不是靠代码管理
- “周五下午了，发吧”
- Error budget 已耗尽，但功能开发照常推进

## 验证

部署前：

- [ ] 发布前检查清单已完成（所有分项均为 green）
- [ ] Feature flag 已配置妥当（如适用）
- [ ] 回滚计划已书面记录
- [ ] 监控 dashboards 已搭建就绪
- [ ] 团队已收到部署通知

部署后：

- [ ] Health check 返回 200
- [ ] Error rate 正常
- [ ] 响应延迟正常
- [ ] 关键用户流程端到端可用
- [ ] 日志正常采集流入
- [ ] 回滚已实测，或已验证可随时执行

对每个已发布的服务：

- [ ] Error budget 策略已就位：明确预算跌破 20% 以及彻底耗尽时分别该采取什么行动
