#!/usr/bin/env python3
"""One-command pre-merge check for the planner. Read-only, concise output.

Replaces several separate verification steps (and their tool calls) with one:
commits on the branch, changed files, merge conflicts against the base,
append-only files that lost lines, and protected paths that were touched.

Usage:
  python scripts/merge_check.py <head-branch> [--base origin/main]
         [--append-only FILE ...] [--protected PATH ...]
Exit code: 0 = READY, 1 = NOT READY, 2 = usage/git error.
"""
import argparse
import subprocess
import sys


def git(*args, check=True):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(r.stderr.strip() or f"git {' '.join(args)} failed")
    return r


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("head")
    p.add_argument("--base", default="origin/main")
    p.add_argument("--append-only", nargs="*", default=[], help="files that may only gain lines (registries, logs)")
    p.add_argument("--protected", nargs="*", default=[], help="paths that must not change")
    a = p.parse_args()
    problems = []
    try:
        sha = git("rev-parse", a.head).stdout.strip()
        commits = git("log", "--oneline", f"{a.base}..{a.head}").stdout.strip().splitlines()
        files = git("diff", "--name-only", f"{a.base}...{a.head}").stdout.split()
        stat = git("diff", "--shortstat", f"{a.base}...{a.head}").stdout.strip()
        merge = git("merge-tree", "--write-tree", "--name-only", a.base, a.head, check=False)
        if merge.returncode == 1:
            conflicted = [l for l in merge.stdout.splitlines()[1:] if l and not l.startswith(("Auto-merging", "CONFLICT"))]
            problems.append(f"merge conflicts with {a.base}: {', '.join(conflicted) or 'see git merge-tree'}")
        elif merge.returncode != 0:
            raise RuntimeError(merge.stderr.strip() or "git merge-tree failed (needs git >= 2.38)")
        for f in a.append_only:
            diff = git("diff", f"{a.base}...{a.head}", "--", f).stdout.splitlines()
            removed = [l for l in diff if l.startswith("-") and not l.startswith("---")]
            if removed:
                problems.append(f"append-only file {f} lost/changed {len(removed)} line(s)")
        for path in a.protected:
            touched = [f for f in files if f == path or f.startswith(path.rstrip("/") + "/")]
            if touched:
                problems.append(f"protected path changed: {', '.join(touched)}")
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    print(f"head {sha}  ·  {len(commits)} commit(s)  ·  {stat or 'no changes'}")
    for c in commits[:15]:
        print(f"  {c}")
    if len(commits) > 15:
        print(f"  … {len(commits) - 15} more")
    print(f"files: {', '.join(files[:20])}{' …' if len(files) > 20 else ''}")
    if problems:
        print("NOT READY:")
        for pr in problems:
            print(f"  - {pr}")
        return 1
    print("READY: no conflicts, append-only and protected rules respected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
