# 18 · Continuous Improvement (Get Smarter With Every Session)

**Goal:** The agent gets better **during** the project, not only between projects. Each invocation and each session should leave behind something that makes the next one faster, cheaper, or better: a lesson, a script, a shortcut, a better approach.

A model doesn't remember between sessions by itself. **The project remembers for it**, through files the agent writes and reads.

## 1. Learn as you work: `LESSONS.md`

Keep a short, living file of lessons for this project. Add an entry when something **surprised** you, **cost more than expected**, or **worked notably well**:

```markdown
- [2026-10-14] Integration tests fail locally unless Redis is running → use `make test-env` first. (saved ~3 failed runs)
- [2026-10-15] Library X's pagination is 0-based, unlike our API. Wrapped it in `adapters/x.ts`.
- [2026-10-16] Generating fixtures by script was 5× faster than writing them by hand → `scripts/gen_fixtures.py`.
```

- **Read it at the start of each session** (it's linked from `AGENTS.md` or `STATUS.md`).
- **Keep it useful, not long:** merge duplicates, delete lessons that no longer apply, and promote stable lessons into `AGENTS.md`, `MODULE.md`, or a script.

## 2. Automate what repeats

**If you do the same thing a second time, consider scripting it. By the third time, script it.**

- Typical candidates: setting up test data, running a sequence of checks, generating boilerplate, regenerating maps or docs, collecting a status report, bulk-renaming, checking release readiness.
- Put scripts in `scripts/`, give each a one-line description at the top, and list them in `AGENTS.md` (or let the project map list them).
- A script turns a repeated multi-step job (many tool calls, many tokens, some chance of mistakes) into one reliable command.

## 3. When a task is hard, change the approach

Don't keep repeating an approach that is failing. After **two real attempts** that didn't work:

1. **Step back:** write down what you tried, what happened, and why you think it failed.
2. **Generate alternatives,** at least two genuinely different ones:
   - a different algorithm, library, or architecture;
   - solving a simpler version first, then generalizing;
   - breaking the task into smaller verifiable pieces;
   - building a small tool or script that makes the task easier;
   - looking for how others solved it ([13](13-execution-orchestration.md) §4b);
   - reproducing the problem in isolation (a minimal example).
3. **Pick the most promising one with a reason,** and try it.
4. If you are still stuck, **escalate** with a summary of what was tried, so the owner or planner doesn't start from zero.

## 4. Look for better results, not just "done"

When a task is complete, ask briefly: *is there a clearly better way that is worth it?* (simpler code, a faster approach, a better library, a missing edge case). If yes and it is cheap, do it. If it is expensive, **propose** it as a follow-up instead of silently expanding the scope.

## 5. Remember failures and decisions

- **Failure log** (in `LESSONS.md` or `docs/failures.md`): what was tried and failed, why, and a **reopen-if** condition, e.g. "Rejected library Y: too slow for 10k rows. *Reopen if* it adds streaming support." This prevents retrying dead ends, while still allowing a fair second look later.
- **Decisions are superseded, not re-argued.** If a recorded decision should change, write a new decision record that replaces it and explains what changed. Don't re-debate it in every session.

## 6. Improve the playbook itself

At the end of each project (or a major milestone), run a short retrospective:

- What worked well? What wasted time or tokens? What went wrong?
- Which lessons apply to **all** projects, not just this one?

Turn those general lessons into proposed changes to this playbook (`ai-playbook`). That's how the system gets better with each project.

## Self-check at the end of a session

- [ ] Did I record any lesson worth keeping?
- [ ] Did I do anything repetitive that should become a script?
- [ ] Did I leave the maps, status, and docs more accurate than I found them?
- [ ] Is there a better approach I noticed but didn't pursue? (Propose it.)
