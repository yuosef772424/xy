# Revision Notes

Working notes collected while the instructions are being written one by one. **Don't apply these piecemeal.** They will all be applied together in one final consolidation pass, so the whole playbook is designed with a full view.

## Log of added instructions

| # | Instruction | File | Integrated into AGENTS.md? |
|---|---|---|---|
| 1 | Honest judgment: no flattery, no reflexive criticism | `playbooks/00-honest-judgment.md` | Yes (section 0) |
| 2 | Evidence over agreement: research to correct bias, with cost proportional to stakes | `playbooks/00b-evidence-over-agreement.md` | **No, deferred to the final pass** |
| 3 | Architecture planning, kept separate from execution | `playbooks/12-architecture-planning.md` | **No, deferred** |
| 4 | Execution orchestration: planner + builder agents, token/quality balance (adapted from the owner's `WORKING_METHOD.md`) | `playbooks/13-execution-orchestration.md`, `templates/agent-brief.md`, `templates/status.md` | **No, deferred** |

## Notes for the final pass

### Structure
- **Numbering:** `00` and `00b` are temporary. Renumber all playbooks once the full list is known, possibly grouped by theme (Behavior / Process / Engineering / Communication).
- **Merge candidates:** `00-honest-judgment` and `00b-evidence-over-agreement` are two halves of one idea ("calibrated judgment"). Consider merging them into one playbook with two parts, or keeping them separate but cross-linked.
- **Keep `AGENTS.md` short.** It is loaded into context on every task, so every line has a cost. Make it an index of short rules plus links; the details live in playbooks. Target: under ~100 lines.
- **Duplication:** `AGENTS.md` section 6 duplicates `templates/project-instructions.md`. Keep only one source of truth.

### Content
- **Research tools vary by environment.** Some agents have no web search. Add a fallback: "if you can't search, say what you would check and mark the claim as unverified".
- **Language rule:** add "reply in the user's language; keep files in the project's language" to the communication playbook (in this project: chat in Arabic, files in English).
- **Conflicts between rules:** add a short priority order for when rules collide, e.g. *safety > honesty > user's explicit instructions > playbook defaults > style*.
- **Cost awareness in general:** the "effort ∝ stakes × uncertainty" idea from `00b` also applies to planning, testing, and review depth. Consider stating it once as a global principle.

### From instructions 3–4 (architecture vs execution)
- **Overlap with `02-planning` and `11-new-project`:** `02` covers planning a single task, `11` covers project setup, and `12`/`13` cover multi-phase projects. In the final pass, decide the boundaries clearly; `11` can probably become the "skeleton" step inside `12`.
- **Tool-specific content:** `13` mentions Claude Code features (`Agent`, worktrees, `/compact`, `/context`, `/usage`, PR subscriptions). Keep the principles general and move the tool-specific mechanics into a "Claude Code notes" box, so the playbook still works with other agents.
- **"Merge in the same turn" only fits solo projects.** On team projects, human review is needed and PRs stay open. Made conditional in `13`; double-check in the final pass that this doesn't conflict with `07-git-and-pull-requests`.
- **The numbers are from one project** (10% cache price, 95k–160k per review, 50k context limit). Label them as examples measured in 2026-10 that may change, not as fixed rules.
- **Global principle candidate:** "save on overhead, never on verification" (from `13` §6) pairs with "effort ∝ stakes × uncertainty" (from `00b`). Together they could become one top-level cost principle in `AGENTS.md`.
- **Single small-task mode:** `13` is heavy for small projects. Add a rule for when to use it, e.g. only for 3+ phases or multi-day work; otherwise just use the core loop.

### Validation
- **Instructions reduce sycophancy but don't remove it,** because it comes partly from training. Add an `evals/` folder with test prompts (deliberately bad ideas, false claims stated confidently, pushback on correct answers, and good ideas that should *not* be criticized) to measure whether the instructions work with each model.
