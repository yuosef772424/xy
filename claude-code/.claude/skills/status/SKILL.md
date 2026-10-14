---
name: status
description: Produce a short, measurable status report for the owner, readable on a phone. Use when the owner asks where things stand.
---
Gather cheaply (git log --oneline, git diff --stat, the latest test counts, STATUS.md), then report:
- ✅ done (with numbers: phases, tests passing, features vs plan)
- 🔄 in progress
- ❌ failed or blocked, and why
- ❓ decisions needed from the owner, with options and your recommendation
- approximate cost of this period, if known
Lead with a one-line summary. Change no files unless asked.
