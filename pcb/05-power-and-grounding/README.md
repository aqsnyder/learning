# Power Distribution and Grounding

## Why This Section Matters

Poor power design is the #1 cause of board failures and noise issues. A clean, low-impedance power distribution network and proper grounding are the foundation everything else depends on. Get this wrong and no amount of clever routing or filtering will save your design. Rick Hartley's grounding lecture alone has saved more PCB designs than any other single resource.

## Prerequisites

- [Section 04 — PCB Layout Fundamentals](../04-pcb-layout-fundamentals/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | On the Rick Hartley recommended reading list |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑⭐ | 🎥 Video | How to Achieve Proper Grounding | Rick Hartley | [YouTube](https://www.youtube.com/watch?v=ySuUZEjARPY) | THE definitive lecture on grounding. If you watch one video on PCB design, make it this one. |
| 🔑⭐ | 🎥 Video | Power Distribution Networks | Rick Hartley | [YouTube](https://www.youtube.com/watch?v=WnLRHuvl6Eg) | PDN design fundamentals — understanding impedance, decoupling, and energy delivery. |
| 🔑 | 🎥 Video Series | Phil's Lab — Power Design Tutorials | Phil's Lab | [YouTube](https://www.youtube.com/@PhilsLab) | Practical power supply layout with hands-on KiCad examples. |
| ⭐ | 📕 Book | Fast Circuit Boards: Energy Management | Ralph Morrison | — | How energy travels as fields, not currents. Reframes how you think about power delivery at the physics level. |
| ⭐ | 📕 Book | Principles of Power Integrity for PDN Design Simplified | Smith, Bogatin | — | PDN theory made accessible. Target impedance, decoupling strategies, and simulation. |
| | 🔧 Tool | Saturn PCB Design Toolkit | — | [Website](https://saturnpcb.com/saturn-pcb-toolkit/) | Calculators for trace width, via current, thermal resistance, and more. Essential desktop tool. |
| | 💡 Concept | Decoupling Capacitor Placement and Selection | — | — | Strategy for choosing values, quantities, and placement of decoupling caps relative to IC power pins. |
| | 💡 Concept | Ground Plane Splits | — | — | When and why to split ground planes (usually: don't). Understand the consequences before you cut a plane. |

## Suggested Order

1. **Rick Hartley — How to Achieve Proper Grounding** — Watch this first; it will reshape how you think about current return paths
2. **Rick Hartley — Power Distribution Networks** — Understand PDN impedance and why it matters
3. **Phil's Lab power design tutorials** — See practical implementation of power design principles
4. **Fast Circuit Boards: Energy Management** — Deepen your physics intuition about energy flow
5. **Decoupling capacitor placement and selection** — Learn the practical rules for cap selection and placement
6. **Ground plane splits** — Understand why splitting planes is almost always a mistake
7. **Principles of Power Integrity** — Formalize your PDN knowledge with Bogatin's approach
8. **Saturn PCB Toolkit** — Use the calculators to verify your designs quantitatively
