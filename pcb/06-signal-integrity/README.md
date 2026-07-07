# Signal Integrity

## Why This Section Matters

As frequencies rise, traces become transmission lines and physics takes over. Signal integrity is the discipline that bridges PCB layout with electromagnetic theory. Understanding impedance, reflections, crosstalk, and return paths is what separates a board that works on the bench from one that works reliably in production. This is where the books on Rick Hartley's reading list become essential.

## Prerequisites

- [Section 04 — PCB Layout Fundamentals](../04-pcb-layout-fundamentals/README.md)
- [Section 05 — Power Distribution and Grounding](../05-power-and-grounding/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | On the Rick Hartley recommended reading list |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑⭐ | 📕 Book | Signal and Power Integrity — Simplified | Eric Bogatin | [Amazon](https://www.amazon.com/Signal-Power-Integrity-Simplified-3rd/dp/013451341X) | THE most approachable signal integrity book. Bogatin explains transmission lines, impedance, and crosstalk with clarity and intuition. Start here. |
| 🔑⭐ | 📕 Book | High-Speed Digital Design: A Handbook of Black Magic | Howard Johnson, Martin Graham | — | The signal integrity bible. Dense but indispensable — covers everything from rise times to termination strategies. |
| ⭐ | 📕 Book | Right the First Time, Vols I and II | Lee Ritchey | — | Physics-first approach to high-speed PCB design. Practical rules derived from electromagnetic fundamentals. |
| 🔑 | 🎥 Video Series | Robert Feranec — Signal Integrity and High-Speed Design | Robert Feranec | [YouTube](https://www.youtube.com/@RobertFeranec) | DDR routing, differential pairs, impedance control, and real-world high-speed design walkthroughs. |
| 🔑 | 🎥 YouTube Channel | Dr. EMC | Dr. EMC | [YouTube](https://www.youtube.com/@DrEMC) | Transmission lines, simulation, and EMC theory. Excellent visual explanations of field behavior. |
| | 🔧 Tool | UltraCAD Calculators | — | [Website](https://www.ultracad.com/calc.htm) | Impedance, trace width, and via calculations. Useful for quick design verification. |
| | 💡 Concept | Controlled Impedance | — | — | What it means, how to specify it to your fab house, and why your stackup determines your trace geometry. |
| | 💡 Concept | Differential Pairs | — | — | Routing rules, coupling, and when to use differential signaling (USB, LVDS, Ethernet, DDR). |
| | 💡 Concept | Return Paths and Reference Planes | — | — | Where the current actually flows. A trace is only half the circuit — the return path through the reference plane completes it. |

## Suggested Order

1. **Signal and Power Integrity — Simplified** — Start with Bogatin; read at least the first half for core concepts
2. **Dr. EMC** — Watch transmission line and field visualization videos to build intuition
3. **Robert Feranec SI and high-speed design** — See practical application: DDR routing, differential pairs
4. **Controlled impedance** — Understand how to specify impedance to your fab house
5. **Return paths and reference planes** — Internalize where current actually flows (ties back to Rick Hartley's grounding lecture)
6. **Differential pairs** — Learn the routing rules and when differential signaling is required
7. **High-Speed Digital Design: Black Magic** — Deep dive into the SI bible; use as reference alongside practical work
8. **Right the First Time** — Physics-first design rules from Lee Ritchey
9. **UltraCAD Calculators** — Verify your impedance and trace geometry calculations
