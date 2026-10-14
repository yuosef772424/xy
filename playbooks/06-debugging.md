# 06 · Debugging: Root Cause, Not Symptoms

> **Goal:** Find and fix the real cause, and lock it in with a test. · **Read when:** something fails and the cause isn't obvious. · **Pays off because:** fixing symptoms creates repeat bugs; a systematic approach is faster than guessing.

## Steps
1. **Reproduce** reliably and minimally. Without a reproduction you are guessing.
2. **Read the whole error:** the stack trace, logs, and the exact line it points to.
3. **Check the baseline:** run the failing test on the parent commit, or on the main branch (for example in a temporary worktree). If it fails there too, it's a pre-existing failure. Report it as such instead of chasing it inside your change.
4. **Hypothesize** ("X happens because Y") and **test** with the smallest experiment: a log line, a debugger, a unit test.
5. **Narrow down** with binary search over code, input, or commits (`git bisect`).
6. **Fix the cause,** check whether the same bug exists elsewhere, and add a **regression test**.
7. **Clean up** temporary logs and experiments.

**Ask:** What changed recently (code, dependencies, config, data, environment)? Is it deterministic? Intermittent failures usually point to timing, ordering, or shared state.

**After two real attempts that didn't work,** stop and change the approach ([09](09-improvement.md) §3) instead of repeating it.

## Anti-patterns
Random changes until it works · calling something "flaky" without evidence · hiding the symptom with `try/catch` or `sleep` · fixing the symptom in three places instead of the cause in one.
