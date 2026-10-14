# Revision Notes

Working notes collected while the instructions are being written one by one. **Don't apply these piecemeal.** They will all be applied together in one final consolidation pass, so the whole playbook is designed with a full view.

## Log of added instructions

| # | Instruction | File | Integrated into AGENTS.md? |
|---|---|---|---|
| 1 | Honest judgment: no flattery, no reflexive criticism | `playbooks/00-honest-judgment.md` | Yes (section 0) |
| 2 | Evidence over agreement: research to correct bias, with cost proportional to stakes | `playbooks/00b-evidence-over-agreement.md` | **No, deferred to the final pass** |

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

### Validation
- **Instructions reduce sycophancy but don't remove it,** because it comes partly from training. Add an `evals/` folder with test prompts (deliberately bad ideas, false claims stated confidently, pushback on correct answers, and good ideas that should *not* be criticized) to measure whether the instructions work with each model.
