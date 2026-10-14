# Tools Registry

General tools for any project. Check this list **before** building something new; improve an existing tool rather than duplicating it. See [09 · Improvement §4](../playbooks/09-improvement.md).

| Tool | Purpose | Status | Measured benefit | Last checked |
|---|---|---|---|---|
| [`gen_map.py`](gen_map.py) | Generates `PROJECT_MAP.md` (modules, purposes, file sizes); `--check` mode for CI | experimental | not yet measured; expected to replace most exploratory file reads at task start | 2026-10-14 |

## Ideas backlog (not built yet)
- `status_report`: collect git/CI/test counts into a short report for the owner or `STATUS.md`.
- `check` runner: run fast/full checks with condensed, agent-friendly output.
- `eval_runner`: semi-automate the cases in `evals/`.
- `new_project`: scaffold a project with `AGENTS.md`, maps, the check commands, and templates.
