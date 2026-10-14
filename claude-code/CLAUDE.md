# Project instructions

@AGENTS.md

## Start of every session
- Read `STATUS.md` (current state) and the recent entries of `LESSONS.md` (the session-start hook shows them).
- Navigate with `PROJECT_MAP.md` and each module's `MODULE.md`; don't read the whole codebase.

## PR notifications: off
Do not watch PRs. After creating any PR, unsubscribe from its activity in the same turn, and don't reply to PR notifications. Check CI and reviews on demand with one call when needed. (Owner instruction: every notification wakes the session and re-reads its whole context.)

## Available helpers
- Subagents: `builder` (one phase per branch), `researcher` (read-only research), `reviewer` (read-only review).
- Skills: `/handoff`, `/status`, `/propose`.
- Tools registry: `scripts/README.md`.
