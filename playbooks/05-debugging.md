# 05 · Debug

**Goal:** Find the **root cause**, not just a way to make the symptom go away.

## Steps

1. **Reproduce.** Get a reliable, minimal way to trigger the bug. Without a repro, you are only guessing.
2. **Read the whole error.** Read the full stack trace, logs, and the exact line it points to.
3. **Form a hypothesis.** "X happens because Y."
4. **Test the hypothesis** with the smallest possible experiment: a log line, a debugger, a unit test.
5. **Narrow down.** Use binary search across code, input, or commits (`git bisect`).
6. **Fix the cause.** Then check whether the same bug exists elsewhere.
7. **Lock it in** with a regression test.
8. **Clean up** temporary logs and experiments.

## Questions to ask

- What changed recently: code, dependencies, config, data, environment?
- Does it fail on the main branch too?
- Is it deterministic or intermittent? Intermittent failures usually point to timing, ordering, or shared state.

## Anti-patterns

- Changing things at random until it works.
- Calling something "flaky" without evidence.
- Adding `try/catch` or `sleep` to hide the symptom.
- Fixing the symptom in three places instead of the cause in one.
