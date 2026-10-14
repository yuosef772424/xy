# Contributing

Contributions that make agents do better work are welcome.

## Writing a playbook

- **Write instructions, not essays.** Use the imperative: "Run the tests", not "It is good to run tests".
- **Be concrete.** Give commands, checklists, and short examples.
- **Keep it short.** One playbook should take under 5 minutes to read.
- **Start every playbook with:** `> **Goal:** … · **Read when:** … · **Pays off because:** …`. A file with no clear benefit over its cost doesn't belong here: merge it into another file or drop it.
- **Then follow the shape:** *Steps or rules → Checklist → Anti-patterns*, keeping only the parts that add value.
- **State the goal and the desired outcome; treat numbers as guidelines.** Write "keep it short enough to read in a minute (around 60 lines)", not "max 60 lines". Models differ, and so do projects.
- **Be tool-agnostic.** Mention specific tools only as examples.

## Process

1. Create a branch.
2. Prefer extending an existing playbook over adding a new one. Agents propose changes via `PROPOSALS.md` instead of editing rules directly.
3. Link new files from `README.md`, and from `AGENTS.md` §7 if agents need to find them.
4. Open a pull request explaining what problem the change solves.
