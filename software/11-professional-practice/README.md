# Professional Practice and Technical Leadership

## Why This Section Matters

Senior architects don't just understand code — they make decisions, communicate trade-offs, write documentation, and lead technical direction. These soft skills multiply your impact.

---

## Prerequisites

- All previous sections (00–10)

---

## 🎯 Learning Objectives

After this section you can:
- Write ADRs and design docs that let a cold reader reconstruct the decision, the alternatives considered and the trade-offs.
- Produce calibrated estimates — ranges with a stated confidence — and measure your own calibration over time.
- Draft a team AI-use policy that sets review depth by risk, data-handling rules and attribution, and stress-test it against concrete scenarios.
- Synthesize individual decisions into a one-page engineering strategy using Larson's design-docs-to-strategy method.
- Give review feedback that teaches (severity labels, rationale, acknowledgment of what's good) and write review norms for a team.

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Book | The Software Engineer's Guidebook | Gergely Orosz | — | Career navigation from senior to staff+ engineer. Covers everything from coding interviews to organizational impact. Practical and modern. |
| 🔑 | Book | Staff Engineer: Leadership Beyond the Management Track | Will Larson | [Link](https://staffeng.com/) | What staff engineers actually do. Archetypes, operating models, and how to create impact without direct authority. |
| | Book | An Elegant Puzzle: Systems of Engineering Management | Will Larson | — | Engineering org design. How teams, processes, and systems interact. Valuable even for ICs who want to understand the environment they work in. |
| 🔑 | Newsletter | The Pragmatic Engineer | Gergely Orosz | [Link](https://blog.pragmaticengineer.com/) | Industry insights and practices from inside Big Tech and high-growth startups. The best engineering newsletter for career growth. |
| | Concept | Technical decision-making | — | — | ADRs (Architecture Decision Records). Document the *why* behind decisions so future you (and future AI) can understand the reasoning. |
| | Concept | Writing technical documentation | — | — | RFCs, design docs, runbooks. Clear writing is the highest-leverage skill for a senior engineer. |
| | Concept | Estimating and planning | — | — | Breaking work down, communicating timelines, managing expectations. The skill most engineers underinvest in. |
| | Concept | Mentoring and code review culture | — | — | Building team quality standards. Code review is teaching, not gatekeeping. |
| 🤖 | Concept | Leading in the AI era | — | — | Setting team AI policies, reviewing AI adoption, maintaining code quality standards. Define when and how your team uses AI tools. |
| | Book | The Manager's Path | Camille Fournier | — | Even for ICs, understanding management helps you work with managers effectively and decide if leadership is your path. |
| | Article | Documenting Architecture Decisions | Michael Nygard | [Link](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | 2011. The post that introduced ADRs: one short record per decision with Title, Context, Decision, Status, Consequences. Start here for the "Technical decision-making" row. |
| 🔑 | Framework (Free) | Diátaxis | Daniele Procida | [Link](https://diataxis.fr/) | Organize documentation by what the reader needs: tutorials, how-to guides, reference, explanation. The fix for docs that blur all four, and clearly typed docs make better context for coding agents too. |

---

## Suggested Order

1. **The Software Engineer's Guidebook** — Start here for a comprehensive map of the senior→staff engineer journey.
2. **The Pragmatic Engineer newsletter** — Subscribe and read regularly. Stay current on industry practices.
3. **Staff Engineer** — Read to understand what staff-level impact looks like in practice.
4. **Technical decision-making (ADRs) + Documenting Architecture Decisions** — Read Nygard's post, then start writing Architecture Decision Records for your projects.
5. **Writing technical documentation + Diátaxis** — Practice writing RFCs and design docs, and structure user docs by reader need. Clear writing = clear thinking.
6. **Estimating and planning** — Learn to break work down and communicate realistic timelines.
7. **Mentoring and code review culture** — Build the habit of teaching through code review.
8. **Leading in the AI era** — Define your team's AI policies and quality standards.
9. **An Elegant Puzzle** — Read to understand engineering organizations as systems.
10. **The Manager's Path** — Read to understand your managers and decide your own career direction.

---

## 🛠️ Practice

1. **Backfill three ADRs** — Pick three decisions already made in your projects, e.g., RTOS vs superloop, COBS vs SLIP framing, or uv vs pip-tools. Write an ADR for each in Michael Nygard's format (Title, Context, Decision, Status, Consequences), including the alternatives you rejected and why. Done when a colleague or a fresh agent session, given only the ADRs, correctly answers "why not X?" for every rejected option. *(~3 h · technical decision-making (ADRs))*
2. **Calibration log** — For your next ten tasks, mixing agent-assisted and hand-done work, write down a 90% confidence interval for the effort before you start, and the actual effort when you finish. Then compute:
   - your hit rate (target ≈ 9 out of 10);
   - the median ratio of actual to estimate;
   - whether agent-assisted tasks are more or less predictable than hand-done ones.

   Done when you've changed one thing about how you estimate, based on the data. *(~1 h setup + 2–3 weeks of logging · estimating and planning; the tech-lead material in Orosz's The Software Engineer's Guidebook)*
3. **Team AI policy** — Draft a one-to-two-page AI-use policy for a small hardware/firmware team. Cover:
   - approved tools;
   - data that must never be pasted: secrets, customer data, unreleased designs;
   - required review depth by risk class, e.g., bootloader and security code vs test scripts;
   - commit attribution and licensing/IP checks;
   - how AI-written tests get validated.

   Stress-test it with five scenarios — for example, an agent proposes a bootloader change; a contractor pastes a customer's log into a chatbot; an AI-written test suite is the only evidence for a release. Done when the text alone gives an unambiguous answer for every scenario. *(~3 h · leading in the AI era; The Pragmatic Engineer newsletter)*
4. **Review-comment audit** — Collect your last 30 code-review comments, either ones you gave or AI-reviewer comments you accepted. Classify each on four questions: Was a severity label used? Was a rationale given? Is it teaching or gatekeeping? What's the tone? Rewrite the five weakest using Google's "How to Write Code Review Comments" (from Section 03). Then write half a page of review norms for your team. *(~2 h · mentoring and code-review culture)*
5. **Model a team system** — Through Larson's systems-thinking lens in *An Elegant Puzzle* (stocks, flows, feedback), model a dynamic you live with as a 30-line Python simulation. One example is open firmware bugs: inflow is bugs found per week, outflow is bugs fixed per engineer-week. Then test a policy change: agents double fix throughput, but less-reviewed code raises inflow by 30%. Done when you can state the new steady state and name the highest-leverage variable. *(~2 h · Larson, An Elegant Puzzle)*

**🏗️ Mini-project — Decision Portfolio:** Pick a real upcoming decision, such as the firmware-update architecture from Sections 07–08 or the test-data backend from Section 06.
- **Design doc:** write at most six pages covering context, goals and non-goals, the proposal, alternatives with rejection reasons tied to the goals, security/testability/observability, rollout and rollback, and open questions. Start from a template in Orosz's "Companies Using RFCs or Design Docs and Examples of These".
- **Review:** run an async review with an AI red-team prompt plus at least one human, and record the outcome as an ADR.
- **Strategy:** following the advice in Larson's *Staff Engineer* guides — "write five design documents, and pull the similarities out" — synthesize this doc and your three ADRs into a one-page engineering strategy.

Deliverable: `projects/software/11-decision-portfolio/`. Success: every review comment is resolved, or explicitly declined with a reason, and a cold reader can state in three sentences the decision, the strongest rejected alternative and the strategy's two main rules. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What sections does a Nygard-style ADR have? Why is an accepted ADR superseded rather than edited?
2. How does a design doc/RFC differ from an ADR in purpose, length and timing?
3. Name Larson's four staff-engineer archetypes. Which one best fits a founder-engineer in a small hardware company, and why?
4. In Larson's model, how do design docs become a strategy, and how do strategies become a vision?
5. Your 90% intervals contained the actual value only 5 times out of 10. What does that tell you, and what two adjustments would you make?
6. Misconception check: "Documentation slows a small team down." When does a design doc save time, and when is it waste?
7. Name three rules an AI-use policy for firmware should contain, and the risk each one controls.
8. Explain to a smart friend in three sentences what separates staff-level impact from being a very good senior engineer.
