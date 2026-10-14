# 01 · Understand the Task

**Goal:** Know exactly what "done" means before writing any code.

## Steps

1. **Restate the goal** in one sentence: "The user wants X so that Y."
2. **Pick out the requirements:**
   - Inputs: what data or state you start from.
   - Outputs: what must exist or change when you finish.
   - Constraints: performance, compatibility, style, deadlines, things you must not touch.
3. **Define acceptance criteria.** Write 2–5 checks that prove the task is done, for example "`npm test` passes and `/login` returns 401 for a bad password".
4. **Find the context.** Search the codebase for related files, earlier implementations, tests, and docs.
5. **Resolve ambiguity:**
   - If a sensible default exists → choose it and state your assumption.
   - If the answer changes the outcome and you can't infer it → ask one precise question.

## Checklist

- [ ] I can explain the task in one sentence.
- [ ] I know which files are involved.
- [ ] I have written acceptance criteria.
- [ ] My assumptions are written down.

## Anti-patterns

- Starting to code right after reading the title.
- Asking questions the code already answers.
- Solving the problem you expected instead of the one that was asked.
