# Reading and Reviewing Code

> **Why this section matters:** In the age of AI-generated code, your primary skill is READING code, not writing it. This section teaches you to navigate unfamiliar codebases, conduct effective code reviews, and spot issues that AI tools miss.

**Prerequisites:** Sections 01–02.

---

## 🎯 Learning Objectives

After this section you can:
- Navigate an unfamiliar codebase starting from its entry points, tests and API surface, and produce a call-path trace and module map that you then verify in a debugger.
- Name code smells from Fowler's catalog and complexity red flags from Ousterhout on sight, and propose the specific named refactoring for each.
- Run a structured review following Google's reviewer guide (design → functionality → complexity → tests → naming and comments), and write comments labelled by severity (Nit / Optional / FYI).
- Measure your own review recall against expert reviewers and seeded defects, and turn your misses into checklist items.
- Spot common security defects during review: injection and unsafe deserialization in Python; overflows and use-after-free in C.

---

## Resources

| # | Type | Resource | Notes |
|---|------|----------|-------|
| 1 | 🔑 Book | *The Art of Readable Code* — Boswell and Foucher | How to evaluate whether code is clear and maintainable |
| 2 | 🔑 Book | *Code Reading: The Open Source Perspective* — Diomidis Spinellis | The only book dedicated to reading (not writing) code |
| 3 | 🔑 Book | *Refactoring: Improving the Design of Existing Code* (2nd ed) — Martin Fowler (2018) | Recognize code smells and know the fix |
| 4 | 🔑 Book | *A Philosophy of Software Design* (2nd ed) — John Ousterhout (2021) | Managing complexity, the #1 code review skill |
| 5 | Guide | [Google's Engineering Practices: Code Review Guidelines](https://google.github.io/eng-practices/review/) | How Google does code reviews |
| 6 | 🔑🤖 Practice | Review AI-generated code critically | Treat every AI output as a PR from a junior developer |
| 7 | Book | [*The Programmer's Brain*](https://www.manning.com/books/the-programmers-brain) — Felienne Hermans (2021) | The cognitive science of reading code: why unfamiliar code overloads working memory, and concrete techniques (state tables, dependency graphs, mental models) to read it faster. Trains this section's core skill directly |
| 8 | Book | [*Your Code as a Crime Scene* (2nd ed)](https://pragprog.com/titles/atcrime2/your-code-as-a-crime-scene-second-edition/) — Adam Tornhill (2024) | Read a codebase through its git history: hotspots (complexity × churn), change coupling, knowledge distribution. Tells you where to spend review effort in a large or agent-generated codebase |

### Key Concepts

| Concept | Why It Matters |
|---------|---------------|
| Code smells | Recognize anti-patterns: long methods, deep nesting, god objects |
| Reading unfamiliar codebases | Start from tests, entry points, and API surfaces |
| Static analysis as a reading aid | Use linters and type checkers to understand code faster |
| Reviewing for security | Common vulnerabilities in Python (injection, deserialization) and C (buffer overflows, use-after-free) |

---

## Suggested Order

```
1. The Art of Readable Code (quick read, sets the standard)
2. The Programmer's Brain (how reading code actually works; techniques to practice)
3. A Philosophy of Software Design (learn to think about complexity)
4. Code Reading (practice navigating real codebases)
5. Refactoring (catalog of smells and systematic fixes)
6. Your Code as a Crime Scene (use git history to decide where to look first)
7. Google Code Review Guidelines (professional review process)
8. Practice: review AI-generated code on every project
```

---

## 🛠️ Practice

1. **Annotated read: CPython's `queue.py`** — Read `Lib/queue.py` (~400 lines) end to end. Produce:
   - (a) a diagram of its one lock and three `Condition`s (`not_empty`, `not_full`, `all_tasks_done`), showing which methods wait on each and which notify it;
   - (b) the invariant tying `unfinished_tasks` to `put()`/`task_done()`;
   - (c) an explanation of how `LifoQueue` and `PriorityQueue` reuse all the locking by overriding only `_put`/`_get` (name the pattern);
   - (d) predictions for four edge cases: `task_done()` called once too often, `put(block=False)` on a full queue, `get(timeout=0)` on an empty one, and `get()` after `shutdown()`.

   Verify each prediction in a REPL (Python ≥ 3.13). *(~2 h · Spinellis, Code Reading, on reading data structures and control flow; The Art of Readable Code)*
2. **Trace a call through `requests`** — In a fresh clone of `psf/requests`, find every hop from `requests.get()` to the urllib3 call that touches the network. Use only reading tools: ripgrep, go-to-definition, and `git log --stat` to find hotspots. No debugger yet. Record each hop as file:line. Also record where the `timeout` argument becomes a urllib3 timeout object, and where `max_retries` is applied. Then set a breakpoint on the urllib3 call and compare the real stack with your trace. Done when they match hop for hop, after less than 60 minutes of reading. *(~2 h · Spinellis on tackling large projects and on code-reading tools; this section's "start from tests, entry points and API surfaces")*
3. **Calibrate against real reviewers** — Pick three merged PRs with substantive review threads in a library you use (e.g., PyVISA, pyserial, pytest). Review each PR's *first* revision cold, using Google's "What to Look For in a Code Review", and label your comments Nit, Optional or FYI. Then read the actual thread and score yourself on three counts: caught, missed, and extra (noting whether each extra was valid). Done when you have a hit/miss table across the three PRs and one sentence naming your blind spot. *(~3 h · Google Engineering Practices: "What to Look For in a Code Review", "Navigating a CL in Review", "How to Write Code Review Comments")*
4. **Smell census of an unconstrained AI module** — Give an agent one sentence and nothing else: "Write a Python CLI that loads a CSV of production-test measurements, computes per-test statistics, flags out-of-limit results and writes an HTML report." Annotate the output with:
   - every smell from Fowler's catalog, by name;
   - every Ousterhout red flag (shallow module, information leakage, pass-through method, …);
   - every naming or comment problem from *The Art of Readable Code*.

   Then write characterization tests and apply the three highest-value refactorings by their catalog names (e.g., Split Phase, Extract Function, Replace Primitive with Object), keeping the tests green throughout. *(~3 h · Refactoring ch. 3 "Bad Smells in Code" and the refactoring catalog; A Philosophy of Software Design on deep modules, information hiding and red flags; The Art of Readable Code)*
5. **Seeded-defect PR review** — Have one agent session implement a real change in one of your repos, e.g., "add retries with exponential backoff and a per-command timeout to the instrument driver". Have a second, separate session inject three subtle defects into that branch and record them in a sealed file, for example:
   - an off-by-one in the retry loop;
   - a swallowed exception;
   - user input interpolated into a SCPI or SQL string.

   Review the PR against a checklist with three parts:
   - Google's list;
   - a security section: injection, unsafe deserialization and path traversal in Python; bounds, integer overflow and use-after-free in C;
   - AI-specific checks: invented APIs, unrelated edits, tests that mirror the implementation.

   Done when you've scored your recall and added a checklist line for every defect you missed. Keep the checklist; Sections 05, 08, 09 and 10 extend it. *(~3 h · Google review guide; this section's "Review AI-generated code critically" practice; for the security part, OWASP Top 10 and the SEI CERT C Coding Standard, listed in Section 08)*

**🏗️ Mini-project — ARCHITECTURE.md for a Dependency:** Write an `ARCHITECTURE.md` of at most two pages for a mid-size library you rely on (PyVISA, pyserial or pyOCD). Cover:
- its purpose;
- a code map: the key modules, and what *not* to look for where;
- the core abstractions and their invariants;
- the lifecycle of one typical call;
- cross-cutting concerns (errors, timeouts, logging);
- five smells or risks, each with file:line.

Before writing, list eight "where is…/why does…" navigation questions and verify their answers yourself. Deliverable: `projects/software/03-architecture-md/`. Success: a fresh AI session given only the repo and your document answers at least 7 of the 8 correctly, using fewer tool calls than a session without it. *(~8 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What standard does Google's guide say a CL must meet to be approved, and what is that standard explicitly *not*?
2. Name Ousterhout's three symptoms of complexity, and give a one-line code example of each.
3. What is a "deep module", and why is a class full of one-line pass-through methods a red flag?
4. A method reaches into another object's fields more than its own. Name the smell and the refactoring that fixes it.
5. Why start reading an unfamiliar codebase from its tests and entry points, instead of browsing files in order?
6. Misconception check: "CI is green and coverage is 95%, so this AI-generated PR is safe to approve." List three things you still must check yourself.
7. Name two Python and two C vulnerability classes you scan for in every review, and the code pattern that signals each.
8. Explain to a smart friend in three sentences why reading code becomes the scarcer skill once AI writes most of it.
