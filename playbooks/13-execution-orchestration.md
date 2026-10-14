# 13 · Execution Orchestration (One Planner, Builder Agents, Low Token Cost)

**Goal:** Turn the roadmap into merged, verified work through phases run by builder agents, while keeping token cost low **without** lowering quality.

Input: `ARCHITECTURE.md` and `ROADMAP.md` from [architecture planning](12-architecture-planning.md). The execution planner **follows** the architecture; it doesn't redesign it.

## 1. Roles

| Role | Runs as | Model | Does |
|---|---|---|---|
| **Owner** | the human | — | decides, supplies data or results, runs `/compact` when asked |
| **Planner / reviewer** | the one main session | strong model | picks the next phases, writes agent briefs, reviews by evidence, merges, keeps `STATUS.md` |
| **Builder** | a subagent launched by the planner | cheaper model (for example `sonnet`) | implements one phase = one branch = one PR, runs the checks, reports in ≤ 40 lines |
| **Fix agent** | a subagent launched by the planner | cheaper model | fixes one PR or moves work between branches; never merges |

The owner doesn't open separate build sessions: every builder is a subagent of the planner.

## 2. Where the cost comes from

Each time the planner is **invoked**, it re-reads its whole context: system prompt, tools, and conversation. Cached tokens are cheap (about 10% of normal input), but a large context times many wake-ups still adds up. For example, 30 wakes × 350k tokens ≈ 10M tokens re-read.

**The main cost drivers are the number of planner wakes × the planner's context size.**

Things that wake the planner:

1. a message from the owner;
2. a background agent finishing (once, at the end);
3. a background shell command finishing;
4. events on a subscribed PR: CI results, reviews, comments, merges. Opening a PR may subscribe the session automatically.

## 3. Planner rules

- **One wake does a whole batch.** In a single turn: verify the finished phase, open/merge its PR, update `STATUS.md`, and launch the next agents. Never wake up just to say "noted".
- **Control PR subscriptions.** On solo projects: open, mark ready, and merge in the same turn. If a PR must stay open for human review, unsubscribe from its events unless you actually need to react to them.
- **No long-running commands in the planner.** Long test suites run inside the builder's task, and the builder reports the counts.
- **Background vs foreground agents.** Run an agent in the background only when the planner has nothing else to do in the meantime. If you need the result in this turn, run it in the foreground.
- **Isolation.** Agents running in parallel each get their own worktree or clone. Two agents, or an agent and the planner, must never share a working tree.
- **Never commit another agent's work in progress,** even if a hook complains about uncommitted changes.
- **Keep the planner context small:**
  - Builders return short reports. The planner doesn't read big files or logs itself.
  - Verify with cheap commands: `git log --oneline`, `git diff --stat`, `git merge-tree`.
  - Keep messages ≤ ~50k tokens. Before reaching that, give the owner a ready `/compact <what to keep>` text.
- **Stay silent on routine notifications** (merged, ready, subscribed), or answer in one line.

## 4. Agent briefs (cache-friendly)

- **Shared prefix.** Prompt caching works on prefixes, so start every brief with the same **COMMON RULES** block, byte for byte ([template](../templates/agent-brief.md)). Put the task-specific part last.
- **Give exact pointers.** Every agent re-reads its own files, so give exact paths and line ranges, and list previous results it must not redo.
- **Every brief contains:** goal and definition of done; the branch and its base; constraints (no force-push, no merge, append-only registries, one change type per commit); the checks to run before pushing; and the report format (≤ 40 lines: full head SHA, commits, test counts, deviations).
- **Deviations:** the builder lists every deviation from the brief, and the planner explicitly accepts or rejects each one.
- **Model choice:** use the cheaper model by default. Use a stronger model only for open-ended research or design, and state why.

## 5. Review and merge

1. Read the builder's report, then **re-check its claims with cheap commands**, not by trusting the narrative: commit order, protected files, registry diffs, conflicts (`merge-tree`).
2. Apply the acceptance rule mechanically. A failed phase is a valid result: record it as a failure, don't hide it.
3. Create the PR → mark it ready → merge with the full head SHA, all in one turn (solo projects).
4. Put the `STATUS.md` update in the same batch, never in a turn of its own.

## 6. Balancing token cost and quality

Saving tokens matters, but **rework is the most expensive token cost of all**. Save on *overhead*, never on *verification*.

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

## 7. When execution hits an architecture problem

If a builder reports that the planned structure doesn't work (for example, an interface is missing, or two phases must touch the same file):

1. Stop the affected phases. Don't patch around it silently.
2. Write the problem down in one paragraph with evidence.
3. Make a small fix if it stays inside one module and changes no contract; record it in `STATUS.md`.
4. Otherwise, re-open [architecture planning](12-architecture-planning.md) in its own session, update `ARCHITECTURE.md` and `ROADMAP.md`, and then resume.

## 8. Owner checklist

- Talk to the planner only to decide, to supply data or results, or to run the `/compact` text it gives you.
- Watch context size and cost: planner messages should stay under ~50k tokens.
- Start each new project in a **new** planner session, and give it only `ARCHITECTURE.md`, `ROADMAP.md`, `STATUS.md`, and this playbook. Never reuse a huge old context.

## 9. Lessons behind these rules

- One planner wake ≈ a full re-read of its context. Notification chains (subscribed → ready → merged) each cost a wake.
- Measured agent reviews cost 95k–160k tokens each. That is still cheaper than the same reading in the planner context, which would be re-read on every later wake.
- An agent and the planner once shared a clone, and the planner's `git checkout` failed against the agent's uncommitted file. Hence the isolation rule.
