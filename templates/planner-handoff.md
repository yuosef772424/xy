# PLANNER HANDOFF

> Written by the planner for the **next planner session** only. Builder, researcher, and reviewer agents don't read this file unless their brief names it.
> **Aim:** a fresh planner can continue in a few minutes, with no history. Keep it compact (often 1–3k tokens). **Point to files instead of copying them.** Only record what isn't already in `STATUS.md`, `ROADMAP.md`, or the decision records.

**Written:** <date, time> · **Repo:** <owner/repo> · **Base:** <branch> @ <sha>

## Role & mode
- I am the <PLANNER/REVIEWER> for <repo>. Builders: <who and which model, one phase per PR>.
- Language: reply to the owner in <language>, short, decisions first; plans, prompts, and docs in <language>.
- Authority: <merge mode, e.g. "may merge with the full 40-char expectedHeadSha, then unsubscribe" (decision D-xxx)>; PR watching: <off>.

## Owner preferences (only the ones not in AGENTS.md)
- <e.g. few planner invocations; batch review + decisions + launches; paste-ready prompts>

## Plan pointers
- Plan files: <paths>. Decisions: <D-001..D-00n, path>. Current order: <A → B ‖ C → …>.
- Key constraints: <e.g. holdout rules, data cut-off dates, budgets>.

## Done since the last handoff
- MERGED: <#PR: one line each>. CLOSED: <#PR: why>.

## In flight
- Open branches and PRs: <branch / #PR @ sha: state>.
- Running agents: <task, branch, what to verify when it finishes>.

## Next batch (do these in one turn)
1. <verify X: commands / checks>
2. <merge / launch Y with brief Z>

## Open owner items
- <questions or inputs waiting on the owner>

## Review checklist & conventions
- <pointer to the checklist file, or a short list: commit order, protected files, checks with the baseline count, registry append-only>
- Agent prompts: identical COMMON RULES prefix ([template](agent-brief.md)); task part last; model <sonnet>.
