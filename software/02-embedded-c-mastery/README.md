# Embedded C Mastery

> **Why this section matters:** Embedded C is where software meets hardware. Reading firmware code requires understanding memory layout, register manipulation, and real-time constraints — skills that AI agents struggle with and that demand human architectural judgment.

**Prerequisites:** Basic programming.

---

## Resources

| # | Type | Resource | Notes |
|---|------|----------|-------|
| 1 | 🔑 Book | *The C Programming Language* (K&R, 2nd ed) — Kernighan and Ritchie (1988) | THE definitive C reference |
| 2 | 🔑 Book | *Expert C Programming: Deep Secrets* — Peter van der Linden | Linking, memory, and advanced C |
| 3 | 🔑 Book | *Making Embedded Systems* (2nd ed) — Elecia White (2024) | Best intro to embedded architecture and design patterns |
| 4 | Book | *Embedded Software Design* — Jacob Beningo | Modern firmware architecture and maintainability |
| 5 | Book | [*Embedded C Coding Standard*](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — Barr Group | Minimizing bugs and improving portability |
| 6 | 🔑 YouTube | [Modern Embedded Systems Programming — Quantum Leaps (Miro Samek)](https://www.youtube.com/@StateMachineCOM) | Gold standard for embedded concepts and state machines |
| 7 | 🔑 Blog | [Embedded Artistry](https://embeddedartistry.com/) | Modular, testable firmware architecture articles |
| 8 | Blog | [Jacob Beningo](https://beningo.com/) | Firmware architecture best practices |
| 9 | Course | FastBit Embedded Brain Academy (Udemy) | ARM Cortex-M, bare-metal, RTOS |

### Key Concepts

| Concept | Why It Matters |
|---------|---------------|
| Pointers, memory layout, and stack vs heap | Read C code without confusion |
| `volatile`, `const`, and `static` qualifiers | Critical for embedded correctness |
| Register manipulation and memory-mapped I/O | Hardware-software interface |
| Interrupt handling and ISR design | Real-time responsiveness |
| HAL (Hardware Abstraction Layer) design | Decoupling hardware from logic |

---

## Suggested Order

```
1. K&R (read cover-to-cover, it's short)
2. Making Embedded Systems (embedded architecture and thinking)
3. Expert C Programming (fill in the deep C knowledge)
4. Quantum Leaps YouTube (state machines and real-time patterns)
5. Embedded Artistry blog (ongoing reference for firmware design)
6. Embedded C Coding Standard (adopt as your style guide)
```
