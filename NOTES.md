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

## Owner directives (keep these when editing)
1. No flattery and no reflexive criticism; balanced, evidence-based judgment.
2. Separate architecture planning from execution; structure by rules.
3. Deep research is worth its cost; never skimp on research or quality to save tokens.
4. Rules state goals and outcomes; numbers are flexible guidelines.
5. The agent must improve every session: lessons, alternative approaches, tools, proposals.
6. Every file must have a goal whose benefit exceeds its cost.

## Open items
- **Validate the Claude Code kit in a real project** (subagent and skill frontmatter, hook path). Fix and note any format drift.
- **Run `evals/`** on the current model and record the results.
- **Build `new_project`** (scaffolds a project with the whole playbook in one command); it is the top item in `PROPOSALS.md`.
- Consider converting the long playbooks (11–13) into on-demand Claude Code skills, so they load only when relevant.
- Gaps to fill only when a real project needs them: privacy-law specifics, mobile-app specifics (store review, offline), multi-person teams.
- `gen_map.py` upgrades: exported symbols per file, a dependency graph, monorepo support.
