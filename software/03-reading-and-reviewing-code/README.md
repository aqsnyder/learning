# Reading and Reviewing Code

> **Why this section matters:** In the age of AI-generated code, your primary skill is READING code, not writing it. This section teaches you to navigate unfamiliar codebases, conduct effective code reviews, and spot issues that AI tools miss.

**Prerequisites:** Sections 01–02.

---

## Resources

| # | Type | Resource | Notes |
|---|------|----------|-------|
| 1 | 🔑 Book | *The Art of Readable Code* — Boswell and Foucher | How to evaluate whether code is clear and maintainable |
| 2 | 🔑 Book | *Code Reading: The Open Source Perspective* — Diomidis Spinellis | The only book dedicated to reading (not writing) code |
| 3 | 🔑 Book | *Refactoring: Improving the Design of Existing Code* (2nd ed) — Martin Fowler (2018) | Recognize code smells and know the fix |
| 4 | 🔑 Book | *A Philosophy of Software Design* — John Ousterhout | Managing complexity, the #1 code review skill |
| 5 | Video | [Google's Engineering Practices: Code Review Guidelines](https://google.github.io/eng-practices/review/) | How Google does code reviews |
| 6 | 🔑🤖 Practice | Review AI-generated code critically | Treat every AI output as a PR from a junior developer |

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
2. A Philosophy of Software Design (learn to think about complexity)
3. Code Reading (practice navigating real codebases)
4. Refactoring (catalog of smells and systematic fixes)
5. Google Code Review Guidelines (professional review process)
6. Practice: review AI-generated code on every project
```
