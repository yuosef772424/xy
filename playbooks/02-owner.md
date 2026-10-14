# 02 · Working With the Owner

> **Goal:** The owner spends their time on decisions and direction, not on chasing status or untangling reports. · **Read when:** every session (the summary is in `AGENTS.md`). · **Pays off because:** the owner's time and attention are the scarcest resource in the project.

## 1. A question is not a request
If the owner **asks**, answer and **change nothing**. If the answer suggests a change, offer it ("Want me to do this?"). When a message is ambiguous, treat it as a question and offer the action.

## 2. Correct the premise before executing
If a request rests on a mistaken assumption, say so briefly first, propose the corrected version, then proceed with it (or ask, if the correction changes the outcome a lot). Never silently carry out a request you believe is based on an error.

## 3. Asking for decisions
- Ask only when the decision is **really the owner's**: it changes the outcome, the cost, or the direction, and you can't infer it.
- Put **all open questions in one message**. For each: one or two lines of context, 2–4 options, and **your recommendation** with its reason.
- For everything else: choose the sensible default, state it, and continue.

## 3b. Autonomy: don't make the owner a bottleneck
Each project states in its `AGENTS.md` what agents may do **without asking**, so the owner only sees what really needs them:

| Level | Agents may, without asking |
|---|---|
| **Cautious** | Read, plan, propose; edit only on approval |
| **Standard** (default) | Edit, test, commit, push branches, open draft PRs; ask before merging, deleting, deploying, or spending |
| **Trusted** | Also merge after CI and review pass (small or experimental projects) |

Whatever the level, the irreversible actions in [03](03-safety.md) still need approval. To keep the owner's load low: batch questions, review `PROPOSALS.md` in periodic batches (not one by one), and put a ready-to-paste hand-off in every report that continues elsewhere.

## 4. Language
Talk to the owner in **their language**. Technical files (code, comments, commits, technical docs) default to **English**, which is clearer for tools and models and usually costs fewer tokens; a project may override this in its `AGENTS.md`. User-facing text uses the product's target languages.

## 5. Reports
**Aim:** understood in under a minute, on a phone.
- Outcome first, then details. Use short sections and tables.
- **Make progress measurable:** numbers and before/after comparisons (tests, features done vs planned, files changed, performance, cost).
- Separate clearly: ✅ done · ❌ failed or not done · ❓ needs your decision.
- Be honest: say exactly what failed or was skipped. When something is verified, say so plainly.
- Scale the length to the work: a one-line fix gets a one-line report.

## 6. Hand-off messages
When work continues in another session, end with a **ready-to-paste message** (the `/handoff` skill in the [Claude Code kit](../claude-code/README.md)): the goal and current state (with links), what was just done and found, the next step(s), decisions already made, and open questions. Make it as short as possible while letting a fresh session continue without asking.

## 7. Git and merging
- Work on branches; open PRs as **drafts** while the work is in progress. One logical change per commit, with imperative messages.
- **Important projects** (production, shared, or valuable code): the **owner** reviews and merges.
- **Small, experimental, or solo projects:** the planner may merge after CI passes and its review is done, if the owner allowed it ([13](13-execution.md)).
- Record the mode in the project's `AGENTS.md`. Never reopen a PR the owner closed. Never force-push shared branches.
