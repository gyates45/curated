#!/usr/bin/env python3
"""Save the day's brief to a Readwise Reader library.

Runs after each data refresh in GitHub Actions. Reads dashboard/data/news.json,
renders a compact HTML digest, and saves it as a document via the Readwise
Reader API (POST https://readwise.io/api/v3/save/), where it lands in the
account's library like an emailed newsletter would.

Needs READWISE_TOKEN in the environment (a repo Actions secret; tokens come
from https://readwise.io/access_token). Without the token the script exits 0
with a notice, so the refresh never fails over the optional delivery. An API
failure exits 1 to make a broken delivery visible in the Actions run.

Optional: READWISE_LOCATION=feed files the brief under Reader's Feed section
instead of the inbox (default "new").
"""

from __future__ import annotations

import html
import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "news.json"
SITE_URL = "https://gyates45.github.io/curated/"
API_URL = "https://readwise.io/api/v3/save/"
TIMEOUT = 30


def esc(text: str) -> str:
    return html.escape(text or "", quote=True)


def build_digest(data: dict) -> tuple[str, str, str]:
    """Return (title, unique_url, html_body) for the day's brief."""
    raw = (data.get("generated_at") or "")[:10]
    try:
        day = datetime.strptime(raw, "%Y-%m-%d")
        day_label = f"{day.strftime('%B')} {day.day}, {day.year}"
    except ValueError:
        raw = "latest"
        day_label = "latest"

    parts = [
        f'<p>Top stories in AI, practical AI for SMEs, and the small-firm '
        f'legal market — <a href="{SITE_URL}">open the live dashboard</a>.</p>'
    ]
    for cat in data.get("categories", []):
        items = cat.get("items") or []
        if not items:
            continue
        parts.append(f"<h2>{esc(cat.get('title'))}</h2>")
        parts.append("<ul>")
        for item in items:
            line = (
                f'<li><a href="{esc(item.get("url") or SITE_URL)}">'
                f'{esc(item.get("title"))}</a> — {esc(item.get("source"))}'
            )
            if item.get("summary"):
                line += f"<br><small>{esc(item['summary'])}</small>"
            parts.append(line + "</li>")
        parts.append("</ul>")

    title = f"AI & Small Law Daily Brief — {day_label}"
    unique_url = f"{SITE_URL}?brief={raw}"  # one Reader document per day
    return title, unique_url, "\n".join(parts)


def save_to_readwise(token: str, title: str, url: str, body: str) -> None:
    payload = {
        "url": url,
        "html": body,
        "title": title,
        "category": "article",
        "location": os.environ.get("READWISE_LOCATION", "new"),
        "tags": ["daily-brief"],
        "saved_using": "curated-dashboard-action",
    }
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Token {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as resp:
        print(f"Readwise accepted the brief (HTTP {resp.status}): {title}")


def main() -> int:
    token = os.environ.get("READWISE_TOKEN", "").strip()
    if not token:
        print("READWISE_TOKEN not set; skipping Readwise delivery.")
        return 0

    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"cannot read {DATA_PATH}: {exc}", file=sys.stderr)
        return 1

    title, url, body = build_digest(data)
    try:
        save_to_readwise(token, title, url, body)
    except Exception as exc:  # noqa: BLE001 - surface any delivery failure
        print(f"Readwise delivery failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
