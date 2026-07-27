#!/usr/bin/env python3
"""Sync Readwise highlights into second-brain/sources/readwise/ as markdown.

One file per book/article/video, frontmatter + highlights, idempotent:
incremental runs append only new highlights (tracked via <!-- rw:ID -->
markers); --full rebuilds files from scratch.

Python standard library only. Auth: READWISE_TOKEN env var (get yours at
https://readwise.io/access_token).

The default output directory is GITIGNORED because this repo is public and
raw highlights are copyrighted text. See scripts/README.md before changing
that. Use --exclude-tag for anything (e.g. client material) that shouldn't
even land on disk here.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API_URL = "https://readwise.io/api/v2/export/"
HERE = Path(__file__).resolve().parent
DEFAULT_OUT = HERE.parent / "sources" / "readwise"
STATE_FILE = HERE / ".sync-state.json"
ID_MARKER = re.compile(r"<!-- rw:(\d+) -->")


# ---------------------------------------------------------------- API client

def fetch_page(token, cursor=None, updated_after=None):
    """Fetch one page from the export API, honoring 429 rate limits."""
    params = {}
    if cursor:
        params["pageCursor"] = cursor
    if updated_after:
        params["updatedAfter"] = updated_after
    url = API_URL + ("?" + urllib.parse.urlencode(params) if params else "")
    request = urllib.request.Request(url, headers={"Authorization": f"Token {token}"})
    while True:
        try:
            with urllib.request.urlopen(request, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as err:
            if err.code == 429:
                wait = int(err.headers.get("Retry-After", "30"))
                print(f"  rate limited; sleeping {wait}s …", file=sys.stderr)
                time.sleep(wait)
                continue
            if err.code == 401:
                sys.exit("error: Readwise rejected the token (401). "
                         "Check READWISE_TOKEN — https://readwise.io/access_token")
            raise


def iter_books(token, updated_after=None):
    cursor = None
    while True:
        page = fetch_page(token, cursor=cursor, updated_after=updated_after)
        yield from page.get("results", [])
        cursor = page.get("nextPageCursor")
        if not cursor:
            return


# ------------------------------------------------------------- md rendering

def slugify(text, max_length=60):
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "untitled").lower()).strip("-")
    return slug[:max_length].rstrip("-") or "untitled"


def yaml_str(value):
    """A JSON string is a valid YAML string — safe for arbitrary titles."""
    return json.dumps(value if value is not None else "", ensure_ascii=False)


def book_tag_names(book):
    return [t.get("name", "") for t in (book.get("book_tags") or []) if t.get("name")]


def keepable_highlights(book):
    kept = []
    for h in book.get("highlights", []):
        text = (h.get("text") or "").strip()
        if not text or h.get("is_discard"):
            continue
        if text.startswith("![](") and text.endswith(")"):
            continue  # image-only highlight; noise in a text vault
        kept.append(h)
    return kept


def render_highlight(h):
    lines = ["> " + line for line in (h.get("text") or "").strip().splitlines()]
    block = "\n".join(lines)
    note = (h.get("note") or "").strip()
    if note:
        block += f"\n\n**note:** {note}"
    loc = h.get("location")
    if loc is not None and h.get("location_type") not in (None, "none"):
        block += f"\n<small>{h.get('location_type')} {loc}</small>"
    return f"{block}\n<!-- rw:{h.get('id')} -->\n"


def render_book(book, highlights, synced_on):
    fm = [
        "---",
        f"title: {yaml_str(book.get('readable_title') or book.get('title'))}",
        "type: source",
        f"author: {yaml_str(book.get('author'))}",
        f"category: {book.get('category') or 'article'}",
        f"source_url: {yaml_str(book.get('source_url'))}",
        f"readwise_url: {yaml_str(book.get('readwise_url'))}",
        "tags: [" + ", ".join(yaml_str(t) for t in book_tag_names(book)) + "]",
        f"synced: {synced_on}",
        "---",
        "",
    ]
    body = []
    if (book.get("document_note") or "").strip():
        body += [f"**Why I saved this:** {book['document_note'].strip()}", ""]
    if (book.get("summary") or "").strip():
        body += ["## Summary", "", book["summary"].strip(), ""]
    body += ["## Highlights", ""]
    body += [render_highlight(h) for h in highlights]
    return "\n".join(fm + body)


def merge_new_highlights(existing_text, highlights):
    """Append only highlights whose rw:ID isn't already in the file."""
    seen = set(ID_MARKER.findall(existing_text))
    fresh = [h for h in highlights if str(h.get("id")) not in seen]
    if not fresh:
        return existing_text, 0
    text = existing_text.rstrip("\n") + "\n\n"
    text += "\n".join(render_highlight(h) for h in fresh)
    return text, len(fresh)


# -------------------------------------------------------------------- state

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")


# --------------------------------------------------------------------- main

def sync(args):
    token = args.token or os.environ.get("READWISE_TOKEN")
    if not token:
        sys.exit("error: set READWISE_TOKEN (https://readwise.io/access_token) "
                 "or pass --token")

    excludes = {t.strip().lower() for t in args.exclude_tag}
    excludes |= {t.strip().lower()
                 for t in os.environ.get("READWISE_EXCLUDE_TAGS", "").split(",")
                 if t.strip()}

    out_dir = Path(args.out) if args.out else DEFAULT_OUT
    out_dir.mkdir(parents=True, exist_ok=True)

    state = load_state()
    updated_after = None if args.full else state.get("updated_after")
    run_started = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    synced_on = run_started[:10]

    mode = "full backfill" if updated_after is None else f"incremental since {updated_after}"
    print(f"sync: {mode} → {out_dir}")

    created = updated = skipped_excluded = skipped_empty = new_highlights = books_seen = 0
    for book in iter_books(token, updated_after=updated_after):
        if args.limit and books_seen >= args.limit:
            print(f"  --limit {args.limit} reached; stopping (state not saved)")
            break
        books_seen += 1

        tags_lower = {t.lower() for t in book_tag_names(book)}
        if tags_lower & excludes:
            skipped_excluded += 1
            continue

        highlights = keepable_highlights(book)
        if not highlights:
            skipped_empty += 1
            continue

        name = f"{slugify(book.get('readable_title') or book.get('title'))}--rw{book.get('user_book_id')}.md"
        path = out_dir / name

        if path.exists() and not args.full:
            merged, added = merge_new_highlights(path.read_text(), highlights)
            if added:
                if not args.dry_run:
                    path.write_text(merged)
                updated += 1
                new_highlights += added
                print(f"  ~ {name} (+{added})")
        else:
            if not args.dry_run:
                path.write_text(render_book(book, highlights, synced_on))
            created += 1
            new_highlights += len(highlights)
            print(f"  + {name} ({len(highlights)})")

    hit_limit = bool(args.limit and books_seen >= args.limit)
    if not args.dry_run and not hit_limit:
        save_state({"updated_after": run_started})

    print(f"done: {created} created, {updated} updated, {new_highlights} highlights added, "
          f"{skipped_excluded} excluded by tag, {skipped_empty} empty/skipped"
          + (" [dry-run]" if args.dry_run else ""))


def self_test():
    book = {
        "user_book_id": 42, "title": "A Test: Book?!", "readable_title": "A Test: Book?!",
        "author": "Someone", "category": "articles", "source_url": "https://x.example",
        "readwise_url": "https://readwise.io/x", "document_note": "why note",
        "summary": "", "book_tags": [{"name": "legal-ai"}],
        "highlights": [
            {"id": 1, "text": "First \"insight\"", "note": "use this", "location": 3,
             "location_type": "order"},
            {"id": 2, "text": "![](https://img.example/x.png)"},
            {"id": 3, "text": "Second insight", "is_discard": True},
        ],
    }
    assert slugify("A Test: Book?!") == "a-test-book"
    assert slugify("") == "untitled"
    assert slugify("x" * 100).__len__() <= 60
    kept = keepable_highlights(book)
    assert [h["id"] for h in kept] == [1], kept
    text = render_book(book, kept, "2026-07-27")
    assert text.startswith("---\n") and '"A Test: Book?!"' in text
    assert "<!-- rw:1 -->" in text and "rw:2" not in text and "rw:3" not in text
    assert "**Why I saved this:** why note" in text
    merged, added = merge_new_highlights(text, kept)
    assert added == 0 and merged == text
    merged, added = merge_new_highlights(text, kept + [{"id": 9, "text": "New one"}])
    assert added == 1 and "<!-- rw:9 -->" in merged
    print("self-test OK")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--full", action="store_true",
                   help="ignore sync state; rebuild every file from scratch")
    p.add_argument("--limit", type=int, default=0,
                   help="process at most N books (trial runs; state is not saved)")
    p.add_argument("--exclude-tag", action="append", default=[], metavar="TAG",
                   help="skip books carrying this Readwise tag (repeatable; "
                        "also reads READWISE_EXCLUDE_TAGS=a,b,c)")
    p.add_argument("--out", default=None,
                   help=f"output directory (default: {DEFAULT_OUT})")
    p.add_argument("--token", default=None, help="Readwise token (else READWISE_TOKEN)")
    p.add_argument("--dry-run", action="store_true", help="report without writing")
    p.add_argument("--self-test", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args()
    if args.self_test:
        self_test()
        return
    sync(args)


if __name__ == "__main__":
    main()
