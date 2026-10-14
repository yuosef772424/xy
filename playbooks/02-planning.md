# 02 · Plan the Work

**Goal:** Turn the task into small, ordered steps that you can verify.

## When to plan

- One-line fix → no written plan needed.
- Multi-file change, new feature, or refactor → write a plan first.
- Architecture or data-model change → write a plan **and** get approval.

## How to plan

1. **List the files** to create or change, with one line on why for each.
2. **Order the steps** so that each one leaves the project working (builds and passes its tests).
3. **Attach a verification** to each step: a test, a command, or a manual check.
4. **Identify risks:** migrations, public API changes, performance, security.
5. **Choose the simplest design** that meets the requirements. Don't add features nobody asked for.

## Plan template

```markdown
## Goal
<one sentence>

## Steps
1. <change> — verify by <test/command>
2. ...

## Risks
- <risk> → <mitigation>

## Out of scope
- <things deliberately not done>
```

## Anti-patterns

- Plans so long that they never get carried out.
- "Big bang" changes that only work once every step is finished.
- Designing for imagined future requirements.
