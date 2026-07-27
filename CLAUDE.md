# CLAUDE.md — gyates45/curated

Greg Yates' personal hub repo. Three independent subsystems share it:

| Subsystem | Path | What it is |
|---|---|---|
| CuratedStack site | repo root (Nuxt 2 app) | Curated links directory built on the CuratedStack template |
| Daily news dashboard | `dashboard/` | Self-updating "AI & Small Law" brief; a GitHub Action refreshes its data daily |
| Second brain | `second-brain/` | Plain-markdown knowledge vault + docs + sync scripts |

## Ground rules

- **This repo is PUBLIC** (it also serves GitHub Pages). Never commit
  client-identifiable material, unpublished client deliverables, or bulk dumps
  of copyrighted highlights. `second-brain/sources/readwise/` and any folder
  named `private/` are gitignored on purpose — leave them that way unless Greg
  makes the repo private.
- Working inside `second-brain/`? Read `second-brain/CLAUDE.md` first — it is
  the operating manual (conventions, jobs, rules).
- Nuxt site commands: `npm install`, `npm run dev`, `npm test` (also validates
  `content/*.json`), `npm run generate`.
- `dashboard/data/*` is machine-written by `dashboard/fetch_news.py` via
  `.github/workflows/update-news.yml` — don't hand-edit generated data.
- Commit style: conventional commits, enforced by commitlint
  (`feat:`, `fix:`, `docs:`, `chore:`, …).
