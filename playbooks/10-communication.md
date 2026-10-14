# 10 · Communication & Reporting

**Goal:** Let the user understand the result in 30 seconds.

## Final report format

```markdown
**Done:** <one-sentence outcome>

**Changes**
- <file or area>: <what changed>

**Verified**
- `<command>` → passed
- <manual check>

**Not done / open**
- <anything skipped, failed, or needing a decision>
```

## Rules

- **Lead with the outcome,** not the process.
- **Be honest:** if something failed or was skipped, say so clearly.
- **Be specific:** "3 of 120 tests fail in `auth.spec.ts`" beats "some tests fail".
- **Don't over-hedge:** if something is verified, say it plainly.
- **Ask good questions:** one question with options and your recommendation.
- Don't narrate every step; report results.

## Asking a question

> The API can return dates as ISO strings or Unix timestamps. **I recommend ISO** (the rest of the API uses it). Should I go with ISO?
