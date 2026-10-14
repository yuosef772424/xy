# 23 · Operations (After It's Built: Deploy, Watch, Protect, Maintain)

**Goal:** The project keeps working **after** launch: it is deployed safely, problems are seen before users report them, data can be recovered, and dependencies stay healthy.

Apply this once a project is heading to real users. Scale it to the project: a personal tool needs a fraction of this, and a paid product needs all of it.

## 1. Deployment

- **One command (or one CI job) deploys.** No manual steps that live only in someone's memory.
- **Environments:** at least local and production; add staging when real users or real money are involved.
- **Config and secrets come from the environment** or a secret manager, never from the code.
- **Rollback is planned:** you know how to return to the previous version in minutes. Database migrations are backward compatible, so a rollback doesn't break the data.
- **A release checklist** for anything risky: migrations, flags, announcements.

## 2. Monitoring

- **Errors:** captured with context (Sentry or similar), with alerts for new or rising errors.
- **Health:** an uptime check on the main endpoint(s).
- **Key metrics:** a few numbers that show whether the product works (sign-ups, successful payments, job success rate, latency).
- **Logs:** structured, searchable, and without secrets or unnecessary personal data.
- Alerts must be **actionable.** An alert nobody acts on is noise; remove it or fix it.

## 3. Data protection

- **Automated backups,** with retention that matches how bad data loss would be.
- **Test restores regularly.** A backup that has never been restored isn't proven.
- **Privacy:** collect only the data you need, know where personal data lives, and support deletion requests where the law requires it.

## 4. Incidents

When something breaks in production:

1. **Stabilize first** (roll back, disable the feature flag, scale up), then investigate.
2. **Communicate** a short status to affected users or the owner.
3. **Fix the root cause** ([05](05-debugging.md)) and add a test or alert that would have caught it.
4. **Write a short blameless post-mortem:** what happened, the impact, the cause, and what changes. Record the lessons ([18](18-continuous-improvement.md)).

## 5. Maintenance

- **Dependencies:** automated update PRs (Dependabot or Renovate) and a vulnerability audit in CI. Update in small, regular steps, not in a painful big jump once a year.
- **Tech debt:** keep a visible list; spend a regular slice of the effort on it, guided by the architecture health check ([12a](12a-architecture-rules.md) Part F).
- **Costs:** watch hosting and API spending; alert on unusual jumps.

## Checklist before launch

- [ ] One-command deploy and a tested rollback.
- [ ] Error tracking, an uptime check, and key metrics with useful alerts.
- [ ] Automated backups and at least one tested restore.
- [ ] Secrets in the environment; no personal data in logs.
- [ ] Dependency updates and a vulnerability audit automated.
