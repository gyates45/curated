# NotebookLM project kit

**Use when** one question deserves 10–50 sources (workshop prep, playbook
chapter, market-state question). Two parts: interrogation prompts for inside
NotebookLM, then the distill-back step with Claude so the knowledge survives
the notebook.

## 1 · Setup

- Name the notebook after the **question**, not the topic.
- Load: the relevant PDFs/article URLs/YouTube links from Reader, plus the
  matching vault notes and MOC (upload the `.md` files — they're small).

## 2 · Interrogate (inside NotebookLM)

Run these in order:

1. "Across all sources, what are the 5 strongest claims relevant to
   [question]? Cite which sources support each."
2. "Where do these sources disagree with each other? Be specific."
3. "What evidence contradicts [my current position — paste from the vault
   note]?"
4. "What questions do these sources fail to answer about [question]?"
5. "Which single source is most load-bearing? If it's wrong, what falls?"

Generate the audio overview for drive-time; take capture-notes as you listen.

## 3 · Distill back (Claude Code, afterwards)

---
Here are my conclusions from a NotebookLM deep-dive on: **<question>**

<paste NotebookLM's key answers + your own reactions>

Turn this into: (a) 1–3 evergreen notes (claim-shaped, `status: seed`,
`sources:` listing the actual underlying sources — not "NotebookLM"), linked
into `<MOC path>`; (b) an update to the MOC's open-questions list — mark what
this dive answered and add what it surfaced. Show me drafts before writing.
---

Then the notebook is disposable. If it never got distilled, the dive didn't
happen.
