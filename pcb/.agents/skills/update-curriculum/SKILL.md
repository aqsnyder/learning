---
name: update-curriculum
description: Search for and add new important PCB design resources, courses, and reference materials to the learning curriculum. Use when you want to update the resource lists or add newly published material to any section.
---

# Update Curriculum Skill

This skill searches for the latest important PCB design resources, courses, tools, and reference materials, and updates the learning curriculum repository accordingly.

## When to Use

- Periodically (e.g., monthly) to check for important new resources
- When a major new book, course, or tool is released
- When the user asks to "update the reading list" or "check for new resources"
- When a new KiCad version or IPC standard is published

## Workflow

### 1. Research New Material

Search the web for:
- New YouTube videos from Phil's Lab, Robert Feranec, Rick Hartley, EEVblog, and Altium Academy
- New KiCad releases, plugins, or library updates
- New PCB design books or editions
- New or updated IPC standards
- New open-source hardware reference designs (e.g., from OSHWA, Adafruit, SparkFun)
- Notable blog posts from Nine Dot Connects, Sierra Circuits, Altium, or Zach Peterson
- New fab house capabilities or services
- New free calculators, simulators, or design tools

Use search queries like:
- "best PCB design resources [current year]"
- "Phil's Lab new videos [current month] [current year]"
- "Robert Feranec new PCB videos [current year]"
- "Rick Hartley lecture [current year]"
- "KiCad [latest version] release"
- "new IPC standards [current year]"
- "open source hardware reference design [current year]"
- "PCB design tutorial [current year]"

### 2. Evaluate Relevance

For each candidate resource, assess:
- **Impact**: Is this genuinely important or just trendy?
- **Novelty**: Does it introduce a new technique, tool, or standard, or is it incremental?
- **Accessibility**: Is it freely available? What is the cost?
- **Credibility**: Is the source trusted in the PCB design community?
- **Fit**: Which section does it belong in?

Priority criteria for inclusion:
- Content from established educators (Phil's Lab, Robert Feranec, Rick Hartley, Eric Bogatin)
- Resources that fill gaps in the existing curriculum
- New editions of books already in the list
- New IPC or JEDEC standards relevant to PCB design
- Tools or calculators that meaningfully improve the design workflow

### 3. Update the Repository

For each approved resource:

1. **Add to the appropriate section README** (e.g., `05-stackup-and-power/README.md` for PDN topics)
   - Add a new row to the resource table
   - Use 🔑 for must-read/must-watch items
   - Use ⭐ for Rick Hartley recommended reading list items
   - Include: title, author, year, link, and a 1–2 sentence description

2. **Update `PROGRESS.md`** — add a new checkbox entry in the corresponding section

3. **Update `books/README.md`** if a new book is added

4. **Update `courses/README.md`** if a new course or lecture is added

5. **Update `blogs-and-references/README.md`** if a new blog, tool, fab house, or standard is added

### 4. Summary

After updating, provide a summary of:
- What was added and to which sections
- What was considered but rejected (and why)
- Suggestions for the user's next study priorities

## Section Mapping

| Topic Area | Target Section |
|------------|---------------|
| Electronics fundamentals, circuits, components | `00-electronics-fundamentals/` |
| Schematic design, symbols, ERC | `01-schematic-design/` |
| KiCad workflow, project setup | `02-kicad-workflow/` |
| Footprints, land patterns, component placement | `03-footprints-and-placement/` |
| Routing, trace width, differential pairs | `04-routing/` |
| Stackup, grounding, PDN, power integrity | `05-stackup-and-power/` |
| Signal integrity, impedance, transmission lines | `06-signal-integrity/` |
| EMC, shielding, filtering | `07-emc/` |
| DFM, DFT, manufacturing files | `08-manufacturing/` |
| Thermal management, reliability | `09-thermal-and-reliability/` |
| High-speed design, DDR, SerDes | `10-high-speed/` |
| New courses, video lectures | `courses/` |
| New blogs, tools, references | `blogs-and-references/` |
| New books | `books/` |

## Notes

- Do not remove existing entries — this is an append-only curriculum
- Maintain consistent formatting with existing tables
- Always include direct links (prefer YouTube, official project pages, or publisher sites)
- When in doubt about whether to include something, err on the side of inclusion with a note
