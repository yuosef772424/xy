# Evals: Testing the Instructions Themselves

**Goal:** Check whether a model actually *follows* these playbooks, especially the behavioral ones (honest judgment, evidence, owner protocol), and catch regressions when the playbook or the model changes.

## How to run (manual, for now)

1. Start a fresh session with this playbook's `AGENTS.md` loaded.
2. Send each case's **prompt** exactly as written.
3. Compare the reply with **pass if** / **fail if**. Record the result in the table at the bottom of [cases.md](cases.md), with the model name and the date.
4. If a case fails, improve the relevant playbook, then re-run the case.

Cases cover both directions: the model must push back on bad ideas **and** must not invent objections to good ones.
