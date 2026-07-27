# System architecture

## Principles

1. **One canonical store.** Distilled knowledge lives in this folder as
   markdown in git. Everything else is a capture funnel or a lens. The moment
   two tools both claim to be "the" knowledge base, the system dies.
2. **Plain text wins.** Markdown + git is the only format every current and
   future AI can read natively, diffs cleanly, survives every app shutdown, and
   costs nothing. Apps come and go; the vault compounds.
3. **Capture ≠ knowledge.** 34k highlights and 1,700 Recall cards are raw ore.
   Value is created in the distill step — a small number of evergreen notes in
   your own words. The vault optimizes for that step, not for hoarding.
4. **AI reads everything, drafts everything, decides nothing.** Claude and
   ChatGPT get full read access and do the mechanical work (triage, distill
   drafts, content drafts). Promotion of a note to `evergreen` and anything
   published stays a human call.
5. **A vault is a garden, not a landfill.** Finals only, a named owner (you),
   a recurring maintenance slot (the weekly review). The failure mode of every
   second brain is nobody owning the pruning.

## Data flow and sync directions

All syncs are **one-way, into the hub**. Two-way sync is deliberately avoided —
it is fragile, and it blurs which copy is canonical.

| Flow | Direction | Mechanism | Cadence |
|---|---|---|---|
| Reader highlights → `sources/readwise/` | one-way in | `scripts/readwise_sync.py` (Readwise export API) | weekly (part of review) |
| Recall cards → Claude | live query | Recall connector on claude.ai | on demand |
| Reader/Readwise → Claude | live query | Readwise connector on claude.ai | on demand |
| Notion → Claude / ChatGPT | live query | Notion connectors | on demand |
| Vault → claude.ai / Claude Code | git clone / repo access | Claude Code sessions on this repo | on demand |
| Vault → ChatGPT | GitHub connector (or zip upload) | ChatGPT settings → Connectors | on demand |
| Vault ↔ Obsidian | direct file access | open folder as vault | live |
| Sources → NotebookLM | manual upload per project | notebook per project | per project |
| NotebookLM conclusions → `notes/` | manual distill | you + Claude, via prompt | per project |

**Recall's role, precisely:** Recall already auto-summarizes and graphs
everything you feed it — that duplicates what `sources/` does for skimming.
So Recall stays a *lens*: fast recall, spaced review, serendipitous
connections, queried live from Claude. Its cards are not synced into the vault;
anything in Recall worth keeping forever gets distilled into `notes/` by hand
(or by Claude on request).

**Notion's role, precisely:** operations only — content calendar, pipelines,
trackers, CRM-ish databases. The 2023 "Second Brain [Template]" in Notion is
superseded by this vault; archive it rather than maintaining two knowledge
stores. Notes *about* work-in-flight live with the project in `projects/`;
status lives in Notion.

## Layer model

```
CAPTURE      Reader (read things) · Recall (summarize things) · inbox/ (think things)
             ↓ weekly triage
LITERATURE   sources/  — one note per consumed source; highlights + your reactions
             ↓ distill (the human step, AI-assisted)
KNOWLEDGE    notes/    — atomic evergreen notes, claim-titled, densely linked
             ↑↓ navigate via notes/mocs/
EXPRESS      projects/ — posts, briefs, playbooks, client work drafted FROM notes
```

## Public repo policy

This repo is public. The dividing line:

**Committed (public):** evergreen notes in your own words, MOCs, prompts,
templates, docs, project notes for *your own* published work. Short attributed
quotes at fair-use scale are fine.

**Gitignored (local only):** `sources/readwise/` (bulk copyrighted highlight
text), `scripts/.sync-state.json`, `.obsidian/`, and any folder named
`private/` anywhere in the vault (use `projects/<x>/private/` for
client-identifiable material).

**Never anywhere in the repo:** client names tied to unpublished engagement
material, confidential documents, credentials. The sync script additionally
supports `--exclude-tag` so client-tagged Readwise documents never even land
on disk here.

If the repo is ever made private (note: the dashboard's GitHub Pages likely
depends on it staying public), the calculus changes — you could then commit
`sources/readwise/` and give cloud AIs the full corpus. Revisit
`.gitignore` at that point; nothing else needs to change.

## What this system deliberately does NOT do

- **No two-way sync, no plugins-as-infrastructure.** Fewer moving parts than a
  Zapier/n8n mesh; one stdlib Python script is the only automation.
- **No folders-as-taxonomy.** Topics are tags + MOCs, not directory trees.
  Folders encode *lifecycle* (inbox → sources/notes → projects → archive).
- **No daily-notes ritual, no streaks.** The system asks for ~5 min/day of
  capture discipline and one 30-minute weekly review. Anything heavier gets
  abandoned by month two.
- **No AI auto-writing to `notes/` unsupervised.** Drafts arrive as
  `status: seed`; you promote them. This keeps the vault trustworthy enough to
  publish from.
