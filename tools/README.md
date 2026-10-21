# Tools

Three small Python scripts. They need Python 3.11 or newer and nothing else.

| Script | Who runs it | What it does |
|---|---|---|
| `progress.py` | learners | Your private checklists, progress bars and time log, kept in `my/` (git ignores it). |
| `build.py` | maintainers | Regenerates everything derived from the data: resource tables, PROGRESS templates, book and course indexes, learning paths and the main page's section index. |
| `check_repo.py` | maintainers and CI | Offline checks: links between files, section anatomy, tier lists, valid data, nothing stale, nothing personal committed. |

```bash
python tools/progress.py init      # once: creates my/ with your own checklists
python tools/progress.py status    # progress bars
python tools/build.py              # after editing any resources.toml
python tools/check_repo.py         # before committing; CI runs it on every push
python tools/check_repo.py --strict   # also fails on incomplete resource data
```

## Where the content lives

| You want to change… | Edit | Then |
|---|---|---|
| a resource (title, link, author, marker, description) | `<curriculum>/<NN>-<slug>/resources.toml` | `python tools/build.py` |
| a book or course with no section home | `<curriculum>/extras.toml` | `python tools/build.py` |
| objectives, suggested order, exercises, questions, any prose | the section `README.md`, outside the generated block | `python tools/build.py` if you changed the Core path line, an exercise name or the mini-project name |
| the order of sections, or a "When" note | the learning-path table in the curriculum `README.md` | `python tools/build.py` |

Never edit the generated parts by hand: the block between `<!-- resources:start … -->` and `<!-- resources:end -->` in
each section README, `<curriculum>/PROGRESS.md`, and the marked blocks in `books/README.md`, `courses/README.md`, the
curriculum README and the main README. `build.py` overwrites them, and `check_repo.py` fails while they are stale.

## resources.toml

One file per section. Groups become `###` subsections (a single untitled group is just a table); items become rows.

```toml
intro = '''Optional text shown right under "## Resources".'''

[[groups]]
title = "Foundational Papers"          # optional
intro = '''Optional text before the table.'''
outro = '''Optional text after the table, e.g. cross-links to resources tracked in other sections.'''

[[groups.items]]
id = "hartley-grounding"               # required: a-z, 0-9 and hyphens; unique in the section; never change it
title = "How to Achieve Proper Grounding"   # required; Markdown is allowed (e.g. *Book Title*)
authors = "Rick Hartley"               # people or the publishing organization
year = "2016"                          # a string: "2016", "2003, 2007", "1961–1969"
type = "video"                         # required; see the list below
label = "Talk"                         # optional: overrides the type's display name
marks = ["core"]                       # optional: core (🔑), masterwork (🔑🔑), canon (⭐), ai (🤖)
url = "https://www.youtube.com/watch?v=ySuUZEjARPY"
link_text = "YouTube"                  # the visible link text
more_links = [{ text = "Slides", url = "https://…" }]
link_note = "*(text shown after the links)*"
description = "Why it's here, in a sentence or two."
access = "free"                        # free, paid or partial
level = "intermediate"                 # beginner, intermediate or advanced (used by the book and course indexes)
verified = 2026-10-21                  # the last date someone opened the link and checked title, authors and year
track = false                          # optional: leave it out of PROGRESS (for pure cross-references)
short = "Hartley — Grounding"          # optional: shorter name for the PROGRESS checklist
```

**Types:** `book`, `paper`, `article`, `report`, `blog`, `standard`, `app-note`, `docs`, `tutorial`, `course`,
`lecture`, `video`, `video-series`, `encyclopedia`, `website`, `database`, `tool`, `podcast`, `practice`, `concept`.
`concept` is legacy: a row with no source. `check_repo.py --strict` fails on it.

**Rules the checker enforces:** at most three items per section are marked `core` (or `masterwork`), and the
section's `**Core path (🔑):**` line names exactly that many items. `id`s must not change once published,
because learners' ticks are keyed on them.

**Verified dates.** Set `verified` only after opening the link yourself and checking the title, the author order
and the year (and the edition, for books). An item verified more than a year ago is due for a re-check
(the quarterly audit does this).

## PROGRESS.md and my/

`<curriculum>/PROGRESS.md` is a generated, blank template. Every line ends with an ID comment
(`<!-- id:pcb/05/hartley-grounding -->`) that GitHub doesn't display. `progress.py init` copies the templates into
`my/progress/`; learners tick boxes there. `progress.py sync` rebuilds each copy from the latest template and keeps
every tick whose ID still exists. A ticked item that disappears upstream moves to a "Removed upstream" list at the
end of the file, so nothing is lost silently.

## License

The code in this folder is MIT-licensed (see [LICENSE](LICENSE)). Everything else in the repo is CC BY 4.0
(see the [root LICENSE](../LICENSE)).
