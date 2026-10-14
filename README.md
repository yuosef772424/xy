# ai-playbook

> A library of English Markdown instructions that teach AI agents (and humans) **how to do project work the best way**.

Drop these files into any repository and your AI assistant (Claude Code, Cursor, Copilot, Codex, …) gets a clear, tested way of working: how to understand a task, plan it, write code, test, debug, review, document, and ship it.

## Why

AI agents are only as good as their instructions. Most projects give them none, so they guess. This playbook replaces guessing with a consistent process, so every project starts out **high quality by default**.

## What's inside

| Path | Purpose |
|------|---------|
| [`AGENTS.md`](AGENTS.md) | The core rules. Copy this into any project as the agent's entry point. |
| [`playbooks/`](playbooks/) | Step-by-step guides, one per kind of task. |
| [`templates/`](templates/) | Ready-to-fill files: project instructions, task briefs, PR descriptions. |
| [`prompts/`](prompts/) | How to write prompts that get great results. |

### Playbooks

0. [Honest judgment: no flattery, no reflexive criticism](playbooks/00-honest-judgment.md)
0b. [Evidence over agreement: research to correct bias](playbooks/00b-evidence-over-agreement.md)
1. [Understand the task](playbooks/01-understand-the-task.md)
2. [Plan the work](playbooks/02-planning.md)
3. [Write code](playbooks/03-writing-code.md)
4. [Test](playbooks/04-testing.md)
5. [Debug](playbooks/05-debugging.md)
6. [Review code](playbooks/06-code-review.md)
7. [Git, commits & pull requests](playbooks/07-git-and-pull-requests.md)
8. [Documentation](playbooks/08-documentation.md)
9. [Security](playbooks/09-security.md)
10. [Communication & reporting](playbooks/10-communication.md)
11. [Start a new project](playbooks/11-new-project.md)

## Quick start

1. Copy `AGENTS.md` into the root of your project. Name it `CLAUDE.md` for Claude Code, or keep it as `AGENTS.md` for tools that read that file.
2. Fill in the project-specific section using [`templates/project-instructions.md`](templates/project-instructions.md).
3. Optionally copy the `playbooks/` folder too, and reference it from your `AGENTS.md`.
4. Give tasks using [`templates/task-brief.md`](templates/task-brief.md) for the best results.

## Principles

- **Honest, balanced judgment.** Don't flatter bad ideas; don't attack good ones.
- **Understand before acting.** Read the code and the request before you change anything.
- **Small, verified steps.** Make each change minimal and prove it works.
- **Match the codebase.** New code should look like it was always there.
- **Honest reporting.** Say what was done, what was not, and what failed.
- **Leave it better.** Each task should leave the project clearer than before.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Each playbook should be short, practical, and written as instructions.
