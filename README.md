# ai-playbook

> A playbook **and a toolkit** that make AI agents (Claude Code first, any agent in principle) do project work the way a strong senior team would: honest, researched, well-structured, verified, and cost-aware.

Copy it into a project, and every session starts with clear rules, a working process, maps, tools, and memory, instead of starting from zero.

## What makes it different
- **Honest judgment by design:** no flattery, no reflexive criticism, and claims checked against evidence.
- **Structure by rules, not taste:** an extension test and CI-enforced architecture rules prevent the "great first design, tangled later" pattern.
- **Research before building:** market, competitors, feasibility, and prior art for each phase.
- **Smart cost:** a planner with cheap builder agents, maps instead of reading everything, batching, and investing tokens where they pay off.
- **It learns:** lessons, tools, and proposals make every session, and every project, better than the last.
- **Automatic in Claude Code:** subagents, skills, and hooks load the right behavior on their own.

## What's inside
| Path | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | The core rules, read every session. Copy it into any project. |
| [`playbooks/`](playbooks/) | Detailed guides, each read only when its topic comes up (list below). |
| [`claude-code/`](claude-code/) | **Claude Code kit:** `CLAUDE.md`, `builder` / `researcher` / `reviewer` subagents, `/handoff` · `/status` · `/propose` skills, and a session-start hook. |
| [`templates/`](templates/) | Project instructions, `MODULE.md`, task and agent briefs, status, market research, PR description. |
| [`scripts/`](scripts/) | Reusable tools, listed in the [tools registry](scripts/README.md) (for example `gen_map.py` for project maps). |
| [`evals/`](evals/) | Test cases that check whether a model actually follows these rules. |
| [`PROPOSALS.md`](PROPOSALS.md) | Inbox of proposed new instructions, waiting for the owner's review. |
| [`NOTES.md`](NOTES.md) | Revision history and open items for the playbook itself. |

### Playbooks
Each one opens with its **goal**, **when to read it**, and **why it pays off**.

| # | Playbook | Topic |
|---|---|---|
| 00 | [Principles](playbooks/00-principles.md) | Goals over rigid numbers, rule priority, value over minimum cost |
| 01 | [Judgment](playbooks/01-judgment.md) | Honest assessment and evidence-based answers |
| 02 | [Working with the owner](playbooks/02-owner.md) | Questions vs requests, decisions, reports, hand-offs, merging |
| 03 | [Safety & security](playbooks/03-safety.md) | Product security and agent safety |
| 04 | [Task workflow](playbooks/04-task-workflow.md) | Understand → plan → build → review |
| 05 | [Testing](playbooks/05-testing.md) | Automated checks and test output the model can afford to read |
| 06 | [Debugging](playbooks/06-debugging.md) | Root cause, baseline check, regression test |
| 07 | [Maps & docs](playbooks/07-maps-and-docs.md) | Navigate without reading everything |
| 08 | [Efficiency](playbooks/08-efficiency.md) | Token budget, batching, fewer round-trips |
| 09 | [Improvement](playbooks/09-improvement.md) | Lessons, alternatives, tools & R&D, proposals |
| 10 | [Market research](playbooks/10-market-research.md) | Competitors, differentiation, feasibility verdict |
| 11 | [Architecture](playbooks/11-architecture.md) | Design and set up a project before building it |
| 12 | [Architecture rules](playbooks/12-architecture-rules.md) | Scope, extension test, decomposition, CI enforcement |
| 13 | [Execution](playbooks/13-execution.md) | One planner, builder agents, smart cost |
| 14 | [Product quality](playbooks/14-product-quality.md) | UX, accessibility, RTL & localization, performance |
| 15 | [Operations](playbooks/15-operations.md) | Deploy, monitor, back up, maintain |
| 16 | [Prompting](playbooks/16-prompting.md) | Agent briefs and prompts inside LLM features |

## Quick start
1. Copy `AGENTS.md`, `playbooks/`, `templates/`, and `scripts/` into your project.
2. For Claude Code, also copy the contents of `claude-code/` (see its [README](claude-code/README.md)).
3. Fill in section 8 of `AGENTS.md` using [`templates/project-instructions.md`](templates/project-instructions.md).
4. New project? Start with [11 · Architecture](playbooks/11-architecture.md). An existing project? Generate the map (`python scripts/gen_map.py`) and add a `MODULE.md` per module.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). Agents propose changes through [`PROPOSALS.md`](PROPOSALS.md); the owner reviews them in batches.
