# 06 · Review Code

**Goal:** Catch real problems before they ship, and give feedback that is easy to act on.

## Review order (most important first)

1. **Correctness.** Does it do what the task asked? Edge cases? Error handling?
2. **Security.** Injection, auth checks, secrets, unsafe input. → [Security playbook](09-security.md)
3. **Data safety.** Migrations, data loss, backward compatibility.
4. **Tests.** Do they actually cover the change?
5. **Design.** Is it the simplest workable approach? Does it reuse existing code?
6. **Readability.** Names, structure, comments.
7. **Style.** Only what the linter does not already catch.

## How to give feedback

- Label severity: **blocking**, **should fix**, or **nit (optional)**.
- For every claim, give a concrete failure scenario: "If `items` is empty, line 42 divides by zero."
- Suggest a fix, not just a problem.
- Point out what is done well too.

## Reviewing your own diff

Before you call anything done, read your diff as if someone else wrote it and you had to approve it:

- [ ] Nothing unrelated changed.
- [ ] No debug code, secrets, or TODOs left behind.
- [ ] Every new branch of logic has been run at least once.
- [ ] I would be comfortable defending each line.
