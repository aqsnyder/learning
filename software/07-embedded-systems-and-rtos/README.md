# Embedded Systems and RTOS

## Why This Section Matters

Embedded systems have unique constraints — real-time deadlines, limited memory, hardware interfaces — that require architectural judgment AI tools can't provide. This is where your hardware background meets software mastery.

---

## Prerequisites

- [Section 02 — Embedded C Mastery](../02-embedded-c-mastery/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Trace a FreeRTOS context switch on Cortex-M33 from an API call through PendSV and the scheduler, and confirm the sequence on hardware.
- Demonstrate priority inversion on a board, and choose correctly between binary semaphores, mutexes, queues and task notifications.
- Perform rate-monotonic analysis (utilization bound plus exact response-time analysis) and compare it with measured worst-case response.
- Structure firmware as active objects driven by hierarchical state machines, and unit-test the state machines off-target.
- Diagnose HardFaults and stack overflows from the fault-status registers, the stacked exception frame and a saved core dump.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| | Book | Making Embedded Systems (2nd ed) | Elecia White | 2024 | — | Architecture and design patterns for embedded — hardware/software interfaces, state machines, power management, and testable firmware design. |
| 🔑 | YouTube | Modern Embedded Systems Programming | Quantum Leaps (Miro Samek) | — | [Link](https://www.youtube.com/@StateMachineCOM) | Professional embedded practices from bare-metal up. Covers registers, interrupts, state machines, and RTOS concepts with hands-on board demos. |
| 🔑 | RTOS | FreeRTOS | — | — | [Link](https://www.freertos.org/) | THE open-source RTOS. Start here — tasks, queues, semaphores, timers. Massive community, runs on everything from Cortex-M0 to ESP32. |
| | RTOS | Zephyr Project | Linux Foundation | — | [Link](https://zephyrproject.org/) | Modern, Linux Foundation–backed RTOS. Growing fast with excellent driver support, Bluetooth/networking stacks, and a CMake-based build system. |
| | Concept | Task scheduling | — | — | — | Preemptive vs cooperative scheduling, priority inversion, rate-monotonic analysis, and real-time guarantees. |
| | Concept | Mutexes, semaphores, and queues | — | — | — | Inter-task communication and synchronization primitives. Understand when to use each and the pitfalls (deadlocks, priority inversion). |
| | Concept | State machines and event-driven firmware | — | — | — | The Samek approach — hierarchical state machines (UML statecharts) as the backbone of robust, maintainable firmware architecture. |
| | Concept | DMA, interrupts, and peripheral drivers | — | — | — | Hardware-software boundary: interrupt priorities (NVIC), DMA transfers, and writing clean peripheral abstraction layers. |
| | Concept | Bootloaders and OTA updates | — | — | — | Field-updatable firmware: dual-bank architectures, secure boot, image signing, and rollback strategies. |
| | Concept | Debugging embedded systems | — | — | — | JTAG/SWD debugging, logic analyzers, oscilloscopes, and printf-over-RTT. The tools and techniques for when things go wrong at the hardware level. |
| | Blog | Embedded Artistry | Phillip Johnston | — | [Link](https://embeddedartistry.com/) | Testable, modular firmware — clean C architecture, build systems, testing strategies, and professional embedded development practices. |
| | Blog | Interrupt (Memfault) | Memfault team | — | [Link](https://interrupt.memfault.com/) | Professional firmware engineering articles covering debugging, RTOS internals, OTA, fault handling, and embedded best practices. |
| | Tool | CMake for embedded | — | — | — | Cross-compilation toolchains, toolchain files, and managing multi-target embedded builds with modern CMake. |
| | Tool | GDB for embedded | — | — | — | JTAG/SWD debugging with GDB — connecting via OpenOCD/J-Link, setting hardware breakpoints, and inspecting registers. |
| 🔑 | Book | Definitive Guide to Arm Cortex-M23 and Cortex-M33 Processors | Joseph Yiu | 2020 | [Link](https://shop.elsevier.com/books/definitive-guide-to-arm-cortex-m23-and-cortex-m33-processors/yiu/978-0-12-820735-2) | The architecture reference for Armv8-M cores such as the Cortex-M33 in STM32U5 parts: exception and interrupt model, MPU, fault handling, FPU/DSP, debug and trace, and TrustZone security. Read it alongside your part's reference manual. |
| | Book (Free) | Mastering the FreeRTOS Real Time Kernel: A Hands-On Tutorial Guide | Richard Barry and the FreeRTOS team | 2023 | [Link](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book) | The official FreeRTOS tutorial book, now maintained openly on GitHub (CC BY-SA): tasks, queues, software timers, interrupt management, resource management, event groups, task notifications. |
| | Book (Free) | Practical UML Statecharts in C/C++ (2nd ed) | Miro Samek | 2008 | [Link](https://www.state-machine.com/psicc2) | The book behind "the Samek approach" above: hierarchical state machines and active objects for event-driven embedded C, and the design of the QP framework. Free PDF from the author. |
| | Article | How to debug a HardFault on an ARM Cortex-M MCU | Chris Coleman (Memfault) | 2019 | [Link](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug) | Decode CFSR/HFSR/BFAR, recover the stacked registers and call stack, and capture fault data for post-mortem analysis, with worked examples. Keep it open the first time a board faults. |
| | Article series | From Zero to main(): Bare metal C | François Baldassari (Memfault) | 2019 | [Link](https://interrupt.memfault.com/blog/zero-to-main-1) | What runs between reset and `main()`: vector table, startup code, `.data`/`.bss` initialization. Follow-up parts demystify linker scripts and bootstrapping newlib. Read before editing a linker script or CMake toolchain file. |
| | Book (Free) | The Embedded Rust Book | Rust Embedded WG (resources team) | — | [Link](https://docs.rust-embedded.org/book/) | Optional: embedded Rust on Cortex-M (examples on an STM32F3DISCOVERY), written for people who already know Rust basics and embedded C. Use it to evaluate Rust for new firmware; vendor HALs and RTOSes remain C-first. |

---

## Suggested Order

**Core path (🔑):** Quantum Leaps videos → Yiu's Cortex-M23/M33 guide → FreeRTOS

1. **Miro Samek — Modern Embedded Systems Programming (YouTube)** — Start here for a visual, hands-on introduction from bare-metal up.
2. **Making Embedded Systems (Elecia White)** — Read alongside for the architectural perspective: design patterns, state machines, and system decomposition.
3. **From Zero to main()** — Learn what happens before `main()`: startup code, vector table, memory initialization.
4. **Definitive Guide to Cortex-M23/M33 (Yiu)** — Learn the core your MCU actually runs: exceptions, NVIC priorities, MPU, faults, TrustZone. Use as a reference from here on.
5. **FreeRTOS + Mastering the FreeRTOS Real Time Kernel** — Set up FreeRTOS on a dev board and work through the book. Implement tasks, queues, and semaphores on real hardware.
6. **Concepts: Task scheduling, mutexes/semaphores, interrupts/DMA** — Study these as you encounter them in FreeRTOS and Samek's videos.
7. **State machines and event-driven firmware + Practical UML Statecharts** — Dive deeper into the Samek approach once you've seen the basics.
8. **Embedded Artistry blog** — Read articles on modular firmware design, testing embedded code, and clean C architecture.
9. **Debugging (JTAG/SWD, GDB, logic analyzers) + the HardFault article** — Build debugging skills as you work on increasingly complex firmware. Go deeper in [Section 12](../12-firmware-toolchain-debug-and-observability/README.md) (OpenOCD, SWO/RTT tracing, reset telemetry).
10. **CMake for embedded** — Set up proper cross-compilation toolchains for your projects. Section 12 covers toolchain files, presets and reproducible builds.
11. **Bootloaders and OTA updates** — Study when you're ready to deploy firmware to the field. Section 12 covers MCUboot; Section 08 covers the threat model.
12. **Zephyr Project** — Explore as a modern RTOS alternative once you're comfortable with FreeRTOS.
13. **Interrupt (Memfault) blog** — Read ongoing articles to stay current on professional firmware engineering.
14. **The Embedded Rust Book** — Optional: evaluate Rust for a new, self-contained firmware project.

---

## 🛠️ Practice

1. **Read the kernel, then watch it run** — A low-priority task calls `xQueueSend()` while a higher-priority task is blocked on that queue. In FreeRTOS-Kernel, trace everything that happens until the woken task runs its first instruction, following the path through `queue.c`, `tasks.c` and the Cortex-M33 port (`portable/GCC/ARM_CM33_NTZ/non_secure/portasm.c`). Draw it as a sequence diagram that shows:
   - which registers the hardware stacks and which the port saves;
   - where the critical sections are;
   - where each task's PSPLIM gets loaded.

   Confirm the order with breakpoints on your board. *(~4 h · FreeRTOS kernel source; Interrupt, "ARM Cortex-M RTOS Context Switching"; Quantum Leaps #23–24 "RTOS Part-2" and "RTOS Part-3")*
2. **Priority inversion on the bench** — Create three tasks. Low and high share a resource; medium is CPU-bound. Guard the resource first with a binary semaphore, then with a mutex. Toggle one GPIO per task and capture the timeline on a logic analyzer, or with a trace tool such as SEGGER SystemView. Done when you have two captures (unbounded vs bounded blocking of the high-priority task), the measured worst-case blocking time for each, and an explanation of how `xTaskPriorityInherit()` changes the timeline. *(~4 h · FreeRTOS docs on mutexes vs binary semaphores; Quantum Leaps #28 "RTOS Part-7: Mutual exclusion mechanisms")*
3. **RMA by hand, then on the board** — Take this task set with rate-monotonic priorities (period / worst-case execution time):

   | Task | Period | WCET |
   |------|--------|------|
   | ADC | 1 ms | 0.15 ms |
   | Control | 10 ms | 2 ms |
   | Comms | 50 ms | 10 ms |
   | UI | 100 ms | 25 ms |

   Compute the utilization and compare it with the Liu–Layland bound, then run exact response-time analysis by iteration. You should find U = 0.80, above the four-task bound of ≈ 0.757, yet every deadline is met; the UI task's worst-case response is ≈ 69.5 ms. Find the largest UI execution time that still fits, and explain why it is so large (look at the periods). Then implement the set on FreeRTOS with calibrated busy-loops and measure worst-case response with GPIO toggles and a logic analyzer. Account for the gap between analysis and measurement: tick, context-switch and interrupt overhead. *(~4 h · task-scheduling concepts; Quantum Leaps #26 "RTOS Part-5: What is 'real-time'?" and #43 "Active Objects in Real-Time Part-1: Run-to-Completion and RMS/RMA")*
4. **Hierarchical state machine for a data logger** — Draw a UML statechart for a data logger:
   - a `Powered` superstate containing `Idle`, `Armed`, `Acquiring` and `Uploading`;
   - separate `Fault` and `LowPower` states;
   - `BATTERY_LOW` handled once, in `Powered`;
   - entry/exit actions that start and stop the ADC.

   Implement it in C, either hand-coded the Samek way or with QP/C and the QM tool. Unit-test every (state, event) pair off-target with Unity. Done when your transition table and tests agree cell for cell, and no leaf state mentions `BATTERY_LOW`. *(~5 h · Quantum Leaps #35–42 state-machine lessons, especially #40 "What is a Hierarchical State Machine?"; Making Embedded Systems ch. 6 "Managing the Flow of Activity"; Embedded Artistry's state-machine articles)*
5. **Fault forensics** — Provoke five faults on purpose:
   - a divide-by-zero with `DIV_0_TRP` set;
   - a read from an address with nothing behind it;
   - an undefined instruction;
   - an unaligned word access with `UNALIGN_TRP` set;
   - a task stack overflow caught by PSPLIM.

   For each fault, decode CFSR and HFSR (plus MMFAR/BFAR when they're valid) and the stacked PC and LR in GDB, down to the faulting source line. Then write a HardFault handler that saves the registers to a `.noinit` RAM region and prints them after the next reset. *(~4 h · Interrupt, "How to debug a HardFault on an ARM Cortex-M MCU"; Making Embedded Systems ch. 9 "Getting into Trouble"; GDB for embedded)*

**🏗️ Mini-project — Event-Driven Data Logger:** Turn exercise 4 into a FreeRTOS application built from active objects, each with its own queue and run-to-completion state machine. Include:
- ADC sampling via circular, double-buffered DMA whose half- and full-transfer interrupts only post events;
- a processing object;
- a link object that streams COBS-framed packets with sequence numbers over UART;
- RTT (Section 12) or SystemView tracing;
- the fault handler from exercise 5.

Build it with CMake and a cross-compilation toolchain file (set up in [Section 12](../12-firmware-toolchain-debug-and-observability/README.md)). Deliverable: `projects/software/07-event-logger/` plus a Python receiver. Success:
- a 24-hour soak shows zero sequence gaps;
- every task keeps at least 25% stack margin (`uxTaskGetStackHighWaterMark`);
- you report the measured worst-case ISR and event-handling latency.

Stretch: port one active object to Zephyr (Quantum Leaps #56) and compare footprint and latency. *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. On exception entry, which registers does Cortex-M hardware stack automatically, and which must the RTOS port save itself? Why does the context switch run in PendSV at the lowest priority?
2. In a dual-slot firmware update, what must the bootloader verify before jumping to a new image, and how does it recover if power fails mid-update?
3. FreeRTOS binary semaphore vs mutex: which has priority inheritance, and why must you never give a mutex from an ISR?
4. State the Liu–Layland utilization bound. Why can a task set above the bound still be schedulable?
5. A 10 kHz ADC interrupt takes 12 µs per run. What fraction of the CPU does it consume, and roughly how much does that stretch a task with 2 ms of work?
6. Misconception check: "Using an RTOS makes the firmware real-time." What actually decides whether deadlines are met?
7. After a HardFault, which registers tell you what happened and where? When can you trust the fault-address registers?
8. Explain to a smart friend in three sentences why active objects with state machines beat a superloop full of flags for device firmware.
