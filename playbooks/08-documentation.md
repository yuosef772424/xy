# 08 · Documentation

**Goal:** Help the next person (or agent) succeed without having to ask you.

## What every project needs

- **README:** what it is, how to install, how to run, how to test.
- **Agent instructions** (`AGENTS.md` / `CLAUDE.md`): conventions, commands, gotchas.
- **Decision records** for important architectural choices: context → decision → consequences.

## Writing rules

- Start with the most important information.
- Use commands that can be copy-pasted, and test them before you publish.
- Prefer short sections, lists, and tables over long paragraphs.
- Show examples: one good example beats three paragraphs.
- Update the docs in the **same change** as the code they describe.

## Code comments

- Explain *why* and non-obvious constraints.
- Don't narrate what the code already says clearly.
- Delete comments that are no longer true.
