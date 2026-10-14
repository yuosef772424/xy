#!/usr/bin/env python3
"""Install ai-playbook into a new or existing project, without overwriting anything.

Copies AGENTS.md, playbooks/, templates/, the general scripts, and the Claude Code kit
(CLAUDE.md + .claude/), and creates STATUS.md and LESSONS.md if missing.
Existing files are never overwritten; conflicts are reported with what to merge by hand.

Usage:
  python scripts/install_playbook.py /path/to/project            # dry run: show the plan
  python scripts/install_playbook.py /path/to/project --apply    # actually install
"""
import argparse
import os
import shutil
import stat
import sys

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_EXTS = {".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".java", ".kt", ".rs", ".rb", ".php", ".cs", ".swift"}

STATUS_STUB = """# STATUS

> Read first in every session. Keep it short enough to understand the project state in about a minute.

**Last updated:** <date>  ·  **Current focus:** <phase or task>

## State
- <what works, what is in progress, what is blocked>

## Next steps
1. <next concrete step>

## Decisions needed from the owner
- <none>
"""

LESSONS_STUB = """# LESSONS

> Short, living log. Add an entry when something surprised you, cost more than expected, or worked notably well.
> Tag lessons that apply to all projects with [playbook-proposal].

"""


def plan_copies(target):
    """Return a list of (src, dst) file pairs to install."""
    pairs = [(os.path.join(SRC, "AGENTS.md"), os.path.join(target, "AGENTS.md"))]
    for folder in ("playbooks", "templates"):
        for name in sorted(os.listdir(os.path.join(SRC, folder))):
            pairs.append((os.path.join(SRC, folder, name), os.path.join(target, folder, name)))
    for name in ("gen_map.py", "doc_health.py", "install_playbook.py", "README.md"):
        pairs.append((os.path.join(SRC, "scripts", name), os.path.join(target, "scripts", name)))
    kit = os.path.join(SRC, "claude-code")
    for root, _, files in os.walk(kit):
        for name in files:
            src = os.path.join(root, name)
            if name == "README.md" and root == kit:
                pairs.append((src, os.path.join(target, ".claude", "README.md")))  # kit guide
                continue
            pairs.append((src, os.path.join(target, os.path.relpath(src, kit))))
    return pairs


# Links that point into the playbook repository itself are rewritten for the project layout.
LINK_REWRITES = {
    "](../claude-code/README.md)": "](../.claude/README.md)",
    "[`PROPOSALS.md`](../PROPOSALS.md)": "`PROPOSALS.md` (in the ai-playbook repository)",
    "](claude-code/README.md)": "](.claude/README.md)",
}


def copy_file(src, dst):
    if dst.endswith(".md"):
        with open(src, encoding="utf-8") as f:
            text = f.read()
        for old, new in LINK_REWRITES.items():
            text = text.replace(old, new)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(text)
        shutil.copystat(src, dst)
    else:
        shutil.copy2(src, dst)


def is_existing_project(target):
    for root, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in {"node_modules", "venv", ".venv"}]
        if any(os.path.splitext(f)[1] in SOURCE_EXTS for f in files):
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", help="project directory")
    parser.add_argument("--apply", action="store_true", help="write files (default is a dry run)")
    args = parser.parse_args()

    target = os.path.abspath(args.target)
    if not os.path.isdir(target):
        print(f"error: {target} is not a directory", file=sys.stderr)
        return 2

    created, skipped = [], []
    for src, dst in plan_copies(target):
        rel = os.path.relpath(dst, target)
        if os.path.exists(dst):
            skipped.append(rel)
            continue
        created.append(rel)
        if args.apply:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            copy_file(src, dst)
            if dst.endswith(".sh"):
                os.chmod(dst, os.stat(dst).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    for name, content in (("STATUS.md", STATUS_STUB), ("LESSONS.md", LESSONS_STUB)):
        dst = os.path.join(target, name)
        if os.path.exists(dst):
            skipped.append(name)
        else:
            created.append(name)
            if args.apply:
                with open(dst, "w", encoding="utf-8") as f:
                    f.write(content)

    mode = "Installed" if args.apply else "Would install (dry run; add --apply)"
    print(f"{mode}: {len(created)} files · kept existing: {len(skipped)}")
    if skipped:
        print("\nAlready present, NOT overwritten (merge by hand if needed):")
        for rel in skipped:
            print(f"  - {rel}")
        if "AGENTS.md" in skipped or "CLAUDE.md" in skipped:
            print("  → Add the playbook rules to your existing AGENTS.md/CLAUDE.md, or import them with '@AGENTS.md'.")
        if os.path.join(".claude", "settings.json") in skipped:
            print("  → Merge the SessionStart hook from the playbook's claude-code/.claude/settings.json into yours.")

    existing = is_existing_project(target)
    print("\nNext steps:")
    print("  1. Fill in AGENTS.md §8 (see templates/project-instructions.md).")
    print("  2. python scripts/gen_map.py   # create PROJECT_MAP.md")
    if existing:
        print("  3. Existing project: follow playbooks/11-architecture.md § 'Adopting in an existing project'.")
    else:
        print("  3. New project: start with playbooks/11-architecture.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
