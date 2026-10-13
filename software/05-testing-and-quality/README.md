# Testing and Quality Assurance

## Why This Section Matters

AI can generate tests, but YOU need to evaluate whether they actually test the right things. Understanding testing strategy is how you prevent AI-generated code from shipping with a false sense of safety.

---

## Prerequisites

- [Section 01](../01-python-mastery/README.md) through [Section 02](../02-embedded-c-mastery/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Design a test portfolio (unit, integration, hardware-in-the-loop, end-to-end) for a product that mixes Python and firmware, and justify its proportions with the testing pyramid.
- Write property-based tests with Hypothesis (round-trip, invariant, model/oracle and stateful) that find edge cases example-based tests miss.
- Unit-test embedded C off-target with Unity, CMock and Ceedling, mocking the HAL at a link seam.
- Judge AI-generated tests by mutation score as well as coverage, and explain why coverage ≠ correctness.
- Put legacy code under characterization tests before changing it, using Feathers' seam model.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Python Testing with pytest (2nd ed) | Brian Okken | 2022 | — | THE Python testing reference. Covers fixtures, parametrize, plugins, and real-world testing patterns. |
| | Concept | Testing pyramid | — | — | — | Unit, integration, end-to-end — know the right ratio and why most projects get it wrong. |
| | Book | Test Driven Development: By Example | Kent Beck | 2002 | — | TDD philosophy and practice. The red-green-refactor cycle and thinking through tests first. |
| | Book | Working Effectively with Legacy Code | Michael Feathers | 2004 | — | Adding tests to untested code — a skill that's increasingly relevant when reviewing and integrating AI-generated output. |
| 🤖 | Practice | Review AI-generated tests | — | — | — | Critical skill: Do they test behavior or implementation? Do they cover edge cases? Are assertions meaningful? Or are they just making the coverage number go up? |
| | Tool | pytest | — | — | [Link](https://docs.pytest.org/) | Python testing framework — the standard for Python projects. |
| | Tool | pytest-cov | — | — | — | Code coverage analysis for pytest. Useful, but remember: coverage ≠ correctness. |
| | Tool | Unity Test Framework | ThrowTheSwitch | — | [Link](http://www.throwtheswitch.org/unity) | Unit testing for embedded C. Lightweight, no stdlib dependency, works on bare-metal targets. |
| | Tool | Ceedling | ThrowTheSwitch | — | [Link](http://www.throwtheswitch.org/ceedling) | Build and test system for C projects. Wraps Unity + CMock into a Ruby-based test runner. |
| | Tool | CMock | ThrowTheSwitch | — | [Link](http://www.throwtheswitch.org/cmock) | Mocking framework for C. Auto-generates mock functions from headers. |
| | Concept | Property-based testing with Hypothesis | — | — | [Link](https://hypothesis.readthedocs.io/) | Let the computer find edge cases. Generates random inputs to break your assumptions — catches bugs humans never think of. |
| | Concept | Mutation testing | — | — | — | Verify your tests actually catch bugs by injecting small code changes and checking if tests fail. The ultimate test-quality metric. |
| | Concept | Static analysis (mypy, pylint, cppcheck, clang-tidy) | — | — | — | Automated quality gates that catch type errors, style violations, and potential bugs before runtime. |
| | Concept | CI/CD pipelines | — | — | — | Automated testing on every commit. Tests only matter if they run automatically and block broken code. |
| 🔑 | Book | Test-Driven Development for Embedded C | James W. Grenning | 2011 | [Link](https://pragprog.com/titles/jgade/test-driven-development-for-embedded-c/) | The embedded TDD book, with Unity and CppUTest: test doubles, spies, and mocks for hardware-facing code, testing "right next to the hardware," and adding tests to legacy C. Read it before or while setting up Unity/CMock. |
| 🔑 | Book | Unit Testing Principles, Practices, and Patterns | Vladimir Khorikov | 2020 | [Link](https://www.manning.com/books/unit-testing) | Universal guidelines for judging whether a test is worth keeping, spotting test anti-patterns, and when mocks help or hurt (the classical vs. London schools). The best rubric for the "review AI-generated tests" practice above. |

---

## Suggested Order

**Core path (🔑):** *Python Testing with pytest* → *Unit Testing Principles, Practices, and Patterns* → *Test-Driven Development for Embedded C*

1. **Testing pyramid (concept)** — Understand the testing strategy landscape before writing any tests.
2. **Python Testing with pytest** — Learn the primary Python testing tool hands-on.
3. **Review AI-generated tests (practice)** — Start critically evaluating AI test output immediately. Make this a habit.
4. **Unit Testing Principles, Practices, and Patterns** — Get a rubric for what makes a test valuable; apply it to every AI-written test.
5. **Test-Driven Development for Embedded C** — Learn how to test hardware-facing C code with test doubles.
6. **Unity Test Framework + CMock** — Set up C testing for embedded projects.
7. **Test Driven Development (Kent Beck)** — Understand the TDD philosophy, even if you don't practice it dogmatically.
8. **Property-based testing (Hypothesis)** — Add this to your toolkit for finding edge cases automatically.
9. **Static analysis tools** — Set up mypy/pylint for Python, cppcheck/clang-tidy for C as automated quality gates.
10. **CI/CD pipelines** — Automate everything so tests run on every commit. For firmware on real boards, continue in [Section 13](../13-hil-testing-and-lab-automation/README.md) (simulation in CI, HIL rigs, instrument control).
11. **Working Effectively with Legacy Code** — Read when you're integrating AI output into existing codebases.
12. **Mutation testing** — Use to audit test suite quality when you want maximum confidence.

---

## 🛠️ Practice

1. **Audit AI-written tests** — Ask an agent to "write comprehensive pytest tests" for a small module you own, such as measurement statistics or a SCPI response parser.
   - Record line and branch coverage with pytest-cov.
   - Run mutmut and compute the mutation score.
   - Classify every surviving mutant: missing assertion, test coupled to the implementation, untested edge case, or equivalent mutant.
   - Rewrite the tests (fixtures, `parametrize`, `pytest.approx` with tolerances you can justify) until the mutation score rises substantially while coverage barely moves.

   Done when you have a before/after table and three named anti-patterns from the AI's tests, each added to your Section 03 review checklist. *(~4 h · Okken, Python Testing with pytest, on fixtures and parametrization; this section's "Review AI-generated tests"; pytest-cov; mutation testing)*
2. **Break a COBS codec with Hypothesis** — Have an agent write a COBS encoder/decoder, the byte-stuffing you'd put on a UART link. Write these properties:
   - `decode(encode(x)) == x`;
   - the encoding contains no `0x00` bytes;
   - `len(encode(x)) <= len(x) + len(x)//254 + 1`;
   - decoding arbitrary bytes either returns data or raises your defined error, and never does anything else.

   Generate inputs with `st.binary(max_size=2000)`, plus `@example`s of zero-free runs of 253, 254 and 255 bytes. Separately, add a `RuleBasedStateMachine` that checks a ring-buffer class against `collections.deque(maxlen=N)` as the model. Done when the suite finds and shrinks a real bug. If the code is clean, the suite must catch a 254-boundary bug that you plant. *(~3 h · Hypothesis docs on strategies, `@example` and stateful testing)*
3. **Off-target driver tests with Ceedling** — Run `ceedling new` to create a project for an I²C temperature-sensor driver. TMP117 is a good example: a 16-bit two's-complement result at 7.8125 m°C/LSB, and a device-ID register at 0x0F. Put `#include "mock_i2c.h"` in the test so CMock generates the bus mock from your HAL header. Test-drive the driver red → green → refactor, using Beck's *Fake It* first and then *Triangulate*. Cover these cases:
   - init writes the expected configuration;
   - a wrong device ID is rejected;
   - raw-to-°C conversion is exact at +25 °C, at −40 °C and for raw 0x8000;
   - an I²C NACK returns an error instead of hanging.

   Enable the gcov plugin. Done when `ceedling gcov:all` shows at least 90% line coverage on the driver, and deleting any single guard turns a test red. *(~4 h · Unity, CMock and Ceedling (ThrowTheSwitch); Grenning, Test-Driven Development for Embedded C; Beck, Test Driven Development: By Example; Feathers on link seams)*
4. **Characterize before you change** — Take an untested legacy script or C module: one of yours, or an AI-generated one from an earlier section. Before touching any logic:
   - pin its current behavior with characterization tests (golden files via `tmp_path`, captured output via `capsys`);
   - find a seam: an object seam in Python (inject the dependency), or a link seam in C (substitute a test double at link time).

   Only then make one intended behavior change. Done when the diff in test expectations is exactly that change and nothing else. *(~3 h · Feathers, Working Effectively with Legacy Code, on the seam model and characterization tests; Okken on built-in fixtures)*
5. **Static-analysis gate** — Run mypy (or pyright) and ruff/pylint on a Python repo. Run cppcheck plus clang-tidy on the C driver from exercise 3. Triage every finding as a bug, a risk or noise, and suppress the noise explicitly with a reason comment. Wire all four tools into a GitHub Actions job that fails on new findings. Done when a seeded type error and a seeded out-of-bounds array index each turn the pipeline red. *(~3 h · static analysis with mypy, pylint, cppcheck and clang-tidy; CI/CD pipelines)*

**🏗️ Mini-project — Bench HIL Rig:** Build a pytest-driven hardware-in-the-loop rig for your STM32 board:
- **Setup:** a session-scoped fixture flashes the firmware (`STM32_Programmer_CLI`, OpenOCD or pyOCD; OpenOCD is covered in Section 12) and opens the serial port. Tests drive the Section 02 command shell.
- **Stimulus and measurement:** bench instruments over PyVISA/SCPI (both listed in Section 13). A PSU sets the ADC input (current-limited, and kept below VDDA) and a DMM measures it. Without instruments, use a resistor divider.
- **I/O and timing:** a jumper loops a GPIO output back to an input. Timing assertions use a second timer's input capture or a USB logic analyzer.
- **Organization:** mark hardware tests `@pytest.mark.hil` and emit JUnit XML. Keep the Ceedling and Python unit suites running in CI without hardware.

Deliverable: `projects/software/05-hil-rig/` plus a photo of the setup. Success: `pytest -m hil` runs unattended from power-on in under 2 minutes, and a planted firmware bug (wrong ADC scaling, swapped GPIO) is caught and named in the report. Next, [Section 13](../13-hil-testing-and-lab-automation/README.md) turns this rig into shared CI infrastructure. *(~14 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Sketch the testing pyramid for a product with firmware, a Python host tool and a bench fixture. What lives at each level, and why does HIL sit near the top?
2. What does mutation testing measure that coverage doesn't? Describe a test with 100% line coverage that kills zero mutants.
3. Name four kinds of property you can test with Hypothesis, with one embedded-flavored example of each.
4. What is a "seam" in Feathers' sense, and which kind does CMock rely on?
5. In Beck's TDD, what are "Fake It" and "Triangulate"? When do you skip straight to "Obvious Implementation"?
6. An AI-generated test mocks the unit's own private helper and asserts it was called with specific arguments. What's wrong with that, and what should the test assert instead?
7. Twenty HIL tests each flake independently 0.25% of the time. Roughly what fraction of full runs fail spuriously, and how does that change the way people treat a red build?
8. Explain to a smart friend in three sentences why "all tests pass" isn't the same as "the code works".
