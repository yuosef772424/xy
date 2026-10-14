# 12 · Architecture Rules: Structure by Rules, Not by Taste

> **Goal:** A structure that stays clean as the project **grows and changes**, so that adding a feature means *adding* code, not *rewriting* it. · **Read when:** designing ([11](11-architecture.md)), adding a module, and during architecture health checks. · **Pays off because:** it prevents the typical AI pattern of an elegant first design that tangles under change and forces repeated restructuring.

**The typical AI failure:** the first structure looks excellent, but every change adds a small shortcut. After enough changes the modules are tangled, and the only way out is a full restructure, which then happens again. These rules prevent that in three ways: they decide the structure by **explicit criteria**, they test it against the **future feature list**, and they **enforce it automatically** so it can't drift.

Apply these rules during [architecture planning](11-architecture.md). Any exception needs a written decision record.

---

## Part A · Scope: what we build now vs later

### A1. Classify every feature (MoSCoW)

| Class | Meaning | Goes into |
|---|---|---|
| **Must (MVP)** | Without it, the product has no reason to exist | First phases of the roadmap |
| **Should (v1.x)** | Important, but the product works without it | Later phases |
| **Could (later)** | Nice to have; build only if the data supports it | Backlog |
| **Won't (now)** | Explicitly out of scope | Listed, so nobody builds it by accident |

Rule: the MVP is the **smallest set that tests the core value**. If it feels long (more than a handful of main features), look for what can move to Should.

### A2. Design for the full list, build only the MVP

- **Build** only Must features.
- **Design the structure** so every Should and Could feature has an obvious place to land.
- Don't write code for future features (YAGNI), but don't block them either.

### A3. The extension test (required)

For **every** Should/Could feature, write one line: *which modules change, and how*.

| Result | Meaning |
|---|---|
| Adds a new module or a new plugin/strategy only | ✅ excellent |
| Changes 1 module internally | ✅ good |
| Changes 2 modules' internals | ⚠️ acceptable; justify it |
| Changes the core, a shared contract, or 3+ modules | ❌ the structure is wrong; redesign before building |

This test is the main defense against future entanglement. It turns "will this scale?" from an opinion into a check.

---

## Part B · Decomposition rules

### B1. Split by business capability, not only by technical layer
- ✅ `billing/`, `catalog/`, `users/`, `notifications/`, each containing its own API, logic, and data access.
- ❌ Only `controllers/`, `services/`, `models/`, where every feature touches every folder.
- Technical layers can exist *inside* each module.

### B2. High cohesion, low coupling
- Things that change together live together.
- A module should be explainable in one sentence. If the sentence needs "and", consider splitting it.

### B3. Start as a modular monolith
- One deployable app with strict internal module boundaries.
- Split into separate services only with **evidence**: different scaling needs, separate teams, or separate release cycles. Microservices on day one are a common source of unnecessary complexity.

### B4. Isolate the core from the details
- **Core / domain:** the business rules. Pure, with no framework, database, or HTTP code.
- **Adapters:** database, external APIs, UI, queues. They plug into the core through interfaces (ports).
- Result: swapping a database or a payment provider means changing one adapter, not the core.

---

## Part C · Dependency and communication rules

### C1. One-way dependencies, no cycles
- Dependencies point **inward**: adapters → application → domain. Never the reverse.
- No circular dependencies between modules, ever.

### C2. Talk through public interfaces only
- Each module exposes one public entry point (`index`, a `public` package, or an API).
- Importing another module's internal files is forbidden.

### C3. Each module owns its data
- No module reads or writes another module's tables directly. Ask the owning module through its interface.
- Shared database tables are the most common hidden coupling.

### C4. Prefer events for side effects
- "Order placed → send email, update stats" should be an event the other modules subscribe to, not direct calls from `orders` into every other module.
- This way, adding a new reaction means adding a subscriber, without touching the publisher.

### C5. Cross-cutting concerns live in one place
- Auth, logging, error handling, config, and i18n each live in one shared module with a clear interface. They are never re-implemented per feature.

---

## Part D · Designing for change

### D1. Put extension points where variation is expected
- Use the Should/Could list to find the **known variation points**: payment providers, notification channels, export formats, AI models, and so on.
- Put a strategy or plugin interface there **now**, with only one implementation. Adding the second one is then cheap.
- Don't add extension points anywhere else; speculative abstraction is also a cost.

### D2. Stable contracts
- APIs, events, and schemas are versioned. Changes are backward compatible (add fields; don't rename or remove them).
- Database migrations are forward-only and safe to run on live data.

### D3. Configuration and feature flags
- Variation that is a value (limits, URLs, toggles) goes in config, not in code branches.
- Unfinished features ship behind flags, so the main branch always stays releasable.

---

## Part E · Controlled growth

### E1. Size guidelines (adjust per stack and language)
These are signals to look closer, not mechanical limits. The goal: each unit stays easy to understand and change.

| Unit | Look closer around | Typical action |
|---|---|---|
| Function | ~50 lines | Extract functions |
| File | ~300–400 lines | Split by responsibility |
| Module | one-sentence purpose; ~15–20 files | Split by sub-capability; record the decision |
| Public interface | ~10–15 exported operations | Check whether the module is doing two jobs |

### E2. Adding a new module needs a reason
State in the decision record: why no existing module fits, what it owns, and its dependencies. This prevents both "god modules" and "a module per file".

### E3. Refactor continuously, in small steps
- Every few phases, run an **architecture health check** (Part F). Fix drift immediately in small PRs.
- A big rewrite is a sign that small corrections were skipped.

---

## Part F · Enforcement: make the rules automatic

Rules that live only in a document will drift, especially with AI builders. **Enforce them in CI:**

| Rule | Example tools |
|---|---|
| No cycles; allowed dependency directions; no internal imports | `dependency-cruiser`, `eslint-plugin-boundaries` (JS/TS); `import-linter` (Python); ArchUnit (Java); `go vet` + internal packages (Go) |
| Size and complexity limits | linter rules (`max-lines`, `complexity`), `radon`, SonarQube |
| Contract compatibility | OpenAPI/schema diff checks, consumer contract tests |
| Module data ownership | separate schemas or DB users per module; review checklist |

**Architecture health check** (every few phases, run by a review agent):
1. Dependency graph: any new cycles or forbidden edges?
2. Largest files and modules: over their limits?
3. Re-run the extension test for the remaining Should/Could features: is it still ✅?
4. Report the findings and file small fix phases.

---

## Part G · A plan that is cheap to change

- **Each phase delivers a working increment.** No phase leaves the system half-built.
- **Phases depend on contracts, not on each other's internals,** so they can be reordered or dropped.
- **Unclear areas get a short spike phase** (time-boxed exploration) before committing to a design.
- **The roadmap is a living document:** reprioritizing means editing `ROADMAP.md`, not redesigning.
- **Decisions are recorded with what would make them wrong** ("revisit if traffic exceeds X"), so changing them later is a planned event, not a crisis.

---

## Architecture checklist (must pass before execution starts)

- [ ] Every feature is classified Must / Should / Could / Won't.
- [ ] The extension test passes (✅ or a justified ⚠️) for every Should/Could feature.
- [ ] Modules are split by capability, each with a one-sentence purpose.
- [ ] The dependency direction is defined, and there are no cycles.
- [ ] Every module has a public interface and owns its own data.
- [ ] Extension points exist only at known variation points.
- [ ] The rules are enforced by CI tools, not only written down.
- [ ] The phases are small, each delivers a working increment, and dependencies are explicit.
