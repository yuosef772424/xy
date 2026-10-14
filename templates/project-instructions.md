# <Project Name> — Agent Instructions

> Copy to your project root as `AGENTS.md` or `CLAUDE.md`, together with the core rules from this playbook's `AGENTS.md`.

## Overview
<What this project does, for whom, in 2–3 sentences.>

## Tech stack
- Language / runtime:
- Framework:
- Database:
- Hosting:

## Commands
| Task | Command |
|------|---------|
| Install | `...` |
| Run locally | `...` |
| Test (all) | `...` |
| Test (single file) | `...` |
| Lint / format | `...` |
| Build | `...` |

## Structure
- `src/` — 
- `tests/` — 
- `docs/` — 

## Conventions
- Naming:
- Error handling:
- Testing style:
- Commit / branch format:

## Gotchas
- <Non-obvious things that break, slow you down, or surprise newcomers.>

## Working agreements
- Language of technical files: English (default) / other:
- Project tier: tiny / small / medium / large (see playbooks/00-principles.md §6)
- Autonomy level: cautious / standard / trusted (see playbooks/02-owner.md §3b)
- Merge mode: owner merges / planner may merge after CI and review / planner merges locally without a PR (solo, unprotected base)
- PR watching: off (default: unsubscribe right after creating a PR; check CI on demand) / on for specific PRs
- Model for builder agents: e.g. sonnet

## Do not touch
- <Generated files, vendored code, sensitive configs.>
