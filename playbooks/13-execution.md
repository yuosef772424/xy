# 13 · Execution: One Planner, Builder Agents, Smart Cost

> **Goal:** Turn the roadmap into merged, verified work through phases run by builder agents, getting the most out of the budget **without** lowering quality. · **Read when:** running a multi-phase project (roughly 3+ phases or multi-day work; for smaller work, the [task workflow](04-task-workflow.md) is enough). · **Pays off because:** it removes the biggest cost drivers (planner wakes × context size) while keeping verification strict.

Input: `ARCHITECTURE.md` and `ROADMAP.md` from [architecture planning](11-architecture.md). The execution planner **follows** the architecture; it doesn't redesign it.

## 1. Roles

| Role | Runs as | Model | Does |
|---|---|---|---|
| **Owner** | the human | — | decides, supplies data or results, runs `/compact` when asked |
| **Planner / reviewer** | the one main session | strong model | picks the next phases, writes agent briefs, reviews by evidence, merges, keeps `STATUS.md` |
| **Builder** | a subagent launched by the planner | cheaper model (for example `sonnet`) | implements one phase = one branch = one PR, runs the checks, reports briefly |
| **Fix agent** | a subagent launched by the planner | cheaper model | fixes one PR or moves work between branches; never merges |

The owner doesn't open separate build sessions: every builder is a subagent of the planner.

## 2. Where the cost comes from

Each time the planner is **invoked**, it re-reads its whole context: system prompt, tools, and conversation. Cached tokens are cheap (about 10% of normal input at the time of writing), but a large context times many wake-ups still adds up. For example, 30 wakes × 350k tokens ≈ 10M tokens re-read.

**The main cost drivers are the number of planner wakes × the planner's context size.**

Things that wake the planner:

1. a message from the owner;
2. a background agent finishing (once, at the end);
3. a background shell command finishing;
4. events on a subscribed PR: CI results, reviews, comments, merges. Opening a PR may subscribe the session automatically;
5. **a stop hook that rejects the end of a turn**, for example "there are uncommitted changes". The planner is sent back to work, answers, tries to stop again, and is rejected again. This loop can repeat many times.

### 2b. Wake budget: typical waste and its fix
Measured in a real project (2026-10): a single "merge #19 and launch the fix for #13" step produced **about 8 planner wakes**, when 2 would have been enough. The causes, and the fixes:

| Wasted wake | Cause | Fix |
|---|---|---|
| "ready" and "merged" notifications, ×2 PRs | Opening a PR auto-subscribed the session | Create → ready → merge in **one turn**, then unsubscribe at once. If the PR stays open for review, unsubscribe right after creating it |
| A separate PR just for `STATUS.md` | Status was updated in its own cycle | Add the `STATUS.md` commit **to the same PR before merging** it (from the planner's worktree) |
| Repeated "won't commit, the file belongs to the agent" answers | The fix agent worked in the **planner's own clone**, so the stop hook kept seeing uncommitted changes | **Every** agent works in its own worktree (`isolation: "worktree"`), not only parallel ones. The planner's clone stays clean |
| Replies to routine notices | Acknowledging | Stay silent. The real fix is not receiving them (row 1) |

**Target:** one wake per completed agent, plus one per owner message. Anything more is waste, so find its cause and remove it.

## 3. Planner rules

- **One wake does a whole batch** ([08](08-efficiency.md) §2). In a single turn: verify the finished phase, open/merge its PR, update `STATUS.md`, and launch the next agents. Never wake up just to say "noted".
- **Control PR subscriptions.** Where the planner may merge ([02](02-owner.md) §7): open, mark ready, and merge in the same turn. If a PR must stay open for human review, unsubscribe from its events unless you actually need to react to them.
- **No long-running commands in the planner.** Long test suites run inside the builder's task, and the builder reports the counts.
- **Background vs foreground agents.** Run an agent in the background only when the planner has nothing else to do in the meantime. If you need the result in this turn, run it in the foreground.
- **Give agents complete chains.** When the steps are well-specified, one agent does the whole chain (fix → test → push → open the PR as ready, with the report in its body), so the planner wakes **once** to verify and merge, instead of after each step.
- **Isolation, always.** **Every** agent gets its own worktree or clone, even when it is the only one running. The planner's own working tree must stay clean: uncommitted files there trigger stop-hook loops (§2b). When the planner edits docs while agents run, it uses its own worktree too.
- **Never commit another agent's work in progress,** even if a hook complains about uncommitted changes.
- **Keep the planner context small:**
  - Builders return short reports. The planner doesn't read big files or logs itself.
  - Verify with cheap commands: `git log --oneline`, `git diff --stat`, `git merge-tree`.
  - Keep the conversation compact (in one project, ~50k tokens of messages worked well). Before it grows large, give the owner a ready `/compact <what to keep>` text, or a hand-off for a fresh session ([02](02-owner.md) §6).
- **Stay silent on routine notifications** (merged, ready, subscribed), or answer in one line.

## 4. Agent briefs (cache-friendly)

- **Shared prefix.** Prompt caching works on prefixes, so start every brief with the same **COMMON RULES** block, byte for byte ([template](../templates/agent-brief.md)). Put the task-specific part last. In Claude Code, the `builder`, `researcher`, and `reviewer` subagents from the [kit](../claude-code/README.md) carry these rules.
- **Give exact pointers.** Every agent re-reads its own files, so give exact paths and line ranges, and list previous results it must not redo.
- **Every brief contains:** goal and definition of done; the branch and its base; constraints (no force-push, no merge, append-only registries, one change type per commit); the checks to run before pushing; and the report format (short, around 40 lines: full head SHA, commits, test counts, deviations).
- **Deviations:** the builder lists every deviation from the brief, and the planner explicitly accepts or rejects each one.
- **Model choice:** use the cheaper model by default. Use a stronger model only for open-ended research or design, and state why.

## 5. Prior-art research for each phase

**Goal:** Before building a phase, find out what already exists, so builders reuse proven solutions and learn from others' mistakes instead of reinventing them.

**What to look for**, in projects that are similar *or not*, as long as they solved the same **task**:
- libraries or services that already do the job (build vs buy vs reuse);
- open-source implementations of the same feature: how they structured it, and what their issue tracker says went wrong;
- known patterns, best practices, and common pitfalls for this type of task;
- security or performance lessons ("X approach broke at scale because…").

**Scale the research to the phase** (cost balance):

| Phase type | Research | Who |
|---|---|---|
| Routine (CRUD, config, small UI) | **None**, or a quick check of the project's own `docs/prior-art/` | The builder itself |
| Standard feature with known solutions (auth, payments, file upload, search) | **Quick:** 3–8 searches; pick a library or pattern | A short research step at the start of the builder's task |
| Novel, risky, or core feature | **Dedicated research agent** that compares 2–4 approaches and returns a recommendation | A separate research agent, before the builder |

**Rules:**
- **Report in ≤ 30 lines:** options found, the recommendation, why, links, and the license of any reusable code.
- **Save the findings** in `docs/prior-art/<topic>.md`, so later phases reuse them instead of searching again.
- **Check licenses** before copying code: MIT, Apache-2.0, and BSD are usually fine with attribution; GPL/AGPL need an explicit decision.
- **Check health** before adding a dependency: recent releases, open issues, maintainers, and download counts.
- **Respect the architecture:** a borrowed solution must fit the module rules in [12](12-architecture-rules.md). If it requires breaking them, escalate (see §8).
- **Batch research for parallel phases** into one agent when their topics overlap.
- **Don't skimp on non-trivial research to save tokens.** Finding a better existing solution halfway through costs far more ([08](08-efficiency.md)).

## 6. Review and merge

1. Read the builder's report, then **re-check its claims with cheap commands** (one call: [`scripts/merge_check.py`](../scripts/merge_check.py) `<branch> --base origin/main --append-only <registries> --protected <paths>` reports commits, files, conflicts, and append-only or protected-path violations, with a READY / NOT READY verdict), not by trusting the narrative: commit order, protected files, registry diffs, conflicts (`merge-tree`).
2. Apply the acceptance rule mechanically. A failed phase is a valid result: record it as a failure, don't hide it.
3. Where the planner may merge ([02](02-owner.md) §7): create the PR → mark it ready → merge with the full head SHA, all in one turn. Otherwise open the PR as a draft, mark it ready for the owner, and unsubscribe from its events.
4. Put the `STATUS.md` update **in the same PR, before merging it**, never in a separate PR or a turn of its own.

## 7. Balancing cost and quality

Saving tokens matters, but **rework is the most expensive cost of all**. Save on *overhead*; never save on *verification* or on *research* ([08](08-efficiency.md)).

| Save here (overhead) | Never cut here (quality) |
|---|---|
| Extra planner wakes, acknowledgements, chatter | Running the tests and checks for every phase |
| The planner reading large files or logs | Re-checking a builder's claims before merging |
| Strong models on routine, well-specified phases | A strong model for design, ambiguous bugs, or security |
| Long builder reports | Listing deviations and failures |
| Re-reading the whole design in every session | A clear definition of done in every brief |

**Rules of thumb:**

- **Spend in proportion to risk.** Routine phase → cheap model, short brief. Risky phase (data migration, auth, payments, core interfaces) → stronger model or an extra review agent.
- **A review agent can be cheaper than self-review.** An agent review can cost 95k–160k tokens, but doing the same reading in the planner context costs it again on every later wake.
- **Escalate instead of looping.** If a builder fails the same phase twice, stop. Either rewrite the brief, split the phase, or send it back to architecture planning. Don't keep retrying with the same brief.
- **Measure.** Check context size (`/context`) and cost (`/usage`) regularly, and adjust the batching when a phase turns out unexpectedly expensive.

## 8. When execution hits an architecture problem

If a builder reports that the planned structure doesn't work (for example, an interface is missing, or two phases must touch the same file):

1. Stop the affected phases. Don't patch around it silently.
2. Write the problem down in one paragraph with evidence.
3. Make a small fix if it stays inside one module and changes no contract; record it in `STATUS.md`.
4. Otherwise, re-open [architecture planning](11-architecture.md) in its own session, update `ARCHITECTURE.md` and `ROADMAP.md`, and then resume.

## 9. Owner checklist

- Talk to the planner only to decide, to supply data or results, or to run the `/compact` text it gives you.
- Watch context size and cost (`/context`, `/usage`); ask for a hand-off when the conversation grows large.
- Start each new project in a **new** planner session, and give it only `ARCHITECTURE.md`, `ROADMAP.md`, `STATUS.md`, and this playbook. Never reuse a huge old context.

## 10. Lessons behind these rules

- One planner wake ≈ a full re-read of its context. Notification chains (subscribed → ready → merged) each cost a wake.
- (Measured in one project, 2026-10; numbers will vary.) Agent reviews cost 95k–160k tokens each. That is still cheaper than the same reading in the planner context, which would be re-read on every later wake.
- An agent and the planner once shared a clone, and the planner's `git checkout` failed against the agent's uncommitted file. Hence the isolation rule.
- Again later: a fix agent ran in the planner's clone, and the stop hook's "uncommitted changes" check kept re-waking the planner. Together with PR notifications and a separate STATUS PR, one step cost about 8 wakes instead of 2 (§2b). Hence **isolation always**, and "STATUS in the same PR".
