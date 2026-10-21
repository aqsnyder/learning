# Contributing

Fixes and additions are welcome: a dead link, a wrong author, a better resource, a clearer exercise.
The bar for every change is the same: **you opened it and checked it.**

## Fix or add a resource

1. Find the section. Each curriculum's README lists its sections in order, with what each one covers.
2. Edit that section's `resources.toml`, not the table in its README: the table is generated from the file.
   Every field is described in [tools/README.md](tools/README.md).
3. Open the link and check the exact title, the author order, the year and (for a book) the edition against the
   publisher's or author's page, the arXiv abstract page, or the DOI record. Then set `verified` to today's date.
   Never write a URL or an author list from memory.
4. If the resource changes what a learner should read first, update the section's
   `**Core path (🔑):**` line and its Suggested Order. If an exercise or question should use it, update that too.
5. Run:

   ```bash
   python tools/build.py          # regenerate tables, checklists and indexes
   python tools/check_repo.py     # must report 0 problems
   ```

6. Open a pull request. Say what you checked and how (for example "title and authors from the arXiv page").

## Standards

- **Cite people, not organizations,** when a work names its authors.
- **🔑 marks the core path**, at most three per section, chosen by what the section's objectives and exercises
  need. ⭐ marks only items on a named external list (Ilya Sutskever's list in ml, Rick Hartley's reading list in
  pcb, the canon in btc); those lists are never extended.
- **Label speculation and advocacy** (unreplicated findings, price models, vendor claims) in the description.
- **One home per topic.** If a resource already lives in another section, link to it there instead of adding a
  duplicate row.
- **Never change an item's `id`.** Learners' progress is keyed on it.
- **No investment advice,** and nothing about private people, employers or products.

## Exercises and questions

Exercises say what to produce, how to check it, and roughly how long it takes, and name the resources they use.
Check Yourself questions have answers in the section's `ANSWERS.md` when it exists: if you change a question,
change its answer too.

## License

By contributing, you agree that your contribution is licensed under the same terms as the repo:
CC BY 4.0 for content and MIT for the code in `tools/`.
