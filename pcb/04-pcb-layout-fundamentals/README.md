# PCB Layout Fundamentals

## Why This Section Matters

This is the core skill — placing components and routing traces. Everything you've learned about schematics, stackups, and materials converges here. Good layout is part engineering, part art: component placement alone determines 90% of whether a board will work well. This section builds the hands-on muscle memory and design intuition that separates a schematic that *could* work from a PCB that *does* work.

## Prerequisites

- [Section 01 — Electronics Fundamentals](../01-electronics-fundamentals/README.md)
- [Section 02 — Schematic Design](../02-schematic-design/README.md)
- [Section 03 — PCB Stackup and Materials](../03-pcb-stackup-and-materials/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | On the Rick Hartley recommended reading list |

## Resources

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| 🔑 | 🎥 Video Series | Phil's Lab — PCB Layout Tutorials | [YouTube](https://www.youtube.com/@PhilsLab) | Step-by-step layout walkthroughs with theory. Excellent for building practical intuition alongside conceptual understanding. |
| 🔑 | 🎥 Video Series | Robert Feranec — Layout and Routing | [YouTube](https://www.youtube.com/@RobertFeranec) | Professional-grade layout techniques from an experienced PCB designer. |
| 🔑 | 🎓 Course | KiCad PCB Editor Guide | [Docs](https://docs.kicad.org/8/) | Official layout tool documentation. Essential reference for KiCad-based workflows. |
| | 🎥 Video | Altium Academy — Routing Tutorials | [YouTube](https://www.youtube.com/@AltiumAcademy) | Routing walkthroughs in Altium Designer; concepts transfer to any EDA tool. |
| 🔑 | 💡 Concept | Component Placement Strategy | — | Place before you route; placement is 90% of the design. Group by function, minimize critical path lengths, and think about thermal and mechanical constraints first. |
| | 💡 Concept | Design Rule Check (DRC) | — | Understanding and configuring manufacturer constraints. Your DRC settings should match your fab house's capabilities. |
| | 💡 Concept | Copper Pours and Fills | — | Ground planes, power planes, thermal relief. When and how to use polygon pours effectively. |

## Suggested Order

1. **KiCad PCB Editor Guide** — Get comfortable with the tool you'll be using for all exercises
2. **Phil's Lab layout tutorials** — Watch the walkthroughs to see the full placement-to-routing workflow
3. **Component Placement Strategy** — Internalize the principle: placement is 90% of the design
4. **Robert Feranec layout and routing** — Level up with professional techniques and real-world examples
5. **DRC and manufacturer constraints** — Learn to configure rules that match your fab house
6. **Copper Pours and Fills** — Understand ground planes and thermal relief
7. **Altium Academy routing** — Broaden exposure to different EDA tool approaches
