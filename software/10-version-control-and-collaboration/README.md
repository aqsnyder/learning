# Version Control and Collaboration

## Why This Section Matters

Git is the backbone of all modern software. Understanding branching strategies, pull request workflows, and collaboration patterns is essential for overseeing AI-generated code changes.

---

## Prerequisites

- Basic command line familiarity

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Book (Free) | Pro Git | Scott Chacon, Ben Straub | [Link](https://git-scm.com/book/en/v2) | THE Git reference. Read chapters 1–3 for fundamentals, then use the rest as a reference. Covers everything from basics to internals. |
| 🔑 | Interactive | Learn Git Branching | — | [Link](https://learngitbranching.js.org/) | Visual, interactive Git tutorial. The best way to build intuition for how branches, merges, and rebases actually work. |
| | Concept | Branching strategies | — | — | Git Flow, GitHub Flow, trunk-based development. Understand the trade-offs and when each strategy fits your team size and release cadence. |
| | Concept | Pull request best practices | — | — | Writing good PR descriptions, reviewing effectively, keeping PRs small and focused. The PR is a communication tool, not just a merge gate. |
| 🤖 | Concept | Managing AI-generated PRs | — | — | Reviewing large diffs, ensuring atomic changes, verifying AI didn't introduce unrelated modifications. AI PRs need stricter review than human ones. |
| | Concept | Rebasing vs merging | — | — | When to use each. Rebase for clean history, merge for preserving context. Know the trade-offs and your team's convention. |
| | Concept | Git bisect | — | — | Finding the commit that introduced a bug. A powerful debugging tool that most developers underuse. |
| | Concept | Git hooks and automation | — | — | Pre-commit checks, linting, formatting. Automate quality gates so review can focus on logic and design. |
| | Tool | GitHub Actions / CI-CD | — | — | Automated testing and deployment pipelines. The infrastructure that makes continuous delivery possible. |
| | Concept | Monorepos vs polyrepos | — | — | Trade-offs for project organization. Monorepos simplify dependency management; polyrepos simplify ownership boundaries. |

---

## Suggested Order

1. **Learn Git Branching (interactive)** — Start here. Build visual intuition for Git operations.
2. **Pro Git (chapters 1–3)** — Read for a solid conceptual foundation. Reference later chapters as needed.
3. **Branching strategies** — Understand Git Flow vs GitHub Flow vs trunk-based development.
4. **Pull request best practices** — Learn to write and review PRs effectively.
5. **Managing AI-generated PRs** — Apply stricter review discipline to AI-generated changes.
6. **Rebasing vs merging** — Understand when to use each and why it matters for history.
7. **Git hooks and automation** — Set up pre-commit hooks for linting and formatting.
8. **GitHub Actions / CI-CD** — Build automated testing and deployment pipelines.
9. **Git bisect** — Learn this debugging superpower for finding regression commits.
10. **Monorepos vs polyrepos** — Understand the organizational trade-offs for larger projects.
