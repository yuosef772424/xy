# 11 · Start a New Project

**Goal:** A new project that is easy to run, test, and extend from day one.

## Steps

1. **Define the project** in 3 lines: problem, users, core feature.
2. **Choose a boring, well-supported stack** unless there is a strong reason not to.
3. **Set up the skeleton:**
   - `README.md` (install / run / test)
   - `AGENTS.md` from this playbook
   - `.gitignore`, `.env.example` (never `.env`)
   - Formatter + linter + test runner, each runnable with one command
   - CI that runs lint + tests on every PR
4. **Build the thinnest end-to-end slice first:** one feature working from input to output.
5. **Iterate** in small PRs, each with tests.

## Definition of a healthy project

- [ ] A newcomer can run it in under 10 minutes using only the README.
- [ ] `test`, `lint`, and `build` are single commands.
- [ ] CI blocks merges when checks fail.
- [ ] No secrets in the repository.
- [ ] Agent instructions are up to date.
