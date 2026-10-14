# 11 · Architecture Planning: Design the Project Before Building It

> **Goal:** Decide *what* to build and *how it's shaped*, write it down, and set up the project so that execution never has to rethink it. · **Read when:** starting a new project, or at a major milestone that changes the structure. · **Pays off because:** this is the cheapest point to fix mistakes. A structural error found later costs restructuring, rework, and many agent runs.

## Two planning jobs, kept separate
| | **Architecture planning** (this file) | **Execution** ([13](13-execution.md)) |
|---|---|---|
| Question | What do we build, and how is it structured? | How do we get it built, phase by phase? |
| When | Once at the start; again only at major milestones | Throughout the project |
| Session | Its own session, closed when done | Fresh sessions that start from this file's outputs |
| Model and effort | Strongest model, high effort | Strong planner; cheaper builders |
| Output | `RESEARCH.md`, `ARCHITECTURE.md`, `ROADMAP.md`, decision records, project skeleton | Merged PRs, `STATUS.md` |

**Why separate them:** design needs wide exploration (a large context); execution needs a small context that gets re-read on every wake. Mixing them makes every execution step pay for the design discussion, and it tempts the executor to redesign in the middle of a phase.

## Steps
1. **Research the market and feasibility first** → [10](10-market-research.md). Get a GO / GO-WITH-CHANGES / NO-GO verdict. Don't design a project that shouldn't be built.
2. **Define the problem:** users, the core job the product does for them, success criteria, non-goals. List the constraints: budget, deadline, skills, hosting, compliance, existing systems.
3. **Classify the features** (Must / Should / Could / Won't) and **apply the architecture rules** → [12](12-architecture-rules.md), including the **extension test**. The structure comes from the rules, not from taste.
4. **Decide what is hard to reverse** (stack, data model, module boundaries, interfaces, deployment) by comparing 2–3 options with evidence ([01](01-judgment.md) Part B, usually with a research agent). Decide quickly on anything easy to reverse.
5. **Split the work into phases.** Each phase is one builder, one branch, one PR; delivers a working increment; has a definition of done that commands can check; lists its dependencies; and is flagged **parallel-safe** if no other open phase touches its files. Use a short time-boxed **spike** phase for unclear areas.
6. **Record the decisions** as short decision records, each with a *revisit if* condition.
7. **Set up the skeleton:** `README.md` · `AGENTS.md` (from this playbook, with the project section filled in from [the template](../templates/project-instructions.md)) · the [Claude Code kit](../claude-code/README.md) · `.gitignore` and `.env.example` (never `.env`) · `PROJECT_MAP.md` + the generator, and a `MODULE.md` per module ([07](07-maps-and-docs.md)) · the `check:fast` / `check` / `check:full` commands and a pre-commit hook ([05](05-testing.md)) · CI with the architecture rules ([12](12-architecture-rules.md) Part F) · `STATUS.md` and `LESSONS.md`.
8. **Build the thinnest end-to-end slice first:** one feature working from input to output.
9. **Freeze.** Close the session. From now on, changing the architecture is deliberate: re-open this process, write a superseding decision record, and update the roadmap.

## Outputs
- `RESEARCH.md` ([template](../templates/market-research.md)): market, competitors, differentiation, feasibility verdict.
- `ARCHITECTURE.md`: purpose, module map, data model, interfaces, tech choices and why. Short enough for a planner to read every session (a few hundred lines at most).
- `ROADMAP.md`: ordered phases with goal, scope, definition of done, dependencies, and the parallel-safe flag. A living document: reprioritizing means editing it, not redesigning.
- `docs/decisions/NNN-title.md`, plus the skeleton from step 7.

**A healthy project:** a newcomer can run it from the README in minutes · test, lint, and build are single commands · CI blocks bad merges · no secrets in the repository · the maps are fresh.

## Anti-patterns
Building before module boundaries are clear · phases like "build the backend" that are too big to review · letting execution quietly change the architecture · designing parts no phase needs yet.
