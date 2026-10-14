#!/usr/bin/env python3
"""Check that the docs agents rely on are still trustworthy. Read-only.

Checks:
  - broken relative links in Markdown files                 (error)
  - MODULE.md files whose folder changed in many commits    (warning: maybe stale)
    since the MODULE.md itself was last updated
  - STATUS.md / LESSONS.md growing too long to read quickly (warning)
  - with --playbook: each playbook starts with a Goal line, and AGENTS.md stays short

Usage:
  python scripts/doc_health.py [--root DIR] [--stale-commits N] [--playbook] [--strict]
Exit code: 1 on errors (or on warnings with --strict), else 0.
"""
import argparse
import glob
import os
import re
import subprocess
import sys

LINK = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")
SKIP = ("node_modules", ".git", "dist", "build", ".venv", "venv")


def md_files(root):
    for path in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
        if not any(part in SKIP for part in path.split(os.sep)):
            yield path


def broken_links(root):
    for path in md_files(root):
        text = open(path, encoding="utf-8", errors="ignore").read()
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
        for m in LINK.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:")) or "<" in target:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                yield f"{os.path.relpath(path, root)} → {target}"


def git(root, *args):
    try:
        return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def stale_modules(root, threshold):
    if git(root, "rev-parse", "--is-inside-work-tree") != "true":
        return
    for path in glob.glob(os.path.join(root, "**", "MODULE.md"), recursive=True):
        folder = os.path.dirname(path)
        last = git(root, "log", "-1", "--format=%H", "--", path)
        if not last:
            continue
        changed = git(root, "rev-list", "--count", f"{last}..HEAD", "--", folder)
        if changed and int(changed) >= threshold:
            yield f"{os.path.relpath(path, root)}: folder changed in {changed} commits since it was updated"


def long_files(root):
    for name, guide in (("STATUS.md", 120), ("LESSONS.md", 150)):
        path = os.path.join(root, name)
        if os.path.exists(path):
            n = sum(1 for _ in open(path, encoding="utf-8"))
            if n > guide:
                yield f"{name} has {n} lines (guideline ~{guide}): summarize or prune it"


def playbook_checks(root):
    for path in sorted(glob.glob(os.path.join(root, "playbooks", "*.md"))):
        if "> **Goal:**" not in open(path, encoding="utf-8").read(600):
            yield f"{os.path.relpath(path, root)}: missing '> **Goal:** … · **Read when:** … · **Pays off because:** …' header"
    agents = os.path.join(root, "AGENTS.md")
    if os.path.exists(agents):
        n = sum(1 for _ in open(agents, encoding="utf-8"))
        if n > 80:
            yield f"AGENTS.md has {n} lines (guideline ~80): it is read every session, keep it short"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".")
    p.add_argument("--stale-commits", type=int, default=5)
    p.add_argument("--playbook", action="store_true", help="also check playbook conventions")
    p.add_argument("--strict", action="store_true", help="treat warnings as errors")
    a = p.parse_args()
    root = os.path.abspath(a.root)

    errors = list(broken_links(root))
    warnings = list(stale_modules(root, a.stale_commits)) + list(long_files(root))
    if a.playbook:
        warnings += list(playbook_checks(root))

    for e in errors:
        print(f"ERROR   broken link: {e}")
    for w in warnings:
        print(f"WARNING {w}")
    print(f"doc_health: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors or (a.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
