# 07 · Maps & Documentation: Navigate Without Reading Everything

> **Goal:** Agents (and people) find the right code by reading short maps, not the whole project; and the docs stay true. · **Read when:** starting any task; setting up a project; changing a module's interface. · **Pays off because:** exploration is one of the biggest token costs, and good maps replace most of it.

## 1. Three layers
| Layer | File | Written by | Read when |
|---|---|---|---|
| **Project map** | `PROJECT_MAP.md` (root) | **Generated** by [`scripts/gen_map.py`](../scripts/gen_map.py) | At the start of every task |
| **Module guide** | `MODULE.md` in each module ([template](../templates/MODULE.md)) | Whoever changes the module | When the task touches that module |
| **Code** | the source files | — | Only the needed files and line ranges |

`ARCHITECTURE.md`, `ROADMAP.md`, `STATUS.md`, and the decision records describe *why* and *what's next*; the maps describe *where*.

## 2. Keeping them true
- **The structural part is generated, never hand-edited.** A pre-commit hook or CI runs `gen_map.py --check` and fails when the map is stale. The fix is always to re-run the generator. The generator also flags source directories that have no `MODULE.md`.
- **The descriptive part is written by hand.** A PR that changes a module's public interface, dependencies, or invariants updates its `MODULE.md` **in the same PR**; reviewers check this. [`scripts/doc_health.py`](../scripts/doc_health.py) flags a `MODULE.md` whose folder changed in many commits since it was last updated, plus broken links and oversized `STATUS.md`/`LESSONS.md` files; the session-start hook shows its warnings. The architecture health check spot-checks a few `MODULE.md` files against the code.
- A `MODULE.md` answers in under a minute: its purpose (one line, copied into the map), public interface, depends on / used by, key files, invariants and gotchas, and how to test it. Make it as short as the module allows; don't restate the code.
- Large projects can add a generated symbol index (`ctags`, tree-sitter) and a dependency graph.

## 3. Reading protocol
1. `PROJECT_MAP.md` → 2. the relevant `MODULE.md` → 3. **search** (`grep`/`rg`) for symbols → 4. read only the needed line ranges (whole files only when they are small, or you're rewriting most of them) → 5. never read generated, vendored, lock, or build files → 6. if the maps were wrong, fix them in the same task.

Planner briefs ([13](13-execution.md)) point builders directly at `MODULE.md` files and line ranges.

## 4. Other documentation
- **README:** what the project is, how to install, run, and test. Commands must be copy-pasteable and tested.
- **Decision records** (`docs/decisions/NNN-title.md`): context → decision → consequences → *revisit if*.
- Update docs in the **same change** as the code. Delete docs and comments that are no longer true.
- Lead with what matters most; prefer lists, tables, and examples over long paragraphs.
