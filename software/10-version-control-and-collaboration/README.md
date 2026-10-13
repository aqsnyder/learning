# Version Control and Collaboration

## Why This Section Matters

Git is the backbone of all modern software. Understanding branching strategies, pull request workflows, and collaboration patterns is essential for overseeing AI-generated code changes.

---

## Prerequisites

- Basic command line familiarity

---

## 🎯 Learning Objectives

After this section you can:
- Explain Git's object model (blobs, trees, commits, refs) well enough to build a commit with plumbing commands and to predict what porcelain commands do to the graph.
- Recover "lost" work — after a hard reset, a deleted branch, a dropped stash or a botched rebase — with the reflog and `git fsck`.
- Find regressions with `git bisect run` (including skip codes), and reconstruct a line's history with `log -L`, `blame -C` and the pickaxe.
- Turn a sprawling AI-generated change into a stack of atomic commits that each build and pass tests, with reviewable PR descriptions.
- Choose a branching strategy and repo layout for a small team that uses agents, and enforce quality gates with hooks, CI and branch protection.

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
| | Article | How to Write a Git Commit Message | Chris Beams | [Link](https://cbea.ms/git-commit/) | 2014. The seven rules (blank line after subject, ≤50-character imperative subject, body wrapped at 72 explaining what and why). Hand it to your agents as the commit-message spec. |
| | Tool | pre-commit | Anthony Sottile et al. | [Link](https://pre-commit.com/) | A framework for managing multi-language Git hooks: run formatters, linters, and checks on every commit, whoever (or whatever) wrote it. The concrete tool behind the "Git hooks and automation" row. |
| 🤖 | Docs | git worktree | Git project | [Link](https://git-scm.com/docs/git-worktree) | Several working trees attached to one repository, each on its own branch. The standard way to run parallel coding-agent sessions without their edits colliding. |

---

## Suggested Order

1. **Learn Git Branching (interactive)** — Start here. Build visual intuition for Git operations.
2. **Pro Git (chapters 1–3)** — Read for a solid conceptual foundation. Reference later chapters as needed.
3. **Branching strategies** — Understand Git Flow vs GitHub Flow vs trunk-based development.
4. **How to Write a Git Commit Message** — Adopt one commit-message convention for yourself and your agents.
5. **Pull request best practices** — Learn to write and review PRs effectively.
6. **Managing AI-generated PRs** — Apply stricter review discipline to AI-generated changes.
7. **Rebasing vs merging** — Understand when to use each and why it matters for history.
8. **Git hooks and automation (pre-commit)** — Set up pre-commit hooks for linting and formatting.
9. **git worktree** — Run parallel agent sessions in isolated checkouts.
10. **GitHub Actions / CI-CD** — Build automated testing and deployment pipelines.
11. **Git bisect** — Learn this debugging superpower for finding regression commits.
12. **Monorepos vs polyrepos** — Understand the organizational trade-offs for larger projects.

---

## 🛠️ Practice

1. **Commit by hand** — Clear Learn Git Branching's Main and Remote level sets, predicting each graph before you run the command. Then, following Pro Git §10.2 "Git Objects" and §10.3 "Git References", build a two-commit history in an empty repo using only plumbing: `hash-object -w`, `update-index`, `write-tree`, `commit-tree` and `update-ref`. Done when `git log --graph` shows your history, `git fsck` is clean, and you can explain why changing one byte in the first commit's file changes the hash of every later commit. *(~3 h · Learn Git Branching; Pro Git ch. 10 "Git Internals")*
2. **Git ER drills** — In a scratch repo, cause each of these disasters and then recover from it:
   - `reset --hard HEAD~3`;
   - `branch -D` on an unmerged branch;
   - a dropped stash;
   - an interactive rebase that squashed the wrong commits;
   - an `--amend` that lost a file.

   Write a one-page "Git ER" card with the exact recovery commands. Done when all five are recovered without re-typing any content. *(~2 h · Pro Git §7.7 "Reset Demystified" and §10.7 "Maintenance and Data Recovery")*
3. **Automated bisect** — Script a 200-commit synthetic history in which one commit introduces a numeric regression (a filter-coefficient change that shifts an output by 0.3%) and a handful of commits don't build. Write a `git bisect run` script that exits 0 for good, 1 for bad and 125 for skip. Done when bisect names the culprit in about ⌈log₂ 200⌉ = 8 test runs plus skips. Stretch: bisect a firmware regression using the Section 05 HIL suite as the oracle, flashing and testing at every step. *(~3 h · Pro Git §7.10 "Debugging with Git")*
4. **Archaeology on a real line** — In a clone of `FreeRTOS/FreeRTOS-Kernel` or `python/cpython`, pick a non-obvious line, such as a check in `queue.c` or a branch in `Lib/queue.py`. Reconstruct why it exists using `git log -L`, `git blame -w -C -C -C`, `git log -S`/`-G`, and the linked issue or PR. Write a 200-word story with commit hashes. Done when the story names the bug or requirement that triggered the line, not just its author. *(~2 h · Pro Git §7.5 "Searching" and §7.10 "Debugging with Git")*
5. **Split the AI mega-diff** — Have an agent make a sprawling change as one commit: a refactor, a feature, reformatting and a dependency bump. Split it into atomic commits with `git add -p`, `git commit --fixup` and `git rebase -i --autosquash`. Stack the commits as two or three PRs, with descriptions covering what changed, why, how it was tested, and how AI was involved. Done when `git rebase --exec "<test command>" main` passes at every commit and each PR can be reviewed in under 15 minutes. Add a PR-size and scope check to your Section 03 review checklist. *(~3 h · pull-request best practices; managing AI-generated PRs; rebasing vs merging; Pro Git §7.6 "Rewriting History")*

**🏗️ Mini-project — Repo Hygiene Kit:** For one real repo (Python + firmware), write a one-page decision covering:
- the branching strategy (trunk-based, GitHub Flow or Git Flow), given your release cadence and any field-support branches;
- the repo layout: monorepo or polyrepo for firmware plus host tools.

Then implement it:
- a `pre-commit` config: ruff, mypy, clang-format, and large-file and secret scanning;
- a commit-msg hook;
- a PR template with an "AI involvement & verification" section;
- CODEOWNERS;
- a GitHub Actions workflow behind branch protection: lint, type-check, pytest, Ceedling, a cross-compile with arm-none-eabi-gcc, upload of the `.elf`/`.map`, and a PR comment showing the flash/RAM size delta.

Deliverable: the configured repo, plus the decision note in `projects/software/10-repo-hygiene/`. Success: a deliberately bad PR — failing test, unformatted code, a fake secret and an 800-line mixed diff — is blocked by at least three independent gates, and a clean PR merges with no manual steps. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Name Git's four object types. What does a branch actually store?
2. After `git reset --hard HEAD~3`, where are those three commits, and what would make them truly unrecoverable?
3. Bisecting 1,000 commits takes roughly how many test runs? What does exit code 125 mean to `git bisect run`?
4. State Pro Git's golden rule of rebasing, and describe what goes wrong when someone breaks it.
5. Name three checks you apply to an AI-generated PR that you might skip for a trusted colleague's PR.
6. A two-person firmware team ships monthly and must patch old releases in the field. Which fits best — trunk-based development, GitHub Flow or Git Flow — and why?
7. Misconception check: "We squash-merge every PR, so commit hygiene inside a PR doesn't matter." What do you lose for bisect, blame and review?
8. Explain to a smart friend in three sentences why Pro Git describes Git as, at bottom, a content-addressable filesystem with a version-control interface on top.
