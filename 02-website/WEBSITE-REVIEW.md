# Actionable AI Website Review — v2 (live WordPress site) — July 2026

**This version supersedes v1**, which reviewed the retired static-HTML prototype in this folder. The live actionableai.net is a different build: a WordPress/Kadence site constructed from `actionable-ai-website-copy.md` + `actionable-ai-wordpress-build-guide.md` (Google Drive → Website folder, April 25–27, 2026).

**How this review was produced.** This session's network policy blocks direct fetches of actionableai.net (and web.archive.org), so the live rendered site could not be loaded from here. The review is based on the next-best authoritative sources: (a) the April copy + build guide the site was built from, (b) the *live current state* of your Calendly account (13 event types) and Kit account (17 forms, 2 published posts, verified domains), and (c) web-search checks. Anything edited inside WordPress since April is invisible to me — Part 7 is a short spot-check list to reconcile against the live pages.

**Reviewed against your three goals, in priority order:** (1) trust + thought leadership, (2) intro-call bookings, (3) email-for-lead-magnet newsletter signups. **Audience:** managing partners and CAOs at Florida firms of **25 lawyers or fewer**.

---

## First: what the current site gets right

Credit where due — the April build is dramatically stronger than the old prototype, and several things v1 flagged are already solved:

- **The Big Law credential leads.** "A former Big Law partner. Not a tech evangelist." / "decades as a corporate partner." This is the right anchor for a managing-partner audience.
- **Location is real.** Daytona Beach Shores appears on About and Contact.
- **No fabricated statistics.** The FAQ's ROI answer — *"I won't promise a number I can't back up"* — is exactly the right proof posture for a young practice, and it converts honesty into differentiation.
- **The FAQ page is genuinely good.** The confidentiality answer (Copilot-in-tenant vs. public chatbot) and "I'm a former lawyer. I am not your lawyer." are trust-builders most competitors won't write.
- **Testimonial framing is honest** ("These speak to how I work. AI-specific case studies coming as engagements complete").
- **Tier naming** ("One Workflow, Done Right") and the "What I won't do" section are strong.
- **Voice** is consistent and right: dry, specific, anti-hype.

The remaining problems are (1) the copy predates three months of business evolution — your positioning, firm-size target, email platform, lead-magnet library, and scheduling infrastructure all changed after April — and (2) a handful of conversion-path defects.

### Scorecard

| Goal | Grade | Summary |
|---|---|---|
| 1. Trust / thought leadership | B− | Strong voice and credential; but Florida is a footnote instead of a strategy, placeholders (testimonials, retainer price, orphaned FAQ answer) may still be live, and the site isn't indexed by search engines yet |
| 2. Book intro calls | C | CTAs exist and Calendly exists, but the promised "20-minute call" doesn't match any real event (all 13 are 30 min), and the "pay at booking via Stripe" flow described on Pricing isn't wired — no Calendly event has payment attached |
| 3. Newsletter via lead magnet | D | The site was built for Beehiiv; you're on Kit. You now have 14 finished lead magnets with live Kit forms and (per the April plan) none on the site. The engine exists; the site doesn't use it |

---

## Part 1 — Business-alignment gaps (the copy is three months behind the business)

### 1.1 "Under 50 people" → "25 lawyers or fewer"

Your stated market is firms under 25 lawyers. The April copy says "under 50" at least five times:

- Home hero subhead ("under 50 people, attorneys included")
- Home Section 4 ("Built for firms under 50")
- About fit list ("Run under 50 people, attorneys included")
- FAQ "What size firm is this built for?" ("Under 50 people… Below 10 is the sweet spot")

Replace all of them with one consistent formulation — recommended: **"firms of 25 lawyers or fewer"** (and keep the FAQ's honest "below 10 is the sweet spot" line if that's still true — specificity like that builds trust). Also update the Fluent Forms firm-size options if a size dropdown exists: Solo / 2–5 / 6–10 / 11–25 / Over 25.

### 1.2 Florida is a mailing address, not a positioning

The current copy names Daytona Beach Shores but then actively nationalizes: "I work with firms across the country," "I cover all 50 states for retainer clients," "Working with small law firms across the U.S." Your brief says the primary market is **Florida managing partners and CAOs**. Two additional reasons Florida-first is right beyond focus:

- **The content angle is unbeatable in-state.** [Florida Bar Ethics Opinion 24-1](https://www.floridabar.org/etopinions/opinion-24-1/) (Jan. 2024) green-lights generative AI with duties — confidentiality (informed consent before confidential data enters third-party tools), competence/oversight, honest billing, Rule 1.18 limits on AI intake ([JD Supra summary](https://www.jdsupra.com/legalnews/florida-bar-advisory-opinion-24-1-gives-9432036/), [Hinshaw analysis](https://www.hinshawlaw.com/en/insights/lawyers-for-the-profession-alert/florida-bar-advisory-opinion-24-1-gives-green-light-to-generative-ai-use-by-lawyers-with-four-ethical-caveats/)). And Florida was the first state to mandate [3 hours of technology CLE per cycle](https://www.floridabar.org/member/cle/general-cle-info-and-requirements/) ([ABA Journal](https://www.abajournal.com/news/article/florida_supreme_court_approves_mandatory_tech_cles_for_lawyers)). "Workflows designed to Opinion 24-1" + "training that satisfies hours partners already owe" are claims a national generalist can't make.
- **The retainer's economics demand it.** One on-site day per month per retainer client "anywhere in the country" is a brutal promise for a solo. Florida-first makes the on-site day a drivable I-4/I-95 corridor trip (Jacksonville–Orlando–Tampa–South Florida) instead of an airfare-and-hotel margin leak.

**Recommended posture: Florida-first, not Florida-only.** Lead with Florida in the hero eyebrow/subhead, add a "Built for Florida practice" section (copy in Part 3), set title tags and schema to Florida, change the footer line to "Daytona Beach Shores, FL · Working with small law firms across Florida" — and keep the FAQ answer that welcomes remote out-of-state work.

### 1.3 The buyer is never named

Add the two personas explicitly — managing partner and CAO/firm administrator. The administrator is usually the person who evaluates you first, clicks every link, and forwards the site to the partner; the practice-area playbooks and FAQ are largely for them. One sentence in the Home "Who I work with" section plus a Role field on the contact form covers it.

### 1.4 Beehiiv → Kit (this one can be silently losing signups)

The copy and build guide wire the newsletter to **Beehiiv embeds** (Blog page, footer, post-footer). Your actual stack is **Kit**: publication "Actionable AI for Law," verified domains `actionable-ai-for-law.kit.com` and **`newsletter.actionableai.net`**, a General Sign Up form, and two published issues of *The Small Firm Brief* (June 3 and June 9). If the live site still carries Beehiiv embeds, every signup is going to a dead or wrong list — check this first, before anything else in this document. Replacement embeds are in Part 5.

Also standardize the newsletter's public name — the published issues say "The Small Firm Brief"; other materials say "The Small Law Firm AI Workflow Brief." Pick one (recommended: **The Small Firm Brief** — shorter, already in print) and use it on the site, the Kit forms, and the masthead.

### 1.5 The April plan deferred lead magnets — but you built them anyway

The build guide's post-launch advice was "lead magnets… come after you have 12 weeks of content." Reasonable in April. It's now July and you have **14 finished magnets with live Kit forms**: nine practice-area playbooks (PI, real estate, T&E, family, business/corporate, commercial litigation, employment, criminal, bankruptcy) plus the Small Firm AI Workflow Playbook, Intake Workflow Playbook, AI Ethics Quick Reference, Vendor Evaluation Worksheet, and AI Readiness Self-Assessment. Goal 3 is unachievable while none of them appear on the site. Part 4 specs the Playbooks page; it's the single highest-leverage addition available to you this month.

---

## Part 2 — Conversion-path defects (goal 2)

1. **"20-minute call" doesn't exist.** Every CTA promises 20 minutes; all 13 Calendly events are 30. When the booking page shows 30, the promise reads as bait-and-switch — precisely the vendor behavior the site rails against. Either change site copy to "a 30-minute call" (recommended; the calls are 30) or create a real 20-minute event.
2. **"Paid in advance via Stripe at booking" isn't wired.** The Pricing page says Assessment ($995) and One Workflow ($1,995) are paid at booking; the build guide says to attach Stripe to those Calendly events and require payment to confirm. **None of your 13 Calendly events currently has payment attached** (`is_paid: false` on all). Either attach Stripe to "AI Readiness Assessment" and "AI Implementation Discussion" in Calendly, or change the Pricing copy to "invoiced at kickoff." A prospect who books expecting to pay and isn't charged is confused; one who reads "pay at booking" and can't is worse.
3. **Use the event you built for this.** You created a "Website Intro Call" event (`calendly.com/gyates-actionableai/website-intro-call`) — presumably for source attribution, which is smart. Every general "Book a Call" CTA on the site should use it (one URL, everywhere, exactly as the April build notes said). Pricing-tier CTAs map to their specific events: `/ai-assessment`, `/ai-implementation-discussion`, `/monthly-retainer-discussion`.
4. **Name collision in the funnel.** "Assessment" currently means: the $995 paid tier, the free "AI Readiness Assessment" Calendly event, *and* the "AI Readiness Assessment" Kit lead magnet. A prospect who downloaded the free PDF will not pay $995 for what sounds identical. Recommended: paid tier stays **Assessment** (it's established on the site); rename the Calendly event to "Assessment — working session" (it's the paid engagement's session) and the Kit magnet to "AI Readiness **Self-Assessment**."
5. **Calendly event hygiene.** 13 active events with overlapping names ("Intro Call," "Website Intro Call," "Playbook Intro Call," "LinkedIn," "LinkedIn Scheduling," "Email Outreach"…) is fine as private source-tracking, but make sure only the intended ones are linked publicly, and note "AI Readiness Assessment " has a trailing space in its name.

---

## Part 3 — Copy revisions (targeted; the April voice and structure should stay)

Unlike v1, this is not a teardown — the April copy is good. These are surgical replacements. Bracketed `[CONFIRM]` items are collected in Part 6.

### 3.1 Home

**Hero (replace):**

> **H1:** AI for small law firms. Without the noise.
>
> **Subhead:** I'm Greg Yates — a former Big Law partner based in Daytona Beach Shores. I help Florida firms of 25 lawyers or fewer turn AI into time saved, fewer admin headaches, and better client experience. No new platforms. No vendor theater. Just better use of the tools you already pay for.
>
> [BUTTON (primary): Book a 30-Minute Call → calendly.com/gyates-actionableai/website-intro-call]
> [BUTTON (secondary): Get a Free Playbook → /playbooks]

*(H1 stays — it's your best line. The subhead now carries: name, credential, geography, firm size. "See Pricing" moves down-page; the secondary hero action becomes the magnet, per your goal order.)*

**Section 4 — retitle and refocus (replace):**

> **H2:** Built for Florida firms of 25 lawyers or fewer
>
> My focus is small firms — 25 lawyers or fewer, and most of my clients are under ten. Managing partners who own the problem. Firm administrators who own the tools. Solos. Boutique litigation shops. Plaintiff firms. Estate planning. Family. Real estate. Whatever the practice area, the math is the same: small headcount, big workload, no time for theater.
>
> I'm based in Daytona Beach Shores and work with firms across Florida — Jacksonville to Miami, Tampa to the Space Coast. Remote works everywhere; retainer clients get me on-site.
>
> A fit if you want practical help, not a pitch deck. A fit if you'd rather get one workflow right than buy six tools you'll never use. A fit if you're skeptical of the hype but curious about what's real.

**NEW section (insert after Section 4) — the Florida trust anchor:**

> **H2:** The Florida Bar already answered "can we use AI?" The real question is "how, safely?"
>
> Ethics Opinion 24-1 says Florida lawyers may use generative AI — with duties attached: confidentiality, competence, supervision, honest billing. Every workflow I build is designed to those duties. Client-confidential information stays out of tools that train on it. A lawyer stays in the loop on anything resembling judgment. Nothing in the setup lets you bill for time you didn't spend.
>
> And since Florida requires three hours of technology CLE every cycle — first state in the country to do it — the training that comes with an engagement isn't just adoption insurance. It's hours your lawyers already owe. [CONFIRM: if any workshop carries approved CLE credit, say so here explicitly; if not, cut this sentence at "adoption insurance."]

**Section 5 (Three ways to start):** keep, with the price for the retainer filled in [CONFIRM — build guide recommended $4,950/mo] and buttons pointed at the tier-specific Calendly events (Part 2 #3).

**Section 7 (Process), Step 1:** "A 20-minute call" → "A 30-minute call."

**NEW slim band above the final CTA — the magnet exchange (goal 3 on the homepage):**

> **H2:** Steal the playbook first. Hire me later — or never.
>
> **The Small Firm AI Workflow Playbook** — the workflows I install most often, written step-by-step for firms of 25 lawyers or fewer. Free, in exchange for your email. It comes with *The Small Firm Brief*: one email a week on what's actually working. Unsubscribe anytime.
>
> [Kit embed — form `a102d27b6a`, see Part 5]

**Final CTA:** keep; "20 minutes" → "30 minutes."

### 3.2 About

- **Subhead (replace):** "Former Big Law corporate partner. Solo consultancy based in Daytona Beach Shores. I work with small law firms across Florida — plain English, practical work, no pitch decks."
- **Fit list:** "Run under 50 people, attorneys included" → "Run 25 lawyers or fewer."
- **Section 5 (replace):**
  > **H2:** Daytona Beach Shores. Working across Florida.
  >
  > Most engagements run remote, which works anywhere. Retainer clients get one full day on-site each month — and because I keep my practice concentrated in Florida, that day is a drive, not a departure gate. Out-of-state firm? Remote advisory and assessments still work fine; ask.
- **Section 6 (testimonials):** the placeholder framing is right — but confirm real quotes are live. If none exist yet, replace the block with the "What I won't do" list from Pricing (character proof you can already back) rather than shipping an empty promise. [CONFIRM]
- **Add one stance to the point-of-view section:** *"**4. The Florida Bar got it right.** Opinion 24-1 isn't a barrier; it's a spec sheet. Confidentiality, supervision, honest billing — if a workflow can't meet those, you shouldn't run it, AI or not."*

### 3.3 Pricing

- Fill `[INSERT MONTHLY PRICE]` if still live. [CONFIRM decided number]
- Reconcile payment language with reality (Part 2 #2): either wire Stripe into the two Calendly events or change both "paid in advance via Stripe at booking" lines to "invoiced at kickoff."
- Fix the orphaned FAQ answer (it likely migrated to the live FAQ): "**H3:** Yes, after the three-month minimum. Month-to-month after that." is an answer with no question. Restore: "**Can we cancel the retainer?**"
- Retainer copy: "one full day on-site each month" → "one full day on-site each month (Florida; travel outside Florida billed at cost)" [CONFIRM policy].

### 3.4 FAQ

- Firm-size answer per 1.1.
- Add two Florida questions:
  > **How do you handle the Florida Bar's AI guidance?** Every workflow is designed to Ethics Opinion 24-1: confidential client information stays out of self-learning tools, lawyers supervise anything resembling judgment, and billing stays honest. I'll walk your team through the why, not just the how.
  >
  > **Can training count toward Florida's technology CLE requirement?** [CONFIRM — if yes: "Yes — Florida requires three hours of technology CLE each cycle, and sessions can be structured to qualify." If not yet: "Florida requires three hours of technology CLE each cycle. My workshops are built as practical tech training; ask about CLE accreditation for your firm's session."]
- The existing "more than half the states have issued guidance" answer: add "— including Florida, whose Opinion 24-1 I design to by default."

### 3.5 Blog

- **Newsletter block (replace Beehiiv):** name it — *The Small Firm Brief* — and embed the Kit General Sign Up form (`8f364d0a1a`, Part 5). Keep your two-line pitch; it's good.
- **Link the real issues now** (also candidates for republishing as native posts so the page isn't empty):
  - "$117 for a contract review. Attorney included." — actionable-ai-for-law.kit.com/posts/117-for-a-contract-review-attorney-included
  - "The AI file note is becoming the whole ballgame" — actionable-ai-for-law.kit.com/posts/the-ai-file-note-is-becoming-the-whole-ballgame
- The build guide's own rule applies: if fewer than two posts are live on the blog itself, hide Blog from nav until republished. [CONFIRM current post count]
- Nav/footer "Newsletter" links → `newsletter.actionableai.net` (verified in Kit; use it as the canonical newsletter home).

### 3.6 Contact

- Replace `[INSERT EMAIL]` / any `actionableai.casa` reference with the real mailbox — `gyates@actionableai.net` [CONFIRM whether a hello@ alias exists; the April notes still recommended a `.casa` alias, which is stale].
- Fluent Forms: add **Role** (Managing partner / Firm administrator / Lawyer / Other) and **Firm size** (Solo / 2–5 / 6–10 / 11–25 / Over 25); keep practice-area dropdown — align its options with the playbook lineup.
- "Where I am" section: swap "I cover all 50 states for retainer clients" for the Florida-first framing (3.2).
- Calendly info box: "20-minute" → "30-minute," link → `website-intro-call`.

### 3.7 Footer (all pages)

- Line: "Daytona Beach Shores, FL · Working with small law firms across Florida"
- Connect column: LinkedIn [CONFIRM URL] · Newsletter → newsletter.actionableai.net · Playbooks → /playbooks · Email → real mailbox

---

## Part 4 — NEW page: /playbooks (the lead-magnet hub)

Add "Playbooks" to the nav (between Pricing and Blog, or replacing FAQ's slot with FAQ moving under About — keep nav ≤ 6 items + button). This page is goal 3's engine and doubles as goal 1 proof: fourteen finished, practice-specific deliverables is a wall of evidence no "thought leadership" blog post matches.

> **H1:** Pick your practice area. Steal the workflows.
>
> **Subhead:** Each playbook maps AI-assisted workflows to one practice area — what to automate, what to leave alone, and how to stay inside the ethics lines — using tools your firm already pays for. Free, in exchange for your email. Each comes with *The Small Firm Brief* (weekly, unsubscribe anytime).

**Practice-area grid** (each card links to its live Kit-hosted page — zero WordPress form work):

| Playbook | Kit URL |
|---|---|
| Personal Injury | actionable-ai-for-law.kit.com/personal-injury-playbook |
| Real Estate | actionable-ai-for-law.kit.com/real-estate-playbook |
| Trusts & Estates | actionable-ai-for-law.kit.com/trusts-estates-playbook |
| Family Law | actionable-ai-for-law.kit.com/family-law-playbook |
| Business & Corporate | actionable-ai-for-law.kit.com/business-corporate-playbook |
| Commercial Litigation | actionable-ai-for-law.kit.com/commercial-litigation-playbook |
| Employment Law | actionable-ai-for-law.kit.com/employment-law-playbook |
| Criminal Law | actionable-ai-for-law.kit.com/criminal-law-playbook |
| Bankruptcy | actionable-ai-for-law.kit.com/bankruptcy-law-playbook |

**Firm-level guides row** (these are the CAO's downloads):

| Guide | Kit URL |
|---|---|
| The Small Firm AI Workflow Playbook — start here | actionable-ai-for-law.kit.com/small-firm-ai-workflows |
| Intake Workflow Playbook | actionable-ai-for-law.kit.com/intake-workflow-playbook |
| AI Ethics Quick Reference | actionable-ai-for-law.kit.com/ethics-reference |
| AI Vendor Evaluation Worksheet | actionable-ai-for-law.kit.com/ai-vendor-evaluation-worksheet |
| AI Readiness Self-Assessment | actionable-ai-for-law.kit.com/ai-readiness-assessment |

**Bottom CTA:** "Want a playbook installed instead of downloaded? → Book a 30-Minute Call."

*(Kit housekeeping while you're in there: rename the form still called "Copy of Vendor Evaluation Worksheet"; decide whether "Vendor AI & Data Governance Audit Plan" and "AI Insurance Audit Playbook" are featured or held back — a curated 10–12 reads better than an exhaustive 14.)*

---

## Part 5 — Wiring appendix

**Kit embeds** (WordPress: Custom HTML block, wrapped in a Row Layout with the alt background per your build guide):

```html
<!-- Homepage magnet band: The Small Firm AI Workflow Playbook -->
<script async data-uid="a102d27b6a" src="https://actionable-ai-for-law.kit.com/a102d27b6a/index.js"></script>

<!-- Blog + footer: General Sign Up (The Small Firm Brief) -->
<script async data-uid="8f364d0a1a" src="https://actionable-ai-for-law.kit.com/8f364d0a1a/index.js"></script>
```

**Calendly:**

```html
<!-- Inline embed where the calendar should be visible (Contact) -->
<div class="calendly-inline-widget"
     data-url="https://calendly.com/gyates-actionableai/website-intro-call?hide_gdpr_banner=1"
     style="min-width:320px;height:700px;"></div>
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>
```

Button destinations: general CTAs → `/website-intro-call`; Assessment → `/ai-assessment`; One Workflow → `/ai-implementation-discussion`; Retainer → `/monthly-retainer-discussion`. Attach Stripe to the first two in Calendly if keeping "pay at booking."

**SEO (Rank Math per-page):** add Florida to the April guide's keywords — Home: *AI for small law firms in Florida*; About: *AI consultant for Florida law firms*; Playbooks: *legal AI playbooks small firms*. Schema: Home → Local Business (Daytona Beach Shores address, `areaServed: Florida`); About → Person.

**Search visibility — two findings from checking the index:**
1. actionableai.net returns **no indexed pages** on a `site:` search. If the site has been live since spring, check: Search Console verified? Sitemap submitted? A stray "Discourage search engines" setting (Settings → Reading) left on from the build?
2. **Name collision:** "actionable ai" searches surface [actionableai.com](https://www.actionableai.com/) — Alan AI, an established AI-platform company. You can't outrank them for the bare name soon; you don't need to. Brand the site in titles as **"Actionable AI for Law"** (you already use exactly this on Kit) and win "actionable ai law / legal / small law firms" instead.

---

## Part 6 — Facts to confirm (blocking items only)

1. Retainer monthly price — decided? (Guide recommended $4,950/mo; old prototype said $2,995.)
2. Testimonials — are real quotes live on About, or is the placeholder still there?
3. Stripe on Calendly — attach to the two paid events, or change Pricing copy to "invoiced"?
4. CLE status of workshops (determines how hard the tech-CLE line can be pushed).
5. Real mailboxes on actionableai.net (gyates@ confirmed; hello@?), and the public LinkedIn URL.
6. Current live blog post count (determines whether Blog stays in nav).
7. Newsletter public name: standardize on "The Small Firm Brief"?
8. On-site day policy for out-of-state retainer clients (travel billed at cost / not offered).

## Part 7 — Spot-check list (reconcile this review against the live pages)

Because the live site couldn't be fetched from this session, verify on the live pages (5 minutes): hero subhead still says "under 50"? · newsletter embed is Beehiiv or Kit? · which Calendly URL the Book-a-Call button uses · "20-Minute" wording · Pricing "paid via Stripe at booking" lines · retainer price placeholder · FAQ orphaned answer ("Yes, after the three-month minimum…") · any `.casa` email · testimonial section state · footer geography line.

## Part 8 — Rollout order

**This week (defects + dead-simple swaps):**
1. Swap Beehiiv embeds → Kit (Part 5) — potential silent signup loss until done
2. Point all CTAs at `website-intro-call`; "20-Minute" → "30-Minute" sitewide
3. Resolve Stripe-at-booking (wire it or reword it); fill retainer price; fix orphaned FAQ answer; kill any `.casa` reference
4. Under-50 → 25-or-fewer, all five locations

**Next two weeks (positioning + goal 3):**
5. Build /playbooks (Part 4) and add the homepage magnet band
6. Florida-first edits: hero subhead, Section 4 rewrite, new Opinion 24-1 section, About/Contact/footer geography, Rank Math keywords + Local Business schema
7. Fix indexing (Search Console, sitemap, reading settings); retitle site "Actionable AI for Law"
8. Republish the two Brief issues as native blog posts; link the Kit archive

**This month (compounding trust):**
9. Cornerstone post: **"Florida Bar Opinion 24-1, translated for managing partners"** — pairs with the AI Ethics Quick Reference magnet as its CTA (write once, capture emails indefinitely)
10. Land real testimonials on About; keep the honest framing
11. Keep the April guide's best rule: one post + one Brief issue a week; every FAQ question is a post

---

*Sources for Florida claims: [Florida Bar Ethics Opinion 24-1](https://www.floridabar.org/etopinions/opinion-24-1/) · [JD Supra](https://www.jdsupra.com/legalnews/florida-bar-advisory-opinion-24-1-gives-9432036/) · [Hinshaw & Culbertson](https://www.hinshawlaw.com/en/insights/lawyers-for-the-profession-alert/florida-bar-advisory-opinion-24-1-gives-green-light-to-generative-ai-use-by-lawyers-with-four-ethical-caveats/) · [Florida Bar CLE requirements](https://www.floridabar.org/member/cle/general-cle-info-and-requirements/) · [ABA Journal](https://www.abajournal.com/news/article/florida_supreme_court_approves_mandatory_tech_cles_for_lawyers). Infrastructure facts (Calendly events, Kit forms/domains/posts) verified live against your connected accounts on July 21, 2026.*
