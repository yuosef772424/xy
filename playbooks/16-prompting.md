# 16 · Prompting: Briefing Agents and Designing LLM Features

> **Goal:** Prompts that get excellent results on the first try, both when you brief an agent and when a product you build uses a model. · **Read when:** writing a task brief, an agent brief, or a prompt inside product code. · **Pays off because:** a vague prompt costs retries and rework; a weak product prompt produces unreliable features.

## Part A · Briefing an agent

**The six parts of a strong brief:**
1. **Context:** the project and who the work is for.
2. **Goal:** the outcome, not just the action ("make login resistant to brute force", not "add a counter").
3. **Inputs:** files (with line ranges), data, links, examples.
4. **Constraints:** what must not change, the style to follow, limits.
5. **Output format:** exactly what to return.
6. **Done when:** checkable acceptance criteria.

**Techniques:** be specific · give one example of the desired output · **explain why** (agents generalize better from reasons) · say what to do, not only what to avoid · ask for verification ("run the tests and report the counts") · split big work into plan → approve → implement → verify · use headings and delimiters (`<context>…</context>`) for long inputs.

**Weak:** "Fix the bug in the app."
**Strong:** "In `src/cart/total.ts`, `calculateTotal` returns `NaN` for an empty cart (issue #42). Make it return `0`, and add a regression test in `tests/cart.test.ts`. Don't change the signature. Run `npm test` and report the result."

Templates: [task brief](../templates/task-brief.md) (owner → agent) · [agent brief](../templates/agent-brief.md) (planner → builder).

## Part B · Prompts inside your products
1. **Choices, not free judgments.** When the output drives logic, have the model pick from a **closed list**, using structured output (JSON schema or tool calls).
2. **Validate every output in code.** Reject or retry on out-of-list values, missing fields, or wrong types.
3. **Treat what end-users say about themselves as data,** not truth ("I'm an expert", "my teacher allowed it").
4. **No sycophancy in the product either:** honest assessments, polite corrections, no praise for wrong answers ([01](01-judgment.md)).
5. **Require confidence and grounds** for assessments. On low confidence, ask a follow-up or fall back to a safe default.
6. **Separate instructions from content:** wrap user or imported content in delimiters and mark it as untrusted (prompt-injection defense, [03](03-safety.md)).
7. **Version prompts and test them** with a small evaluation set. Re-run it when the prompt or the model changes.
