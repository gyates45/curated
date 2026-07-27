# Workflows

Three routines. Total cost: ~5 min/day + 30 min/week + 45 min/month.
Everything heavier than this gets abandoned — that's a design constraint,
not an aspiration.

## Daily capture (≤5 min, ambient)

- Worth reading? → Reader, with ≤2 topic tags + one-line "why saved" note.
- Idea? → one file in `inbox/` (or Obsidian quick note into it). No formatting.
- Done. No daily processing, no streaks, no guilt.

## Weekly review (30 min, pick a fixed slot — e.g. Friday 4pm)

Run it with Claude Code on this repo: open a session and say
**"Run the weekly review"** (it follows
[`resources/prompts/weekly-review.md`](../resources/prompts/weekly-review.md)).
Or do it by hand:

1. **Reader inbox → zero.** Archive what's read, `later` what's genuinely
   next, delete the aspirational clutter. Be ruthless; the queue is a tool,
   not a debt.
2. **Sync highlights:** `python3 scripts/readwise_sync.py` (needs
   `READWISE_TOKEN`).
3. **Vault `inbox/` → zero.** Each file: promote to evergreen note, attach to
   a project, or archive.
4. **Distill 1–3 notes.** From this week's highlights/cards, write 1–3
   evergreen notes (claim-titled, own words, `sources:` filled). Not ten. One
   good note beats ten stubs.
5. **Link them** into the right MOC (`notes/mocs/`).
6. **Express check:** anything this week feed a LinkedIn post, the Small Firm
   Brief, or a playbook? If yes, capture the angle in `inbox/` as `idea-…` or
   draft it now via [`note-to-linkedin-post`](../resources/prompts/note-to-linkedin-post.md).
7. **Projects sweep:** each folder in `projects/` — still active? Next action
   clear? Stalled >1 month → archive or revive.
8. **Commit & push.** `git add second-brain && git commit && git push`. The
   vault only compounds if it leaves your laptop.

## Monthly maintenance (45 min)

- **Tag hygiene** (with Claude, approval-gated): merge duplicates per
  [`capture.md`](capture.md#known-cleanup-candidates-run-as-a-tag-hygiene-job-with-approval).
- **MOC gardening:** orphan notes get homes; MOCs over ~30 links get split;
  dead links get fixed.
- **Recall pass:** 15 minutes of spaced review in Recall; anything that
  resurfaces twice and still matters → evergreen note.
- **NotebookLM deep-dive (optional):** pick one question that deserves 10+
  sources (e.g. "what's the real state of AI adoption in <50-lawyer firms?"),
  build a notebook, interrogate it, distill conclusions back into `notes/` via
  [`notebooklm-project-kit`](../resources/prompts/notebooklm-project-kit.md).
- **Claude Project refresh:** update project knowledge files with the current
  MOCs (see [`ai-playbook.md`](ai-playbook.md#claude-projects)).

## Quarterly (1 hr)

- Re-read your top 20 evergreen notes. Promote `growing` → `evergreen` where
  earned; demote or merge what aged badly.
- Archive sweep: dormant projects, stale resources.
- **Review the system itself:** what got skipped for 4+ weeks? Delete that
  step — the system adapts to you, not the reverse. Update these docs.
