# Capture: what goes where

## The decision table

| You have… | It goes to | How |
|---|---|---|
| An article / newsletter / PDF / YouTube video worth reading | **Readwise Reader** | Save with ≤2 topic tags + a one-line document note: *why saved* |
| Something you need summarized & graphed right now | **Recall** | Save; add topic tag |
| A stray idea, a shower thought, a half-formed take | **`inbox/`** | One markdown file, any format, no ceremony (Obsidian: quick note) |
| A LinkedIn post/newsletter idea | **`inbox/`** | Prefix filename `idea-` |
| A task, a deadline, a content-calendar entry | **Notion** | Existing databases |
| A client document or engagement material | **Notion / local `private/`** | Never in committed vault paths — repo is public |
| A prompt that worked well | **`resources/prompts/`** | Copy it in with a note on when to use it |
| A source you finished + highlighted | flows to **`sources/readwise/`** | automatically, via weekly sync |

Rule of thumb: **if in doubt, Reader.** It is the funnel; the weekly review
sorts the rest.

## While reading (highlight discipline)

- Highlight **claims and mechanisms**, not vibes. If you wouldn't reuse the
  sentence in a post or with a client, don't highlight it.
- Add an inline note starting with a verb when you react: "use in workshop
  deck", "contradicts my take on X", "steal this structure".
- One-line document note = why you saved it. Future-you (and Claude) triage by
  that line.

## Tag vocabulary (controlled)

Use these across Reader, Recall, and vault frontmatter. Max 3 topic tags per item.

**Business core**
`legal-ai` · `small-law-firms` · `smb-ai` · `actionable-ai` (your business
itself) · `consulting` · `playbooks` · `prospects`

**Craft**
`content` · `writing` · `linkedin` · `newsletter` · `marketing` · `seo` ·
`speaking`

**Tools & method**
`ai-tools` plus the specific tool as its own tag when central: `claude` ·
`chatgpt` · `gemini` · `notebooklm` · `mcp` · `n8n` · `zapier` · `notion` ·
`readwise` · `obsidian` — and `productivity` · `systems` · `para`

**Personal**
`health` · `fitness` · `mindset` · `psychology` · `family` · `personal`

Anything not on this list: either don't tag it, or add the tag *here* first so
the vocabulary stays controlled. New tags need a reason.

## Automation tags — hands off

These Reader tags are wired into existing automations (daily brief pipelines,
morning digests). **Never rename, merge, or delete them**, and don't use them
for manual tagging:

`small-law-firm-ai-daily` · `small-law-firm-ai-source` · `smb-ai-daily` ·
`smb-ai-source` · `morning-brief` · `morning-digest` · `daily-briefing` ·
`ai-digest` · `talking-point` · `tool-watch` · `1 - today's news you can use` ·
date-stamped tags (`2026-04-13`, …)

## Known cleanup candidates (run as a "tag hygiene" job, with approval)

- Case duplicates: `actionable-ai` / `ActionableAI` · `small-business` /
  `Small Business`
- Near-duplicates to merge into one: `law` / `legal` / `legal-tech` →
  `legal-ai` where AI-related, `legal` otherwise · `trend` / `trends` ·
  `podcasts` / `podcasting`
- Date-stamped tags older than 90 days: candidates for deletion **if** the
  generating automation no longer reads them — verify before touching.
