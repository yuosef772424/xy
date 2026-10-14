# PLANNER HANDOFF

> For the next planner/maintainer session of this repository only. Subagents don't read this unless a brief names it.

**Written:** 2026-10-14 · **Repo:** yuosef772424/xy (to be renamed `ai-playbook` by the owner) · **Branch:** `ccr-2e4725f6-4jk3ll` (the only branch; no PR is possible until a base branch exists) @ see `git log -1`

## Role & mode
- I maintain **ai-playbook**: English Markdown instructions + tools that make AI agents do project work well. The owner gives instructions one at a time; I implement, verify, commit, and push to the branch above.
- Language: **reply to the owner in Arabic**, short, outcome first, honest about limits. All repository files in **English**.
- Follow this repo's own `AGENTS.md` (honest judgment, question ≠ request, propose rather than silently change rules).

## Owner preferences (beyond AGENTS.md)
- Wants: no flattery but no reflexive criticism; correct their premises; flexible rules (goal + guideline, not hard numbers); each file must have a goal whose benefit exceeds its cost.
- Very cost-aware (planner context × steps), but **never cut research/quality to save tokens**; invest in R&D/tools with positive return, general tools preferred.
- Works as: one planner session + builder subagents (Sonnet); PR watching off; file-based handoffs; fresh session per roadmap item or ~150–200k tokens.
- Other owner projects that inspired rules: `yuosef772424/crypto-signal-prediction` (planner/builder workflow, failure registry F-xxxx, decisions D-xxx), bot2, linebyline.

## State (v1.3), pointers
- History and open items: `NOTES.md` (v1.0 consolidation → v1.1 gap fixes → v1.2 wake budget → v1.3 handoff). Proposals inbox: `PROPOSALS.md`.
- Structure: `AGENTS.md` (54 lines, index) · `playbooks/00–16` · `claude-code/` kit (agents builder/researcher/reviewer; skills handoff/status/propose; session-start hook) · `templates/` · `scripts/` (registry `scripts/README.md`: install_playbook, gen_map, doc_health, merge_check) · `evals/`.
- Verified: kit loads in real Claude Code 2.1.300 (`claude -p` in a scratch dir); installer tested on new + existing scratch projects; `python3 scripts/doc_health.py --playbook` → 0/0.

## Next batch (suggested; ask the owner which)
1. **Pilot on a real project** (owner must add the repo to the session, e.g. crypto-signal-prediction): dry-run `install_playbook.py`, merge their existing `CLAUDE.md`/working method by hand, record baseline metrics (tokens/phase, wakes/step, rework, bugs after merge, owner interventions).
2. Run `evals/cases.md` on the current model; record results.
3. Optional: convert long playbooks (11–13) into on-demand skills; gen_map upgrades (symbols, dep graph).

## Open owner items
- Rename repo `xy` → `ai-playbook` and set the branch as default (`main`) on GitHub.
- Which project to pilot first.

## Conventions
- Before every commit: `python3 scripts/doc_health.py --playbook` (0 errors). Test tools in the scratchpad, never in the repo. Commit messages end with the session's Co-Authored-By/Claude-Session lines; no model names in files.
