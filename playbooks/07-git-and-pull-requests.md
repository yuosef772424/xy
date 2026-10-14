# 07 · Git, Commits & Pull Requests

**Goal:** Keep a clean history that is easy to review and easy to revert.

## Branches

- Never commit directly to `main`.
- Use descriptive names: `feat/login-rate-limit`, `fix/null-invoice-total`.

## Commits

- One logical change per commit.
- Use the imperative mood, with a subject under ~72 characters: `Fix crash when cart is empty`.
- Explain *why* in the body when it isn't obvious.
- Never commit secrets, build output, or large binaries.

## Pull requests

**Title:** what the change does.

**Body:**

```markdown
## Summary
What changed and why.

## Changes
- Bullet list of the main changes.

## How it was tested
- Commands run and results.
- Manual checks.

## Risks / notes
- Anything reviewers should look at closely.
```

## After opening

- Keep CI green: a red PR is never "waiting for review".
- Answer every review comment, either with a fix or a reason.
- Merge the base branch when there are conflicts, and regenerate lockfiles with tools, not by hand.

## Never

- Force-push to a shared branch.
- Rewrite someone else's history.
- Push an empty commit to re-run CI.
