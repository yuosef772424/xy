# 12 · Architecture Planning (Designing the Project's Structure)

**Goal:** Decide *what* the project is and *how it is shaped* before anyone builds it, and write that down so execution never has to rethink it.

This is the first of two separate planning jobs:

| | **Architecture planning** (this file) | **Execution planning** ([13](13-execution-orchestration.md)) |
|---|---|---|
| Question | What do we build, and how is it structured? | How do we get it built, phase by phase, cheaply and correctly? |
| When | Once at the start, then only at major milestones | Continuously, for the whole life of the project |
| Session | Its own session; closed when done | A fresh session that starts from this file's outputs |
| Model / effort | Strongest model, high effort; mistakes here are the most expensive to reverse | Strong model for the planner, cheaper models for builders |
| Output | `ARCHITECTURE.md`, `ROADMAP.md`, decision records | Merged PRs, `STATUS.md` |

**Why separate them:** design needs wide exploration and deep thinking, which means a large context. Execution needs a small, focused context that gets re-read on every wake. Mixing the two makes every execution step pay to re-read the whole design discussion, and it tempts the executor to redesign in the middle of a phase.

## Steps

1. **Define the problem:** users, the core job the project does for them, success criteria, and non-goals.
2. **List the constraints:** budget, deadline, team skills, hosting, compliance, existing systems.
3. **Explore options for the decisions that are hard to reverse:** language and framework, data model, module boundaries, interfaces between modules, and deployment. Compare 2–3 options for each with evidence (see [00b](00b-evidence-over-agreement.md)). Decide quickly on easy-to-reverse choices.
4. **Define module boundaries and contracts.** Each module has one owner phase, a clear public interface, and its own tests. Good boundaries are what let builder agents later work in parallel without conflicts.
5. **Split the work into phases.** Each phase:
   - is small enough for one builder agent, one branch, and one PR;
   - has a definition of done that can be checked by commands;
   - lists its dependencies (which phases must merge first);
   - is marked **parallel-safe** if it touches files no other open phase touches.
6. **Record the decisions** as short records (context → decision → consequences) so nobody re-debates them later.
7. **Freeze.** Close the session. From now on, changing the architecture is a deliberate act: re-open architecture planning, write a new decision record, and update the roadmap.

## Outputs

- **`ARCHITECTURE.md`:** purpose, module map, data model, interfaces, tech choices, and the reason for each. Keep it under ~300 lines; it gets read by every planner session.
- **`ROADMAP.md`:** an ordered list of phases, each with goal, scope (files and modules), definition of done, dependencies, and the parallel-safe flag.
- **`docs/decisions/NNN-title.md`:** one file per major decision.

## Token vs. quality balance at this stage

- **Spend here.** This is the cheapest point to fix a mistake. One extra hour of design can save days of rework and many builder runs.
- **But keep it bounded.** Explore the decisions that are hard to reverse; don't design details that a builder can settle in minutes.
- **Use research agents for wide reading** (comparing libraries, reading large docs), and have them return short summaries, so the design session's context stays focused on decisions.

## Anti-patterns

- Starting to build before the module boundaries are clear. Parallel agents will then collide.
- Phases like "build the backend" that are too big to review in one PR.
- Letting the execution planner quietly change the architecture to make a phase easier.
- Over-designing parts that no phase needs yet.
