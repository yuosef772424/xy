# 19 · Token Budget (Spend for Value, Not for Minimum Cost)

**Goal:** Get the **most value** out of the available usage budget. Savings exist so that there is budget left for what matters, never to cut quality or research.

## The principle

The owner has a usage allowance and wants to use it as effectively as possible. **The most expensive outcome isn't a big research bill. It's discovering halfway through the project** that:

- a better existing solution was available online;
- important features were missing and now require restructuring;
- the idea wasn't viable, or a different approach would have been much better.

A short-sighted saving that leads to rework, a restart, or a weaker product is a **loss**, not a saving.

## Where to spend generously

- **Research at the start of the project:** market, competitors, feasibility ([12b](12b-market-and-feasibility-research.md)), and architecture options ([12](12-architecture-planning.md)). This is the highest-value spending in the whole project.
- **Prior-art research before non-trivial phases** ([13](13-execution-orchestration.md) §4b).
- **Design and decisions that are hard to reverse.**
- **Verification:** tests, reviews, re-checking claims.
- **Hard problems:** trying alternative approaches ([18](18-continuous-improvement.md) §3).

**Don't cut research to save tokens.** If you are unsure whether research is worth it for a decision that is costly to reverse, do it.

## Where to save (waste, not value)

- Re-reading the same files or logs; dumping full output when a summary would do.
- Exploring the whole codebase instead of using the maps ([14](14-codebase-maps.md)).
- Chatter, acknowledgements, and invocations that do nothing ([13](13-execution-orchestration.md) §3).
- Doing by hand what a script can do ([18](18-continuous-improvement.md) §2).
- Strong models on routine, well-specified work.
- Long contexts: start fresh sessions per roadmap item, and keep `STATUS.md` short enough to read in a minute.

## Practical habits

- **Check usage regularly** (for example `/usage` and `/context` in Claude Code) and at the end of each phase. Note in `STATUS.md` roughly what the phase cost compared with what was expected.
- **When a phase costs much more than expected,** find out why: is it waste (fix the process) or necessary work (adjust the estimate)?
- **When the budget really is tight,** tell the owner and propose what to drop or defer. **Don't quietly lower quality.**

## Self-check

- [ ] Did I skip research that could change a hard-to-reverse decision? If so, do it.
- [ ] Is anything I'm doing pure repetition that a map, script, or summary could replace?
- [ ] Would the owner rather pay this cost now, or discover the problem later? (Usually now.)
