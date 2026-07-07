---
name: update-curriculum
description: Search for and add new important software engineering resources, AI development workflow practices, and technical leadership materials to the learning curriculum.
---

# Update Curriculum Skill

This skill searches for the latest important software engineering resources, AI coding workflow practices, and technical leadership materials, and updates the software learning curriculum accordingly.

## When to Use

- When a new Python or C language version is released
- When new AI coding tools or best practices emerge (agents, IDEs, prompting techniques)
- When notable architecture, design patterns, or testing books are published
- When new security vulnerabilities or frameworks gain prominence
- When the user asks to "update the reading list" or "check for new resources"
- Periodically (e.g., monthly) to check for important new material, especially in Section 09

## Workflow

### 1. Research New Material

Search the web for:

**Python & Embedded Engineering**
- Python release announcements and "What's New" pages
- Embedded engineering blogs: Embedded Artistry, Interrupt (Memfault), Barr Group
- New Python frameworks, testing tools, or linters
- Embedded C best practices and safety-critical standards updates (MISRA, CERT C)

**AI Coding Workflows**
- Simon Willison's blog (https://simonwillison.net/) — the primary source for practical AI-assisted development
- AI coding tool releases and updates (Cursor, Copilot, Cline, Antigravity, Devin)
- New prompt engineering techniques for code generation
- Research on AI code quality, security, and correctness

**Architecture & Leadership**
- The Pragmatic Engineer newsletter (https://blog.pragmaticengineer.com/)
- Engineering blogs from major tech companies (Google, Meta, Netflix, Stripe, Uber)
- Conference talks (Strange Loop, GOTO, QCon, PyCon, Embedded Systems Conference)
- New books on software architecture, system design, or technical leadership

Use search queries like:
- "best software engineering books [current year]"
- "AI coding workflow best practices [current year]"
- "embedded C security vulnerabilities [current year]"
- "Python [version] new features"
- "[conference name] [current year] best talks"

### 2. Evaluate Relevance

For each candidate resource, assess:

- **Architectural focus**: Does it teach design thinking and code reading, not just implementation?
- **Code reading/review emphasis**: Does it help you *understand* and *review* code, not just write it?
- **Practical applicability**: Can you apply this to real Python or Embedded C projects?
- **Quality**: Is this from a trusted source with a track record?
- **Novelty**: Does it cover something the curriculum doesn't already address?

Priority criteria for inclusion:
- Resources that teach code reading and architectural thinking
- AI workflow practices that improve review quality and development speed
- Security resources relevant to Python and C
- Books or talks from recognized industry leaders
- Resources that fill gaps in the existing curriculum

### 3. Update the Repository

For each approved resource:

1. **Add to the appropriate section README** (see Section Mapping below)
   - Add a new row to the resource table
   - Use 🔑 for must-read/must-watch items
   - Use 🤖 for AI-workflow-specific resources
   - Include: type, title, author, link, and a 1-2 sentence description

2. **Update `PROGRESS.md`** if it exists — add a new checkbox entry in the corresponding section

3. **Update the root `README.md`** if the new resource is a foundational addition

### 4. Summary

After updating, provide a summary of:
- What was added and to which sections
- What was considered but rejected (and why)
- Suggestions for the user's next study priorities

## Section Mapping

| Topic Area | Target Section |
|------------|---------------|
| Computer science fundamentals, how computers work | `00-cs-fundamentals/` |
| Python mastery, C programming, code reading | `01-foundations/` or `02-core-programming/` |
| Design patterns, architecture, system design | `03-architecture/` |
| Testing, TDD, property-based testing | `04-testing/` |
| Operating systems, networking, databases | `05-systems/` |
| Embedded systems, RTOS, hardware interfaces | `06-embedded-systems/` |
| Performance, profiling, optimization | `07-performance/` |
| Security vulnerabilities, SRE, reliability | `08-security-and-reliability/` |
| AI coding tools, prompt engineering, agent workflows | `09-agentic-ai-workflows/` |
| Git, CI/CD, collaboration | `10-version-control-and-collaboration/` |
| Career growth, technical leadership, documentation | `11-professional-practice/` |

## Notes

- **Append-only** — never remove existing entries from the curriculum
- Maintain consistent formatting with existing tables
- Always include direct links (prefer official docs, free resources, or author pages)
- When in doubt about whether to include something, err on the side of inclusion with a note
- **Section 09 (Agentic AI Workflows) is the fastest-evolving section** — prioritize checking this area for updates. AI coding tools and practices change rapidly; this section should be reviewed more frequently than others.
