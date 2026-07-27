# scripts/

## `readwise_sync.py` — Readwise → `sources/readwise/`

Pulls highlights via the [Readwise export API](https://readwise.io/api_deets)
into one markdown file per source. Python 3.8+, standard library only.

```sh
export READWISE_TOKEN=xxx        # from https://readwise.io/access_token

python3 readwise_sync.py --limit 20    # trial run: first 20 sources, no state saved
python3 readwise_sync.py --full        # full backfill (see note below)
python3 readwise_sync.py               # weekly incremental: only new/updated
```

- **Incremental by default.** A state file (`.sync-state.json`, gitignored)
  remembers the last run; existing files get new highlights appended
  (deduplicated by highlight ID), never duplicated.
- **First full backfill takes a while.** The account has ~35k highlights and
  Readwise rate-limits the API; the script waits and resumes automatically on
  429s. Start it and let it run.
- **`--exclude-tag TAG`** (repeatable, or `READWISE_EXCLUDE_TAGS=a,b,c`):
  sources carrying that Readwise tag never land on disk here. Use it for
  client-engagement tags and anything else that shouldn't exist outside
  Readwise, even locally.
- `--dry-run` previews, `--out DIR` redirects, `--self-test` runs the offline
  unit checks.

### Privacy: why the output is gitignored

This repo is **public**. `sources/readwise/` holds bulk verbatim text from
copyrighted articles/newsletters plus potentially client-adjacent material —
so it stays local-only (`.gitignore` covers it). The synced files still give
you and any *local* AI session (Claude Code on your machine, Obsidian search)
the full corpus; cloud AIs read the distilled `notes/` instead, which is the
point of the system anyway.

If the repo ever goes private, committing `sources/readwise/` becomes a
reasonable choice — flip the `.gitignore` line and push. Don't set this up as
a GitHub Action before then: it would need the token as a secret only to
write files git ignores.

### Suggested automation (local)

Weekly is enough — it's step 2 of the weekly review. If you want it ambient,
a local cron/launchd job on your machine works:

```
0 15 * * 5  cd ~/curated && READWISE_TOKEN=xxx python3 second-brain/scripts/readwise_sync.py
```
