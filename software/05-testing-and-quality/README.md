# Testing and Quality Assurance

## Why This Section Matters

AI can generate tests, but YOU need to evaluate whether they actually test the right things. Understanding testing strategy is how you prevent AI-generated code from shipping with a false sense of safety.

---

## Prerequisites

- [Section 01](../../software/01-python-fundamentals/README.md) through [Section 02](../../software/02-c-fundamentals/README.md)

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Python Testing with pytest (2nd ed) | Brian Okken | 2022 | — | THE Python testing reference. Covers fixtures, parametrize, plugins, and real-world testing patterns. |
| 🔑 | Concept | Testing pyramid | — | — | — | Unit, integration, end-to-end — know the right ratio and why most projects get it wrong. |
| | Book | Test Driven Development: By Example | Kent Beck | 2002 | — | TDD philosophy and practice. The red-green-refactor cycle and thinking through tests first. |
| | Book | Working Effectively with Legacy Code | Michael Feathers | 2004 | — | Adding tests to untested code — a skill that's increasingly relevant when reviewing and integrating AI-generated output. |
| 🔑🤖 | Practice | Review AI-generated tests | — | — | — | Critical skill: Do they test behavior or implementation? Do they cover edge cases? Are assertions meaningful? Or are they just making the coverage number go up? |
| | Tool | pytest | — | — | [Link](https://docs.pytest.org/) | Python testing framework — the standard for Python projects. |
| | Tool | pytest-cov | — | — | — | Code coverage analysis for pytest. Useful, but remember: coverage ≠ correctness. |
| | Tool | Unity Test Framework | ThrowTheSwitch | — | [Link](http://www.throwtheswitch.org/unity) | Unit testing for embedded C. Lightweight, no stdlib dependency, works on bare-metal targets. |
| | Tool | Ceedling | ThrowTheSwitch | — | [Link](http://www.throwtheswitch.org/ceedling) | Build and test system for C projects. Wraps Unity + CMock into a Ruby-based test runner. |
| | Tool | CMock | ThrowTheSwitch | — | [Link](http://www.throwtheswitch.org/cmock) | Mocking framework for C. Auto-generates mock functions from headers. |
| | Concept | Property-based testing with Hypothesis | — | — | [Link](https://hypothesis.readthedocs.io/) | Let the computer find edge cases. Generates random inputs to break your assumptions — catches bugs humans never think of. |
| | Concept | Mutation testing | — | — | — | Verify your tests actually catch bugs by injecting small code changes and checking if tests fail. The ultimate test-quality metric. |
| | Concept | Static analysis (mypy, pylint, cppcheck, clang-tidy) | — | — | — | Automated quality gates that catch type errors, style violations, and potential bugs before runtime. |
| | Concept | CI/CD pipelines | — | — | — | Automated testing on every commit. Tests only matter if they run automatically and block broken code. |

---

## Suggested Order

1. **Testing pyramid (concept)** — Understand the testing strategy landscape before writing any tests.
2. **Python Testing with pytest** — Learn the primary Python testing tool hands-on.
3. **Review AI-generated tests (practice)** — Start critically evaluating AI test output immediately. Make this a habit.
4. **Unity Test Framework + CMock** — Set up C testing for embedded projects.
5. **Test Driven Development (Kent Beck)** — Understand the TDD philosophy, even if you don't practice it dogmatically.
6. **Property-based testing (Hypothesis)** — Add this to your toolkit for finding edge cases automatically.
7. **Static analysis tools** — Set up mypy/pylint for Python, cppcheck/clang-tidy for C as automated quality gates.
8. **CI/CD pipelines** — Automate everything so tests run on every commit.
9. **Working Effectively with Legacy Code** — Read when you're integrating AI output into existing codebases.
10. **Mutation testing** — Use to audit test suite quality when you want maximum confidence.
