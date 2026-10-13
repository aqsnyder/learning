# 📝 Notes

This folder holds your understanding in your own words, not copies of the sources. Use one file per section you study:

```
notes/<curriculum>/<NN>-<slug>.md      e.g. notes/pcb/06-signal-integrity.md
```

Writing the note is part of learning the section. If a paragraph won't come out simply, that's where you don't understand it yet. Go back to the source for that part only.

## Template

```markdown
# <Section title>: notes
*Started YYYY-MM-DD · Reviewed YYYY-MM-DD, YYYY-MM-DD*

## In one paragraph
<Explain the section to a smart friend with no jargon. This is the Feynman test.>

## Key ideas
- <idea>: <why it's true / where it comes from / when it fails>

## Check Yourself: my answers
1. <answer written from memory> → *corrections after checking:* <…>

## Practice log
- Exercise 2: <result, numbers, what surprised me> (link to `projects/…` if any)

## Open questions
- <things to ask NotebookLM/Claude or to test on the bench>

## Flashcards
<question> :: <answer>
```

**Flashcards:** one `question :: answer` pair per line. You can import them into Anki with `::` as the field separator.

**Spaced review:** after finishing a section, re-answer its ✅ Check Yourself questions after about a day, a week, and a month. Add each date to the *Reviewed* line.
