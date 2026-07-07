# Agentic AI Development Workflows

## Why This Section Matters

This is the future of software development. AI agents will write most of the code, but humans must architect systems, define constraints, review output, and ensure correctness. This section teaches you to be the orchestrator.

---

## Prerequisites

- [Section 01 — Foundations](../01-foundations/README.md)
- [Section 02 — Core Programming](../02-core-programming/README.md)
- [Section 03 — Architecture](../03-architecture/README.md)
- [Section 04 — Testing](../04-testing/README.md)
- [Section 05 — Systems](../05-systems/README.md)

---

> 🤖 Every resource in this section is AI-workflow specific.

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑🤖 | Concept | The human-in-the-loop model | — | — | You are the architect, AI is the junior developer. Never blindly accept. Define the *what* and *why*, let AI handle the *how*. |
| 🔑🤖 | Concept | Prompt engineering for code | — | — | Clear context, constraints, and iterative refinement. Specify architecture, not implementation. The better your prompt, the less you review. |
| 🔑🤖 | Concept | Reviewing AI-generated code | — | — | Three-layer review: logic correctness, security, architectural alignment. AI code passes syntax checks but fails design intent — learn to catch that. |
| 🔑🤖 | Concept | AI-assisted code review workflow | — | — | Use AI to review AI output (meta-review), then apply human judgment. The human reviews the *review*, not just the code. |
| 🔖🤖 | Concept | Project context and constraints files | — | — | `AGENTS.md`, rules files, skills — teaching AI your project's conventions. The better the context, the fewer corrections needed. |
| 🤖 | Concept | Task decomposition for agents | — | — | Break complex features into atomic, verifiable tasks. Each task should have a clear input, output, and success criteria. |
| 🤖 | Concept | Testing AI output | — | — | AI writes code, you write (or review) the tests. Tests are the specification. If the AI can't pass your tests, the prompt was unclear. |
| 🤖 | Concept | Avoiding the "Tower of Babel" | — | — | Maintaining style consistency when multiple agents generate code. Enforce linting, formatting, and naming conventions ruthlessly. |
| 🔑🤖 | Blog | Simon Willison's blog | Simon Willison | [Link](https://simonwillison.net/) | The best writing on practical AI-assisted development. Honest, detailed, and focused on real workflows rather than hype. |
| 🤖 | Blog | Cursor/Copilot best practices | — | — | IDE agent workflows and tips. Learn the keyboard shortcuts, context tricks, and prompting patterns specific to your tooling. |
| 🤖 | Concept | When NOT to use AI | — | — | Security-critical code, novel algorithms, hardware-specific timing. Know the boundaries — AI is a tool, not a replacement for expertise. |
| 🤖 | Concept | Version control discipline with AI | — | — | Atomic commits, meaningful diffs, avoiding AI commit message spam. Every commit should tell a story a reviewer can follow. |
| 🔑🤖 | Practice | Build a project entirely with AI assistance | — | — | Practice the architect role end-to-end. Define requirements, decompose tasks, prompt agents, review output, iterate. The capstone exercise. |

---

## Suggested Order

1. **The human-in-the-loop model** — Internalize the mindset first: you are the architect, AI is the builder.
2. **Prompt engineering for code** — Learn to write prompts that produce reviewable, architecturally sound output.
3. **Reviewing AI-generated code** — Build your three-layer review discipline: correctness → security → architecture.
4. **Task decomposition for agents** — Practice breaking features into atomic, testable units.
5. **Testing AI output** — Write tests first, then let AI implement. Tests are your specification language.
6. **Project context and constraints files** — Set up `AGENTS.md` and rules to reduce review burden.
7. **AI-assisted code review workflow** — Layer AI review on top of your own for efficiency.
8. **Simon Willison's blog** — Read his practical guides on AI-assisted development.
9. **Avoiding the "Tower of Babel"** — Enforce consistency across multi-agent output.
10. **Version control discipline with AI** — Establish commit hygiene rules for AI-generated changes.
11. **When NOT to use AI** — Learn the boundaries. Know when to write code yourself.
12. **Cursor/Copilot best practices** — Optimize your IDE agent workflow.
13. **Build a project entirely with AI assistance** — The capstone: practice everything end-to-end.
