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

1. **Add to the appropriate section README** (e.g., `05-power-and-grounding/README.md` for PDN topics)
   - Add a new row to the resource table
   - Use 🔑 for must-read/must-watch items
   - Use ⭐ only for the 12 books in `documents/Ricks-Reading-Recommendation.pdf` (never for Rick's own talks or anything else)
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
| Electronics fundamentals, circuits, op amps, SPICE simulation | `00-electronics-fundamentals/` |
| PCB structure, laminates and materials, IPC-2221 | `01-pcb-anatomy-and-materials/` |
| Schematic capture, symbols, ERC, libraries, KiCad project setup | `02-schematic-capture/` |
| Component selection, sourcing, lifecycle, packages | `03-component-selection/` |
| Placement, routing, DRC, copper pours, KiCad PCB editor | `04-pcb-layout-fundamentals/` |
| Grounding, PDN, decoupling, power-supply layout, trace current (IPC-2152) | `05-power-and-grounding/` |
| Signal integrity, impedance, transmission lines, differential pairs, interface layout (USB, Ethernet, PCIe) | `06-signal-integrity/` |
| EMC, shielding, filtering, compliance standards | `07-emc-and-compliance/` |
| Stackup, layer count, via types, impedance-controlled stackups | `08-multi-layer-and-stackup/` |
| DFM/DFA, fab outputs, panelization, output automation (kicad-cli, KiBot, KiKit) | `09-dfm-and-fabrication/` |
| Thermal, BGA/HDI, flex, RF, field/thermal simulation, KiCad scripting | `10-advanced-topics/` |
| Open-source reference designs | `11-reference-projects/` |
| Analog front ends, precision measurement, ADC/reference design, source-measure, sensor front ends (taken after 05) | `12-analog-mixed-signal-and-precision-measurement/` |
| Bring-up, probing, fault-finding, boundary scan, production test (taken after 09) | `13-bring-up-test-and-debug/` |
| New courses, video lectures | `courses/` |
| New blogs, tools, references | `blogs-and-references/` |
| New books | `books/` |

## Verification & Curation Rules (mandatory)

Earlier AI-generated updates to this repo introduced fabricated authors, resources that don't exist, and links to the wrong papers (all fixed in the October 2026 review — see `reviews/2026-10-deep-dive/`). Every update must follow these rules:

1. **Open every link before adding it.** Fetch the arXiv abs page, the DOI record (`https://api.crossref.org/works/<DOI>`), the official page, or the YouTube oEmbed record (`https://www.youtube.com/oembed?url=<url>&format=json`) and confirm the exact title, author order, year, and edition. Never write a URL or an author list from memory.
2. **Cite people, not organizations,** when a work lists authors ("Templeton et al.", not "Anthropic").
3. **When in doubt, leave it out.** List doubtful or unverifiable candidates in your summary instead of adding them.
4. **Correct, don't just append.** Fix wrong metadata in place. If a resource is superseded or dead, say so in its description and in your summary. (Append-only means don't silently delete — it does not mean leave errors.)
5. **Keep the learning layer whole.** A new resource goes into the section table, its Suggested Order, and `PROGRESS.md`. A new section must ship with the full anatomy — Why · Prerequisites · 🎯 Learning Objectives · Resources · Suggested Order · 🛠️ Practice (+ 🏗️ mini-project) · ✅ Check Yourself — plus a PROGRESS block (see the root `.agents/skills/audit-curriculum/SKILL.md`). Append new sections at the next number and state where to take them; don't renumber.
6. **Markers are closed lists.** ⭐ only for items on this curriculum's named list. Use 🔑 sparingly — at most 3 core items per section. Each section's Suggested Order opens with a "**Core path (🔑):**" line naming its 🔑 items; if you add or remove a 🔑, update that line too, then run `python tools/build_index.py` to refresh the learning-path table in the curriculum README.
7. **Label speculation and advocacy as such** (e.g. unconfirmed theories, price models, vendor claims), and prefer measured evidence.
8. **Run `python tools/check_repo.py`** from the repo root before finishing — it must report 0 problems.
9. **One home per topic.** Check the overlap table in `STUDY-GUIDE.md`. If a resource's topic lives in another curriculum, cross-link to it there instead of adding a duplicate row.

## Notes

- Do not remove existing entries — this is an append-only curriculum
- Maintain consistent formatting with existing tables
- Always include direct links (prefer YouTube, official project pages, or publisher sites)
- When in doubt, leave it out — list doubtful candidates in your summary instead of adding them
