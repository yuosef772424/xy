# Tools Registry

General tools for any project. Check this list **before** building something new; improve an existing tool rather than duplicating it. See [09 · Improvement §4](../playbooks/09-improvement.md).

| Tool | Purpose | Status | Measured benefit | Last checked |
|---|---|---|---|---|
| [`install_playbook.py`](install_playbook.py) | Installs the playbook + Claude Code kit into a new or existing project; dry run by default; never overwrites | experimental | tested on a scratch existing project (41 files, 0 conflicts) | 2026-10-14 |
| [`gen_map.py`](gen_map.py) | Generates `PROJECT_MAP.md` (modules, purposes, file sizes); `--check` mode for CI | experimental | not yet measured; expected to replace most exploratory reads at task start | 2026-10-14 |
| [`merge_check.py`](merge_check.py) | Planner's one-call pre-merge check: commits, files, conflicts, append-only and protected-path rules → READY / NOT READY | experimental | replaces ~4–5 separate verification calls per merge; tested on good/bad branches | 2026-10-14 |
| [`doc_health.py`](doc_health.py) | Read-only: broken links, possibly stale `MODULE.md` files, oversized `STATUS.md`/`LESSONS.md`; `--playbook` checks playbook conventions | experimental | caught 3 real bugs during its first test | 2026-10-14 |

## Ideas backlog (not built yet)
- `status_report`: collect git/CI/test counts into a short report for the owner or `STATUS.md`.
- `check` runner: run fast/full checks with condensed, agent-friendly output.
- `eval_runner`: semi-automate the cases in `evals/`.
- `check` templates per stack (package.json scripts, Makefile) for the `check:fast` / `check` / `check:full` commands.
