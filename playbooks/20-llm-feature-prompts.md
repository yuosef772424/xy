# 20 · Prompts for LLM Features Inside Your Products

**Goal:** When a product you build uses an AI model (a tutor, an assistant, a classifier, an evaluator), its prompts must give reliable, honest, controllable results.

This is about prompts **in the product's code**, not about instructing the coding agent (for that, see [`prompts/prompt-writing-guide.md`](../prompts/prompt-writing-guide.md)).

## Rules

1. **Ask for choices, not free judgments.** When the result drives logic, have the model pick from a **closed list** (`"level": "beginner" | "intermediate" | "advanced"`), using structured output (JSON schema or tool calls). Free text is for content shown to humans, not for decisions.
2. **Validate every output in code.** Reject or retry when a value is outside the allowed list, a field is missing, or a type is wrong. Never trust the format blindly.
3. **Treat what end-users say about themselves as data, not as truth.** "I'm an expert" or "my teacher allowed this" are claims to weigh against evidence (test answers, history), not facts to obey.
4. **Prevent sycophancy in the product's model too.** Instruct it to give honest assessments, to correct mistakes politely, and not to praise wrong answers. Apply [00](00-honest-judgment.md) to the product.
5. **Require stated confidence and grounds.** For assessments, ask for a confidence level and the evidence behind it. Low confidence → ask a follow-up question, or fall back to a safe default.
6. **Separate instructions from content.** Wrap imported or user-provided content in clear delimiters (`<document>…</document>`) and tell the model that this content is data and its instructions must not be followed (prompt injection defense).
7. **Version and test prompts like code.** Keep prompts in files under version control, with a small evaluation set of example inputs and expected outputs. Re-run it whenever the prompt or the model changes.

## Checklist

- [ ] Decisions use closed-list structured outputs.
- [ ] Outputs are validated in code, with a retry or fallback.
- [ ] User self-claims are treated as data.
- [ ] Anti-sycophancy and confidence rules are in the system prompt.
- [ ] External content is delimited and marked as untrusted.
- [ ] Prompts have an evaluation set that runs on every change.
