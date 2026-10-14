# Claude Code Kit

Ready-made Claude Code configuration that turns this playbook from *documents to read* into **behavior that loads automatically**. Copy the contents of this folder into the root of any project.

| File | What it does |
|---|---|
| `CLAUDE.md` | Loaded at the start of every session. It imports `AGENTS.md` and points to the project state files. |
| `.claude/agents/builder.md` | A builder subagent (cheaper model) for executing one phase ([13](../playbooks/13-execution.md)). |
| `.claude/agents/researcher.md` | A read-only research subagent for prior-art and market research ([10](../playbooks/10-market-research.md), [13](../playbooks/13-execution.md) §5). |
| `.claude/agents/reviewer.md` | A read-only reviewer subagent ([04](../playbooks/04-task-workflow.md) §4). |
| `.claude/skills/handoff/` | `/handoff`: writes a ready-to-paste hand-off message ([02](../playbooks/02-owner.md) §6). |
| `.claude/skills/status/` | `/status`: a short measurable status report for the owner. |
| `.claude/skills/propose/` | `/propose`: adds a proposal to the playbook's inbox ([09](../playbooks/09-improvement.md) §5). |
| `.claude/hooks/session-start.sh` | Shows `STATUS.md` and recent `LESSONS.md` entries when a session starts, so every session begins with the current state. |
| `.claude/settings.json` | Registers the hook. |

## Why this matters

- **Skills and subagents load only when needed** (progressive disclosure). The full playbook doesn't sit in the context on every turn, which saves tokens while keeping the knowledge available.
- **Hooks make habits automatic:** reading the state and the lessons no longer depends on the model remembering to do it.

## Install

```bash
cp -r claude-code/CLAUDE.md claude-code/.claude /path/to/your-project/
chmod +x /path/to/your-project/.claude/hooks/session-start.sh
```

Then copy `AGENTS.md` (and optionally `playbooks/`) into the project, and fill in its project-specific section.

> Claude Code's configuration format evolves. If something doesn't load, check the current docs for skills, subagents, and hooks, and update the kit (and propose the fix via `/propose`).
