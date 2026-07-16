#!/usr/bin/env python3
"""Fetch, rank, and store the day's top stories for the Daily Brief dashboard.

Categories:
  1. top_ai         Top AI news
  2. ai_sme         Practical AI for small & medium-sized businesses
  3. small_law      Small law firm news
  4. ai_small_law   AI for small law firms
  5. law_consulting Consulting & practice management for small law firms

Sources are Google News RSS searches plus a handful of curated RSS/Atom feeds.
Standard library only, so it runs on a bare GitHub Actions runner.

Usage:
  python dashboard/fetch_news.py           # fetch, rank, write data files
  python dashboard/fetch_news.py --regen   # rebuild news.js from news.json
"""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"
JSON_PATH = DATA_DIR / "news.json"
JS_PATH = DATA_DIR / "news.js"

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
FETCH_TIMEOUT = 20
MAX_ITEMS = 10
MIN_FRESH_ITEMS = 3  # below this, backfill a category from the previous run


def gnews_rss(query: str) -> str:
    return (
        "https://news.google.com/rss/search?q="
        + urllib.parse.quote(query)
        + "&hl=en-US&gl=US&ceid=US:en"
    )


def gnews_web(query: str) -> str:
    return "https://news.google.com/search?q=" + urllib.parse.quote(query)


# Each source is a dict:
#   url      feed URL (Google News RSS search or a site feed)
#   weight   base score for items from this source
#   require  optional list of OR-groups; an item must match at least one term
#            of every group (word-boundary match on title+summary). Used to
#            narrow broad site feeds; Google News queries are already narrow.
CATEGORIES = [
    {
        "id": "top_ai",
        "title": "Top AI News",
        "tagline": "The day's biggest stories in artificial intelligence.",
        "more_url": gnews_web("artificial intelligence when:1d"),
        "window_hours": 48,
        "boost": [
            "openai", "anthropic", "google", "deepmind", "meta", "microsoft",
            "model", "launch", "funding", "billion", "regulation", "chips",
            "agents", "research", "breakthrough",
        ],
        "sources": [
            {"url": gnews_rss("artificial intelligence when:1d"), "weight": 6},
            {"url": gnews_rss('("OpenAI" OR "Anthropic" OR "Google DeepMind" OR "Meta AI" OR "Microsoft AI") when:1d'), "weight": 7},
            {"url": gnews_rss('AI (launch OR funding OR regulation OR model) when:1d'), "weight": 6},
            {"url": "https://techcrunch.com/category/artificial-intelligence/feed/", "weight": 9},
            {"url": "https://venturebeat.com/category/ai/feed/", "weight": 8},
            {"url": "https://www.theverge.com/rss/index.xml", "weight": 9,
             "require": [["ai", "artificial intelligence", "openai", "anthropic", "chatbot", "llm"]]},
        ],
    },
    {
        "id": "ai_sme",
        "title": "AI for SMEs",
        "tagline": "Practical ways small and medium-sized businesses are putting AI to work.",
        "more_url": gnews_web('AI "small business" when:7d'),
        "window_hours": 96,
        "boost": [
            "practical", "adopt", "adoption", "tools", "guide", "how",
            "productivity", "automate", "automation", "customers", "marketing",
            "revenue", "workflow", "save", "affordable",
        ],
        "sources": [
            {"url": gnews_rss('AI "small business" when:3d'), "weight": 7},
            {"url": gnews_rss('AI ("small businesses" OR "SMBs" OR "SMEs") (tools OR adopt OR productivity) when:3d'), "weight": 7},
            {"url": gnews_rss('"artificial intelligence" "small business" (practical OR guide OR "how to") when:7d'), "weight": 6},
            {"url": "https://smallbiztrends.com/feed/", "weight": 6,
             "require": [["ai", "artificial intelligence", "chatgpt", "copilot", "automation", "chatbot"]]},
        ],
    },
    {
        "id": "small_law",
        "title": "Small Law Firm News",
        "tagline": "What's happening in the small-firm and solo legal market.",
        "more_url": gnews_web('"small law firm" OR "solo practitioner" when:7d'),
        "window_hours": 192,
        "boost": [
            "small firm", "small firms", "solo", "boutique", "clients",
            "billing", "growth", "hiring", "succession", "malpractice",
            "fees", "practice",
        ],
        "sources": [
            {"url": gnews_rss('"small law firm" OR "small law firms" when:7d'), "weight": 7},
            {"url": gnews_rss('"solo practitioner" OR "solo attorney" OR "boutique law firm" when:7d'), "weight": 6},
            {"url": gnews_rss('"law firm" ("small firm" OR solo) (management OR growth OR billing OR clients) when:7d'), "weight": 5},
            {"url": "https://abovethelaw.com/feed/", "weight": 8,
             "require": [["small firm", "small firms", "small law", "solo", "boutique"]]},
            {"url": "https://www.attorneyatwork.com/feed/", "weight": 7},
            {"url": "https://lawyerist.com/feed/", "weight": 7},
        ],
    },
    {
        "id": "ai_small_law",
        "title": "AI for Small Law Firms",
        "tagline": "Legal AI tools, adoption, and ethics through a small-firm lens.",
        "more_url": gnews_web('AI "small law firm" OR "legal AI" when:7d'),
        "window_hours": 192,
        "boost": [
            "small firm", "small firms", "solo", "affordable",
            "practice management", "clio", "mycase", "smokeball", "adoption",
            "ethics", "drafting", "intake", "research", "paralegal",
        ],
        "sources": [
            {"url": gnews_rss('AI ("small law firm" OR "small law firms" OR "solo attorney") when:7d'), "weight": 8},
            {"url": gnews_rss('"legal AI" ("small firm" OR "small firms" OR solo) when:7d'), "weight": 7},
            {"url": gnews_rss('("legal tech" OR "legal technology") AI lawyers when:3d'), "weight": 5},
            {"url": "https://www.lawnext.com/feed", "weight": 8,
             "require": [["ai", "artificial intelligence", "generative", "genai", "copilot", "llm"]]},
            {"url": "https://www.artificiallawyer.com/feed/", "weight": 8},
        ],
    },
    {
        "id": "law_consulting",
        "title": "Consulting for Small Law Firms",
        "tagline": "Consultants, coaches, and practice-management advice for small firms.",
        "more_url": gnews_web('"law firm" consulting "small firm" when:14d'),
        "window_hours": 360,
        "boost": [
            "consultant", "consulting", "coach", "coaching",
            "practice management", "pricing", "profitability", "marketing",
            "succession", "strategy", "advisory",
        ],
        "sources": [
            {"url": gnews_rss('"law firm" (consultant OR consulting OR advisory) ("small firm" OR solo OR "small law") when:14d'), "weight": 7},
            {"url": gnews_rss('"legal practice management" (consultant OR consulting OR coach) when:14d'), "weight": 6},
            {"url": gnews_rss('"law firm coach" OR "law practice consultant" OR "law firm consultancy" when:14d'), "weight": 6},
            {"url": "https://www.attorneyatwork.com/feed/", "weight": 6,
             "require": [["consult", "consulting", "coach", "advisor", "practice management"]]},
        ],
    },
]

# Build the most specific categories first so a story lands in the narrowest
# section it fits; display order stays as declared in CATEGORIES.
BUILD_ORDER = ["ai_small_law", "law_consulting", "ai_sme", "small_law", "top_ai"]


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def fetch_url(url: str) -> bytes | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001 - any feed failure is non-fatal
            log(f"  fetch attempt {attempt} failed for {url}: {exc}")
    return None


TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def strip_html(text: str) -> str:
    return WS_RE.sub(" ", html.unescape(TAG_RE.sub(" ", text or ""))).strip()


def clip(text: str, limit: int = 240) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def parse_date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = parsedate_to_datetime(raw)  # RFC 822 (RSS)
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))  # ISO (Atom)
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _text(el: ET.Element | None) -> str:
    return (el.text or "").strip() if el is not None else ""


def parse_feed(raw: bytes, feed_url: str) -> list[dict]:
    """Parse RSS 2.0 or Atom into a list of raw item dicts."""
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        log(f"  XML parse error for {feed_url}: {exc}")
        return []

    items = []
    is_gnews = "news.google.com" in feed_url

    for item in root.iter("item"):  # RSS 2.0
        title = strip_html(_text(item.find("title")))
        link = _text(item.find("link"))
        source_el = item.find("source")
        source = strip_html(_text(source_el))
        summary = strip_html(_text(item.find("description")))
        published = parse_date(_text(item.find("pubDate")))
        if is_gnews:
            # Google News titles end in " - Publisher" and descriptions are
            # just markup around the same headline; drop both.
            if source and title.endswith(" - " + source):
                title = title[: -len(" - " + source)].rstrip()
            summary = ""
        if not source:
            source = urllib.parse.urlparse(link or feed_url).netloc.removeprefix("www.")
        if title and link:
            items.append({"title": title, "url": link, "source": source,
                          "published": published, "summary": clip(summary)})

    if not items:  # Atom
        ns = {"a": "http://www.w3.org/2005/Atom"}
        feed_title = strip_html(_text(root.find("a:title", ns)))
        for entry in root.findall("a:entry", ns):
            title = strip_html(_text(entry.find("a:title", ns)))
            link = ""
            for link_el in entry.findall("a:link", ns):
                if link_el.get("rel") in (None, "alternate"):
                    link = link_el.get("href", "")
                    break
            summary = strip_html(_text(entry.find("a:summary", ns)))
            published = parse_date(
                _text(entry.find("a:published", ns)) or _text(entry.find("a:updated", ns))
            )
            source = feed_title or urllib.parse.urlparse(feed_url).netloc.removeprefix("www.")
            if title and link:
                items.append({"title": title, "url": link, "source": source,
                              "published": published, "summary": clip(summary)})
    return items


def kw_match(term: str, text: str) -> bool:
    return re.search(r"\b" + re.escape(term.lower()) + r"\b", text) is not None


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()[:60]


def build_category(cat: dict, now: datetime, seen: set[str],
                   feed_cache: dict[str, list[dict]]) -> list[dict]:
    window = timedelta(hours=cat["window_hours"])
    candidates: dict[str, dict] = {}

    for src in cat["sources"]:
        if src["url"] not in feed_cache:
            raw = fetch_url(src["url"])
            feed_cache[src["url"]] = parse_feed(raw, src["url"]) if raw else []
            log(f"  {len(feed_cache[src['url']]):3d} items  {src['url'][:110]}")
        for item in feed_cache[src["url"]]:
            text = (item["title"] + " " + item["summary"]).lower()
            if any(not any(kw_match(t, text) for t in group)
                   for group in src.get("require", [])):
                continue
            if item["published"] and now - item["published"] > window:
                continue
            key = norm_title(item["title"]) or item["url"]
            if key in candidates and candidates[key]["weight"] >= src["weight"]:
                continue
            candidates[key] = {**item, "weight": src["weight"], "key": key}

    scored = []
    for item in candidates.values():
        score = float(item["weight"])
        if item["published"]:
            age_h = (now - item["published"]).total_seconds() / 3600
            score += max(0.0, 1.0 - age_h / cat["window_hours"]) * 30
        else:
            score -= 4  # undated items rank behind anything fresh
        text = (item["title"] + " " + item["summary"]).lower()
        hits = sum(1 for term in cat["boost"] if kw_match(term, text))
        score += min(hits, 4) * 6
        scored.append((score, item))

    scored.sort(key=lambda pair: pair[0], reverse=True)

    picked = []
    for score, item in scored:
        if item["key"] in seen or item["url"] in seen:
            continue
        seen.add(item["key"])
        seen.add(item["url"])
        picked.append({
            "title": item["title"],
            "url": item["url"],
            "source": item["source"],
            "published": item["published"].isoformat().replace("+00:00", "Z")
                         if item["published"] else None,
            "summary": item["summary"],
        })
        if len(picked) >= MAX_ITEMS:
            break
    return picked


def load_previous() -> dict:
    try:
        return json.loads(JSON_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def backfill(cat_id: str, fresh: list[dict], previous: dict, seen: set[str]) -> list[dict]:
    """Top a thin category back up with items from the previous run."""
    if len(fresh) >= MIN_FRESH_ITEMS:
        return fresh
    prev_items = next((c["items"] for c in previous.get("categories", [])
                       if c["id"] == cat_id), [])
    for item in prev_items:
        key = norm_title(item.get("title", ""))
        if key in seen or item.get("url") in seen:
            continue
        seen.add(key)
        seen.add(item.get("url", ""))
        fresh.append(item)
        if len(fresh) >= MIN_FRESH_ITEMS:
            break
    return fresh


def write_outputs(data: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, ensure_ascii=False, indent=2)
    JSON_PATH.write_text(text + "\n", encoding="utf-8")
    JS_PATH.write_text("window.NEWS_DATA = " + text + ";\n", encoding="utf-8")
    log(f"wrote {JSON_PATH} and {JS_PATH}")


def main() -> int:
    if "--regen" in sys.argv:
        previous = load_previous()
        if not previous:
            log("no existing news.json to regenerate from")
            return 1
        write_outputs(previous)
        return 0

    now = datetime.now(timezone.utc)
    previous = load_previous()
    seen: set[str] = set()
    feed_cache: dict[str, list[dict]] = {}
    results: dict[str, list[dict]] = {}

    by_id = {c["id"]: c for c in CATEGORIES}
    for cat_id in BUILD_ORDER:
        cat = by_id[cat_id]
        log(f"category {cat_id}")
        results[cat_id] = build_category(cat, now, seen, feed_cache)

    total_fresh = sum(len(v) for v in results.values())
    if total_fresh == 0:
        log("no items fetched at all; keeping previous data files untouched")
        return 1

    for cat_id in BUILD_ORDER:
        results[cat_id] = backfill(cat_id, results[cat_id], previous, seen)

    data = {
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "categories": [
            {
                "id": cat["id"],
                "title": cat["title"],
                "tagline": cat["tagline"],
                "more_url": cat["more_url"],
                "items": results[cat["id"]],
            }
            for cat in CATEGORIES
        ],
    }
    write_outputs(data)
    log(f"done: {total_fresh} fresh items across {len(CATEGORIES)} categories")
    return 0


if __name__ == "__main__":
    sys.exit(main())
