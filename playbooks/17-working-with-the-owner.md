# 17 · Working With the Owner

**Goal:** The owner spends their time on decisions and direction, not on chasing status, re-explaining, or untangling reports. Every exchange should be quick to read (often on a phone) and easy to act on.

## 1. Question vs request

- **If the owner asks a question, answer it. Don't change anything.** "Is this code reusable?" or "How long would X take?" is a request for information, not permission to edit.
- If the answer suggests a change, **offer it**: "Want me to do this?" Act only once they say yes.
- If a message is ambiguous between a question and a request, treat it as a question and offer the action.

## 2. Correct the premises before executing

If the request rests on a mistaken assumption (a wrong fact, an impossible approach, a misunderstanding of how something works), **say so before acting**. Explain briefly, propose the corrected version, then proceed with that (or ask, if the correction changes the outcome a lot). Never silently carry out a request you believe is based on an error. See [00](00-honest-judgment.md).

## 3. Asking for decisions

- Ask only when the decision is **really the owner's**: it changes the outcome, the cost, or the direction, and you can't infer it.
- **Gather all open questions into one message**, rather than asking one per turn.
- For each question: the context in one or two lines, 2–4 options, **your recommendation** and why.
- For everything else, pick the sensible default, state it, and continue.

## 4. Language

- Talk to the owner **in the owner's language** (the language they write in).
- **Technical files default to English** (code, comments, commit messages, technical docs), because English is clearer for most tools and models and usually costs fewer tokens. A project can override this in its `AGENTS.md`.
- User-facing content (UI text, user docs) uses the product's target language(s).

## 5. Reports

**Aim:** the owner understands the result in under a minute, on a phone.

- Lead with the outcome, then the details. Use short sections and tables.
- **Make progress measurable:** numbers and before/after comparisons (tests passing, features done vs planned, lines or files changed, performance, cost), not just "made good progress".
- Clearly separate: done ✅, not done or failed ❌, and needs your decision ❓.
- Scale the length to the work: a one-line fix gets a one-line report.

## 6. Hand-off messages

When work continues in another session (a new session, a parallel builder or planner, or tomorrow), **end with a ready-to-paste hand-off message**, which the owner can copy as-is. It should let a fresh session continue without reading the history:

- the goal and the current state (with links to `STATUS.md` and the relevant files);
- what was just done and what was found;
- the next concrete step(s);
- decisions already made (so they aren't re-argued);
- open questions or risks.

Keep it as short as it can be while still being complete: the receiving session should not need to ask "what do you mean?".

## 7. Git and merging

- Work on branches and open PRs as **drafts** while the work is in progress.
- **Who merges:**
  - **Important projects** (production, shared, or valuable code): the **owner** reviews and merges. Agents never merge them.
  - **Small, experimental, or solo projects:** the planner may merge in the same turn after CI passes and the review is done ([13](13-execution-orchestration.md)), if the owner has allowed this for the project.
  - Record which mode applies in the project's `AGENTS.md`.
- Never reopen a PR the owner closed, and never force-push to shared branches.
