# 14 · Codebase Maps (Navigate Without Reading Everything)

**Goal:** An agent finds the right code by reading **maps**, not the whole project. Fewer tokens per task, fewer round-trips spent exploring, and the context stays small.

## The three layers

| Layer | File | Size | Who writes it | Read when |
|---|---|---|---|---|
| **L0 · Project map** | `PROJECT_MAP.md` (root) | 1–3 pages | **Generated** by a script | At the start of every task |
| **L1 · Module guide** | `MODULE.md` in each module folder | ≤ 60 lines | The builder who changes the module | When the task touches that module |
| **L2 · Code** | the source files | — | — | Only the specific files and line ranges needed |

Plus the architecture-level docs from [12](12-architecture-planning.md) (`ARCHITECTURE.md`, `ROADMAP.md`, `STATUS.md`), which describe *why*. The maps describe *where*.

## L0 · `PROJECT_MAP.md` (generated, never hand-edited)

- Produced by [`scripts/gen_map.py`](../scripts/gen_map.py) (or an equivalent for your stack). It lists every module with its one-line purpose, and every source file with its size.
- **Kept up to date automatically:** a pre-commit hook or CI step runs `gen_map.py --check` and fails if the map is stale. The fix is always the same command: `python scripts/gen_map.py`.
- Optional extras for large projects: a symbol index (`ctags`, tree-sitter) and a dependency graph (`dependency-cruiser`, `pydeps`, `madge`), generated the same way.

## L1 · `MODULE.md` (one per module)

Use [the template](../templates/MODULE.md). It answers, in under a minute of reading:

- **purpose:** one line (this exact `purpose:` line is copied into the project map);
- **public interface:** what other modules may call;
- **depends on / used by:** its edges in the dependency graph;
- **key files:** a few lines each on what lives where;
- **invariants and gotchas:** rules that must never break;
- **how to test:** the exact command for this module only.

**Freshness rules:**
- If a PR changes a module's public interface, dependencies, or invariants, it must update that module's `MODULE.md` **in the same PR**. Reviewers check this.
- CI fails if a source directory has no `MODULE.md`; `gen_map.py` lists these under ⚠️.
- Hand-written text can't be fully verified by a machine. The architecture health check ([12a](12a-architecture-rules.md) Part F) includes spot-checking a few `MODULE.md` files against the code.

## Reading protocol for agents

1. Read `PROJECT_MAP.md`.
2. Pick the module(s) the task touches, and read their `MODULE.md`.
3. **Search before reading:** `grep`/`rg` for symbols, and use the symbol index if there is one.
4. Read **only** the needed line ranges. Read a whole file only if it is small (under ~200 lines) or you are rewriting most of it.
5. Never read generated, vendored, lock, or build files.
6. If the maps were wrong or missing something, fix them in the same task.

**Briefs from the planner** ([13](13-execution-orchestration.md)) should point builders directly at L1 files and line ranges, so builders skip steps 1–2.

## Anti-patterns

- "Let me read the whole `src/` folder to understand the project."
- A hand-maintained file tree that silently goes stale.
- A `MODULE.md` that repeats the code line by line instead of explaining purpose and contracts.
- Maps so detailed that reading them costs as much as reading the code.
