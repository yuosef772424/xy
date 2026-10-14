# 08 · Efficiency: Spend for Value, Batch Work, Cut Waste

> **Goal:** Get the most value from the usage budget: more done per invocation, with no loss of quality or research. · **Read when:** planning work, running agents, or when a phase costs more than expected. · **Pays off because:** the budget is limited, and the most expensive outcome is rework, not research.

## 1. The budget principle
The most expensive outcome **isn't a large research bill**. It's discovering halfway through that a better solution existed, that key features were missing, or that the idea wasn't viable. A short-sighted saving that causes rework or a weaker product is a **loss**.

| Spend generously on | Save on (waste) |
|---|---|
| Research at the start: market, feasibility, architecture options | Re-reading the same files or logs |
| Prior-art research before non-trivial phases | Exploring the codebase instead of using the maps ([07](07-maps-and-docs.md)) |
| Hard-to-reverse design decisions | Chatter, acknowledgements, invocations that do nothing |
| Verification: tests, reviews, re-checking claims | Manual work that a script can do ([09](09-improvement.md)) |
| Alternatives for hard problems; useful tools and R&D | Strong models on routine, well-specified work |
| | Long contexts: start fresh sessions per roadmap item |

**Never cut research or verification to save tokens.** If the budget really is tight, tell the owner and propose what to defer. Never quietly lower quality.

**Measure:** check usage regularly (for example `/usage` and `/context` in Claude Code). Note in `STATUS.md` roughly what each phase cost compared with the estimate. When a phase costs much more than expected, ask whether it was waste (fix the process) or necessary work (fix the estimate).

## 2. Batching: more per invocation
Every invocation re-reads the whole context, so fewer invocations means fewer re-reads. But oversized batches grow the context and cause rework. **Aim for the right batch size, not the largest.**

**Batch tasks that are:** independent · in the same area (context loaded once) · small and well-specified · covered by the same checks.
**Don't batch:** risky tasks (migrations, auth, payments, core interfaces); tasks that depend on what you learn from another task; tasks spread across modules that need a lot of extra context. As a rough guide, keep a builder batch to a handful of tasks and a few hundred changed lines.

**Quality guards:** plan the whole batch first, with a definition of done for each task · one commit per task · fast checks after each task, the full check at the end · **stop on an unclear failure,** and don't pile changes onto a broken base · report each task separately · self-review the whole diff.

## 3. Fewer round-trips within a turn
- Run independent tool calls **in parallel** (read several files, lint and test together).
- **Search, don't browse.** One `grep` beats opening five files.
- **Script repetitive edits**, then review the diff.
- Read once; take notes; don't re-open files you already read.
- Gather what you need, decide, then make the change in one go.

## Self-check
- [ ] Am I skipping research that could change a hard-to-reverse decision? (Do it.)
- [ ] Is anything here pure repetition that a map, script, or summary could replace?
- [ ] Are my batched tasks independent, separately committed, and separately verified?
