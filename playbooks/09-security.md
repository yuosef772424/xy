# 09 · Security

**Goal:** Don't introduce vulnerabilities. Assume all input is hostile.

## Checklist for every change

- [ ] **Input validation:** every external input is validated (type, length, format).
- [ ] **Injection:** SQL uses parameters; shell commands never interpolate user input; HTML output is escaped.
- [ ] **Auth:** every protected endpoint checks *who* the user is and *what* they may access.
- [ ] **Secrets:** no keys or passwords in code, logs, or commits; use environment variables or a secret manager.
- [ ] **Dependencies:** new packages are well maintained and pinned.
- [ ] **Errors:** error messages and logs don't leak internals or personal data.
- [ ] **Least privilege:** tokens, roles, and file permissions grant only what is needed.

## If you find a vulnerability

- Don't publish details in public issues.
- Report it privately to the maintainers and suggest a fix.
- If a secret was committed, treat it as leaked: **rotate it**. Deleting the commit is not enough.

## Anti-patterns

- "It's internal, so it doesn't need auth."
- Rolling your own crypto.
- Disabling TLS verification to get past an error.
