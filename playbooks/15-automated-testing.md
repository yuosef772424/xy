# 15 · Automated Testing (Let Machines Verify)

**Goal:** Machines check correctness cheaply and repeatably, so the model doesn't spend tokens re-reading code to convince itself, and the owner doesn't have to check by hand.

Every check that a script can do is a check the model doesn't have to do by reading. Automated tests are the biggest token saver in the whole workflow.

## 1. One command per level

Every project exposes these commands (via `make`, `npm run`, `just`, or similar):

| Command | Runs | Target time |
|---|---|---|
| `check:fast` | format, lint, type check, map freshness, and the unit tests of the changed modules | < 1 minute |
| `check` | everything above + all unit and integration tests + architecture rules | < 10 minutes |
| `check:full` | + end-to-end and slow tests | CI only |

Builders run `check:fast` while working and `check` before pushing. CI runs `check:full`.

## 2. What to automate

- **Unit tests:** the business logic in each module's core.
- **Integration tests:** module ↔ database, module ↔ external API (with fakes or containers).
- **Contract tests:** public interfaces, API schemas, events. These catch breaking changes between modules.
- **End-to-end tests:** a few critical user journeys only (they are slow and brittle).
- **Architecture tests:** dependency rules and size limits ([12a](12a-architecture-rules.md) Part F).
- **Map freshness:** `scripts/gen_map.py --check` ([14](14-codebase-maps.md)).
- **Security:** dependency audit and secret scanning.

## 3. Rules

- **Tests come with the code.** A phase's definition of done includes its tests. A bug fix starts with a failing test.
- **Each module's tests run alone** (`how to test` in its `MODULE.md`), so a builder only runs what it touched.
- **Deterministic:** no real network, clock, or randomness without control. A flaky test gets fixed or reported, never ignored.
- **Coverage gate on changed code** (for example, ≥ 80% of new or changed lines), not a global vanity number.
- **Never skip, disable, or weaken a test to get green.**

## 4. Token-efficient test output

Test output can be huge. Configure it so the model reads only what matters:

- Quiet mode on success: one summary line (`312 passed in 41s`).
- On failure: only the failing tests, with short tracebacks (e.g. `pytest -q --tb=short`, `vitest --reporter=dot`, `go test ./... 2>&1 | tail -50`).
- Write full logs to a file; the agent opens them only if the summary isn't enough.
- Builders **report counts** (passed/failed/skipped), not raw logs. See [13](13-execution-orchestration.md) §4.

## 5. Hooks and CI

- **Pre-commit hook:** format, lint, and map freshness. Cheap, so mistakes never reach a commit.
- **CI on every PR:** `check` (or `check:full`), required to pass before merge.
- **The planner trusts CI results plus cheap commands,** not narratives ([13](13-execution-orchestration.md) §5).

## Anti-patterns

- "I read the code carefully and it looks correct" instead of running it.
- A test suite that only passes on one machine.
- Pasting 2,000 lines of test log into the conversation.
- Tests added at the end of the project "when there is time".
