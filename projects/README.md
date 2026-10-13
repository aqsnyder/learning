# 🏗️ Projects

This folder holds deliverables from the 🛠️ Practice blocks and 🏗️ mini-projects:

```
projects/<curriculum>/<NN>-<short-name>/      e.g. projects/pcb/06-si-coupons/
```

Each project folder gets a `README.md`:

```markdown
# <Project name>
*Section: <curriculum>/<NN> · Date: YYYY-MM-DD · Time spent: ~N h*

## Goal and success criterion
<copied from the mini-project prompt>

## What I built
<short description, with links to code, notebooks, schematics, and measurements>

## Result vs. criterion
<numbers. Did it meet the criterion? If not, why not?>

## What I'd do differently / what I learned
```

Conventions:
- Keep notebooks runnable. Pin dependencies in `requirements.txt`, or use `uv` with a `pyproject.toml`.
- Small data can live here. Link large datasets, simulation outputs, and fab files, or store them with Git LFS.
- KiCad projects: commit sources (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, libraries). Generate fab outputs in CI or locally rather than committing them.
- When a project ends, tick its 🏗️ line in the curriculum's `PROGRESS.md`, and link the project from your section note in `notes/`.
