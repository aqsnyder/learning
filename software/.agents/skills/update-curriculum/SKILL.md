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
- AI coding tool releases and updates (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Antigravity, Cline, Devin)
- Evidence on AI-assisted development (randomized studies such as METR's, the annual DORA report) — prefer measured results over vendor claims
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

3. **Update `software/README.md`** (its Key Resources table) if the new resource is a foundational addition

4. **Update the cross-cutting pages** — add a book to `books/README.md` (and fix the title count in `software/README.md`), a tool, blog or newsletter to `blogs-and-references/README.md`, and a course or channel to `courses/README.md`

### 4. Summary

After updating, provide a summary of:
- What was added and to which sections
- What was considered but rejected (and why)
- Suggestions for the user's next study priorities

## Section Mapping

| Topic Area | Target Section |
|------------|---------------|
| Computer science fundamentals, how computers work, algorithms, operating systems, concurrency | `00-cs-foundations/` |
| Python language, Python tooling, Python release changes | `01-python-mastery/` |
| C language, C standards, embedded C coding standards | `02-embedded-c-mastery/` |
| Code reading, code review, refactoring | `03-reading-and-reviewing-code/` |
| Design patterns, software architecture, system design | `04-architecture-and-design-patterns/` |
| Testing, TDD, property-based testing, embedded unit testing | `05-testing-and-quality/` |
| Networking, APIs, databases, infrastructure, observability | `06-systems-and-infrastructure/` |
| Embedded systems, RTOS, MCU architecture, state machines | `07-embedded-systems-and-rtos/` |
| Firmware build systems and toolchains, linker scripts, debug probes, tracing (SWO/RTT), fault and reset telemetry, bootloaders and secure update | `12-firmware-toolchain-debug-and-observability/` |
| Hardware-in-the-loop testing, firmware simulation in CI, instrument control (SCPI, VISA), lab automation | `13-hil-testing-and-lab-automation/` |
| Performance, profiling, optimization | `01-python-mastery/` (Python) or `12-firmware-toolchain-debug-and-observability/` (firmware timing and tracing); there is no dedicated section |
| Security vulnerabilities, secure coding, product-security regulation, SRE, reliability | `08-security-and-reliability/` |
| AI coding tools, context engineering, agent workflows, evidence on AI productivity | `09-agentic-ai-workflows/` |
| Git, CI/CD, collaboration | `10-version-control-and-collaboration/` |
| Career growth, technical leadership, documentation | `11-professional-practice/` |

PROGRESS.md headings use the form `## Section NN — Title`; add each new checkbox under the heading whose number matches the target directory.

## Verification & Curation Rules (mandatory)

Earlier AI-generated updates to this repo introduced fabricated authors, resources that don't exist, and links to the wrong papers (all fixed in the October 2026 review — see `reviews/2026-10-deep-dive/`). Every update must follow these rules:

1. **Open every link before adding it.** Fetch the arXiv abs page, the DOI record (`https://api.crossref.org/works/<DOI>`), the official page, or the YouTube oEmbed record (`https://www.youtube.com/oembed?url=<url>&format=json`) and confirm the exact title, author order, year, and edition. Never write a URL or an author list from memory.
2. **Cite people, not organizations,** when a work lists authors ("Templeton et al.", not "Anthropic").
3. **When in doubt, leave it out.** List doubtful or unverifiable candidates in your summary instead of adding them.
4. **Correct, don't just append.** Fix wrong metadata in place. If a resource is superseded or dead, say so in its description and in your summary. (Append-only means don't silently delete — it does not mean leave errors.)
5. **Keep the learning layer whole.** A new resource goes into the section table, its Suggested Order, and `PROGRESS.md`. A new section must ship with the full anatomy — Why · Prerequisites · 🎯 Learning Objectives · Resources · Suggested Order · 🛠️ Practice (+ 🏗️ mini-project) · ✅ Check Yourself — plus a PROGRESS block (see the root `.agents/skills/audit-curriculum/SKILL.md`). Append new sections at the next number and state where to take them; don't renumber.
6. **Markers are closed lists.** ⭐ only for items on this curriculum's named list. Use 🔑 sparingly — at most 3 core items per section (trimmed to this on 2026-10-13). Each section's Suggested Order opens with a "**Core path (🔑):**" line naming its 🔑 items; if you add or remove a 🔑, update that line too.
7. **Label speculation and advocacy as such** (e.g. unconfirmed theories, price models, vendor claims), and prefer measured evidence.
8. **Run `python tools/check_repo.py`** from the repo root before finishing — it must report 0 problems.
9. **One home per topic.** Check the overlap table in `STUDY-GUIDE.md`. If a resource's topic lives in another curriculum, cross-link to it there instead of adding a duplicate row.

## Notes

- **Append-only** — never remove existing entries from the curriculum
- **Verify before adding** — fetch every new link and confirm title, author(s), year, and edition on the web; never add a URL you have not opened. Earlier AI-generated content in this repo contained hallucinated citations and broken internal links.
- Maintain consistent formatting with existing tables
- Always include direct links (prefer official docs, free resources, or author pages)
- When in doubt, leave it out — list doubtful candidates in your summary instead of adding them
- **Section 09 (Agentic AI Workflows) is the fastest-evolving section** — prioritize checking this area for updates. AI coding tools and practices change rapidly; this section should be reviewed more frequently than others.
