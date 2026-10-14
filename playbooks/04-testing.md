# 04 · Test

**Goal:** Prove that the change works and keeps working.

## Rules

- Every bug fix gets a test that **fails before** the fix and **passes after** it.
- Every new behavior gets at least one happy-path test and one edge-case test.
- Test behavior (inputs → outputs), not implementation details.
- Tests must be deterministic: no reliance on real time, randomness, network, or test order.

## What to cover

- Happy path.
- Boundaries: empty input, zero, maximum size, unicode, `null`/`undefined`.
- Error paths: invalid input, failing dependencies, timeouts.
- Regressions: the exact scenario from the bug report.

## Workflow

1. Run the existing tests first to learn the baseline.
2. Write or update the tests.
3. Run only the affected tests while iterating, for speed.
4. Run the full suite, linter, type checker, and build before you finish.
5. Report the exact commands you ran and their results.

## Anti-patterns

- Deleting, skipping, or loosening a failing test to make it green.
- Tests that pass whatever the code does.
- Mocking everything until the test no longer tests anything real.
- Reporting "tests pass" without having run them.
