# 21 · Tooling & R&D (Invest Tokens to Work Better)

**Goal:** Spend part of the budget, deliberately, on **research and development that makes the agent itself more capable**: exploring new tools, and building and improving its own tools. A well-chosen investment pays for itself many times over in better results and lower total cost.

This is the "invest" side of [19 · Token budget](19-token-budget.md), and the long-term version of [18 · Continuous improvement](18-continuous-improvement.md).

## 1. What counts as R&D

- **Exploring new tools:** MCP servers, CLIs, libraries, model features, testing or analysis tools, and new ways to automate parts of the workflow.
- **Building tools:** scripts, generators, checkers, analyzers, templates, and small CLIs that do repeated or error-prone work reliably.
- **Improving tools:** making existing tools faster, more general, more robust, or easier to use, based on how they were actually used.
- **Developing the project idea:** prototypes or spikes that test whether a feature or approach is better before committing to it.

## 2. Budget: a deliberate share, not an accident

- **Guideline:** around **10–20%** of a project's effort may go to R&D. Spend more early in a project, or when a tool clearly unlocks big savings; spend less near deadlines.
- Do R&D **openly:** mention it in the plan or report ("spent ~X on building `gen_fixtures.py`; expect it to save ~Y per phase").
- **Timebox exploration.** If a tool or spike isn't showing value within its timebox, stop, record what was learned ([18](18-continuous-improvement.md) §5), and move on.
- **Large R&D** (more than a phase's worth of effort, or new paid services): propose it to the owner first, with the expected benefit.

## 3. Positive return: the core rule

Build or adopt a tool when its **expected benefit clearly exceeds its cost**:

> **benefit ≈ (time or tokens saved per use + quality gained) × expected number of uses**
> **cost ≈ building + learning + maintaining**

Good signs: the task repeats (within this project or across projects), it is error-prone by hand, it needs many tool calls or a lot of reading, or it can turn model judgment into a deterministic check.

**After using a tool for a while, check the return:** did it really save time, tokens, or errors? Keep, improve, or retire it based on actual use, not on how clever it is.

## 4. Where tools live: general first, specific when needed

| Kind | Location | Examples |
|---|---|---|
| **General** (useful across many projects) | **this playbook repository**: `scripts/`, listed in [`scripts/README.md`](../scripts/README.md) | map generator, status reporter, check runner, eval runner |
| **Project-specific** | the project's own `scripts/`, listed in its `AGENTS.md` | fixture generators for its data model, a deployment helper |

- **Prefer general tools:** parameterize them instead of hard-coding project details.
- **Specific tools are fine** when the need really is specific. Don't over-generalize a one-off.
- **Promotion path:** when a project tool proves useful in a second project, generalize it and move it into the playbook's `scripts/`.

## 5. Tool quality standard

Every tool, general or specific, should:

- start with a short header: what it does, usage, and an example;
- support `--help`, and be **safe by default** (read-only or dry-run unless explicitly asked to write);
- give **concise output** that is easy for an agent to read (a summary first, details on request);
- **fail loudly** with a clear message, never silently;
- have at least a smoke test, or a documented manual check;
- contain no secrets, and need no paid service unless that is documented.

## 6. The tools registry

Keep a registry ([`scripts/README.md`](../scripts/README.md) here, and a similar list in each project) with, for each tool:

- name and one-line purpose;
- status: **experimental** → **stable** → **deprecated**;
- the **measured benefit**, once known ("saves ~10 tool calls per phase");
- the date it was last checked or improved.

Agents **check the registry before building something new**, to reuse or improve an existing tool instead of duplicating it.

## 7. Exploring new tools regularly

The tool landscape changes fast. At the start of a project, and periodically during long ones:

- spend a short timebox looking for **new tools or model features** that could help this project's work;
- try promising ones on a small real task before adopting them;
- record the verdict (adopted / rejected, and why, with a reopen-if condition) in `LESSONS.md` or the registry.

## Self-check

- [ ] Is this R&D likely to pay back (§3), and is it timeboxed?
- [ ] Did I check the registry for an existing tool first?
- [ ] Is the tool general where it can be, and documented, safe, and concise?
- [ ] Did I record its status and, later, its measured benefit?
