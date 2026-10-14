#!/usr/bin/env bash
# Show the project state and recent lessons at session start, so every session begins informed.
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
if [ -f STATUS.md ]; then echo "=== STATUS.md ==="; head -n 80 STATUS.md; fi
if [ -f LESSONS.md ]; then echo "=== LESSONS.md (latest) ==="; tail -n 20 LESSONS.md; fi
if [ -f scripts/gen_map.py ] && ! python3 scripts/gen_map.py --check >/dev/null 2>&1; then
  echo "NOTE: PROJECT_MAP.md is stale; run: python3 scripts/gen_map.py"
fi
exit 0
