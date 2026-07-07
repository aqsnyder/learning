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

3. **Update the root `README.md`** if the new resource is from the Ilya Sutskever reading list (unlikely but possible if the list is updated)

### 4. Summary

After updating, provide a summary of:
- What was added and to which sections
- What was considered but rejected (and why)
- Suggestions for the user's next study priorities

## Section Mapping

| Topic Area | Target Section |
|------------|---------------|
| Reasoning, agents, multimodal, latest models | `11-frontiers/` |
| New transformer variants or attention mechanisms | `06-transformers-and-attention/` |
| New training techniques or scaling results | `08-scaling-and-training/` |
| New LLM papers | `09-llms-and-language/` |
| New RL papers | `10-reinforcement-learning/` |
| New generative model papers | `07-generative-models/` |
| New courses or lectures | `courses/` |
| New blogs or newsletters | `blogs-and-references/` |
| New books | `books/` |

## Notes

- Do not remove existing entries — this is an append-only curriculum
- Maintain consistent formatting with existing tables
- Always include direct links (prefer arXiv, official project pages, or YouTube)
- When in doubt about whether to include something, err on the side of inclusion with a note
