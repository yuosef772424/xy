# Prompt Writing Guide

**Goal:** Write instructions that make AI agents produce excellent work on the first try.

## The 6 parts of a great prompt

1. **Role & context:** who the agent is working for and what the project is.
2. **Goal:** the outcome, not just the action. "Make login resistant to brute force", not "add a counter".
3. **Inputs:** files, data, links, examples.
4. **Constraints:** what must not change, the style to follow, limits.
5. **Output format:** exactly what to return (code + PR, a table, a list, a file).
6. **Success criteria:** how the result will be judged.

## Techniques that work

- **Be specific.** Vague in, vague out.
- **Give examples** of the desired output; one is often enough.
- **Explain *why*.** Agents generalize better when they understand the reason behind a rule.
- **Say what to do,** not only what to avoid.
- **Ask for verification:** "Run the tests and show me the result."
- **Split big tasks** into stages: plan → approve → implement → verify.
- **Use structure:** headings, lists, and delimited sections (`<context>...</context>`) for long inputs.

## Before / after

**Weak:**
> Fix the bug in the app.

**Strong:**
> In `src/cart/total.ts`, `calculateTotal` returns `NaN` when the cart is empty (see issue #42). Fix it so an empty cart returns `0`. Add a regression test in `tests/cart.test.ts`. Don't change the function's signature. Run `npm test` and report the result.

## Reusable prompt skeleton

```markdown
You are working on <project>, a <short description>.

## Task
<goal>

## Context
<relevant files, links, background>

## Constraints
- <constraint>

## Done when
- <acceptance criterion>

Follow AGENTS.md. Plan first if the change touches more than one file. Report what you changed and how you verified it.
