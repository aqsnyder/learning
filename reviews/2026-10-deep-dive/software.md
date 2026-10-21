# Software Engineering — Review

> **Deep-dive review, October 2026** · curriculum: [`software/`](../../software/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict
The curriculum has the right spine for its intended learner: Python plus embedded C, reading and reviewing code over typing it, architecture, and human-in-the-loop AI. Its core picks are sound: *Fluent Python*, *Making Embedded Systems*, *Refactoring*, *A Philosophy of Software Design*, and Samek's videos.

It fell short in three ways:
- **It was stale.** Five flagship books were an edition behind, K&R was billed as "THE definitive C reference", and the "future-facing" Section 09 had nothing from 2024–2026.
- **It was thin exactly where an embedded engineer works every day.** Debugging, CMake, bootloaders, ADRs and documentation were "Concept" rows with no source. There was no Cortex-M reference, no embedded TDD book, no networking, and no CERT C.
- **Its wiring was broken.** 12 internal links pointed at directories that never existed, and so did the agent skill's section map.

It also leans toward web/SaaS-backend and interview-prep material (System Design Interview, Terraform, *The Web Application Hacker's Handbook* as 🔑). None of that matters much to someone who builds firmware and test instruments.

**Grade as found: C+** (roughly B after this pass). The single most important improvement is to re-center on the bench. The two proposed sections were approved and now exist as Section 12 (firmware toolchain, debug and observability) and Section 13 (hardware-in-the-loop testing and lab automation). What remains is for the learner to take them in their marked positions and run Section 09 as a parallel, evidence-based track from day one.

## Scorecard
Scores are for the curriculum **as found**, before my edits.

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 — CS Foundations | 2 | 4 | 3 | 3 | 3 | C | Names Teach Yourself CS as the roadmap but leaves out its systems, OS and algorithms books, the parts an embedded C engineer needs most |
| 01 — Python Mastery | 3 | 4 | 3 | 4 | 4 | B− | Excellent book core; missing 3.13–3.15 changes, concurrency, profiling, and Python on the bench |
| 02 — Embedded C Mastery | 3 | 3 | 2 | 4 | 4 | C+ | K&R presented as the definitive reference; nothing after C89; no MISRA or CERT |
| 03 — Reading & Reviewing Code | 3 | 4 | 3 | 4 | 4 | B− | Right canon for the curriculum's core skill; lacks the cognition of reading and history-based analysis |
| 04 — Architecture & Design Patterns | 3 | 3 | 2 | 3 | 2 | C | Web/distributed-centric and 🔑-heavy, with broken links and two flagship books an edition behind |
| 05 — Testing & Quality | 3 | 3 | 3 | 4 | 4 | C+ | Lists Unity/CMock but not the embedded TDD book; no hardware-in-the-loop or simulation; broken links |
| 06 — Systems & Infrastructure | 2 | 3 | 3 | 3 | 2 | C− | No networking at all; duplicates 04, 10 and 11; SaaS-backend emphasis |
| 07 — Embedded Systems & RTOS | 3 | 3 | 3 | 4 | 4 | C+ | Right topics, but the debugging, CMake and bootloader rows had no sources, and there was no Cortex-M or FreeRTOS text |
| 08 — Security & Reliability | 2 | 3 | 2 | 3 | 2 | C− | Web-pentest emphasis (🔑 on a 2011 book); no CERT C, embedded security, supply chain, or CRA |
| 09 — Agentic AI Workflows | 2 | 2 | 1 | 2 | 3 | D | One real source, no 2024–2026 material, 5 broken links, overstated claims, gated behind 6 sections |
| 10 — Version Control & Collaboration | 3 | 5 | 3 | 3 | 4 | B− | Accurate basics; no commit convention, hook tool or worktrees; placed late for a day-one skill |
| 11 — Professional Practice | 3 | 4 | 3 | 4 | 4 | B− | Credible staff-engineer canon; ADR, documentation and estimation rows had no sources |
| 12 — Firmware Toolchain, Debug & Observability (new) | — | — | — | — | — | — | Created in this pass from Proposal A; not self-scored |
| 13 — HIL Testing & Lab Automation (new) | — | — | — | — | — | — | Created in this pass from Proposal B; not self-scored |

## Section-by-section

### 00 — Computer Science Foundations
- **Strengths:**
  - Teach Yourself CS as the roadmap.
  - MIT 6.006 (free, Spring 2020 offering).
  - Two on-ramps (CS50, Grokking) for different learning styles.
- **Problems:**
  - ✔ Teach Yourself CS was typed "Book (Free)"; it is a guide.
  - ✔ Grokking was listed with no edition (books/ said 2016). The 2nd edition came out in 2024.
  - ✔ CS50 was typed "Video" and called the "best intro CS course ever made"; changed to Course with a neutral description.
  - ✔ No pointer to the math curriculum for discrete math. I added a cross-link to math/00 (Epp, Bazett) instead of duplicating it.
  - ✔ "Use Teach Yourself CS to guide everything", yet the section omitted that guide's architecture, OS and algorithms picks. All three are now added.
  - ✱ The table schema differs from Sections 04–11.
  - ✱ SICP (Scheme) is low-yield for this learner; keep it optional.
- **Missing:**
  - Number representation and floating point
  - Memory hierarchy and caches
  - Concurrency fundamentals
  - Networking basics (now in 06)
  - Discrete math (now cross-referenced)
- **Added:**
  - Computer Systems: A Programmer's Perspective (3rd ed) — Randal Bryant & David O'Hallaron — 2015
  - Operating Systems: Three Easy Pieces — Remzi & Andrea Arpaci-Dusseau — v1.10, 2023
  - The Algorithm Design Manual (3rd ed) — Steven Skiena — 2020

### 01 — Python Mastery
- **Strengths:**
  - Fluent Python 2e, Effective Python 3e, Robust Python and Cosmic Python make a top-tier core.
  - Modern tooling (uv, ruff, type checkers) is present.
- **Problems:**
  - ✔ *Effective Python* 3e was described as "90 specific ways". That is the 2nd edition's subtitle; the 3rd is "125 Specific Ways" (Nov 2024).
  - ✔ *Hypermodern Python Tooling* had no year and an inaccurate tool list (now 2024; uv, Hatch, Poetry, Nox, pytest, Ruff, mypy, pre-commit).
  - ✔ Nothing on Python 3.13–3.15. 3.15 shipped on 2026-10-09: free-threading became officially supported in 3.14, plus the JIT, lazy annotations, lazy imports and a sampling profiler.
  - ✱ The mypy/pyright row has no links.
  - ✱ Real Python is a generic website entry.
- **Missing:**
  - Concurrency models (asyncio vs threads vs processes; the free-threaded build)
  - Packaging and distribution (pyproject, wheels, publishing an open-source host package)
  - Profiling (cProfile, sampling profilers)
  - Python on the bench (pyserial, PyVISA, numpy/pandas for measurement data)
  - CLI design
- **Added:**
  - What's New in Python (3.13 → 3.15), with the free-threading HOWTO — Python Software Foundation docs — 2024–2026

### 02 — Embedded C Mastery
- **Strengths:**
  - *Making Embedded Systems* 2e, BARR-C, Samek's videos and Embedded Artistry form a good practical core.
- **Problems:**
  - ✔ K&R was called "THE definitive C reference", but it covers ANSI C (C89) only.
  - ✔ No modern C text existed for C11/C17/C23 (C23 = ISO/IEC 9899:2024).
  - ✔ No MISRA, although the update skill tells agents to track it.
  - ✱ The FastBit/Udemy entry has no link and no specific course.
  - ✱ The Beningo book has no year (not verified; left as is).
- **Missing:**
  - C11 atomics and the memory model (`volatile` is not atomic)
  - Undefined behavior and host-side sanitizers (UBSan/ASan)
  - Warnings-as-errors policy
  - Fixed-point arithmetic
  - Reading CMSIS and vendor HAL code
- **Added:**
  - Modern C (3rd ed) — Jens Gustedt — 2025 (free CC-licensed edition linked)
  - Effective C (2nd ed) — Robert C. Seacord — 2024
  - MISRA C:2025 — MISRA — 2025

### 03 — Reading and Reviewing Code
- **Strengths:**
  - The right canon for the curriculum's thesis: Spinellis, Fowler, Ousterhout and Google's guide.
  - The AI-output review practice is explicit.
- **Problems:**
  - ✔ APoSD was listed without edition (2nd ed, 2021).
  - ✔ Google's code review guidelines were typed "Video"; they are a written guide.
  - ✱ The examples in *Code Reading* (2003) are dated, though the book is still unique.
- **Missing:**
  - How reading works cognitively
  - Using git history to target review
  - Navigation tooling (LSP, call graphs)
  - Using agents to explore unfamiliar code, and checking their explanations
  - A firmware-specific review checklist (ISR safety, `volatile`/atomics, timing, resource ownership)
- **Added:**
  - The Programmer's Brain — Felienne Hermans — 2021
  - Your Code as a Crime Scene (2nd ed) — Adam Tornhill — 2024

### 04 — Architecture and Design Patterns
- **Strengths:**
  - Strong general architecture canon: Fundamentals of Software Architecture (FoSA), *The Hard Parts*, Ousterhout, GoF/Head First, DDD, *Release It!* (in 06).
- **Problems:**
  - ✔ Broken prerequisite links (`01-python-fundamentals`, `03-git-and-collaboration`).
  - ✔ FoSA was listed as 2020; the 2nd edition came out in March 2025.
  - ✔ APoSD was listed as 2018; the 2nd edition is 2021.
  - ✔ DDIA was listed as 2017; the 2nd edition (Kleppmann & Chris Riccomini) came out in March 2026.
  - ✔ The System Design Interview channel had no author and read as active. It is Mikhail Smarshchok's channel: 7 videos, inactive.
  - ✱ 7 of 14 rows are 🔑, so there is no visible core path.
  - ✱ Distributed web systems dominate. There is nothing on embedded or event-driven architecture, or on firmware↔host protocol design.
- **Missing:**
  - Embedded architecture (active objects, HAL/BSP layering; partly in 07 via Samek)
  - Device↔host protocol and API design (framing, versioning, compatibility)
  - Quality attributes and fitness functions
  - Architecture communication (C4 now added; ADRs live in 11)
- **Added:**
  - The C4 model — Simon Brown — living site (CC BY 4.0)

### 05 — Testing and Quality
- **Strengths:**
  - The right emphasis on judging AI-generated tests.
  - Unity/CMock/Ceedling, Hypothesis and mutation testing are all named.
- **Problems:**
  - ✔ Broken prerequisite links (`01-python-fundamentals`, `02-c-fundamentals`).
  - ✔ Embedded C testing was listed as tools only, with no book (Grenning added).
  - ✱ "Mutation testing… the ultimate test-quality metric" is overstated.
  - ✱ The static-analysis row names pylint while the curriculum promotes ruff.
  - ✱ The concept rows (mutation testing, static analysis, CI/CD) have no sources.
- **Missing:**
  - Hardware-in-the-loop testing and simulation (Renode/QEMU); see Proposal B
  - On-target coverage
  - Fuzzing for protocol parsers
  - Contract tests between firmware and host software
- **Added:**
  - Test-Driven Development for Embedded C — James W. Grenning — 2011
  - Unit Testing Principles, Practices, and Patterns — Vladimir Khorikov — 2020

### 06 — Systems Design and Infrastructure
- **Strengths:**
  - DDIA and *Release It!* are excellent.
  - Observability is at least named.
- **Problems:**
  - ✔ DDIA updated to the 2nd edition (2026).
  - ✔ No networking content at all (Beej's Guide added).
  - ✱ *The Software Engineer's Guidebook* is a career book; it is misplaced here and duplicated in 11.
  - ✱ "Git advanced workflows" duplicates Section 10.
  - ✱ Terraform/Ansible and the *System Design Interview* books are low-value for an embedded/instrument founder.
  - ✱ The databases, queues and observability rows have no sources.
- **Missing:**
  - Serialization and message framing (protobuf/CBOR/COBS)
  - USB device classes (CDC, USBTMC)
  - Storage for measurement data (SQLite/HDF5/Parquet)
  - Device-fleet telemetry
- **Added:**
  - Beej's Guide to Network Programming — Brian "Beej Jorgensen" Hall — v3.3.2, 2026

### 07 — Embedded Systems and RTOS
- **Strengths:**
  - The right concept list: scheduling, priority inversion, NVIC/DMA, bootloaders/OTA, debugging.
  - The best educators: White, Samek, Embedded Artistry, Interrupt.
- **Problems:**
  - ✔ Broken prerequisite link (`02-c-fundamentals`, labelled "C Fundamentals").
  - ✔ "The Samek approach" had no book (PSiCC2 added; free PDF).
  - ✔ FreeRTOS had no learning text (the official book added).
  - ✔ The debugging, startup and linker rows had no sources (HardFault article and Zero-to-main series added).
  - ✱ The CMake, GDB and bootloader rows still lack sources; see Proposal A.
- **Missing:**
  - A Cortex-M architecture reference (added)
  - MPU and stack-overflow protection
  - Low-power design
  - Watchdogs
  - Timing analysis
  - TrustZone-M / Trusted Firmware-M
  - Zephyr devicetree and Kconfig
  - SWO/RTT tracing
- **Added:**
  - Definitive Guide to Arm Cortex-M23 and Cortex-M33 Processors — Joseph Yiu — 2020
  - Mastering the FreeRTOS Real Time Kernel: A Hands-On Tutorial Guide — Richard Barry & FreeRTOS team — GitHub edition 2023 (maintained through 2026)
  - Practical UML Statecharts in C/C++ (2nd ed) — Miro Samek — 2008
  - How to debug a HardFault on an ARM Cortex-M MCU — Chris Coleman (Memfault) — 2019
  - From Zero to main(): Bare metal C (series) — François Baldassari (Memfault) — 2019
  - The Embedded Rust Book — Rust Embedded WG resources team — living

### 08 — Security and Reliability Engineering
- **Strengths:**
  - Security review of AI output is called out.
  - Bandit and Semgrep.
  - The SRE book and blameless post-mortems.
- **Problems:**
  - ✔ Broken prerequisite links (`01-foundations`, `02-core-programming`).
  - ✔ *The Web Application Hacker's Handbook* (2011) was 🔑. Its lead author's company built the free Web Security Academy instead of a 3rd edition; I removed the 🔑, dated the entry and linked the Academy.
  - ✔ The OWASP Top 10 entry didn't reflect the 2025 edition, which added Software Supply Chain Failures at A03.
  - ✔ "Secure C programming" had no source (SEI CERT C added).
  - ✱ The section is web-app security first, but the intended learner ships firmware and host tools.
- **Missing:**
  - Embedded security (secure boot, key storage, debug-port lockdown/readout protection, TrustZone)
  - Software supply chain (SBOM, pinning, provenance)
  - Product-security regulation (CRA added)
  - Fuzzing
  - Agent and prompt-injection security (covered in 09)
- **Added:**
  - SEI CERT C Coding Standard — CMU SEI — living wiki (2016 edition PDF)
  - We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs — Spracklen et al. — 2025 (USENIX Security; arXiv 2024)
  - EU Cyber Resilience Act (overview) — European Commission — 2024 (reporting duties since 11 Sep 2026)
  - Threat Modeling Manifesto — Braiterman, Shostack et al. — undated page

### 09 — Agentic AI Development Workflows
- **Strengths:**
  - Good instincts: the human-in-the-loop model, tests as spec, context files, commit hygiene, and "when not to use AI".
- **Problems:**
  - ✔ Five broken prerequisite links (`01-foundations` … `05-systems`); remapped, and 03 and 06 added.
  - ✔ The 🔖 marker isn't in the legend; changed to 🔑.
  - ✔ "The better your prompt, the less you review" conflicts with the evidence; corrected to "less rework, not less review".
  - ✔ "If the AI can't pass your tests, the prompt was unclear" was oversimplified. Corrected to check the spec, the tests and the task size, and to watch for weakened or special-cased tests.
  - ✔ Zero 2024–2026 sources (9 added).
  - ✱ "Cursor/Copilot best practices" is a placeholder row with no author or link.
  - ✱ The section is gated behind 01–06, although the intended learner uses agents daily. I added a note to run it in parallel.
  - ✱ 12 of the 13 original rows had no source: 10 "Concept" rows, the capstone practice row, and the Cursor/Copilot placeholder.
- **Missing:**
  - How to measure your own agent workflow (cycle time, rework, escaped defects)
  - Cost and latency trade-offs
  - Permissions and sandboxing
  - Giving agents a verifiable check when the system under test is a board (ties to Proposal B)
- **Added:**
  - Building effective agents — Erik Schluntz & Barry Zhang (Anthropic) — 2024
  - Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity, plus METR's Feb 2026 design update — Becker, Rush, Barnes, Rein — 2025/2026
  - State of AI-assisted Software Development 2025 — Google Cloud DORA — 2025
  - Effective context engineering for AI agents — Anthropic Applied AI team — 2025
  - Claude Code best practices — Anthropic — living docs
  - AGENTS.md — Codex/Amp/Jules/Cursor/Factory, now Agentic AI Foundation — 2025
  - Model Context Protocol — Anthropic (originator), open standard — 2024 (spec rev. 2026-07-28 current)
  - The lethal trifecta for AI agents — Simon Willison — 2025
  - Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl — Birgitta Böckeler — 2025

  Nine additions is above the usual 0–5. That is deliberate: this is the fastest-moving section and it had effectively one source. Each addition covers a distinct need: agent architecture, two pieces of evidence, context, daily practice, two standards, security, and spec-driven workflows.

### 10 — Version Control and Collaboration
- **Strengths:**
  - Pro Git plus Learn Git Branching is the right pair.
  - AI-generated PR discipline and bisect are covered.
- **Problems:**
  - ✱ Placed 10th although it is a day-one skill; make it early or parallel.
  - ✱ The "GitHub Actions / CI-CD" row has no link.
- **Missing:**
  - Commit conventions (added)
  - Concrete hook tooling (added)
  - Worktrees for parallel agents (added)
  - Signed commits and tags
  - Semantic versioning and changelogs
  - Reproducible firmware builds and release artifacts
- **Added:**
  - How to Write a Git Commit Message — Chris Beams — 2014
  - pre-commit — Anthony Sottile et al. — tool
  - git worktree (docs) — Git project — docs

### 11 — Professional Practice and Technical Leadership
- **Strengths:**
  - A credible staff-engineer canon: Orosz, Larson, Fournier.
  - "Leading in the AI era" is a good row.
- **Problems:**
  - ✔ The ADR and documentation rows had no sources (Nygard and Diátaxis added).
  - ✱ "Estimating and planning" still has no source. I didn't add one because the search budget ran out before I could verify McConnell's or Brooks's book.
  - ✱ The framing is "IC inside big tech". There is little for a founder or CTO of a small hardware company, or for stewarding an open-source host-software project.
- **Missing:**
  - An estimation text
  - Open-source stewardship (license choice, CONTRIBUTING, governance)
  - Small-team engineering management
- **Added:**
  - Documenting Architecture Decisions — Michael Nygard — 2011
  - Diátaxis — Daniele Procida — living framework

### 12 — Firmware Toolchain, Debug, and Observability (new)
- **Status:** ✔ Created at `software/12-firmware-toolchain-debug-and-observability/README.md` (approved Proposal A).
  - Recommended position: after 07's reading, and before 07's mini-project, which uses its build and tracing setup.
  - Pointers added in 07 (Suggested Order steps 9–11 and the mini-project), the README learning path, PROGRESS and the SKILL.md mapping.
- **Contents:**
  - 5 verified resources and 5 concept rows. Each concept row points to its source in Section 07 or 09, so nothing is duplicated.
  - Learning objectives, 5 practice exercises, a mini-project ("Agent-Ready Firmware Harness") and 8 Check Yourself questions.
- **Design choices:**
  - *From Zero to main()* and the HardFault article stay in 07, because 07's merged objectives and fault-forensics exercise depend on them. Section 12 cross-references them instead of moving them.
  - The exercises extend what earlier sections already ask for rather than repeating it: 02's "Where does it live?", 07's fault forensics and data logger, and 08's update threat model.
- **Added:**
  - Professional CMake: A Practical Guide (22nd ed) — Craig Scott — current edition (covers CMake 4.2)
  - OpenOCD — OpenOCD project — 0.12.0, 2023
  - SEGGER RTT — SEGGER — docs
  - sigrok / PulseView — sigrok project — tool
  - MCUboot — MCUboot project — docs (v2.4.0)

### 13 — Hardware-in-the-Loop Testing and Lab Automation (new)
- **Status:** ✔ Created at `software/13-hil-testing-and-lab-automation/README.md` (approved Proposal B).
  - Recommended position: after 05 for the instrument-control half; the simulation and CI half goes right after 12.
  - Pointers added in 05 (Suggested Order step 10 and the Bench HIL Rig mini-project), the README learning path, PROGRESS and the SKILL.md mapping.
- **Contents:**
  - 5 verified resources and 5 concept rows.
  - Learning objectives, 5 practice exercises, a mini-project ("Hardware CI Pipeline") and 8 Check Yourself questions.
- **Design choices:** it builds on the merged mini-projects rather than duplicating them.
  - 01's Typed Instrument Library is hardened with error-queue discipline and record/replay.
  - 05's Bench HIL Rig becomes shared CI infrastructure: labgrid remote access, locking, flake tracking.
  - 04's Lab-Automation Walking Skeleton is listed as helpful background.
  - Grenning stays in 05 and is reached through the Section 05 prerequisite.
- **Added:**
  - PyVISA — PyVISA developers — docs
  - SCPI (Standard Commands for Programmable Instrumentation, IVI's wording) — IVI Foundation — page
  - PyMeasure — PyMeasure developers — docs
  - labgrid — Pengutronix and contributors — docs
  - Renode — Antmicro — 1.17.0, 2026

### books/
- **Problems:**
  - ✔ Stale data in 5 rows: APoSD 2018 → 2e 2021, FoSA 2020 → 2e 2025, DDIA 2017 → 2e 2026 (with Riccomini), Grokking 2016 → 2e 2024, Effective Python "90" → "125".
  - ✔ "THE C reference" on K&R.
  - ✱ The header claims the list is "ordered from foundational to advanced"; it isn't.
  - ✱ About half the list is 🔑.
- **Added:**
  - CS:APP 3e
  - Modern C 3e
  - Test-Driven Development for Embedded C
  - Definitive Guide to Cortex-M23/M33

  That brings the list to 24 titles; the README count is updated.

### courses/
- **Problems:**
  - ✔ The System Design Interview source was blank and the channel is inactive.
  - ✱ The file mixes blogs and newsletters (Embedded Artistry, Interrupt, Pragmatic Engineer, Simon Willison) that duplicate blogs-and-references.
  - ✱ No firmware courses beyond Samek.
  - ✱ "Source" is blank for ArjanCodes and Talk Python.
- **Added:** nothing needed.

### blogs-and-references/
- **Problems:**
  - ✔ `cursor.sh` now redirects to `cursor.com`.
  - ✔ "Antigravity (Google) — Your current AI development environment" was a stale, personal note with no link. Now links antigravity.google; Google launched it Nov 2025.
  - ✱ No embedded tooling links (OpenOCD, SEGGER, sigrok); see Proposal A.
- **Added:**
  - Claude Code docs
  - Model Context Protocol
  - AGENTS.md

  These are tool links that mirror Section 09.

### PROGRESS.md
- **Problems:**
  - ✔ 17 section items had no checkbox: SICP, Real Python, Beningo blog, FastBit, static analysis as a reading aid, Head First DP, *Pragmatic Programmer*, DDD, pytest-cov, mutation testing, IaC, *Release It!*, CMake for embedded, Cursor/Copilot row, monorepos, mentoring, *The Manager's Path*. All added.
  - ✔ Edition labels updated.
  - ✱ "Books (supplementary)" double-tracks books that already sit under their sections.
  - ✱ APoSD is tracked twice (03, 04), and DDIA twice (04, 06).
- **Added:** 37 checkboxes for new resources, plus 17 for previously untracked items.

### README.md
- **Problems:**
  - ✔ Book count changed from 20 to 24.
  - ✱ "Key Resources" lists K&R with no C89 caveat; *Modern C* would be the modern pick.
  - ✱ The learning path is strictly linear. 09 (agents) and 10 (git) should be parallel tracks.
  - ✱ "AI agents write most of the code" is a forecast. The evidence (METR, and DORA's "AI amplifies") supports framing AI as an amplifier that needs measurement.

## Corrections made
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| 00-cs-foundations/README.md:13 | Teach Yourself CS typed "Book (Free)" | "Guide (Free)" | https://teachyourselfcs.com/ |
| 00-cs-foundations/README.md:15 | *Grokking Algorithms* (no edition) | (2nd ed) … (2024) | https://www.manning.com/books/grokking-algorithms-second-edition |
| 00-cs-foundations/README.md:16 | CS50 typed "Video", "Best intro CS course ever made" | "Course", neutral description | https://cs50.harvard.edu/ |
| 01-python-mastery/README.md:14 | Effective Python 3e "90 specific ways" | "125 specific ways" | https://effectivepython.com/ |
| 01-python-mastery/README.md:17 | Hypermodern Python Tooling (no year), "uv, pytest, mypy" | (2024), full tool list | https://www.oreilly.com/library/view/hypermodern-python-tooling/9781098139575/ |
| 02-embedded-c-mastery/README.md:13 | K&R "THE definitive C reference" | Classic; covers C89 only, pair with a modern text | https://www.cppreference.com/w/c/23.html |
| 03-reading-and-reviewing-code/README.md:16 | APoSD (no edition) | (2nd ed) (2021) | https://www.i-programmer.info/book-watch-archive/14822-a-philosophy-of-software-design-2nd-ed-yaknyam-press-.html |
| 03-reading-and-reviewing-code/README.md:17 | Google CR guidelines typed "Video" | "Guide" | https://google.github.io/eng-practices/review/ |
| 04-architecture-and-design-patterns/README.md:11 | `../../software/01-python-fundamentals/…`, `../../software/03-git-and-collaboration/…` | `../01-python-mastery/…`, `../03-reading-and-reviewing-code/…` | repo tree |
| 04-architecture-and-design-patterns/README.md:19 | FoSA, 2020 | FoSA (2nd ed), 2025 | https://oreilly.com/library/view/fundamentals-of-software/9781098175504 |
| 04-architecture-and-design-patterns/README.md:22 | APoSD, 2018 | APoSD (2nd ed), 2021 | (as above) |
| 04-architecture-and-design-patterns/README.md:25 | DDIA, Kleppmann, 2017 | DDIA (2nd ed), Kleppmann & Riccomini, 2026 | https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html |
| 04-architecture-and-design-patterns/README.md:27 | SDI channel, author "—", described as live | Mikhail Smarshchok; 7 videos, inactive | https://developereducators.com/channel/systemdesigninterview/ |
| 05-testing-and-quality/README.md:11 | `../../software/01-python-fundamentals/…`, `../../software/02-c-fundamentals/…` | `../01-python-mastery/…`, `../02-embedded-c-mastery/…` | repo tree |
| 06-systems-and-infrastructure/README.md:19 | DDIA, Kleppmann, 2017 | DDIA (2nd ed), Kleppmann & Riccomini, 2026 | (as above) |
| 07-embedded-systems-and-rtos/README.md:11 | "Section 02 — C Fundamentals" → `../../software/02-c-fundamentals/…` | "Embedded C Mastery" → `../02-embedded-c-mastery/…` | repo tree |
| 08-security-and-reliability/README.md:11–12 | `../01-foundations/…`, `../02-core-programming/…` | `../01-python-mastery/…`, `../02-embedded-c-mastery/…` | repo tree |
| 08-security-and-reliability/README.md:20 | OWASP Top 10 (no edition note) | Notes 2025 edition: A03 Supply Chain, A10 Exceptional Conditions | https://owasp.org/Top10/2025/ |
| 08-security-and-reliability/README.md:21 | WAHH 🔑, undated | Not 🔑; "(2nd ed, 2011)"; dated note and Web Security Academy link | https://portswigger.net/web-security/web-application-hackers-handbook |
| 09-agentic-ai-workflows/README.md:11–16 | 5 links to nonexistent `01-foundations`…`05-systems` | 6 links to real 01–06 directories | repo tree |
| 09-agentic-ai-workflows/README.md:31 | "The better your prompt, the less you review." | "Better prompts and context mean less rework, not less review." | https://arxiv.org/abs/2507.09089 |
| 09-agentic-ai-workflows/README.md:34 | 🔖🤖 (not in legend) | 🔑🤖 | README legend |
| 09-agentic-ai-workflows/README.md:36 | "If the AI can't pass your tests, the prompt was unclear." | Check spec, tests and task size; watch for weakened or special-cased tests | https://code.claude.com/docs/en/best-practices |
| books/README.md:9 | K&R "THE C reference" | "The classic C text; covers C89 only" | (as K&R above) |
| books/README.md:11 | Effective Python "90 actionable tips" | "125" | https://effectivepython.com/ |
| books/README.md:15 | APoSD 2018 | (2nd ed) 2021 | (as above) |
| books/README.md:16 | FoSA 2020 | (2nd ed) 2025 | (as above) |
| books/README.md:18 | DDIA, Kleppmann, 2017 | (2nd ed), Kleppmann & Riccomini, 2026 | (as above) |
| books/README.md:26 | Grokking Algorithms, 2016 | (2nd ed), 2024 | (as above) |
| courses/README.md:12 | SDI: source "—", "Architecture walkthroughs" | Mikhail Smarshchok; "channel no longer active" | (as above) |
| blogs-and-references/README.md:75 | Cursor → cursor.sh | cursor.com (cursor.sh 302-redirects) | https://cursor.com/ |
| blogs-and-references/README.md:76 | Antigravity: "Your current AI development environment" (no link) | antigravity.google | https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/ |
| README.md:50 | "(20 titles)" | "(24 titles)" | books/README.md |
| .agents/skills/update-curriculum/SKILL.md:90–105 | Section Mapping to `00-cs-fundamentals/`, `01-foundations/`, `03-architecture/`, `07-performance/`… | Real directory names; performance mapped to 01/07; PROGRESS heading rule added | repo tree |
| PROGRESS.md (Sections 00, 03, 04, 06, Books) | Grokking/APoSD/FoSA/DDIA without edition | Edition labels updated; 17 untracked section items added | — |

Totals:
- **Broken internal links fixed:** 12 link targets across 5 files. All 38 relative links in the curriculum now resolve, including the cross-link to math/00 and the Section 12/13 cross-references.
- **Added on top of the 37 new section resources:**
  - The Python 3.13 → 3.15 facts (3.15.0 released 2026-10-09)
  - Minor years (Robust Python 2021, Expert C 1994)
- **Second pass (approved proposals):** 2 new sections, 10 newly added verified resources plus 10 concept rows, and 26 PROGRESS lines.
- **Totals across both passes:** 48 verified resources added, and 80 PROGRESS lines added (37 new items + 17 previously untracked + 26 for Sections 12–13).

## Proposed new sections (not created)

**Status update:** both proposals were approved and created in a second pass as Sections 12 and 13. They are appended so nothing is renumbered. Below is the original proposal text, annotated with what changed.

### A. Firmware Toolchain, Debug & Observability
- **Status:** ✔ Created → `software/12-firmware-toolchain-debug-and-observability/README.md`.
  - Appended as 12; the README learning path says "take after 07", and the section itself says before 07's mini-project.
  - Change from the proposal: *From Zero to main()* and the HardFault article stayed in 07 (07's merged practice depends on them) and are cross-referenced from 12 rather than moved.
- **Position (as proposed):** immediately after 07.
- **Why:**
  - Section 07 names these skills but only as source-less rows: CMake, GDB, debugging, bootloaders.
  - They are the daily mechanics of Cortex-M33 work.
  - They are where coding agents are weakest: an agent can't see a bus fault, a mis-linked section or a stalled DMA. That makes human debugging skill the bottleneck in an agent-heavy workflow.
  - No other curriculum covers them: pcb stops at the board.
- **Outline:**
  1. Cross toolchains (arm-none-eabi GCC/Clang), CMake toolchain files and presets, reproducible builds.
  2. Startup code, linker scripts, map files, memory budgets.
  3. Debug probes and servers (ST-LINK, J-Link, CMSIS-DAP; OpenOCD/pyOCD + GDB; SVD).
  4. Tracing: SWO/ITM, SEGGER RTT, RTOS-aware tracing.
  5. Fault analysis: HardFault decoding, stack-overflow detection, MPU guard regions, asserts.
  6. Logic analyzers and protocol decoders (sigrok/PulseView).
  7. Bootloaders and secure update (MCUboot, image signing, TrustZone).
  8. Field observability: coredumps, reboot reasons, metrics.
- **Resources (all verified):**
  - *Professional CMake: A Practical Guide* (22nd ed, covers CMake 4.2) — Craig Scott (CMake co-maintainer) — https://crascit.com/professional-cmake/ (Ch. 24 "Toolchains And Cross Compiling")
  - OpenOCD — Open On-Chip Debugger (0.12.0, Mar 2023; GDB server, SWD/JTAG, STM32U5 flash support) — https://openocd.org/
  - SEGGER RTT (Real Time Transfer) — https://kb.segger.com/RTT
  - sigrok / PulseView (GPL; logic analyzers, scopes, Python protocol decoders) — https://sigrok.org/
  - MCUboot (secure bootloader for 32-bit MCUs; imgtool signing; Zephyr/NuttX/Mbed support) — https://docs.mcuboot.com/
  - From Zero to main() series — François Baldassari (2019) — https://interrupt.memfault.com/blog/zero-to-main-1 (already added to 07; move here)
  - How to debug a HardFault on an ARM Cortex-M MCU — Chris Coleman (2019) — https://interrupt.memfault.com/blog/cortex-m-hardfault-debug (already added to 07; move here)

### B. Hardware-in-the-Loop Testing & Lab Automation
- **Status:** ✔ Created → `software/13-hil-testing-and-lab-automation/README.md`.
  - Appended as 13; the README says "take after 05, or right after 12".
  - Change from the proposal: Grenning stays in 05. The section builds on the merged 01, 04 and 05 mini-projects instead of repeating them.
- **Position (as proposed):** after Section 05 (Testing) or directly after A.
- **Why:**
  - For an engineer who builds test-and-measurement hardware, instrument command sets (SCPI over USB/Ethernet), Python host software, and automated bench tests are the product itself, not side topics.
  - Verifying agent-written firmware needs automated checks on real hardware.
  - Today software/05 stops at host-side unit tests and pcb stops at fabrication, so this layer belongs to neither.
- **Outline:**
  1. The firmware test pyramid: host unit tests (Unity/CMock) → simulation (Renode/QEMU) → HIL on real boards → bench/system tests.
  2. The instrument-control stack: VISA, IEEE 488.2 and SCPI (command trees, error queue), USBTMC, VXI-11/HiSLIP (LXI).
  3. Python on the bench: PyVISA/PyVISA-py, PyMeasure procedures, pyserial; driver structure; simulated instruments for CI.
  4. HIL rigs: power switching, serial consoles, flashing, fixtures; labgrid + pytest; capturing results.
  5. CI with hardware: self-hosted runners attached to fixtures, flaky-test triage, artifact retention.
  6. Designing your own instrument's SCPI interface (conformance, discoverability, error reporting), and exposing it to agents via MCP.
- **Resources (all verified):**
  - PyVISA ("control all kinds of measurement devices independently of the interface"; GPIB, RS232, USB, Ethernet; PyVISA-py backend) — https://pyvisa.readthedocs.io/en/latest/
  - SCPI (Standard Commands for Programmable Instrumentation, IVI's wording), IVI Foundation; built on IEEE 488.2 and maintained by IVI since 2003 — https://www.ivifoundation.org/About-IVI/scpi.html
  - PyMeasure (instrument classes, experiment procedures, live-plot GUIs) — https://pymeasure.readthedocs.io/en/latest/
  - labgrid (Pengutronix; embedded board control library: power, serial, USB, pytest plugin, remote exporter/coordinator) — https://labgrid.readthedocs.io/en/latest/
  - Renode (Antmicro; open-source emulation for firmware CI with Robot Framework; STM32 peripherals; 1.17.0 released Sep 2026) — https://antmicro.com/platforms/renode/ (renode.io redirects here)
  - Test-Driven Development for Embedded C — Grenning (2011) — https://pragprog.com/titles/jgade/test-driven-development-for-embedded-c/ (already in 05; cross-reference)

## Cut candidates
- **06 — *The Software Engineer's Guidebook*:** a career book, misplaced in Systems and duplicated in 11 (🔑 in both).
- **06 — "Git advanced workflows":** duplicates Section 10.
- **06 — DDIA:** duplicate of 04 (🔑 in both). Keep it in one place.
- **06 — Infrastructure as Code (Terraform/Ansible):** low relevance for an embedded/instrument founder.
- **04/06 — System Design Interview channel (🔑) and *System Design Interview* Vols 1–2:**
  - The channel has 7 videos and is inactive.
  - The books are interview-prep for web-scale backends.
  - Demote both, or move them to "optional".
- **03/04 — APoSD:** listed with 🔑 in both sections and tracked twice in PROGRESS.
- **08 — *The Web Application Hacker's Handbook* (2011):** superseded by the free Web Security Academy (now non-🔑, with a dated note).
- **09 — "Cursor/Copilot best practices":** a placeholder with no source. The Claude Code best-practices and AGENTS.md rows now cover it, tool-neutrally.
- **02 — FastBit Embedded Brain Academy (Udemy):** no link and no specific course. Make it specific or cut it.
- **00 — SICP:** Scheme-based and low-yield for this learner. Mark it optional.
- **01 — Real Python:** a generic site with no specific path.
- **courses/ — Embedded Artistry, Interrupt, Pragmatic Engineer, Simon Willison:** blogs and newsletters that duplicate blogs-and-references.
- **PROGRESS — "Books (supplementary)":** double-tracks items that already sit under their sections.

## Structural observations
- **Three schemas in one curriculum:**
  - 00–03: `# | Type | Resource | Notes` tables, a "Key Concepts" table, and a code-block Suggested Order.
  - 04–07: 7-column tables with Year.
  - 08–11: no Year column.
  - Recommendation: one schema (`Priority | Type | Resource | Author(s) | Year | Link | Description`) everywhere.
- **🔑 inflation:**
  - About half of all rows are 🔑 (04: 7 of 14; books/: 10 of 20 originally).
  - That hides the core path. Recommend at most 3 🔑 per section, defining a minimal path.
- **Source-less "Concept" rows dominate:**
  - In 09, 12 of 13 original rows had no source; 06, 07, 10 and 11 had several.
  - Each concept row should point to one canonical source, or move to a "Key Concepts" table without a checkbox.
- **Sequencing:**
  - The learning path is strictly linear, but 09 (agents) and 10 (git) are day-one skills for the intended learner.
  - Recommend presenting 09 and 10 as parallel tracks (I added a "run in parallel" note to 09).
  - 06 is web-backend-centric. Now that Sections 12 and 13 exist, consider shrinking 06 to "Networking, Protocols & Data" for instruments.
  - Sections 12 and 13 are numbered last but belong mid-path (after 07, and after 05 or right after 12). The README learning path now says so.
- **Overlap: software/07 ↔ pcb:**
  - pcb has essentially no firmware content; the only touchpoint is pcb/10 "Phil's Lab advanced designs (STM32, FPGA boards)".
  - The real issue is a gap between the two: board bring-up, bench debugging with scopes and logic analyzers, and test automation belong to neither.
  - Sections 12 and 13 now own this. pcb/10 and pcb/11 should cross-link to them; pcb is outside my scope.
- **Overlap: software/00 ↔ math:**
  - math/00 (Epp, *Discrete Mathematics with Applications*; Bazett's discrete-math videos) and math/06 (graph theory and combinatorics) cover the discrete math a CS learner needs.
  - software/00 now cross-links math/00 instead of duplicating it.
  - math/README's "Connections" table already maps Software ↔ math 00/06/08/11.
- **Overlap: software/09 ↔ ml:**
  - ml/11-frontiers has an "Agentic AI" subsection listing *Building Effective Agents* (also now in software/09) and SWE-bench.
  - ml/12 lists METR's time-horizons paper (arXiv 2503.14499).
  - Recommend a cross-link: ml covers agent research and evaluation; software/09 covers day-to-day practice.
- **Agent skill (`.agents/skills/update-curriculum/SKILL.md`):**
  - ✔ The section map pointed at 8 nonexistent directories (`00-cs-fundamentals/`, `01-foundations/`, `02-core-programming/`, `03-architecture/`, `04-testing/`, `05-systems/`, `06-embedded-systems/`, `07-performance/`). Fixed, with a PROGRESS heading rule added.
  - ✔ The tool list was refreshed (Claude Code, Codex, Gemini CLI added) and an "evidence over vendor claims" line added.
  - ✔ Added a "verify before adding" rule.
  - ✱ The skill still says "When in doubt… err on the side of inclusion". That policy produced the placeholder rows; recommend "when in doubt, leave it out and list it in the summary".
  - ✱ It names Simon Willison as "the primary source" for AI practice, which invites single-source bias.
  - ✱ It never asks the agent to re-check existing entries for new editions, or to keep books/README counts and PROGRESS in sync.
- **Missing standard parts:**
  - No per-section "core path" line.
  - No glossary.
  - There is still no explicit capstone. However, 05's Bench HIL Rig, 12's Agent-Ready Firmware Harness and 13's Hardware CI Pipeline now form a de facto capstone track tied to bench work.
- **Verification limits:** the shared WebSearch and WebFetch budgets ran out near the end of this pass. Three candidates I wanted were therefore not added:
  - McConnell's *Software Estimation* or Brooks's *Mythical Man-Month* (for 11)
  - A 3rd edition of *High Performance Python* (for profiling)
  - The HiSLIP spec PDF
- **Not re-verified by me:** existing URLs, which the separate audit covers. The Interrupt and Embedded Artistry links weren't re-fetched.
- **Third pass, scaffold reconciliation (no web calls):** I scanned the merged 🎯/🛠️/✅ blocks in 00–11.
  - Clean: no block cites METR's 19% figure, "90 ways", K&R as definitive, MISRA, or any old broken link target. Fluent Python 2e and Pro Git section numbers match the listed editions.
  - DDIA 2nd-edition dependencies removed in two places:
    - 06's exercise 1 now inlines the `db_set`/`db_get` bash store instead of relying on the 1st edition's example.
    - 04's exercise 4 cites "DDIA on event sourcing" instead of a stream-processing chapter.
  - The Web Application Hacker's Handbook citation in 08's exercise 1 now also names the Web Security Academy.
  - 09's exercise 1 now cites AGENTS.md and the Claude Code best practices instead of the source-less placeholder row.
  - Explicit section pointers were added where an exercise relies on a resource listed elsewhere:
    - 00: FreeRTOS (Section 07)
    - 01: PyVISA (Section 13)
    - 05: OpenOCD (Section 12) and PyVISA/SCPI (Section 13)
    - 07: RTT (Section 12)
    - 08: Making Embedded Systems and the Interrupt blog (Section 07)
- **Repo-level README (outside software/):** its Software Engineering "Sections" line still ends at Professional practice. (Done: the root README now lists both.)
- **To verify (Sections 12–13; written without web access in the second pass):**
  - *Professional CMake* author: the book page says only "a CMake co-maintainer". "Craig Scott" comes from prior knowledge.
  - 12's exercise 5 relies on MCUboot's test-upgrade revert and power-fail-safe swap. These are documented MCUboot features, but my fetch of the docs landing page didn't confirm them.
  - RTT support in debug servers other than J-Link's. The text only tells the reader to check.
  - Renode support for the exact STM32U5 part. The text only tells the reader to check.
  - The HiSLIP 2.0 spec PDF (IVI-6.1, linked from IVI's SCPI page; not fetched).

## Top 5 priorities in this curriculum
1. **Run Section 09 now, in parallel, and make it evidence-based.**
   - Read METR (2025 RCT plus the Feb 2026 update) and DORA 2025 first. Then *Building effective agents*, the Claude Code best practices, and the lethal trifecta.
   - Start measuring your own agent workflow (time to merged change, rework, escaped defects). Your sense of speed is not evidence.
2. **Own what agents can't see.**
   - Yiu's Cortex-M23/M33 guide (exceptions, MPU, TrustZone on your STM32U5).
   - "From Zero to main()" for startup code and linker scripts.
   - The HardFault article.
   - Then work through Section 12 (toolchain, RTT/SWO, OpenOCD, MCUboot) right after 07's reading.
3. **Put automated tests between agents and hardware.**
   - Grenning's embedded TDD with Unity/CMock on the host.
   - Then simulation and HIL with pytest/labgrid/PyVISA (Section 13), so agent-written firmware and host code are checked on real boards and instruments.
4. **Modernize and standardize your C.**
   - Read *Modern C* 3e or *Effective C* 2e (C23).
   - Adopt SEI CERT C plus BARR-C, or a MISRA C:2025 subset, as the review rulebook.
   - Enforce it with static analysis and pre-commit in CI.
5. **Treat product security as a shipping requirement.**
   - The EU CRA's vulnerability-reporting duties have applied since 11 Sep 2026 for products on the EU market.
   - Threat-model your instruments with the Manifesto's four questions.
   - Add dependency verification to every agent-generated change; per the package-hallucination study, at least 5% of LLM-suggested packages don't exist.

## Follow-up pass (2026-10-13)
- **New sections created:** none (12 and 13 already exist).
- **Added:**
  - High Performance Python (3rd ed) — Micha Gorelick, Ian Ozsvald — 2025 — software/01 (row 12, Suggested Order step 7, PROGRESS; Practice 3 now profiles before optimizing and cites ch. 2 "Profiling to Find Bottlenecks"; books/ #26) — https://www.oreilly.com/library/view/high-performance-python/9781098165956/
  - Software Estimation: Demystifying the Black Art — Steve McConnell — 2006 — software/11 (row, Suggested Order step 6, PROGRESS; Practice 2 cites Ch. 2 "How Good an Estimator Are You?" and Ch. 8 "Calibration and Historical Data"; books/ #25) — https://www.oreilly.com/library/view/software-estimation-demystifying/0735605351/
  - IVI-6.1: IVI High-Speed LAN Instrument Protocol (HiSLIP), Revision 2.0 — IVI Foundation — 2020 (Apr 23) — software/13 (row, Suggested Order step 4, PROGRESS) — https://www.ivifoundation.org/downloads/Protocol%20Specifications/IVI-6.1_HiSLIP-2.0-2020-04-23.pdf
- **Removed (confirmed nonexistent):** none.
- **Flags resolved:**
  - 12-firmware-toolchain-debug-and-observability/README.md:33 — *Professional CMake* author and edition (to-verify list) — confirmed: Craig Scott, "a CMake co-maintainer… also the author of the book Professional CMake: A Practical Guide"; "the 22nd Edition, which covers up to CMake 4.2"; the toolchain chapter is Ch. 24 "Toolchains And Cross Compiling", now cited by number — https://crascit.com/about/ ; https://crascit.com/professional-cmake/
  - 12/README.md:96–99 (Practice 5) — MCUboot revert and power-fail behavior (to-verify list) — the design doc confirms that a test swap is reverted on the next boot unless the new image marks itself "OK", that an image's integrity is checked immediately before it is copied into the primary slot (an invalid image's slot is erased), and that "the swap status region allows the bootloader to recover in case it restarts in the middle of an image swap operation". It doesn't discuss power failure as such. The exercise now asks for a swap-based mode with signature checking enabled, says "marks itself OK", and presents the power-cut test as checking that documented reset recovery on the learner's own flash — https://docs.mcuboot.com/design.html
  - 12/README.md:35, :86, :105 — RTT with probes other than J-Link (to-verify list) — OpenOCD documents RTT ("15.6 Real Time Transfer (RTT)": `rtt setup`, `rtt start`, `rtt server start`…), usable on any target that supports background memory access. The RTT row, Practice 3 and the mini-project now say so — https://openocd.org/doc-release/html/General-Commands.html
  - 13-hil-testing-and-lab-automation/README.md:39, :82 — Renode support for the STM32U5 (to-verify list) — Renode's own (incomplete) list of supported targets has STM32F0/F1/F4/F7, G0, H7, L0/L1, L552, W108 and WBA52 platforms but no STM32U5. The row now says so, and Practice 3 falls back to the STM32L552 (also a Cortex-M33) — https://renode.readthedocs.io/en/latest/introduction/supported-boards.html
  - 13/README.md:52 — found while verifying HiSLIP: Suggested Order step 2 sent the reader to "the spec it links to", but the only PDF IVI's SCPI page links is the HiSLIP spec. Step 2 now points to the SCPI specification on IVI's specifications page — https://www.ivifoundation.org/About-IVI/scpi.html ; https://www.ivifoundation.org/specifications/default.html
  - 09-agentic-ai-workflows/README.md:59 — Claude Code and AGENTS.md (independent check V5) — per the official docs, Claude Code v2.1.277 or later reads `AGENTS.md` directly, but by default only when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` exists in the working directory or above it. Otherwise it reads only the CLAUDE.md files, unless one imports `@AGENTS.md` or *Project instructions* is set to `claude-md-and-agents-md`. The row now says exactly this and links the docs section. The checker's offline belief that an import or symlink is always needed is out of date; the docs' own summary is "Claude can also read a repository's AGENTS.md files in place of CLAUDE.md" — https://code.claude.com/docs/en/memory#agents-md
  - 04-architecture-and-design-patterns/README.md:108 (Check Yourself Q1) — *Fundamentals of Software Architecture* 2nd-edition "laws" (V5) — confirmed that the 2nd edition adds a third law to the first edition's two ("For the second edition, we added a third law…", episode notes for the 2nd edition's Chapter 1, 19 Jun 2025). Q1 now asks for all the laws and notes the third. The objective at :21 already said "laws" and needed no change — https://softwarearchitecturebookclub.buzzsprout.com/2377730/episodes/16931605-software-architecture-fundamentals-2nd-edition-introduction-laws-of-software-architecture
  - 01-python-mastery/README.md:34 — Python 3.13–3.15 claims (free-threading, JIT) — all correct as written. 3.13 (released 7 Oct 2024): experimental free-threaded mode, and "a basic JIT compiler… currently disabled by default". 3.14 (7 Oct 2025): "PEP 779: Free-threaded Python is officially supported", deferred annotations (PEP 649/749), JIT still "experimental". 3.15 ("released on 9 October 2026"): PEP 810 lazy imports, the PEP 799 `profiling` package with the Tachyon sampling profiler, a stable ABI for free-threaded builds (`abi3t`, PEP 803), and "the experimental JIT compiler has been significantly upgraded". Added the dates, "off by default", the abi3t ABI and the JIT's still-experimental status — https://docs.python.org/3.13/whatsnew/3.13.html ; https://docs.python.org/3.14/whatsnew/3.14.html ; https://docs.python.org/3.15/whatsnew/3.15.html
  - 09/README.md:56 — DORA 2025 wording — confirmed: "nearly 5,000 technology professionals"; "90% of survey respondents report using AI at work"; a positive relationship with throughput, while AI adoption "does continue to have a negative relationship with software delivery stability"; "AI doesn't fix a team; it amplifies what's already there". Added "30% report little or no trust in the code generated by AI". The dora.dev page itself carries only the amplifier sentence; the figures come from the launch post (Harvey & DeBellis, 23 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report ; https://dora.dev/research/2025/dora-report/
  - 09/README.md:55 — METR RCT and Feb 2026 update wording — paper confirmed (Becker, Rush, Barnes, Rein; 16 developers, 246 tasks; +19% completion time; developers estimated a 20% speedup). The update is "We are Changing our Developer Productivity Experiment Design" (24 Feb 2026; Becker, Rush, Tom Cunningham, Rein, Khalid Mahamud): a follow-up started August 2025 with 57 developers and 800+ tasks. Developers increasingly declined to take part, or withheld tasks (30–50% said so), because they didn't want to work without AI, which makes the central estimate "challenging to interpret" and likely a lower bound. METR believes developers are likely more sped up in early 2026 but calls its data "only very weak evidence" of how much. The row's wording now follows the post, and the update's authors are added — https://arxiv.org/abs/2507.09089 ; https://metr.org/blog/2026-02-24-uplift-update/
  - 09/README.md:57 (+ PROGRESS.md:196) — "Anthropic Applied AI team" as author (V5) — the post (29 Sep 2025) is written by Prithvi Rajasekaran, Ethan Dixon, Carly Ryan and Jeremy Hadfield; they are now named — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - 09/README.md:5, :126; 03-reading-and-reviewing-code/README.md:109 — "AI agents will write most of the code" stated as fact (V5 tone) — now framed as the curriculum's bet, grounded in DORA's 90% adoption figure and the contested METR evidence (sources as above). Both "smart friend" questions now say "as AI/agents write more of the code", and 09's also asks what the learner would measure. `software/README.md:7` is the owner's own philosophy statement and was left unchanged.
  - .agents/skills/update-curriculum/SKILL.md:82 — the skill never said to update books/, courses/ or blogs/ (V5) — added step 4 (cross-cutting pages plus the README title count) and applied it to this pass's two books: books/ #25–26 and `software/README.md:54` 24 → 26 titles. The "append-only" note was left as is, because rule 4 already defines append-only as "don't silently delete".
  - 01-python-mastery/README.md:80 — `pyright --strict` (V5) — already reworded before this pass to `typeCheckingMode = "strict"`; no change needed.
- **Still unverified:**
  - Beningo, *Embedded Software Design* (software/02 row 4) — year still blank. The Crossref lookup (`api.crossref.org/works/10.1007/978-1-4842-8279-3`) returned HTTP 429 and wasn't retried, per the rate-limit rule.
  - The wording of FoSA 2e's third law — only its existence is confirmed, so the repo doesn't quote it.
  - MCUboot under real power loss — the docs cover a restart in the middle of a swap, not power failure explicitly. Practice 5 now tests this instead of asserting it.
  - Brooks, *The Mythical Man-Month* — not pursued; McConnell fills the estimation gap.
- **For the owner to decide:**
  - 🔑 inflation (V5, "a curation call") — not changed. Software has 9 🔑 in 09, 7 in 04, 6 in 02, 5 each in 01, 03 and 07, and 4 each in 00, 05, 06 and 11, against the ~3 rule. Suggestion for 09, following this review's priority 1: keep 🔑 on METR and *Building effective agents*, move one to the Claude Code best practices, and demote the six unsourced concept, practice and blog rows.
  - The cut candidates above (e.g., the source-less "Cursor/Copilot best practices" row) are still in place; nothing was deleted.

## Tier lists (2026-10-13)
🔑 trimmed to ≤3 per section; each Suggested Order now opens with a "Core path" line. Reverse any call by re-adding 🔑 to the row and the Core path line.
| Section | 🔑 kept | 🔑 removed (why, ≤8 words) |
|---|---|---|
| 00 | *Grokking Algorithms*; CS:APP; MIT 6.006 | Teach Yourself CS (roadmap; teaches no objective itself) |
| 01 | *Effective Python*; *Fluent Python*; *Robust Python* | *Architecture Patterns with Python* (architecture; only the mini-project uses it); `typing` docs (reference docs, not core reading) |
| 02 | *Modern C*; *Making Embedded Systems*; Quantum Leaps videos | K&R (C89 only; practice code uses C99 headers); *Expert C Programming* (go-deeper text; assumes C knowledge); Embedded Artistry (ongoing blog; reference) |
| 03 | *A Philosophy of Software Design*; *Code Reading*; *Refactoring* | *The Art of Readable Code* (go-deeper; objectives rest on the others); "Review AI-generated code critically" (practice row with no source) |
| 04 | *Clean Architecture*; GoF *Design Patterns*; *Fundamentals of Software Architecture* | *A Philosophy of Software Design* (core in 03, a prerequisite); DDIA (core in 06, its objectives' home); *The Hard Parts* (go-deeper after *Fundamentals*); System Design Interview channel (inactive interview-prep channel) |
| 05 | *Python Testing with pytest*; "Review AI-generated tests" (practice); Grenning, *TDD for Embedded C* | Testing pyramid (concept row with no source) |
| 06 | DDIA; *System Design Interview* Vol 1–2; ByteByteGo | *The Software Engineer's Guidebook* (career book, misplaced here; stays core in 11) |
| 07 | Quantum Leaps videos; Yiu's Cortex-M23/M33 guide; FreeRTOS | *Making Embedded Systems* (core in 02, a prerequisite); Embedded Artistry (ongoing blog; reference) |
| 09 | METR RCT + Feb 2026 update; *Building effective agents*; Simon Willison's blog | Five concept rows (human-in-the-loop, prompt engineering, reviewing AI code, AI-assisted review, context files) and "Build a project entirely with AI assistance" (unsourced rows; nothing to read) |
| 11 | *The Software Engineer's Guidebook*; *Staff Engineer*; The Pragmatic Engineer | Diátaxis (no exercise uses it) |

- 09: the follow-up pass's suggestion to move a 🔑 onto the Claude Code best practices row was not applied, because the trim only removes 🔑 and tool-specific items stay off the core path. The third slot went to Simon Willison's blog, which objective 5, Practice 5 and the mini-project use.
- `books/README.md` #1 *The C Programming Language*: 🔑 removed (it lost 🔑 in 02, its only section).
- `courses/README.md` #4 System Design Interview channel: 🔑 removed (it lost 🔑 in 04, its only section).
- `blogs-and-references/README.md` Embedded Artistry: 🔑 removed (it lost 🔑 in 02 and 07).
- `.agents/skills/update-curriculum/SKILL.md` rule 6: now says "at most 3" and to keep the Core path line in sync (the "many sections still exceed this" note was obsolete).
- books/README.md #12 Viafore, *Robust Python*: 🔑 added (core in 01)
- books/README.md #15 Gamma, Helm, Johnson & Vlissides, *Design Patterns*: 🔑 added (core in 04)
- books/README.md #16 Orosz, *The Software Engineer's Guidebook*: 🔑 added (core in 11)
- books/README.md #17 Larson, *Staff Engineer*: 🔑 added (core in 11)
- books/README.md #18 Bhargava, *Grokking Algorithms* (2nd ed): 🔑 added (core in 00)
- books/README.md #19 Okken, *Python Testing with pytest* (2nd ed): 🔑 added (core in 05)
- books/README.md #20 Chacon & Straub, *Pro Git*: 🔑 added (core in 10)
- software/README.md legend: 🔑 row now reads "**Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line"
- software/README.md legend: 🔑🤖 row now says "a core-path item" instead of "a must-read"
- software/README.md Key Resources: K&R C removed (not core in any section; unmarked in 02)
- software/README.md Key Resources: Embedded Artistry removed (not core in any section; unmarked in 02 and 07)
- Second check (2026-10-13), from `independent-check.md` "Second check":
  - 05: 🔑 moved from "Review AI-generated tests" (a sourceless practice row, which keeps 🤖) to Khorikov, *Unit Testing Principles, Practices, and Patterns*. Practice 3 now cites Grenning.
  - 08: 🔑 moved from the "Reviewing AI-generated code for security" concept row to the Threat Modeling Manifesto.
  - `courses/README.md` #6 ArjanCodes: 🔑 removed (index-only).
  - `blogs-and-references/` keeps its own 🔑, which means "follow first"; the README legend now says so.
- Final decisions (2026-10-13): the update skill's rule 6 now also says to run `tools/build_index.py` after a 🔑 change.
- Final pass: the Quantum Leaps rows in 02 and 07 and in courses/ now link the *Modern Embedded Systems Programming Course* playlist (checked via YouTube oEmbed: "Modern Embedded Systems Programming Course", Quantum Leaps, LLC), not the whole channel.
