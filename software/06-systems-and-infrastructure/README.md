# Systems Design and Infrastructure

## Why This Section Matters

Understanding how systems connect — APIs, databases, containers, deployment — is essential for architecting solutions and reviewing infrastructure code that AI agents generate.

---

## Prerequisites

- [Section 04 — Architecture and Design Patterns](../04-architecture-and-design-patterns/README.md)

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Designing Data-Intensive Applications | Martin Kleppmann | 2017 | — | Replication, partitioning, consistency, batch and stream processing. If not read in Section 04, start here. |
| 🔑 | Book | The Software Engineer's Guidebook | Gergely Orosz | 2023 | — | Practical senior engineer field guide covering career growth, code reviews, technical strategy, and team dynamics. |
| 🔑 | Newsletter | ByteByteGo | Alex Xu | — | [Link](https://bytebytego.com/) | System design visualized. Weekly breakdowns of how real-world systems — payment processing, rate limiting, CDNs — actually work. |
| | Tool | Docker | — | — | [Link](https://docs.docker.com/) | Containerization fundamentals. Understand images, containers, volumes, networks, and Docker Compose for local development. |
| | Tool | Git advanced workflows | — | — | — | Branching strategies (trunk-based, GitFlow), interactive rebasing, bisecting to find bugs, worktrees. |
| | Concept | REST API design and OpenAPI specifications | — | — | — | Designing clean APIs, versioning strategies, error handling conventions, and machine-readable API contracts. |
| | Concept | Database fundamentals | — | — | — | SQL vs NoSQL trade-offs, indexing strategies, query optimization, normalization vs denormalization, and choosing the right data store. |
| | Concept | Message queues and async processing | — | — | — | RabbitMQ, Redis, Celery — decoupling services, handling background jobs, and managing eventual consistency. |
| | Concept | Monitoring and observability | — | — | — | The three pillars: logging, metrics, and distributed tracing. Know how to diagnose production issues. |
| | Concept | Infrastructure as Code | — | — | — | Terraform, Ansible basics — declarative infrastructure, reproducible environments, and configuration management. |
| 🔑 | Book | System Design Interview (Vol 1 and 2) | Alex Xu | 2020–2022 | — | Step-by-step system design practice. Breaks down real problems: rate limiter, URL shortener, notification system, chat system, and more. |
| | Book | Release It! (2nd ed) | Michael Nygard | 2018 | — | Stability patterns for production systems — circuit breakers, bulkheads, timeouts, and designing for failure. |

---

## Suggested Order

1. **Designing Data-Intensive Applications** — The foundational text. Read first if you skipped it in Section 04.
2. **System Design Interview (Vol 1 and 2)** — Practice structured system design thinking with concrete examples.
3. **ByteByteGo newsletter** — Subscribe and read weekly to build system design intuition over time.
4. **Docker** — Get hands-on with containerization; you'll use it constantly.
5. **REST API design + OpenAPI** — Understand API contracts before building or reviewing them.
6. **Database fundamentals** — SQL, indexing, and choosing the right data store for the problem.
7. **Git advanced workflows** — Level up from basic Git to power-user workflows.
8. **Message queues and async processing** — Learn when and how to decouple with RabbitMQ/Redis/Celery.
9. **The Software Engineer's Guidebook** — Read for the senior engineer perspective on technical strategy and leadership.
10. **Monitoring and observability** — Understand how to diagnose production systems.
11. **Infrastructure as Code** — Learn Terraform/Ansible basics when you start managing environments.
12. **Release It!** — Read when you're designing systems that need to survive real-world failure modes.
