# AI & Small Law — Daily Brief

A self-updating news dashboard covering five beats:

1. **Top AI News** — the day's biggest AI stories
2. **AI for SMEs** — practical AI uses for small and medium-sized businesses
3. **Small Law Firm News** — the solo/small-firm legal market
4. **AI for Small Law Firms** — legal AI tools, adoption, and ethics for small firms
5. **Consulting for Small Law Firms** — consultants, coaches, and practice management

## How it works

```
fetch_news.py  ──►  data/news.json + data/news.js  ──►  index.html
     ▲                                                      (static, no build step)
     │
GitHub Actions (.github/workflows/update-news.yml)
runs daily at 11:15 UTC and commits refreshed data
```

- `fetch_news.py` pulls Google News RSS searches plus curated RSS/Atom feeds
  (TechCrunch, VentureBeat, The Verge, Above the Law, LawSites, Artificial Lawyer,
  Attorney at Work, Lawyerist, …), then dedupes, scores, and keeps the top ~10
  stories per section. Python standard library only — no dependencies.
- Scoring = source weight + freshness decay + topic-keyword boosts. Stories land
  in the most specific section they match, so an "AI for small firms" story won't
  also crowd the general AI section.
- If a niche section comes back thin (fewer than 3 fresh stories), it's topped up
  from the previous day's data so the dashboard never renders empty.
- `index.html` is fully static and reads `data/news.js`, so it works over
  `file://`, GitHub Pages, or any static host. Light/dark theme follows the OS and
  can be toggled (persisted in `localStorage`).

## The daily schedule

The workflow in `.github/workflows/update-news.yml` runs at **11:15 UTC daily**,
on pushes to `main` that touch `dashboard/`, and via a manual **Run workflow**
button under the Actions tab. GitHub only runs scheduled workflows from the
**default branch**, so the daily refresh starts once this lands on `main`.

## Viewing it

- **Locally**: just open `dashboard/index.html` in a browser (or
  `python -m http.server` from the repo root and visit `/dashboard/`).
- **GitHub Pages**: the workflow's `deploy-pages` job publishes `dashboard/` as
  the site root and **enables Pages automatically on its first run after
  merge** — no Settings visit needed. The dashboard is served at
  `https://gyates45.github.io/curated/` and every refresh (daily cron, manual
  run, or dashboard change pushed to `main`) redeploys it.

## Tuning

All sources live in the `CATEGORIES` list at the top of `fetch_news.py` — each
entry is a Google News query or feed URL with a weight, optional `require`
keyword filters, per-section freshness windows (`window_hours`), and `boost`
keywords. Edit that list to add feeds, drop sources, or re-tune ranking; run
`python dashboard/fetch_news.py` to test locally (needs outbound network).
