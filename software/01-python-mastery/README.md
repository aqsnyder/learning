# Python Mastery

> **Why this section matters:** Python is the lingua franca of AI, data science, and rapid prototyping. Mastering idiomatic Python means you can read ANY Python codebase — including AI-generated code — and immediately spot anti-patterns, performance issues, and bugs.

**Prerequisites:** Basic Python syntax.

---

## 🎯 Learning Objectives

After this section you can:
- Implement a custom sequence/numeric type through the data model (`__len__`, slicing `__getitem__`, `__iter__`, `__eq__`, arithmetic and reflected operators), and predict which special method Python calls for a given expression.
- Build generator pipelines that process captures larger than RAM in constant memory, and prove it with `tracemalloc`.
- Read how CPython implements `@contextmanager` and `functools.wraps`, then write decorators and context managers that preserve metadata and guarantee cleanup when exceptions occur.
- Use `Protocol`, `NewType`, `Literal`, `Enum` and `TypedDict` with mypy/pyright in strict mode, so that unit mix-ups and invalid modes fail type-checking.
- Set up a reproducible project with uv (lockfile), ruff and pytest, and explain what each `pyproject.toml` table does.

---

## Resources

| # | Type | Resource | Notes |
|---|------|----------|-------|
| 1 | 🔑 Book | *Fluent Python* (2nd ed) — Luciano Ramalho (2022) | THE Python mastery book. Understand the data model, generators, async, and metaprogramming |
| 2 | 🔑 Book | *Effective Python* (3rd ed) — Brett Slatkin (2024) | 125 specific ways to write better Python |
| 3 | 🔑 Book | *Robust Python* — Patrick Viafore (2021) | Type hints, boundaries, and disciplined design |
| 4 | 🔑 Book | [*Architecture Patterns with Python*](https://www.cosmicpython.com/) — Percival and Gregory | DDD, repository pattern, event-driven architecture in Python (free online) |
| 5 | Book | *Hypermodern Python Tooling* — Claudio Jolowicz (2024) | Modern project setup: uv, Hatch, Poetry, Nox, pytest, Ruff, mypy, pre-commit |
| 6 | 🔑 Docs | [Python Type Hints (`typing` module)](https://docs.python.org/3/library/typing.html) | Essential for reading modern Python |
| 7 | Tool | mypy / pyright | Static type checkers — catch bugs before running code |
| 8 | Tool | [uv](https://github.com/astral-sh/uv) | Modern Python package management |
| 9 | Tool | [ruff](https://github.com/astral-sh/ruff) | Fast linter and formatter |
| 10 | Website | [Real Python](https://realpython.com/) | High-quality Python tutorials |
| 11 | Docs | [What's New in Python](https://docs.python.org/3/whatsnew/index.html) (3.13 → 3.15) | Read the notes for every version you ship on. 3.13 (2024) added an experimental free-threaded (no-GIL) build and a basic JIT; 3.14 (2025) made free-threading officially supported (PEP 779) and annotations lazily evaluated (PEP 649/749); 3.15 (Oct 2026) adds explicit lazy imports (PEP 810) and a built-in sampling profiler (PEP 799). Pair with the [free-threading HOWTO](https://docs.python.org/3/howto/free-threading-python.html) before trusting C extensions under threads |

### Key Concepts

| Concept | Why It Matters |
|---------|---------------|
| Python data model (`__dunder__` methods) | How Python objects actually work |
| Generators, iterators, and lazy evaluation | Memory-efficient patterns |
| Decorators and context managers | Metaprogramming you'll see everywhere |

---

## Suggested Order

```
1. Effective Python (quick wins, immediately applicable)
2. Fluent Python (deep mastery of the language)
3. Robust Python (type hints and disciplined design)
4. Architecture Patterns with Python (scaling to real systems)
5. Hypermodern Python Tooling (polish your dev environment)
6. What's New in Python 3.13 → 3.15 (skim each release; re-read before upgrading a tool or test rig)
```

---

## 🛠️ Practice

1. **Reproducible project in an afternoon** — Convert one repo to uv:
   - `uv init`/`uv add`, a src layout and a committed `uv.lock`, run via `uv run pytest`;
   - ruff for lint and format, with a deliberate rule selection;
   - pre-commit hooks.

   Time a cold `uv sync` against your old `pip install -r requirements.txt`. Done when a fresh clone on another machine runs the tests with two commands and you can explain every table in `pyproject.toml`. *(~2 h · Hypermodern Python Tooling on environments, dependency management and linting; uv and ruff docs)*
2. **`Trace`: a data-model drill** — Implement `Trace` (samples + `t0` + `dt` + units) with support for:
   - `len()`, indexing and iteration;
   - slicing, where a step-k slice returns a `Trace` with `dt*k` and the correct `t0`;
   - `==`, `abs()`, `bool()` and an informative `repr`;
   - `+ - *` with scalars and with same-`dt` Traces, raising on mismatched `dt` or units.

   Done when a ~15-case pytest suite passes, `3 * t` works and `sum([t1, t2, t3])` works. Then explain why the last one needed `__radd__`. *(~3 h · Fluent Python ch. 1 "The Python Data Model", ch. 12 "Special Methods for Sequences", ch. 16 "Operator Overloading")*
3. **Constant-memory capture pipeline** — Generate a ~2 GB CSV of synthetic ADC samples (`timestamp, channel, counts`). Compute per-channel RMS over 1-second windows in two ways: list-based, and as a generator pipeline (`read → parse → window → reduce` with `itertools`). For 0.2, 1 and 2 GB inputs, measure runtime and peak memory with `tracemalloc.get_traced_memory()`. (Parsed Python rows take several times the file size in RAM, so run the list-based version only at the sizes your machine can hold.) Done when both outputs agree to floating-point tolerance and the generator version's peak memory stays flat as the input grows 10×. *(~3 h · Fluent Python ch. 17 "Iterators, Generators, and Classic Coroutines"; Effective Python's comprehensions-and-generators items)*
4. **Read `contextlib`, then write your own** — Read `_GeneratorContextManager` in CPython's `Lib/contextlib.py` and `update_wrapper` in `Lib/functools.py`. Write a 10-line annotation covering two things: how an exception raised inside a `with` block gets thrown into the generator, and what happens if the generator swallows it. Then write:
   - (a) `@retry(times=3, on=(TimeoutError,), backoff_s=0.1)`, preserving `__name__`, `__doc__`, `__wrapped__` and `inspect.signature`;
   - (b) an `instrument_session()` context manager (via `@contextmanager`) that always sends "output off".

   Test (b) with a fake instrument that records commands, and with a test that raises mid-block. *(~3 h · Fluent Python ch. 9 "Decorators and Closures" and ch. 18 "with, match, and else Blocks"; Real Python's decorator and context-manager tutorials)*
5. **Type-tighten a real script** — Take one of your untyped tooling scripts (≥ 300 lines). Add annotations incrementally, running `mypy --strict` and pyright in strict mode (`typeCheckingMode = "strict"`) as you go, and log every finding as a real bug, a latent bug or noise. Introduce `NewType` for `Volts`/`Amps`, `Literal["DC", "AC"]`, an `Enum` for instrument modes, a `TypedDict` for config and a `Protocol` for the instrument. Done when both checkers are clean and passing amps where volts are expected fails type-checking. *(~4 h · Robust Python on annotating code and defining your own types; Python `typing` docs; mypy/pyright)*

**🏗️ Mini-project — Typed Instrument Library:** Build a uv-managed package (src layout, lockfile, ruff, `mypy --strict`, pytest) that wraps a bench PSU and DMM over PyVISA (listed in Section 13). It should have:
- `Protocol`-based instrument interfaces and typed units;
- context-managed sessions that force a safe state on exit;
- a generator-based sweep API (`for point in sweep(psu, dmm, volts=...)`);
- a simulated backend via pyvisa-sim (`pyvisa.ResourceManager("bench.yaml@sim")`), so the test suite needs no hardware.

Use the repository/adapter idea from *Architecture Patterns with Python* (ch. 2 "Repository Pattern", ch. 3 "A Brief Interlude: On Coupling and Abstractions") for the instrument boundary. Deliverable: `projects/software/01-instrument-lib/`. Success: `uv run pytest`, `uv run mypy --strict src` and `uv run ruff check` all pass on a clean clone with no instruments attached, and the same sweep script runs unchanged on real instruments. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. For `a + b`, what does Python try first? What makes it fall back, and what does it call next?
2. Why does `sum([t1, t2, t3])` fail on a custom type that only implements `__add__`?
3. A consumer stops iterating a generator early. When does the generator's `finally` block run, and what triggers it?
4. Misconception check: "`@functools.wraps` makes a decorator fully transparent." What does it copy or set, and what does it leave unchanged?
5. What happens with `def log(msg, buf=[])` across repeated calls, and why? What's the idiomatic fix?
6. When would you choose a `typing.Protocol` over an ABC for an instrument interface, and when would you do the reverse?
7. What does a committed `uv.lock` guarantee that a `requirements.txt` with `>=` pins does not?
8. Explain to a smart friend in three sentences how generators let you process a file bigger than your RAM.
