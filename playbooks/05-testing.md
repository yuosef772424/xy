# 05 · Testing: Let Machines Verify

> **Goal:** Correctness is proven by automated checks that are cheap to repeat, not by the model re-reading code. · **Read when:** writing code, setting up a project, or when checks fail. · **Pays off because:** tests are the biggest token-saver and quality guard in the workflow. Every check a script does is one the model doesn't have to do by reading.

## 1. What to test
- **Every bug fix** gets a test that fails before the fix and passes after it.
- **Every new behavior** gets a happy-path test and edge-case tests: empty, zero, maximum, unicode/RTL text, `null`, invalid input, failing dependencies, timeouts.
- Test **behavior** (inputs → outputs), not implementation details. Mock only at the boundaries.
- Levels: **unit** (business logic) · **integration** (module ↔ database or external API, with fakes or containers) · **contract** (public interfaces, schemas, events) · **end-to-end** (only a few critical user journeys) · **architecture** (dependency and size rules, [12](12-architecture-rules.md) Part F) · **map freshness and doc health** (`gen_map.py --check`, `doc_health.py`, [07](07-maps-and-docs.md)) · **security** (dependency audit, secret scan).

## 2. One command per level
| Command | Covers | Rough target |
|---|---|---|
| `check:fast` | format, lint, types, map freshness, unit tests of the changed modules | about a minute |
| `check` | + all unit and integration tests + architecture rules | a few minutes |
| `check:full` | + end-to-end and slow tests | CI |

Builders run `check:fast` while working and `check` before pushing; CI runs `check:full` and must pass before merge. A pre-commit hook runs the cheap checks.

## 3. Rules
- Deterministic tests: no uncontrolled time, randomness, network, or ordering. A flaky test gets fixed or reported, never ignored.
- **Never skip, disable, delete, or weaken a test to get green.**
- A coverage gate on **changed** code (for example ~80% of new lines), not a vanity global number.
- Each module's tests can run on their own (the `how to test` line in its `MODULE.md`).

## 4. Output the model can afford to read
- On success, a one-line summary (`312 passed in 41s`). On failure, only the failing tests with short tracebacks (`pytest -q --tb=short`, a dot reporter, `| tail`).
- Write full logs to a file, and open them only if needed.
- Builders report **counts** (passed/failed/skipped), not raw logs.

## Anti-patterns
"I read it carefully, so it's correct" · tests that pass whatever the code does · mocking everything · pasting thousands of log lines into the conversation · tests "at the end, when there's time".
