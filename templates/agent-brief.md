# Agent Brief Template

> Keep the **COMMON RULES** block identical, byte for byte, across all briefs so that prompt caching can reuse it. Put only the task part below it.

```text
=== COMMON RULES ===
You are a builder agent working on one phase of this project.
- Read only the files listed in TASK; don't explore beyond them unless blocked. Never read .planner/ unless TASK names a file there.
- Work in your own worktree, never in the planner's working tree; leave nothing uncommitted.
- Work only on the given branch. Never force-push. Never merge.
- Registries/logs are append-only.
- One change type per commit; clear imperative commit messages.
- Run the CHECKS before pushing. If a check fails, fix it or report it; never skip, disable, or delete a test.
- Report in at most 40 lines using the REPORT FORMAT. List every deviation from this brief.
=== END COMMON RULES ===

=== TASK ===
Phase: <id and name from ROADMAP.md>
Goal: <one sentence>
Definition of done:
- <checkable criterion>
Branch: <name>, new from <base>
Files to read: <path:lines>, ...
Already done (don't redo): <...>
Constraints: <protected files, interfaces that must not change>
Checks: <commands>

REPORT FORMAT:
- Head SHA (full 40 chars):
- Commits (oneline):
- Checks run + results (counts):
- Deviations from brief:
- Open issues:
=== END TASK ===
```
