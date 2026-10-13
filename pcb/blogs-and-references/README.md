# Essential Blogs, Tools, and Community Resources

---

## Must-Follow Channels and Sites

| Priority | Name | Link | Notes |
|----------|------|------|-------|
| 🔑 | Nine Dot Connects | [ninedotconnects.com](https://www.ninedotconnects.com/) | Professional PCB design education |
| 🔑 | Altium Resources / Blog | [resources.altium.com](https://resources.altium.com/) | Technical articles and design guides |
| | Sierra Circuits Blog | [protoexpress.com/blog](https://www.protoexpress.com/blog/) | Manufacturing perspective on design |
| | FEDEVEL Academy | [fedevel.com](https://www.fedevel.com/) | Robert Feranec's educational platform |
| | Zach Peterson articles (Altium) | — | Signal integrity deep dives |
| 🔑 | LearnEMC (Todd Hubing) | [learnemc.com](https://learnemc.com/) | Free structured EMC tutorials and a weekly EMC question |
| | Analog Devices technical books and MT tutorials | [analog.com](https://www.analog.com/en/resources/technical-books/op-amp-applications-handbook.html) | Free handbooks and tutorials (Op Amp Applications Handbook, MT-031 grounding, MT-101 decoupling) for analog and mixed-signal design |

---

## Design Tools

| Priority | Tool | Link | Notes |
|----------|------|------|-------|
| 🔑 | KiCad | [kicad.org](https://www.kicad.org/) | Free, open-source, industry-standard EDA |
| | Your KiCad Template | [github.com/aqsnyder/KiCAD_Template_Snyder](https://github.com/aqsnyder/KiCAD_Template_Snyder) | Personal KiCad project template (private repo: the link works only when signed in to GitHub as its owner) |
| | Saturn PCB Toolkit | [saturnpcb.com](https://saturnpcb.com/saturn-pcb-toolkit/) | Essential calculators (conductor current per IPC-2152) |
| | UltraCAD Calculators | [ultracad.com/calc.htm](https://www.ultracad.com/calc.htm) | Impedance and trace calculators |
| | Open Source Thermal Sim | [jrainimo.com](https://jrainimo.com/build/2024/11/oss-thermal-simulation-of-pcbs/) | OSS thermal simulation of PCBs |
| | LTspice | [analog.com](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html) | Free SPICE simulator |
| | kicad-cli | [docs.kicad.org](https://docs.kicad.org/10.0/en/cli/cli.html) | Scripted KiCad ERC/DRC and output generation |
| | KiBot | [github.com/INTI-CMNB/KiBot](https://github.com/INTI-CMNB/KiBot) | CI-generated fab and documentation outputs |
| | KiKit | [yaqwsx.github.io/KiKit](https://yaqwsx.github.io/KiKit/latest/) | Panelization and fab presets |
| | openEMS + gerber2ems | [openems.de](https://www.openems.de/) · [gerber2ems](https://github.com/antmicro/gerber2ems) | Open-source FDTD field solving of real PCB traces |
| | FastHenry2 | [fastfieldsolvers.com](https://www.fastfieldsolvers.com/software.htm) | Free 3D inductance/resistance extraction (loop inductance of vias, pads and plane pairs) |
| | JTAG Boundary Scanner (Viveris) | [GitHub](https://github.com/viveris/jtag-boundary-scanner) | Open-source boundary-scan tool with BSDL support (SAMPLE/EXTEST) |

---

## Component Libraries

| Name | Link |
|------|------|
| SnapEDA | [snapeda.com](https://www.snapeda.com/) |
| Ultra Librarian | [ultralibrarian.com](https://www.ultralibrarian.com/) |
| SamacSys | [supplyframe.com/samacsys](https://supplyframe.com/samacsys) |

---

## Fab Houses

| Name | Link |
|------|------|
| JLCPCB | [jlcpcb.com](https://jlcpcb.com/) |
| PCBWay | [pcbway.com](https://www.pcbway.com/) |
| OSH Park | [oshpark.com](https://oshpark.com/) |

---

## Standards

| Standard | Notes |
|----------|-------|
| IPC standards (2221, 7351, 2581) | Industry design and manufacturing standards. IPC-2221 is now at Rev C (2023); the repo's included copy is Rev A (2003) |
| IPC-2152 (2009) | Current-carrying capacity; replaces the old IPC-2221 conductor-sizing charts |
| Gerber Layer Format Specification ([Ucamco](https://www.ucamco.com/en/gerber)) | The official Gerber spec (rev. 2024.05); use X2 attributes |
| IEC 61326-1 (2020) / [IEC 61010-1](https://webstore.iec.ch/en/publication/4279) (2010 + Amd 1, 2016) | EMC and safety standards for measurement, control and laboratory equipment |
| JEDEC | Package naming and component standards |
| J-STD-048A / J-STD-046A ([JEDEC](https://www.jedec.org/node/8470)) | End-of-life and product/process change notification (2025); free from JEDEC with registration (Section 03) |
