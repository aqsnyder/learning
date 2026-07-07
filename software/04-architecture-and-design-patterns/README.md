# Software Architecture and Design Patterns

## Why This Section Matters

Architecture is the skill AI cannot replace. Understanding system design, design patterns, and architectural trade-offs is what makes you the decision-maker, not the typist.

---

## Prerequisites

- [Section 01](../../software/01-python-fundamentals/README.md) through [Section 03](../../software/03-git-and-collaboration/README.md)

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Fundamentals of Software Architecture | Mark Richards, Neal Ford | 2020 | — | THE architecture primer for transitioning from developer to architect. Covers architecture styles, component design, and the soft skills of architecture. |
| 🔑 | Book | Software Architecture: The Hard Parts | Neal Ford, Mark Richards et al. | 2021 | — | Trade-offs when there's no right answer — service granularity, data decomposition, contracts, and distributed workflows. |
| 🔑 | Book | Clean Architecture | Robert C. Martin | 2017 | — | SOLID principles, dependency inversion, and separating business logic from frameworks. The architectural counterpart to Clean Code. |
| 🔑 | Book | A Philosophy of Software Design | John Ousterhout | 2018 | — | Complexity management through deep modules and strategic programming. Complements and challenges some Clean Code dogma. |
| 🔑 | Book | Design Patterns: Elements of Reusable Object-Oriented Software | Gamma, Helm, Johnson, Vlissides (Gang of Four) | 1994 | — | The classic patterns vocabulary — Strategy, Observer, Factory, Decorator, etc. Read for recognition, not memorization. |
| | Book | Head First Design Patterns (2nd ed) | Eric Freeman, Elisabeth Robson | 2020 | — | A more accessible, visual introduction to design patterns. Good if GoF feels too dense. |
| 🔑 | Book | Designing Data-Intensive Applications (DDIA) | Martin Kleppmann | 2017 | — | THE distributed systems bible — replication, partitioning, consistency, batch/stream processing. Essential for any systems architect. |
| | Newsletter | ByteByteGo | Alex Xu | — | [Link](https://bytebytego.com/) | Visual system design explanations. Excellent for building intuition about how real-world systems are built. |
| 🔑 | Video | System Design Interview channel | — | — | [Link](https://www.youtube.com/@SystemDesignInterview) | Practical architecture walkthroughs for real-world system design problems. |
| | Book | The Pragmatic Programmer (20th Anniversary) | Andrew Hunt, David Thomas | 2019 | — | Engineering mindset — DRY, orthogonality, tracer bullets, and pragmatic thinking about software craft. |
| | Book | Domain-Driven Design | Eric Evans | 2003 | — | Aligning code structure with business domains. Essential vocabulary: bounded contexts, aggregates, ubiquitous language. |
| | Concept | SOLID principles | — | — | — | Recognize violations in code review: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion. |
| | Concept | Microservices vs monolith trade-offs | — | — | — | When to decompose, when to stay monolithic, and how to evaluate the distributed systems tax. |
| | Concept | Event-driven architecture, CQRS, and event sourcing | — | — | — | Decoupling through events, separating reads from writes, and using event logs as the source of truth. |

---

## Suggested Order

1. **A Philosophy of Software Design** — Start with complexity management fundamentals. Short, opinionated, and immediately applicable.
2. **Clean Architecture** — Build on that with SOLID principles and dependency boundaries.
3. **Design Patterns (GoF or Head First)** — Learn the shared vocabulary; focus on recognizing patterns in existing code.
4. **Fundamentals of Software Architecture** — Step up to system-level thinking: architecture styles, trade-off analysis, and the architect's role.
5. **Designing Data-Intensive Applications** — Deep-dive into distributed systems, data storage, and consistency models.
6. **Software Architecture: The Hard Parts** — Tackle the messy, real-world decomposition decisions.
7. **System Design Interview channel + ByteByteGo** — Practice applying architectural thinking to concrete system design problems.
8. **Domain-Driven Design** — Read when you're working on complex business domains and need strategic modeling.
9. **The Pragmatic Programmer** — Weave in throughout as an engineering mindset companion.
10. **Concepts (SOLID, microservices, event-driven)** — Revisit as they arise in your architecture reading and code reviews.
