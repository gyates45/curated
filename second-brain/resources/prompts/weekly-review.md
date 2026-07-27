# Weekly review (runner)

**Run in:** Claude Code, on this repo. Trigger with *"Run the weekly review."*
**Prereq:** `READWISE_TOKEN` in env for step 2 (skip gracefully if absent).

---

Run my weekly second-brain review. Work through these steps in order, and at
the end give me one consolidated summary.

1. **Reader triage (assist):** Using the Readwise connector or MCP tools if
   available, list my Reader inbox (location "new") grouped into: read &
   highlight-worthy / looks skippable / stale (>3 weeks old). Recommend
   archive/later/delete per item. Don't move anything without my OK.
2. **Sync:** run `python3 second-brain/scripts/readwise_sync.py`. Report how
   many sources were created or updated.
3. **Vault inbox:** for each file in `second-brain/inbox/`, propose: promote
   to evergreen note (show a draft), attach to a project, or archive. Apply
   what I approve. Inbox must end empty.
4. **Distill:** from this week's new highlights, propose up to 3 evergreen
   notes (claim-shaped title + 5-sentence draft each). I pick; you write them
   into `notes/` with proper frontmatter (`status: seed`) and link each into
   the right MOC.
5. **Express check:** scan what we just processed for post/newsletter/playbook
   angles. List up to 3 as one-liners; save any I like to `inbox/idea-<slug>.md`.
6. **Projects sweep:** for each `projects/` folder, report status and whether
   the next action is stale. Flag archive candidates.
7. **Commit:** stage `second-brain/`, commit
   (`docs(second-brain): weekly review YYYY-MM-DD`), and push.

Summary format: what changed, what I decided, what's still open, this week's
best idea in one line.
