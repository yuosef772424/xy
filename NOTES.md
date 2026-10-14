# Revision Notes

Working notes collected while the instructions are being written one by one. **Don't apply these piecemeal.** They will all be applied together in one final consolidation pass, so the whole playbook is designed with a full view.

## Log of added instructions

| # | Instruction | File | Integrated into AGENTS.md? |
|---|---|---|---|
| 1 | Honest judgment: no flattery, no reflexive criticism | `playbooks/00-honest-judgment.md` | Yes (section 0) |
| 2 | Evidence over agreement: research to correct bias, with cost proportional to stakes | `playbooks/00b-evidence-over-agreement.md` | **No, deferred to the final pass** |
| 3 | Architecture planning, kept separate from execution | `playbooks/12-architecture-planning.md` | **No, deferred** |
| 4 | Execution orchestration: planner + builder agents, token/quality balance (adapted from the owner's `WORKING_METHOD.md`) | `playbooks/13-execution-orchestration.md`, `templates/agent-brief.md`, `templates/status.md` | **No, deferred** |
| 5 | Architecture rules: scope classes, extension test, decomposition, dependency rules, growth limits, CI enforcement | `playbooks/12a-architecture-rules.md` (linked from `12`) | **No, deferred** |
| 6 | Market & feasibility research with a GO / NO-GO verdict | `playbooks/12b-market-and-feasibility-research.md`, `templates/market-research.md` | **No, deferred** |
| 7 | Prior-art research for each execution phase, scaled to the phase's risk | `playbooks/13-execution-orchestration.md` §4b | **No, deferred** |
| 8 | Codebase maps: a generated project map + a `MODULE.md` per module + a reading protocol | `playbooks/14-codebase-maps.md`, `templates/MODULE.md`, `scripts/gen_map.py` | **No, deferred** |
| 9 | Automated testing: check levels, token-efficient output, hooks and CI | `playbooks/15-automated-testing.md` | **No, deferred** |
| 10 | Batching: more tasks per invocation with quality guards | `playbooks/16-batching-work.md` | **No, deferred** |
| 11–13 | Core principles, owner protocol, continuous improvement, token budget, LLM-feature prompts, evals | `00c`, `17`–`20`, `evals/` | **No, deferred** |
| 14 | Tooling & R&D + tools registry | `21`, `scripts/README.md` | **No, deferred** |
| 15 | Proposals inbox (+ gaps: operations, product quality, agent safety, Claude Code kit) | `22`–`25`, `PROPOSALS.md`, `claude-code/` | **No, deferred** |

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

### From instructions 5–7
- **Size:** `12a` is long (~200 lines). It is a reference to consult during design, not something loaded every turn. In the final pass, consider a short "rules summary" (~20 lines) for `ARCHITECTURE.md` plus the full file as a reference.
- **Stack-specific examples:** the tool names in `12a` Part F are examples. Consider per-stack appendices later (JS/TS, Python, Go, Java).
- **Size limits are heuristics,** not laws. Keep the wording "soft limit" so agents don't split files mechanically.
- **Honest expectation:** the rules sharply reduce structural decay, but CI enforcement (Part F) and periodic health checks are what make them hold. Without enforcement they will drift like any document.
- **Research overlap:** `00b` (evidence levels), `12b` (deep market research), and `13` §4b (prior-art per phase) share one cost model. Unify the wording, and possibly extract a shared "research" playbook.
- **Ordering:** `12b` runs *before* `12`'s design steps, so the numbering should reflect the real order: research → scope → architecture → roadmap → execution.
- **Licensing and legal** appear in both `12b` and `13` §4b; they may deserve a small dedicated section in `09-security` or a new compliance playbook.

### From instructions 8–10
- **Correction recorded:** maps can't "update themselves". The *structural* part is regenerated by a script and enforced by CI (`--check`); the *descriptive* part (`MODULE.md`) is updated by the builder in the same PR and spot-checked. The playbook says this explicitly.
- **Correction recorded:** fewer invocations ≠ always fewer tokens. Oversized batches grow the context and cause rework. `16` therefore sets a batch-size guideline and quality guards.
- **`gen_map.py` is a minimal example** (structure + purposes + line counts). Possible upgrades: exported symbols per file (tree-sitter), a dependency graph, and support for monorepos. It was tested in a scratch project: it generates the map, `--check` passes when the map is fresh, and it fails when stale.
- **Overlap:** `04-testing` (how to write tests) and `15-automated-testing` (automation and CI) should be merged or clearly split in the final pass. `16` §5 repeats `13` §3; keep it in one place.
- **Global principle candidate:** "machines verify, models decide". Anything a script can check shouldn't cost model tokens. This belongs in `AGENTS.md` next to the cost principles.
- **The project-setup playbook (`11`)** should include: create `PROJECT_MAP.md` + the generator, the `check:*` commands, the pre-commit hook, and a `MODULE.md` per module from day one.

### Proposed instructions (status after owner approval on 2026-10-14)
Applied: A, B, C, D, E, H, L → `17`; G, M + new continuous improvement → `18`; F, I + new token stance → `19`; K → `20`; N → `00c`; P → `evals/`. **Deferred:** O (post-build ops), until a project is ready to deploy. **Pending edit:** J (baseline check on the parent commit) → add to `05-debugging` in the final pass.
Owner decisions taken by default (owner said "add what you find suitable"): technical files in English, chat in the owner's language; owner merges important projects, planner may merge small or experimental ones.

#### Original list
From Claude's suggestions (S) and from mining the owner's past sessions (P):
- A · Owner-interaction protocol: ask only real decisions, all questions in one message, options + recommendation, short mobile-friendly reports (S1, P9).
- B · Question ≠ request: when the owner only asks, answer and change nothing (P7).
- C · Correct the owner's premises before executing (S2).
- D · Language: chat in the owner's language; files per project, **owner decision needed** (P8 found Arabic docs in one project and English in another).
- E · Hand-off message: end work with a short, ready-to-paste message for the other session or a new session (P3, P4).
- F · Fresh session per roadmap item; `STATUS.md` ≤ 60 lines, read first (P4).
- G · Failure registry with `reopen_if`; supersede decision records, never re-argue them (P5).
- H · Measurable progress reports: before/after comparisons, numbers (P11).
- I · Cost tracking: check usage regularly, trim tool output, report tokens per phase vs estimate (S6, P1).
- J · Baseline check: run a failing test on the parent commit before blaming the change (P14).
- K · Prompt design for LLM features: closed-list choices, treat user claims as data, state confidence, validate outputs in code (P6).
- L · Git: draft PRs; the owner merges; never reopen a closed PR (P10). Conflicts with `13`'s "merge in the same turn"; needs a decision.
- M · Lessons-learned loop after each project, fed back into the playbook (S5).
- N · Rule priority order when instructions conflict (S7).
- O · Post-build: deployment, monitoring, backups, incidents (S8).
- P · `evals/` to test the instructions themselves (S9).

### From instructions 11–13 (flexibility, continuous improvement, token stance)
- **Owner directive: flexible rules.** Rewrite hard numbers across *all* playbooks as goal + guideline in the final pass. Known spots: `13` (≤ 40-line reports, ≤ 50k context), `12a` (size limits table), `14` (≤ 60-line MODULE.md, ~200-line read threshold), `15` (time targets), `16` (~5 tasks / ~300 lines), `12` (~300-line ARCHITECTURE.md), `12b` (10–25 competitors). `00c` §1 now states the principle globally, so a light touch may be enough.
- **Owner directive: tokens are a budget to invest.** The wording of `13` §6 and `16` leans toward "minimize". Align it with `19`: savings come from waste, never from research or verification.
- **`00c` is the seed of the new `AGENTS.md`.** In the final pass, `AGENTS.md` should be roughly: principles (00c) + honest judgment (00 summary) + core loop + owner protocol summary (17) + links.
- **`18` and `NOTES.md` overlap in spirit:** this repository's `NOTES.md` is itself a lessons/improvement log for the playbook. Keep it as the playbook's own retrospective file.

### From instruction 14 (R&D and tooling)
- Added `21-tooling-and-rnd.md` and a tools registry (`scripts/README.md`), with an ideas backlog: status report, check runner, eval runner, new-project scaffolder.
- **Overlap:** `18` §2 (automate repeats) and `21` cover the same habit at different scales. In the final pass, `18` should keep the "notice and script it" habit and link to `21` for standards, budget, and the registry.
- **The R&D share (10–20%) is a guideline** per `00c`; the real test is the return in `21` §3.
- **This repository is itself the general toolbox.** The final `README.md` should present it as playbook + toolkit. The `new_project` scaffolder would be the highest-value next tool, since it applies the whole playbook in one command.

### From instruction 15 (gaps + proposals inbox)
- **Inbox vs notes:** `PROPOSALS.md` holds ideas *for review*; `NOTES.md` holds *accepted* changes waiting for consolidation. Keep both, and say so in the final README.
- **Operations (`23`)** replaces the deferred item O; it is scaled by project type.
- **The Claude Code kit is the main differentiator:** behavior loads automatically (CLAUDE.md import, subagents, skills, a hook) instead of depending on the model reading docs. The hook was tested in a scratch dir. The settings JSON is valid. The skill and agent frontmatter follows the current documented format, but **verify it in a real project** and adjust if Claude Code changed. Possible next: turn the bigger playbooks (12, 12a, 13) into on-demand skills, so they load only when relevant.
- **Remaining gaps noted, not yet written:** data/privacy law specifics (GDPR-style) beyond `23` §3; cost estimation for building the project (time/tokens per phase), now partly in `19`; mobile-app specifics (store review, offline); team collaboration (multiple humans). Add when a real project needs them.

### Validation
- **Instructions reduce sycophancy but don't remove it,** because it comes partly from training. Add an `evals/` folder with test prompts (deliberately bad ideas, false claims stated confidently, pushback on correct answers, and good ideas that should *not* be criticized) to measure whether the instructions work with each model.
