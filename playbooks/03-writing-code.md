# 03 · Write Code

**Goal:** Write code that is correct, readable, and looks native to the project.

## Before writing

- Read at least one neighboring file to learn local conventions: naming, error handling, imports, tests.
- Search for an existing helper before writing a new one.

## While writing

- **Minimal diff:** change only what the task needs.
- **Clear names:** `calculateInvoiceTotal`, not `doCalc`.
- **Small functions:** one responsibility each.
- **Fail loudly at boundaries:** validate external input and handle network and file errors explicitly.
- **Trust internal code:** don't add defensive checks for situations that cannot happen.
- **Comments explain *why*,** not *what*.
- **No magic values:** name your constants.
- **Keep dependencies lean:** add a library only when it clearly earns its place.

## After writing

- Run the formatter and linter.
- Remove debug output, unused imports, and commented-out code.
- Re-read the diff from top to bottom.

## Anti-patterns

- Reformatting unrelated code in the same change.
- Copy-pasting a block instead of extracting a function (after the third copy).
- Clever one-liners that need a paragraph to explain.
- Silently catching and ignoring errors.
