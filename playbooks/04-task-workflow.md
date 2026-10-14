# 04 · Task Workflow: Understand → Plan → Build → Review

> **Goal:** Each task is understood correctly, done with a minimal clean change, and proven to work. · **Read when:** doing any single task (for multi-phase projects, see [11](11-architecture.md) and [13](13-execution.md)). · **Pays off because:** most wasted work comes from solving the wrong problem or from shipping an unverified change.

## 1. Understand
- Restate the goal in one sentence: "The user wants X so that Y."
- Identify the inputs, the expected outputs, and the constraints (including what must not change).
- Write 2–5 **acceptance criteria** that prove it's done, for example "`npm test` passes and `/login` returns 401 for a bad password".
- Find the context through the maps ([07](07-maps-and-docs.md)): related code, tests, and earlier decisions.
- Ambiguity: if there is a sensible default, take it and state the assumption; if the answer changes the outcome, ask one precise question ([02](02-owner.md)).

## 2. Plan (when the task is bigger than a small fix)
- List the files to touch and why; order the steps so that each one leaves the project working; attach a verification to each step.
- Name the risks (migrations, public API, performance, security) and what is out of scope.
- Choose the **simplest design** that meets the requirements; don't build for imagined futures.
- Architecture or data-model changes need the owner's approval.

## 3. Build
- Read a neighboring file first, to match the local style, naming, error handling, and tests. Look for an existing helper before writing a new one.
- **Minimal diff:** change only what the task needs. Don't reformat unrelated code.
- Clear names; small functions with one responsibility; named constants.
- Validate and handle errors at the boundaries (input, network, files); trust internal code.
- Comments explain *why*, not *what*.
- Every behavior change gets a test ([05](05-testing.md)). Update the docs and `MODULE.md` in the same change ([07](07-maps-and-docs.md)).
- Before finishing: format, lint, and remove debug output, dead code, and commented-out code.

## 4. Review (your own diff, and others')
Review in order: **correctness → security → data safety → tests → design and architecture rules → readability → style** (the linter covers most style).
- Label findings: **blocking / should fix / nit**, each with a concrete failure scenario ("if `items` is empty, line 42 divides by zero") and a suggested fix.
- **Self-review before you call anything done:** nothing unrelated changed; no secrets, TODOs, or debug code; every new branch of logic was executed at least once; you could defend every line.

## 5. Report
Summarize what changed, how it was verified (commands and results), and what is still open ([02](02-owner.md) §5).

## Anti-patterns
Coding right after reading the title · asking questions the code already answers · "big bang" changes · silently widening the scope · claiming something works without running it.
