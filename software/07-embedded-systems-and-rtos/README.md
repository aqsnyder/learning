# Embedded Systems and RTOS

## Why This Section Matters

Embedded systems have unique constraints — real-time deadlines, limited memory, hardware interfaces — that require architectural judgment AI tools can't provide. This is where your hardware background meets software mastery.

---

## Prerequisites

- [Section 02 — C Fundamentals](../../software/02-c-fundamentals/README.md)

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Making Embedded Systems (2nd ed) | Elecia White | 2024 | — | Architecture and design patterns for embedded — hardware/software interfaces, state machines, power management, and testable firmware design. |
| 🔑 | YouTube | Modern Embedded Systems Programming | Quantum Leaps (Miro Samek) | — | [Link](https://www.youtube.com/@StateMachineCOM) | Professional embedded practices from bare-metal up. Covers registers, interrupts, state machines, and RTOS concepts with hands-on board demos. |
| 🔑 | RTOS | FreeRTOS | — | — | [Link](https://www.freertos.org/) | THE open-source RTOS. Start here — tasks, queues, semaphores, timers. Massive community, runs on everything from Cortex-M0 to ESP32. |
| | RTOS | Zephyr Project | Linux Foundation | — | [Link](https://zephyrproject.org/) | Modern, Linux Foundation–backed RTOS. Growing fast with excellent driver support, Bluetooth/networking stacks, and a CMake-based build system. |
| | Concept | Task scheduling | — | — | — | Preemptive vs cooperative scheduling, priority inversion, rate-monotonic analysis, and real-time guarantees. |
| | Concept | Mutexes, semaphores, and queues | — | — | — | Inter-task communication and synchronization primitives. Understand when to use each and the pitfalls (deadlocks, priority inversion). |
| | Concept | State machines and event-driven firmware | — | — | — | The Samek approach — hierarchical state machines (UML statecharts) as the backbone of robust, maintainable firmware architecture. |
| | Concept | DMA, interrupts, and peripheral drivers | — | — | — | Hardware-software boundary: interrupt priorities (NVIC), DMA transfers, and writing clean peripheral abstraction layers. |
| | Concept | Bootloaders and OTA updates | — | — | — | Field-updatable firmware: dual-bank architectures, secure boot, image signing, and rollback strategies. |
| | Concept | Debugging embedded systems | — | — | — | JTAG/SWD debugging, logic analyzers, oscilloscopes, and printf-over-RTT. The tools and techniques for when things go wrong at the hardware level. |
| 🔑 | Blog | Embedded Artistry | Phillip Johnston | — | [Link](https://embeddedartistry.com/) | Testable, modular firmware — clean C architecture, build systems, testing strategies, and professional embedded development practices. |
| | Blog | Interrupt (Memfault) | Memfault team | — | [Link](https://interrupt.memfault.com/) | Professional firmware engineering articles covering debugging, RTOS internals, OTA, fault handling, and embedded best practices. |
| | Tool | CMake for embedded | — | — | — | Cross-compilation toolchains, toolchain files, and managing multi-target embedded builds with modern CMake. |
| | Tool | GDB for embedded | — | — | — | JTAG/SWD debugging with GDB — connecting via OpenOCD/J-Link, setting hardware breakpoints, and inspecting registers. |

---

## Suggested Order

1. **Miro Samek — Modern Embedded Systems Programming (YouTube)** — Start here for a visual, hands-on introduction from bare-metal up.
2. **Making Embedded Systems (Elecia White)** — Read alongside for the architectural perspective: design patterns, state machines, and system decomposition.
3. **FreeRTOS** — Set up FreeRTOS on a dev board. Implement tasks, queues, and semaphores on real hardware.
4. **Concepts: Task scheduling, mutexes/semaphores, interrupts/DMA** — Study these as you encounter them in FreeRTOS and Samek's videos.
5. **State machines and event-driven firmware** — Dive deeper into the Samek approach once you've seen the basics.
6. **Embedded Artistry blog** — Read articles on modular firmware design, testing embedded code, and clean C architecture.
7. **Debugging (JTAG/SWD, GDB, logic analyzers)** — Build debugging skills as you work on increasingly complex firmware.
8. **CMake for embedded** — Set up proper cross-compilation toolchains for your projects.
9. **Bootloaders and OTA updates** — Study when you're ready to deploy firmware to the field.
10. **Zephyr Project** — Explore as a modern RTOS alternative once you're comfortable with FreeRTOS.
11. **Interrupt (Memfault) blog** — Read ongoing articles to stay current on professional firmware engineering.
