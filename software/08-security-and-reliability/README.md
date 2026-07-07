# Security and Reliability Engineering

## Why This Section Matters

AI-generated code can introduce subtle security vulnerabilities. You need to recognize injection flaws, buffer overflows, and insecure patterns in both Python and C — especially when reviewing code you didn't write.

---

## Prerequisites

- [Section 01 — Foundations](../01-foundations/README.md)
- [Section 02 — Core Programming](../02-core-programming/README.md)

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Web Resource | OWASP Top 10 | OWASP Foundation | [Link](https://owasp.org/www-project-top-ten/) | THE web vulnerability reference. Understand these ten categories and you'll catch the majority of web security issues in review. |
| 🔑 | Book | The Web Application Hacker's Handbook (2nd ed) | Dafydd Stuttard, Marcus Pinto | — | Practical web security from the attacker's perspective. Teaches you to think like an adversary when reviewing code. |
| 🔑🤖 | Concept | Reviewing AI-generated code for security | — | — | AI often introduces: hardcoded secrets, SQL injection, improper input validation, unsafe deserialization. Build a mental checklist for every AI-generated PR. |
| | Concept | Secure C programming | — | — | Buffer overflows, format string vulnerabilities, integer overflow. The classic low-level attack surface — critical for embedded work. |
| | Concept | Python security pitfalls | — | — | `eval()`, `pickle`, SSRF, path traversal. Python's dynamic nature makes it easy to write insecure code that *looks* clean. |
| | Tool | Bandit | PyCQA | [Link](https://bandit.readthedocs.io/) | Python security linter. Run it on every AI-generated Python file before review. |
| | Tool | Semgrep | Semgrep, Inc. | [Link](https://semgrep.dev/) | Static analysis for security patterns. Write custom rules to enforce your project's security policies. |
| | Concept | Threat modeling | — | — | STRIDE methodology for systematic security review. Ask: what can go wrong? before writing a line of code. |
| | Book (Free) | Site Reliability Engineering (Google SRE Book) | Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy | [Link](https://sre.google/sre-book/table-of-contents/) | Production reliability practices from Google. Error budgets, SLOs, incident management — the operational side of quality. |
| | Concept | Incident response and post-mortems | — | — | Blameless post-mortems, root cause analysis, and building a culture that learns from failures rather than hiding them. |

---

## Suggested Order

1. **OWASP Top 10** — Start here. Memorize the ten categories — they're the vocabulary of web security.
2. **Reviewing AI-generated code for security** — Build your security review checklist specifically for AI output.
3. **Python security pitfalls** — Learn the Python-specific footguns: `eval()`, `pickle`, path traversal.
4. **Secure C programming** — Buffer overflows, format strings, integer overflow — the embedded attack surface.
5. **Bandit + Semgrep** — Set up automated security linting in your workflow before manual review.
6. **The Web Application Hacker's Handbook** — Deep dive into the attacker's mindset. Read the chapters relevant to your stack.
7. **Threat modeling (STRIDE)** — Learn to think systematically about threats before writing code.
8. **Google SRE Book** — Read the chapters on monitoring, alerting, and incident management.
9. **Incident response and post-mortems** — Learn the operational discipline of learning from failures.
