# 16 · Batching Work (More Done per Invocation, Same Quality)

**Goal:** Finish more work per model invocation and per round-trip, **without** lowering quality.

## What actually costs

- **Each invocation** (a new turn, or an agent waking) re-reads the whole context. Fewer invocations → fewer re-reads. See [13](13-execution-orchestration.md) §2.
- **Each round-trip inside a turn** (a tool call, then waiting for the result) also costs a model step. Fewer, larger steps → less overhead.
- **But** a batch that is too big grows the context, mixes concerns, and makes errors harder to trace. When batching causes rework, it costs *more*.

The goal is the **right batch size**, not the largest.

## 1. Batch tasks when they are…

- **independent:** no task needs another task's uncertain result;
- **in the same area:** they share files or a module, so the context is loaded once;
- **small and well-specified:** each has a clear definition of done;
- **verified by the same checks:** one `check:fast` run covers them all.

Examples: three small bug fixes in one module; renaming plus updating the docs plus updating the tests; review the finished phase → merge it → update `STATUS.md` → launch the next agents.

## 2. Don't batch when…

- a task is **risky** (data migration, auth, payments, a core interface): do it alone, with full attention;
- task B depends on **what you learn** from task A: finish A and look at the result first;
- the tasks touch **different modules** that would need a lot of extra context;
- the batch would exceed roughly **5 tasks or ~300 changed lines** for one builder (a guideline; adjust per project).

## 3. Quality guards inside a batch

1. **Plan the whole batch first:** a numbered list of tasks, each with its definition of done.
2. **Make one commit per task,** so each task can be reviewed and reverted on its own.
3. **Verify after each task** with the fast checks; run the full `check` at the end of the batch.
4. **Stop on failure:** if one task fails and the cause is unclear, stop, report what is done and what isn't, and don't pile more changes on a broken base.
5. **Report per task:** done / failed / skipped, with test counts.
6. **Self-review the full diff** once at the end ([06](06-code-review.md)).

## 4. Fewer round-trips inside a turn

- **Run independent tool calls in parallel** (read 3 files at once, run lint and tests together).
- **Search, don't browse:** one `grep` beats opening five files.
- **Script repetitive edits:** one script that changes 20 files beats 20 separate edits. Review the resulting diff.
- **Read once:** use the maps ([14](14-codebase-maps.md)), keep notes, and don't re-open files you already read in this task.
- **Decide fully before acting:** gather what you need, then make the change in one go, instead of edit → check → re-edit loops.

## 5. Planner-level batching

The execution planner ([13](13-execution-orchestration.md)) applies the same idea at its level:
- one wake handles everything that is ready: review, merge, status update, next launches;
- independent phases go to parallel builders (each in its own worktree) and are launched in the same turn;
- small related phases can be merged into one builder brief if they meet §1.

## Self-check

- [ ] Are all the tasks in this batch independent and well-specified?
- [ ] Does each task have its own commit and its own result in the report?
- [ ] Did the checks run after each task, and the full check at the end?
- [ ] Would any task have deserved to be done alone because of its risk?
