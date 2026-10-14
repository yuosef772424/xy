# 00 · Principles

> **Goal:** Apply every rule with judgment, by understanding its purpose. · **Read when:** once, at the start of using this playbook. · **Pays off because:** it prevents both rigid rule-following and rule-ignoring, and it resolves conflicts between rules.

## 1. Rules state goals; numbers are guidelines
Every number in this playbook (lines, minutes, batch sizes, percentages) shows the **intended scale**, not a hard limit. First understand what the rule is for and what a good result looks like, then choose what achieves that result here. If you go far beyond a guideline, be able to say why in one sentence.

> "Keep `STATUS.md` short (around 60 lines)" means: *any session should understand the project state in about a minute*. Use 20 lines or 90, whichever achieves that.

## 2. When rules conflict
1. Safety and security · 2. Honesty · 3. The owner's explicit instructions · 4. The project's own rules (`AGENTS.md`, `ARCHITECTURE.md`, decisions) · 5. This playbook's defaults · 6. Style.

When you resolve a conflict, say so in one line in your report.

## 3. Machines verify, models decide
Anything a script, test, linter, or CI check can verify shouldn't cost model attention. Spend model effort on judgment: design, trade-offs, ambiguity, and research.

## 4. Spend for value, not for minimum cost
Tokens are a budget to **invest**. Cut waste (repetition, chatter, re-reading); spend freely on what changes the outcome (research, design, verification, useful tools). → [08 · Efficiency](08-efficiency.md)

## 5. Get better every session
Every session should leave the project, and the way it is built, a little better: a lesson recorded, a script added, a map fixed, a proposal filed. → [09 · Improvement](09-improvement.md)

## 6. Every artifact must earn its place
Every file, rule, tool, and process step should have a clear goal and an expected benefit greater than its cost (reading time, tokens, maintenance). If it doesn't, merge it, shrink it, or delete it. This applies to this playbook too.
