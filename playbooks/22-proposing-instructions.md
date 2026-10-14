# 22 · Proposing New Instructions (Keep the Playbook Growing)

**Goal:** Good ideas discovered while working (a better rule, a useful habit, a missing check) get **captured instead of lost**, and are reviewed by the owner before they become rules.

## When to propose

Add a proposal when you notice something that would likely help **future** work, for example:

- a lesson from `LESSONS.md` that applies beyond this project ([18](18-continuous-improvement.md));
- a recurring mistake that a rule or check would prevent;
- a gap: a situation no playbook covers;
- a rule that is wrong, outdated, too strict, or in conflict with another;
- a tool worth building or generalizing ([21](21-tooling-and-rnd.md));
- a preference the owner expressed more than once.

Don't propose one-off, project-specific details. Those belong in the project's own `AGENTS.md` or `LESSONS.md`.

## How to propose

1. **Append a row** to [`PROPOSALS.md`](../PROPOSALS.md) in the ai-playbook repository: date, source, the proposal in one line, why (with evidence), scope (general / project type), and status 🆕.
2. **If you can't write to the playbook repository** from the current project, put the proposal in the project's `LESSONS.md` with the tag `[playbook-proposal]`, and **mention it in your hand-off or final report**, so the owner can carry it over.
3. Keep it short. The owner reviews many at once.

## How proposals are reviewed

- The owner reviews the inbox **in batches**, not one by one: ✅ accept, ❌ reject (with a reason), or ⏸ defer (with a reopen-if condition).
- Accepted proposals are **applied together** in a consolidation pass, with the full playbook in view, and logged in `NOTES.md`. Avoid piecemeal edits that make the playbook inconsistent.
- Rejected and deferred proposals stay in the list, so the same idea isn't re-proposed without new evidence.

## Rules

- **Never change a playbook rule silently** because you think it's better. Propose it.
- Follow [00 · Honest judgment](00-honest-judgment.md): propose because of evidence, not to look helpful. Fewer, better proposals beat many weak ones.
