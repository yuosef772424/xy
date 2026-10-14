# Revision Notes

The playbook's own history and open items. New ideas go to [`PROPOSALS.md`](PROPOSALS.md); this file records what was **applied**, and what is still open.

## v1.0 consolidation (2026-10-14)
Twenty-six playbooks plus a prompts guide were merged into **17 playbooks**, ordered by use. Each one opens with its goal, when to read it, and why it pays off (principle: *every artifact must earn its place*).

| New | Merged from |
|---|---|
| 00 Principles | core principles (goals over numbers, rule priority, value over cost) |
| 01 Judgment | honest judgment + evidence over agreement |
| 02 Owner | working with the owner + communication + git/PR rules |
| 03 Safety | security + agent safety |
| 04 Task workflow | understand + planning + writing code + code review |
| 05 Testing | testing + automated testing |
| 06 Debugging | debugging + baseline check on the parent commit |
| 07 Maps & docs | codebase maps + documentation |
| 08 Efficiency | token budget + batching |
| 09 Improvement | continuous improvement + tooling & R&D + proposing instructions |
| 10 Market research | market & feasibility research |
| 11 Architecture | architecture planning + new-project setup |
| 12 Architecture rules | architecture rules (size limits softened to guidelines) |
| 13 Execution | execution orchestration (+ prior-art research, flexible numbers, merge mode) |
| 14 Product quality | product quality |
| 15 Operations | operations |
| 16 Prompting | prompt-writing guide + LLM-feature prompts |

Other changes:
- `AGENTS.md` rewritten as a short index of rules with links (54 lines, down from 69, while covering about 3× more topics).
- Hard numbers rewritten as goal + guideline across the playbooks. Measured numbers are labeled as examples from one project.
- "Minimize tokens" wording aligned with "spend for value; never cut research or verification".
- The project section of `AGENTS.md` now points to the template (no duplication); the template gained language, merge mode, and builder model.
- Owner decisions applied: chat in the owner's language, technical files in English; the owner merges important projects, the planner may merge small ones.

## v1.1: gap fixes (2026-10-14)
Fixes for the risks identified after v1.0, each turned into a mechanism where possible:

| Risk | Fix |
|---|---|
| Weaker rule-following in long sessions | Session-start hook now injects the key rules every session; `AGENTS.md` kept short; `doc_health.py --playbook` guards the playbook's own size and conventions |
| Owner as a bottleneck | Autonomy levels (`02` §3b) + batched proposal reviews |
| Too much process on small projects | Project tiers (`00` §6) |
| Hand-written docs going stale | `scripts/doc_health.py` (stale `MODULE.md`, broken links, oversized status/lessons), shown by the hook |
| Research errors | Two independent sources for key facts, dated findings, a second-agent spot-check (`01`, `10`) |
| Claude Code kit untested | **Tested** with Claude Code 2.1.300: subagents, skills, and the hook all load |
| Planner context growth | Fresh session per roadmap item or at about ⅓–½ of the context window (`08` §2b) |
| Existing projects | `scripts/install_playbook.py` (never overwrites) + "Adopting in an existing project" (`11`) with a ratchet baseline for architecture rules |

Testing caught and fixed 3 bugs: `gen_map` treated docs-only folders as modules; installed playbooks linked to files missing in projects; the tools registry was installed under the wrong name.
Still not automatic: detecting conflicts between rules (handled by the priority order + `PROPOSALS.md`), and judging design or research quality (handled by reviews and health checks).

## v1.2: wake budget (2026-10-14)
From a real planner transcript: one merge-and-launch step cost about 8 wakes instead of 2. Causes: auto-subscribed PR notifications, a separate STATUS PR, and a fix agent working in the planner's clone (so the stop hook kept rejecting "uncommitted changes"). Fixes in `13` §2b and §3: isolation for **every** agent, STATUS inside the same PR, create→ready→merge→unsubscribe in one turn, and complete agent chains. Added `scripts/merge_check.py` (one-call pre-merge verification) and updated the builder agent and the brief template.

## v1.3: file-based planner handoff (2026-10-14)
`/handoff` now writes `.planner/HANDOFF.md` ([template](templates/planner-handoff.md)), commits it, and gives the owner one paste-ready restart line, plus an optional `/compact` line that keeps only the handoff. `.planner/` is planner-only: the subagents, the brief template, and `CLAUDE.md` say not to read it unless a brief names a file there (this is instruction-level separation, not a hard guarantee). Context thresholds: a fresh session after each roadmap item or at ~150–200k tokens; ~500k is an emergency limit. Tested in a real Claude Code session: a ~1k-token handoff was written and committed.

## Owner directives (keep these when editing)
1. No flattery and no reflexive criticism; balanced, evidence-based judgment.
2. Separate architecture planning from execution; structure by rules.
3. Deep research is worth its cost; never skimp on research or quality to save tokens.
4. Rules state goals and outcomes; numbers are flexible guidelines.
5. The agent must improve every session: lessons, alternative approaches, tools, proposals.
6. Every file must have a goal whose benefit exceeds its cost.

## Open items
- **Run `evals/`** on the current model and record the results.
- **Pilot on a real project** and record: tokens per phase, rework count, bugs after merge, owner interventions, eval results.
- Consider converting the long playbooks (11–13) into on-demand Claude Code skills, so they load only when relevant.
- Gaps to fill only when a real project needs them: privacy-law specifics, mobile-app specifics (store review, offline), multi-person teams.
- `gen_map.py` upgrades: exported symbols per file, a dependency graph, monorepo support.
