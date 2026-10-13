# Agentic AI Development Workflows

## Why This Section Matters

This is the future of software development. AI agents will write most of the code, but humans must architect systems, define constraints, review output, and ensure correctness. This section teaches you to be the orchestrator.

---

## Prerequisites

- [Section 01 — Python Mastery](../01-python-mastery/README.md)
- [Section 02 — Embedded C Mastery](../02-embedded-c-mastery/README.md)
- [Section 03 — Reading and Reviewing Code](../03-reading-and-reviewing-code/README.md)
- [Section 04 — Architecture and Design Patterns](../04-architecture-and-design-patterns/README.md)
- [Section 05 — Testing and Quality](../05-testing-and-quality/README.md)
- [Section 06 — Systems and Infrastructure](../06-systems-and-infrastructure/README.md)

> If you already use coding agents every day, don't wait for these: run this section in parallel with Sections 01–06 and come back to it as they deepen your review skills.

---

> 🤖 Every resource in this section is AI-workflow specific.

---

## 🎯 Learning Objectives

After this section you can:
- Write project context files (`AGENTS.md` or your tool's rules file, plus skills) that measurably reduce corrections and convention drift across agent sessions.
- Decompose a feature into atomic agent tasks with explicit inputs, outputs, allowed files and acceptance tests, each landing as one reviewable commit.
- Use tests as the specification for an agent, and detect reward hacking: edited or skipped tests, special-cased inputs, weakened assertions.
- Measure, rather than assume, what AI implementation and AI review get right: run a three-layer review, build a meta-review scorecard, and test productivity claims on your own code with predictions stated up front.
- Decide what not to delegate (hardware timing, security-critical code, novel algorithms), and audit your own agent setup for Willison's "lethal trifecta".

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑🤖 | Concept | The human-in-the-loop model | — | — | You are the architect, AI is the junior developer. Never blindly accept. Define the *what* and *why*, let AI handle the *how*. |
| 🔑🤖 | Concept | Prompt engineering for code | — | — | Clear context, constraints, and iterative refinement. Specify architecture, not implementation. Better prompts and context mean less rework, not less review. |
| 🔑🤖 | Concept | Reviewing AI-generated code | — | — | Three-layer review: logic correctness, security, architectural alignment. AI code passes syntax checks but fails design intent — learn to catch that. |
| 🔑🤖 | Concept | AI-assisted code review workflow | — | — | Use AI to review AI output (meta-review), then apply human judgment. The human reviews the *review*, not just the code. |
| 🔑🤖 | Concept | Project context and constraints files | — | — | `AGENTS.md`, rules files, skills — teaching AI your project's conventions. The better the context, the fewer corrections needed. |
| 🤖 | Concept | Task decomposition for agents | — | — | Break complex features into atomic, verifiable tasks. Each task should have a clear input, output, and success criteria. |
| 🤖 | Concept | Testing AI output | — | — | AI writes code, you write (or review) the tests. Tests are the specification. If the agent can't pass them, check the spec, the tests, and the task size; and when it does pass, check it didn't weaken, skip, or special-case a test to get there. |
| 🤖 | Concept | Avoiding the "Tower of Babel" | — | — | Maintaining style consistency when multiple agents generate code. Enforce linting, formatting, and naming conventions ruthlessly. |
| 🔑🤖 | Blog | Simon Willison's blog | Simon Willison | [Link](https://simonwillison.net/) | The best writing on practical AI-assisted development. Honest, detailed, and focused on real workflows rather than hype. |
| 🤖 | Blog | Cursor/Copilot best practices | — | — | IDE agent workflows and tips. Learn the keyboard shortcuts, context tricks, and prompting patterns specific to your tooling. |
| 🤖 | Concept | When NOT to use AI | — | — | Security-critical code, novel algorithms, hardware-specific timing. Know the boundaries — AI is a tool, not a replacement for expertise. |
| 🤖 | Concept | Version control discipline with AI | — | — | Atomic commits, meaningful diffs, avoiding AI commit message spam. Every commit should tell a story a reviewer can follow. |
| 🔑🤖 | Practice | Build a project entirely with AI assistance | — | — | Practice the architect role end-to-end. Define requirements, decompose tasks, prompt agents, review output, iterate. The capstone exercise. |
| 🔑🤖 | Article | Building effective agents | Erik Schluntz, Barry Zhang (Anthropic) | [Link](https://www.anthropic.com/engineering/building-effective-agents) | Dec 2024. Workflows vs. agents, and five composable patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). Core advice: use the simplest design that works and add agentic complexity only when it measurably helps. |
| 🔑🤖 | Research | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity, plus the Feb 2026 update | Joel Becker, Nate Rush, Elizabeth Barnes, David Rein (METR) | [Paper](https://arxiv.org/abs/2507.09089) · [2026 update](https://metr.org/blog/2026-02-24-uplift-update/) | Randomized trial, 16 experienced maintainers, 246 tasks, early-2025 tools: allowing AI made tasks take 19% longer, while developers believed it made them ~20% faster. METR's late-2025 follow-up (57 developers) could not produce a reliable estimate, partly because many developers refused to work without AI; METR thinks 2026 speedups are probably larger but can't size them. The durable lesson: measure your own workflow, because the feeling of speed is not evidence. |
| 🤖 | Report (Free) | State of AI-assisted Software Development 2025 (DORA) | Google Cloud DORA | [Link](https://dora.dev/research/2025/dora-report/) | Survey of ~5,000 practitioners (Sep 2025): 90% use AI at work; AI adoption now correlates with higher delivery throughput but still with lower delivery stability. Central finding: AI amplifies an organization's existing strengths and weaknesses. |
| 🤖 | Article | Effective context engineering for AI agents | Anthropic Applied AI team | [Link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Sep 2025. Treats context as a finite attention budget: compaction, structured note-taking (e.g. a NOTES.md), sub-agents with clean context windows, just-in-time retrieval. Explains why lean, high-signal context beats exhaustive context. |
| 🤖 | Docs | Claude Code best practices | Anthropic | [Link](https://code.claude.com/docs/en/best-practices) | Concrete agentic-coding discipline: give the agent a check it can run (tests, build, linter), explore → plan → implement → commit, keep CLAUDE.md/AGENTS.md short, clear context between tasks, and review diffs in a fresh context. Tool-specific, but the practices transfer to any coding agent. |
| 🤖 | Spec | AGENTS.md | OpenAI Codex, Amp, Google Jules, Cursor, Factory; now stewarded by the Agentic AI Foundation (Linux Foundation) | [Link](https://agents.md/) | The open "README for agents" convention behind the context-files row above. Read by Codex, GitHub Copilot's coding agent, Cursor, Gemini CLI, Jules, Aider and others; Claude Code reads CLAUDE.md, which can import it with an `@AGENTS.md` line (check the Claude Code docs for current native support). The nearest file to the edited code wins. |
| 🤖 | Spec | Model Context Protocol (MCP) | Anthropic (originator); open standard | [Link](https://modelcontextprotocol.io/) | Open protocol (Nov 2024) for connecting agents to tools and data, supported by Claude, ChatGPT, VS Code, Cursor and others. Learn it as an architect: an MCP server is how you would expose an instrument or test rig to agents, and every server you add widens the attack surface. |
| 🤖 | Article | The lethal trifecta for AI agents | Simon Willison | [Link](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) | Jun 2025. Private data + untrusted content + a way to communicate externally = data exfiltration through prompt injection. The working security model for wiring agents to MCP servers, browsers, and inboxes: guardrails don't reliably stop it, so avoid combining all three. |
| 🤖 | Article | Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl | Birgitta Böckeler (martinfowler.com) | [Link](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | Oct 2025. A hands-on, skeptical look at spec-driven agent tooling: writing a spec first helps, but heavyweight spec workflows misfit small tasks, are tedious to review, and can give a false sense of control. Read before adopting any "spec-driven" process. |

---

## Suggested Order

1. **The human-in-the-loop model** — Internalize the mindset first: you are the architect, AI is the builder.
2. **METR study + DORA 2025 report** — Calibrate expectations with evidence before adopting habits; decide how you'll measure your own results.
3. **Building effective agents** — Learn the vocabulary of agentic systems and the "simplest thing that works" principle.
4. **Prompt engineering for code → Effective context engineering** — Learn to give agents the right context, not just the right words.
5. **Claude Code best practices** — Turn those ideas into a daily loop: verifiable checks, explore → plan → implement → commit.
6. **Reviewing AI-generated code** — Build your three-layer review discipline: correctness → security → architecture.
7. **Task decomposition for agents** — Practice breaking features into atomic, testable units.
8. **Testing AI output** — Write tests first, then let AI implement. Tests are your specification language.
9. **Understanding Spec-Driven-Development** — Decide how much spec your tasks actually need.
10. **Project context and constraints files + AGENTS.md** — Set up `AGENTS.md` and rules to reduce review burden.
11. **AI-assisted code review workflow** — Layer AI review on top of your own for efficiency.
12. **Model Context Protocol + the lethal trifecta** — Connect agents to tools and data without opening an exfiltration path.
13. **Simon Willison's blog** — Read his practical guides on AI-assisted development.
14. **Avoiding the "Tower of Babel"** — Enforce consistency across multi-agent output.
15. **Version control discipline with AI** — Establish commit hygiene rules for AI-generated changes.
16. **When NOT to use AI** — Learn the boundaries. Know when to write code yourself.
17. **Cursor/Copilot best practices** — Optimize your IDE agent workflow.
18. **Build a project entirely with AI assistance** — The capstone: practice everything end-to-end.

---

## 🛠️ Practice

1. **Context-file A/B (the Tower of Babel test)** — Pick a repo that needs three sibling modules, such as three instrument drivers or three CLI subcommands.
   - **Before:** with no context file, have three fresh agent sessions implement one module each. Count divergences in naming, error handling, logging, test layout and docstrings, and count the corrections each module needed.
   - **After:** write `AGENTS.md` (build/test commands, architecture map, conventions, forbidden actions, definition of done) plus ruff and clang-format configs. Repeat with fresh sessions on three new sibling modules.

   Done when you have a before/after table and a v2 of the file that fixes the top three remaining problems. *(~4 h · project context and constraints files; avoiding the "Tower of Babel"; AGENTS.md; Claude Code best practices)*
2. **Decompose, then delegate** — Take a real feature, such as a `MEAS?` query in the firmware command shell plus a matching Python client method with retries. Break it into at most eight tasks, each with inputs, an output, the files allowed to change and an acceptance test. Run each as its own agent task on its own branch, and log prompt → re-prompts → review findings. Done when every task has merged as one atomic commit whose message explains *why*, and you can point to the task descriptions that caused re-prompts and say what they were missing. *(~4 h · task decomposition for agents; prompt engineering for code; version-control discipline with AI)*
3. **Tests as the spec — watch for cheating** — Write failing tests first (pytest plus at least two Hypothesis properties) and an interface stub for a module, e.g., a calibration-curve fitter. Give the agent only those, with the instruction "make the tests pass; do not modify tests." Inspect the result for reward hacking:
   - edited or skipped tests;
   - special-cased inputs;
   - catch-all `except` blocks;
   - loosened tolerances.

   Then mutation-test the implementation. Done when you've documented every shortcut the agent attempted, or shown there were none using `git diff --stat tests/` and the mutation score. *(~3 h · testing AI output; Section 05 tools)*
4. **Meta-review scorecard** — For three agent-generated PRs, do your own three-layer review first (correctness → security → architecture) and write it down. Then have a separate AI session review the same diffs. Build a confusion table with three rows: found by both, found by AI only (split into true and false positives), and found by you only. Before you start, write one prediction you could be proven wrong on, e.g., "AI review will catch ≥ 80% of my correctness findings and < 30% of my architecture findings". Done when you've checked that prediction, can name which issue classes you'll hand to AI review and which you will always check yourself, and have updated your Section 03 review checklist to match. *(~3 h · reviewing AI-generated code (three-layer review); AI-assisted code review workflow)*
5. **Boundaries and the lethal trifecta** — Two parts:
   - (a) Ask an agent to configure a timer for 1 µs input-capture resolution from your board's actual clock tree, and to write a constant-time comparison for a firmware MAC check. Verify every register value against the reference manual, the timing on a scope, and the comparison's branch-free behavior in the disassembly. Log every error the agent made.
   - (b) Read Simon Willison's "The lethal trifecta for AI agents" and audit your own setup: MCP servers, browser access, shell access. List every tool combination that brings together private data, untrusted content and external communication, and decide what to remove or sandbox.

   Done when you've written a one-page policy that sorts work into "never delegate", "delegate with review" and "delegate freely". *(~3 h · when NOT to use AI; Simon Willison's blog)*

**🏗️ Mini-project — Architect-Only Build:** Build a tool you actually need, writing only the spec, the task decomposition, the acceptance tests, the context files and the reviews; agents write everything else. One example is `benchctl`: a CLI that runs a voltage/current characterization sweep over SCPI, stores the results as Parquet and renders plots, with pyvisa-sim in CI. Start from the workflow in Willison's "Here's how I use LLMs to help me write code". Before starting, write down two falsifiable predictions about how the build will go, e.g., "firmware tasks will need twice the re-prompts of Python tasks". Keep a `DEVLOG.md` entry per task: prompt → output → review findings → fix.

Deliverable: `projects/software/09-architect-only/`. Success: every acceptance test you wrote before implementation passes; the history is atomic commits with *why*-messages; and a retrospective checks both predictions and lists at least five concrete changes to your prompts, context files or review checklist, each backed by a devlog entry. *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. In the human-in-the-loop model, which decisions stay with you, and which do you delegate?
2. What belongs in `AGENTS.md`, and what should stay out? Give one example of each from your A/B experiment.
3. List the three review layers in order, with one defect typical of AI-generated code for each.
4. What must every agent task description specify, and how do you know a task is small enough?
5. Name three ways an agent can "make the tests pass" without solving the problem, and how you'd detect each.
6. What are the three ingredients of Willison's lethal trifecta, and why does removing any one of them break the attack?
7. Misconception check: "The AI reviewer approved it, so a human review is redundant." What did your meta-review scorecard show?
8. Explain to a smart friend in three sentences how an engineer's job changes when agents write most of the code.
