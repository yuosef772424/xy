# 09 · Improvement: Lessons, Smarter Approaches, Tools, Proposals

> **Goal:** The agent gets better **during** the project and across projects: it learns, finds better approaches, builds tools, and grows this playbook. · **Read when:** at the end of each session (self-check), when a task is hard, when something repeats, and at project milestones. · **Pays off because:** each improvement compounds. A lesson or tool built once saves effort in every later session.

A model doesn't remember between sessions. **The project remembers for it**, through files.

## 1. `LESSONS.md`: learn as you work
Add an entry when something surprised you, cost more than expected, or worked notably well:
```markdown
- [2026-10-14] Integration tests need Redis → run `make test-env` first. (saved ~3 failed runs)
```
Read it at session start (the [Claude Code kit](../claude-code/README.md) hook shows it automatically). Keep it useful: merge duplicates, delete stale entries, and promote stable lessons into `AGENTS.md`, a `MODULE.md`, or a script.

**Failures and decisions:** log rejected approaches with a **reopen-if** condition ("Rejected library Y: too slow for 10k rows. Reopen if it adds streaming."). Decisions are **superseded** by a new decision record, never re-argued in every session.

## 2. Automate what repeats
If you do something a second time, consider a script; by the third time, write it. Typical candidates: test-data setup, check sequences, boilerplate, status reports, bulk edits. A script turns many tool calls, many tokens, and some risk of error into one reliable command.

## 3. When a task is hard, change the approach
After **two real attempts** that didn't work:
1. Write down what you tried, what happened, and why you think it failed.
2. Generate **at least two genuinely different** alternatives: a different algorithm or library; a simpler version first; smaller verifiable pieces; a helper tool; how others solved it ([13](13-execution.md) §5); a minimal reproduction.
3. Try the most promising one, with a reason.
4. If you are still stuck, escalate with that summary.

When a task is done, ask: *is there a clearly better way?* If it's cheap, do it; if it's expensive, propose it.

## 4. Tools & R&D: invest to work better
- **What counts:** exploring new tools (MCP servers, CLIs, libraries, model features), building and improving your own tools, and spikes that test a better approach.
- **Budget:** a deliberate share, roughly 10–20% of effort as a guideline. More early in a project, less near deadlines. Timebox exploration; propose large R&D to the owner first. Mention R&D openly in plans and reports.
- **Positive return is the rule:** *benefit ≈ (saved per use + quality gained) × expected uses* must clearly exceed *cost ≈ build + learn + maintain*. After real use, check the actual return, then keep, improve, or retire the tool.
- **Where tools live:** **general** tools (preferred) in this playbook's `scripts/`; **project-specific** tools in the project's `scripts/`. When a project tool proves useful in a second project, generalize it and move it here.
- **Quality standard:** a header (purpose, usage, example) · `--help` · safe by default (read-only or dry-run) · concise output · fails loudly · at least a smoke test · no secrets.
- **Registry:** [`scripts/README.md`](../scripts/README.md) lists every tool with its status (experimental → stable → deprecated) and its measured benefit. **Check it before building anything.**
- Periodically spend a short timebox looking for new tools or model features that could help, and record the verdict.

## 5. Grow the playbook: proposals
When you notice something useful **beyond this project** (a general lesson, a recurring mistake that a rule would prevent, a gap, an outdated or too-strict rule, a tool worth generalizing, a preference the owner repeated):
- Add one row to [`PROPOSALS.md`](../PROPOSALS.md): date · source · proposal · why, with evidence · scope · 🆕. Use the `/propose` skill.
- If the playbook repository isn't reachable, tag it `[playbook-proposal]` in the project's `LESSONS.md` and mention it in your report.
- **Never change a playbook rule silently.** The owner reviews proposals in batches (✅ / ❌ with a reason / ⏸ with reopen-if), and accepted ones are applied together in a consolidation pass.
- Propose from evidence; fewer, better proposals beat many weak ones.

At the end of each project, run a short retrospective (what worked, what wasted effort, what went wrong) and turn the general lessons into proposals.

## End-of-session self-check
- [ ] Any lesson worth recording? Any repetition worth a script?
- [ ] Did I leave the maps, status, and docs more accurate than I found them?
- [ ] Any better approach or general insight to propose?
