---
name: handoff
description: Save a planner handoff so a fresh session can continue with a small context. Use when the owner asks for a handoff, when a roadmap item is finished, or when the context grows large (around 150–200k tokens).
---
1. Write `.planner/HANDOFF.md` following `templates/planner-handoff.md`. Overwrite the previous one; git history keeps the old versions.
   - Point to files (STATUS.md, ROADMAP.md, decisions) instead of copying them. Record only what isn't already written down: role and authority, owner preferences, in-flight agents, branches and SHAs, the next batch, open owner items.
   - Keep it as compact as continuity allows (often 1–3k tokens).
   - Never include secrets.
2. Make sure `STATUS.md` is current, then commit and push both files on the planner's working branch, never directly on the default branch unless the project's merge mode allows it. Use your own worktree if agents are running.
3. Reply with a single paste-ready line for the owner:
   `Continue as planner: read .planner/HANDOFF.md (commit <short-sha>), then AGENTS.md and STATUS.md. Start with "Next batch".`
4. If the owner prefers to stay in this session, also give them:
   `/compact Keep only the content of .planner/HANDOFF.md as just written; drop everything else.`
