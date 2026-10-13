# Firmware Toolchain, Debug, and Observability

## Why This Section Matters

Section 07 is about how firmware should be structured. This section is about the machinery you use every day to build it, load it, see inside it while it runs, and find out what went wrong after it has shipped. It is also where coding agents are weakest: an agent can't see a bus fault, a section linked to the wrong address, or a DMA transfer that never finished. It can only check its work if you give it a build it can run in one command, logs it can read, and a fault record it can decode. On a Cortex-M33, with TrustZone, a secure-boot chain and several debug channels to choose from, these skills are worth learning on purpose rather than picking up by accident.

---

## Prerequisites

- [Section 02 — Embedded C Mastery](../02-embedded-c-mastery/README.md), including its "Where does it live?" exercise
- [Section 07 — Embedded Systems and RTOS](../07-embedded-systems-and-rtos/README.md), especially *From Zero to main()*, the HardFault article and Yiu's Cortex-M33 guide. This section builds on them and doesn't repeat them.

> Recommended position: right after Section 07's reading, and before Section 07's mini-project, which uses this section's build and tracing setup.

---

## 🎯 Learning Objectives

After this section you can:
- Build Cortex-M33 firmware from a clean clone with one command (CMake, a toolchain file and presets), and explain every compiler and linker flag that changes the image.
- Change the memory layout: reserve a `.noinit` region, split bootloader from application, run code from RAM. Then prove from the map file and on hardware that startup still behaves.
- Debug from the command line with OpenOCD and GDB (hardware breakpoints, watchpoints, peripheral registers), and choose between semihosting, UART, SWO/ITM, RTT and a GPIO toggle on a logic analyzer for a given timing budget.
- Classify every reset (fault, watchdog, brown-out, software, power-on) from data that survives it, and symbolize the record on the host without a debugger attached.
- Bring up a signed, test-then-confirm firmware update with MCUboot, and explain what each image slot and check protects against.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Professional CMake: A Practical Guide (22nd ed) | Craig Scott | — | [Link](https://crascit.com/professional-cmake/) | Written by a CMake co-maintainer and revised continually; the 22nd edition covers CMake 4.2. For firmware, read the "Toolchains And Cross Compiling" chapter first and use the rest as a reference. Digital only (PDF/EPUB). |
| 🔑 | Tool | OpenOCD (Open On-Chip Debugger) | OpenOCD project | 2023 (0.12.0) | [Link](https://openocd.org/) | Open-source debug server: drives ST-LINK, J-Link and CMSIS-DAP probes over SWD/JTAG, programs flash, and serves GDB. Release 0.12.0 added flash support for STM32U57x/U58x; check that your exact part is supported. Many IDE debug configurations run OpenOCD or a vendor GDB server underneath. |
| | Tool | SEGGER RTT (Real Time Transfer) | SEGGER | — | [Link](https://kb.segger.com/RTT) | Bidirectional I/O through ring buffers in target RAM, read by a J-Link over SWD while the core runs. It needs no extra pins, is far faster than semihosting, and works on parts with no SWO pin. In non-blocking mode the firmware keeps its real-time behavior with no host attached. SEGGER documents it for J-Link probes; if you use another probe, check whether your debug server supports RTT. |
| | Tool | sigrok / PulseView | sigrok project | — | [Link](https://sigrok.org/) | Open-source (GPL) signal-analysis suite for logic analyzers, scopes, multimeters and other bench gear, with stackable protocol decoders written in Python. PulseView is the GUI; the command-line frontend lets test scripts capture and decode. |
| | Tool | MCUboot | MCUboot project (mcu-tools) | — | [Link](https://docs.mcuboot.com/) | Open-governance secure bootloader for 32-bit MCUs: a common flash layout for updates, image signing and key management with `imgtool`, optional encrypted images, and serial recovery via MCUmgr. Runs under Zephyr, NuttX, Mynewt and others. Worth reading even if you keep your own bootloader. |
| | Concept | Linker scripts, map files, and memory budgets | — | — | [Sec 07](../07-embedded-systems-and-rtos/README.md) | Memory regions and output sections, how `.data` is copied and `.bss` zeroed, `.noinit` RAM, bootloader and application slots, code in RAM, and reading a map file to see what is eating flash. Start from the linker-script and newlib parts of *From Zero to main()* in Section 07. |
| | Concept | SWO/ITM tracing and DWT cycle counting | — | — | [Sec 07](../07-embedded-systems-and-rtos/README.md) | printf-style tracing and timestamps over the single-wire output pin, and the DWT cycle counter for timing code in clock cycles. Yiu's Cortex-M33 guide (Section 07) introduces the debug and trace hardware. |
| | Concept | Reset-cause and fault telemetry | — | — | [Sec 07](../07-embedded-systems-and-rtos/README.md) | Fault registers, the stacked frame, reset-cause flags, watchdog and assert information saved across a reset, then reported and symbolized on the host. Builds on Section 07's HardFault article and the Interrupt blog. |
| | Concept | TrustZone-M builds and debugging | — | — | [Sec 07](../07-embedded-systems-and-rtos/README.md) | Separate secure and non-secure images, non-secure-callable entry points, and what a debugger can see in each security state. Yiu's guide (Section 07) covers TrustZone in depth. |
| 🤖 | Concept | Firmware an agent can verify | — | — | [Sec 09](../09-agentic-ai-workflows/README.md) | A one-command build, a flash-and-run script that exits non-zero on failure, and machine-readable logs over RTT or UART. Without them a coding agent can only claim the firmware works; with them it can check. |

---

## Suggested Order

1. **Linker scripts, map files, and memory budgets** — Re-read the linker-script and newlib parts of *From Zero to main()* (Section 07) with your own project's linker script and map file open.
2. **Professional CMake** — Read "Toolchains And Cross Compiling", then write a toolchain file and presets for your board.
3. **OpenOCD** — Flash and debug from the command line with GDB, not only from the IDE.
4. **SWO/ITM tracing and DWT cycle counting** — Add timestamps and cycle-accurate measurements.
5. **SEGGER RTT** — Add a log channel that barely disturbs timing.
6. **sigrok / PulseView** — Capture GPIO and bus traffic next to your logs, and decode the protocols.
7. **Reset-cause and fault telemetry** — Grow Section 07's HardFault handler into a record of every reset.
8. **TrustZone-M builds and debugging** — Split one project into secure and non-secure images.
9. **MCUboot** — Design the update path: slots, signing, test-then-confirm, revert.
10. **Firmware an agent can verify** — Wrap all of it in scripts, and document them in an AGENTS.md.

---

## 🛠️ Practice

1. **Reshape the memory map** — Start from the map file you produced in Section 02's "Where does it live?". Edit the linker script to:
   - reserve a 256-byte `.noinit` RAM region;
   - place one hot function in RAM, in a section that startup code copies from flash;
   - split flash into a 64 KB bootloader region and an application region, and link a blinky into the application region with its own vector table (set `VTOR`).

   Prove each change:
   - the map file shows the new layout;
   - a pattern written to `.noinit` survives a reset;
   - the RAM function runs from SRAM, measured with the DWT cycle counter against the flash version. If there's no speedup on your part, explain why (instruction cache, flash wait states).
   - a ten-line bootloader jumps to the application.

   Finish with a CI step that fails when flash or RAM use exceeds a budget you set. *(~5 h · From Zero to main(), linker-script and newlib parts (Section 07); Yiu's guide on the vector table and memory map (Section 07))*
2. **One-command, reproducible build** — Create a CMake project for your board with a cross-compilation toolchain file and `CMakePresets.json` (Debug and Release). Requirements:
   - one command builds from a clean clone and emits `.elf`, `.hex` and `.map`;
   - warnings are errors in your code but not in vendor code;
   - the git hash and a dirty flag are compiled into the image and printed at boot;
   - no `__DATE__`/`__TIME__` in the image.

   Done when two clean builds produce byte-identical `.bin` files (on two machines, or on one machine and a container), or you can name the cause of every differing byte. *(~4 h · Professional CMake, "Toolchains And Cross Compiling")*
3. **Choose the probe channel by measurement** — Instrument the same 10 kHz timer ISR five ways:
   - semihosting `printf`;
   - UART `printf`;
   - SWO/ITM;
   - RTT (needs a J-Link, or a debug server that supports RTT);
   - a GPIO toggle captured with sigrok/PulseView.

   For each, measure the extra ISR time with the DWT cycle counter, and the highest message rate you can sustain before you lose data or miss interrupts. Deliverable: a one-page table and a rule of thumb for which channel to use when. Semihosting should come out orders of magnitude worse than RTT; explain why from how each one works. *(~4 h · SEGGER RTT; sigrok/PulseView; Yiu's guide on debug and trace (Section 07))*
4. **Every reset has a cause** — Extend the Section 07 fault handler into reset telemetry stored in the `.noinit` region from exercise 1:
   - on every boot, record the reset-cause flags and a boot counter;
   - on a HardFault, a watchdog timeout or a failed `assert`, also save CFSR, HFSR, MMFAR/BFAR (when valid), the stacked PC/LR/xPSR and the current task name;
   - protect the record with a CRC.

   Emit the record as one machine-readable line over RTT or UART. Then write a Python decoder that classifies it and turns addresses into `file:line` from the ELF (`arm-none-eabi-addr2line`). Soak test: a host script uses the Section 02 command shell to trigger a random fault, watchdog hang or clean reset, 500 times. Done when the decoder's classification matches the injected cause every time. *(~6 h · HardFault article and Interrupt blog (Section 07); OpenOCD + GDB to check individual cases)*
5. **Updates that can't brick the device** — Bring up MCUboot on a dev board with two image slots and `imgtool`-signed images; a Zephyr sample is the shortest path. Demonstrate that:
   - an unsigned or corrupted image is rejected;
   - a test upgrade that never confirms itself is reverted on the next reset;
   - cutting power at random moments during 20 upgrades never leaves the board unbootable.

   Then map MCUboot's mechanisms onto your threat model from the Section 08 mini-project ("Hardened Firmware Update Path"): which threats does it cover, and which remain yours? *(~6 h · MCUboot docs; Section 08 mini-project)*

**🏗️ Mini-project — Agent-Ready Firmware Harness:** Extract the build, debug and observability infrastructure from your Section 07 data logger into a reusable template for STM32U5-class boards. A person or a coding agent must be able to drive it from the command line. Include:
- the CMake/presets build from exercise 2, with the flash and RAM budgets from exercise 1 enforced in CI;
- `flash`, `debug` and `run-tests` scripts around OpenOCD (plus RTT if you have a J-Link);
- structured, timestamped logging over RTT or UART;
- the reset telemetry and host decoder from exercise 4;
- an AGENTS.md that documents every command and what "done" means.

Deliverable: `projects/software/12-firmware-harness/`. Success:
- from a clean clone, one command builds, flashes, runs a smoke test and returns pass or fail in under two minutes;
- a deliberately injected fault is reported as `file:line` with no debugger attached;
- a coding agent given only the AGENTS.md fixes a seeded bug and proves it with `run-tests` output.

*(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What does the startup code do between reset and `main()`, and which linker-script symbols does it depend on?
2. `.bss` grew by 4 KB after a change that added no global variables. Where in the map file do you look, and what are two likely causes?
3. Rank semihosting, UART, SWO/ITM, RTT and a GPIO toggle by how much they disturb timing, and say what hardware each one needs.
4. Why does a data watchpoint catch memory corruption that breakpoints miss, and why should you spend watchpoints carefully?
5. What does an image signature protect against, and what doesn't it? How is rollback protection against downgrades different from reverting a bad update?
6. Misconception check: "If it works under the debugger, it works." Give three ways an attached debugger changes how firmware behaves.
7. After an unexplained field reset, what is the minimum data you want saved, and where must it live so startup code doesn't wipe it?
8. Explain to a smart friend in three sentences why a coding agent needs a runnable build-flash-test command before you let it change firmware.
