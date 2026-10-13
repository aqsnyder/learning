---
name: update-curriculum
description: Search for and add new important AI/ML papers, courses, and resources to the learning curriculum. Use when you want to update the frontiers section or add newly published important material to any section.
---

# Update Curriculum Skill

This skill searches for the latest important AI/ML papers, courses, and resources, and updates the learning curriculum repository accordingly.

## When to Use

- Periodically (e.g., monthly) to check for important new papers
- When a major model, paper, or course is released
- When the user asks to "update the reading list" or "check for new papers"

## Workflow

### 1. Research New Material

Search the web for:
- Recent papers from top AI conferences (NeurIPS, ICML, ICLR, CVPR, ACL)
- New arXiv preprints with high citation velocity in cs.LG, cs.CL, cs.CV, cs.AI
- New video lectures or courses from established educators (Karpathy, 3Blue1Brown, Stanford, MIT, DeepMind)
- New blog posts from key authors (Colah, Lilian Weng, Jay Alammar, Anthropic)
- Updates to the Stanford HAI AI Index Report
- Notable new open-source model releases

Use search queries like:
- "most important AI papers [current year]"
- "best new machine learning courses [current year]"
- "breakthrough AI research [current month] [current year]"
- "[conference name] [current year] best papers"

### 2. Evaluate Relevance

For each candidate resource, assess:
- **Impact**: Is this genuinely important or just trendy?
- **Novelty**: Does it introduce a new concept, or is it incremental?
- **Accessibility**: Is it freely available?
- **Fit**: Which section does it belong in?

Priority criteria for inclusion:
- Papers that introduce fundamentally new architectures or techniques
- Papers that significantly advance the state of the art
- Courses or lectures from established, trusted educators
- Resources that fill gaps in the existing curriculum

### 3. Update the Repository

For each approved resource:

1. **Add to the appropriate section README** (e.g., `11-frontiers/README.md` for recent papers)
   - Add a new row to the resource table
   - Use 🔑 for must-read items
   - Include: title, authors, year, link, and a 1-2 sentence description

2. **Update `PROGRESS.md`** — add a new checkbox entry in the corresponding section

3. **Never add ⭐** — the Ilya Sutskever list is a fixed 27-item list (cross-referenced in `ml/README.md`); new items get 🔑 or nothing

### 4. Summary

After updating, provide a summary of:
- What was added and to which sections
- What was considered but rejected (and why)
- Suggestions for the user's next study priorities

## Section Mapping

| Topic Area | Target Section |
|------------|---------------|
| History of AI, landmark retrospectives | `00-historical-foundations/` |
| ML-specific math bridges (matrix calculus, info theory for ML); Ilya-list theory items | `01-math-foundations/` (general math → `../math/`) |
| Classical ML, tabular methods, evaluation methodology | `02-classical-ml/` |
| Backprop, training craft, initialization/normalization basics | `03-neural-network-fundamentals/` |
| Vision architectures, CNNs, ViTs, detection/segmentation | `04-cnns-and-computer-vision/` |
| Recurrent and memory architectures | `05-rnns-sequences-and-memory/` |
| New transformer variants or attention mechanisms | `06-transformers-and-attention/` |
| New generative model papers (diffusion, flows, VAEs, AR image/video) | `07-generative-models/` |
| Training techniques, scaling results, distributed training, inference serving, quantization | `08-scaling-and-training/` |
| LLM papers: pretraining data, tokenization, instruction tuning, open-model reports | `09-llms-and-language/` |
| RL papers, incl. RLHF/DPO/RLVR and reasoning-via-RL | `10-reinforcement-learning/` |
| Reasoning, agents, multimodal, robotics, latest models | `11-frontiers/` |
| Interpretability, alignment, safety evaluations, capability measurement | `12-interpretability-and-alignment/` |
| GNNs, geometric/equivariant DL, AI for science | `13-graphs-geometry-and-science/` |
| On-device/embedded ML (TinyML): MCU runtimes and kernels, int8 deployment, hardware-aware model design, on-target benchmarking, shipping ML in products | `14-edge-and-embedded-ml/` (take after 08; general quantization papers stay in 08) |
| New courses or lectures | `courses/` |
| New blogs or newsletters | `blogs-and-references/` |
| New books | `books/` |

## Verification & Curation Rules (mandatory)

Earlier AI-generated updates to this repo introduced fabricated authors, resources that don't exist, and links to the wrong papers (all fixed in the October 2026 review — see `reviews/2026-10-deep-dive/`). Every update must follow these rules:

1. **Open every link before adding it.** Fetch the arXiv abs page, the DOI record (`https://api.crossref.org/works/<DOI>`), the official page, or the YouTube oEmbed record (`https://www.youtube.com/oembed?url=<url>&format=json`) and confirm the exact title, author order, year, and edition. Never write a URL or an author list from memory.
2. **Cite people, not organizations,** when a work lists authors ("Templeton et al.", not "Anthropic").
3. **When in doubt, leave it out.** List doubtful or unverifiable candidates in your summary instead of adding them.
4. **Correct, don't just append.** Fix wrong metadata in place. If a resource is superseded or dead, say so in its description and in your summary. (Append-only means don't silently delete — it does not mean leave errors.)
5. **Keep the learning layer whole.** A new resource goes into the section table, its Suggested Order, and `PROGRESS.md` — and, if it is a book, course or blog, into the matching `books/`, `courses/` or `blogs-and-references/` index. A new section must ship with the full anatomy — Why · Prerequisites · 🎯 Learning Objectives · Resources · Suggested Order · 🛠️ Practice (+ 🏗️ mini-project) · ✅ Check Yourself — plus a PROGRESS block (see the root `.agents/skills/audit-curriculum/SKILL.md`). Append new sections at the next number and state where to take them; don't renumber.
6. **Markers are closed lists.** ⭐ only for items on this curriculum's named list. Use 🔑 sparingly — at most 3 core items per section. Each section's Suggested Order opens with a "**Core path (🔑):**" line naming its 🔑 items; if you add or remove a 🔑, update that line too, then run `python tools/build_index.py` to refresh the learning-path table in the curriculum README.
7. **Label speculation and advocacy as such** (e.g. unconfirmed theories, price models, vendor claims), and prefer measured evidence.
8. **Run `python tools/check_repo.py`** from the repo root before finishing — it must report 0 problems.
9. **One home per topic.** Check the overlap table in `STUDY-GUIDE.md`. If a resource's topic lives in another curriculum, cross-link to it there instead of adding a duplicate row.

## Notes

- Do not remove existing entries — this is an append-only curriculum
- Maintain consistent formatting with existing tables
- Always include direct links (prefer arXiv, official project pages, or YouTube)
- When in doubt, leave it out — list doubtful candidates in your summary instead of adding them
