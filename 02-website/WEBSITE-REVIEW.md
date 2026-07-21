# Actionable AI Website Review — July 2026

**Scope reviewed:** the five-page site in `02-website/` (the deployable source for actionableai.net): `index.html`, `about.html`, `pricing.html`, `blog.html`, `contact.html`, `post-example.html`.

**Reviewed against your three goals, in your priority order:**
1. Establish trust (in you, and thought leadership)
2. Generate bookings of introductory calls
3. Trade an email address for the newsletter, in exchange for a lead magnet

**Audience:** managing partners and chief administrative officers at Florida law firms of 25 lawyers or fewer.

**Also inspected while preparing this review:** your Calendly account (13 live event types, including one literally named "Website Intro Call") and your Kit account (17 signup forms, including nine practice-area playbooks and a general newsletter form). The single biggest finding of this review is that the website uses none of them.

---

## The verdict in five sentences

The voice and design instincts are genuinely good — plain, confident, anti-hype, and the "tools you already pay for" premise is exactly right for this audience. But the site currently fails all three of its jobs for one structural reason and three positioning reasons. **Structural:** every conversion path is a dummy — the contact form is a `mailto:` that silently fails, the newsletter form submits to nothing, and the scheduler you built your funnel around isn't linked anywhere. **Positioning:** the site never says Florida, never says you were a Big Law partner, and targets "under 50 people" when your business is firms under 25 lawyers. And several proof claims (engagement-average statistics, implied client history) outrun what you can currently back up — which, for an audience of professional skeptics, is worse than having no numbers at all.

### Scorecard

| Goal | Current grade | Why |
|---|---|---|
| 1. Trust / thought leadership | C− | Right voice, but placeholder headshot, dead links, fabricated-looking stats, wrong email domain, fake blog posts, no credentials, no Florida presence |
| 2. Book intro calls | F | "Book a call" leads to a `mailto:` form. Your Calendly is never linked. Conversion is effectively zero by design |
| 3. Newsletter via lead magnet | F | No lead magnet on the site at all (you have 14+ built in Kit). Newsletter form is unwired and credits the wrong platform (Beehiiv; you're on Kit) |

---

## Part 1 — Fix-now trust breakers

These are the things a skeptical managing partner (or their CAO, who *will* click every link before recommending you) notices in the first two minutes. Each one independently kills credibility; together they read as "this consultant's own operations don't work."

1. **Wrong domain on every email link.** All five pages use `hello@actionableai.casa` (footer + contact page + form action). Your site is actionableai.net and your real address (per Calendly) is `gyates@actionableai.net`. An "AI operations consultant" whose email bounces is disqualifying. *(all pages, footer; `contact.html:44,92`)*
2. **The contact form is a `mailto:` form.** `action="mailto:..." method="POST" enctype="text/plain"` opens the visitor's desktop mail client — and on machines without one configured (most corporate Windows setups, many mobile browsers) it does nothing at all, discarding everything they typed. This is your #2 goal failing at the final step. *(`contact.html:44`)*
3. **Visible placeholder headshot.** The About page renders the literal text "[ Replace with headshot.jpg / 4:5 portrait crop / ≥ 1200px wide ]". *(`about.html:35-38`)*
4. **Dead links everywhere.** LinkedIn, X, and Newsletter footer links are `href="#"` on every page. Seven of eight blog posts link to `#`. "Older posts →" links to `#`. "Follow on X" links to twitter.com's homepage. The LinkedIn card on the contact page (`/in/gregyates`) is also `href="#"`.
5. **Unverifiable statistics presented as engagement averages.** "8.5 hrs average time returned…", "3 days → 4 hrs typical…", "Averages from small-firm engagements." *(`index.html:86-100`)* If these come from real engagements you can name (even anonymized: "across six 2025–26 engagements"), keep them and add that attribution. If they are projections or aspirations, they are a liability: the first prospect who asks "which engagements?" ends the relationship. Lawyers are professionally trained to attack unsupported precision. Part 2.4 gives the replacement proof strategy.
6. **A Manhattan phone number on a Florida practice.** (212) 765-0685 reads as New York. If you're positioning as Florida-focused, use a Florida number, a toll-free number, or drop the phone entirely (Calendly makes it unnecessary). *(`contact.html:93`)*
7. **"Hosted on Beehiiv" — you're on Kit.** Stated on the blog page newsletter form and in the About bio. Nothing says "I don't actually run this stack" like crediting the wrong vendor for your own newsletter. *(`blog.html:144`, `about.html:50`)*
8. **20-minute call promised, 30-minute call delivered.** Site copy repeatedly says "20 minutes"; every Calendly event you have is 30. When the booking page shows 30, the promise reads as bait. Standardize on 30 (recommended — the calls *are* 30) or create a real 20-minute event.
9. **Favicon never loads.** `favicon.svg` exists in the folder but no page includes `<link rel="icon" href="favicon.svg" type="image/svg+xml">`, so browsers show a blank tab icon.
10. **Firm-size options contradict your positioning.** The contact form offers "16–30", "31–50", and "Over 50" — and the hero says "Under 50 people." Your business is under 25 lawyers. *(`contact.html:59-66`, `index.html:32`)*
11. **Implied-history claims to soften.** "That's typically eight to twelve active engagements at a time" (`about.html:57`), "a four-lawyer shop in Tulsa… a forty-lawyer regional firm" (`about.html:48`), "Firms I've run this workflow with typically see…" (`post-example.html:67`), and the "Austin firm" case-study teaser (`blog.html:79`). Keep whatever is true; reframe the rest as capacity ("I cap active engagements at eight") and illustration ("Run well, this workflow takes intake-to-engagement from days to hours") rather than history.

---

## Part 2 — Strategic repositioning

### 2.1 Claim Florida. Loudly.

The word "Florida" does not appear once on the site. For your stated audience this is the single largest missed opportunity, because Florida is not just your territory — it's a *content angle* nobody generic can match:

- **The Florida Bar has already blessed AI use — with conditions.** [Ethics Opinion 24-1](https://www.floridabar.org/etopinions/opinion-24-1/) (Jan. 19, 2024) says lawyers may use generative AI but must protect confidentiality (informed consent recommended before putting confidential information into third-party tools), maintain competence and oversight, keep billing honest (no billing clients for time AI saved), and follow advertising rules; AI intake tools must not give legal advice (Rule 1.18 duties). ([JD Supra summary](https://www.jdsupra.com/legalnews/florida-bar-advisory-opinion-24-1-gives-9432036/), [Hinshaw analysis](https://www.hinshawlaw.com/en/insights/lawyers-for-the-profession-alert/florida-bar-advisory-opinion-24-1-gives-green-light-to-generative-ai-use-by-lawyers-with-four-ethical-caveats/)) Every workflow you install "designed to Opinion 24-1" is a claim no out-of-state generalist is making.
- **Florida was the first state to mandate technology CLE** — [3 hours per 3-year cycle](https://www.floridabar.org/member/cle/general-cle-info-and-requirements/), effective 2017 ([ABA Journal](https://www.abajournal.com/news/article/florida_supreme_court_approves_mandatory_tech_cles_for_lawyers)). Your workshops can be pitched as satisfying an obligation partners already have. That converts "nice to have" into "we needed these hours anyway."
- **Practical positioning effects:** "AI consultant for small law firms" is a commodity search; "AI consulting for small law firms in Florida" is winnable. And managing partners refer within state bar circles — a Florida identity compounds.

**How to apply it (without excluding non-Florida business):** Florida-first, not Florida-only. Hero eyebrow, title tags, one dedicated homepage section, About location line, footer line ("Serving law firms across Florida — remote-friendly everywhere"). The pricing FAQ already handles out-of-state gracefully.

### 2.2 Lead with the ex-Big Law credential

Your Kit bio says it plainly: *"Ex-Big Law partner turned peer-credible translator."* The website never mentions it. For managing partners, this is the difference between "a tech consultant who found a niche" and "one of us who went deep on this." It answers the unasked first question — *why should a lawyer listen to you about legal work?* — in four words. It belongs in the homepage lead paragraph, the About H1/opening, and the booking page. (Part 5 lists the specifics to confirm before publishing: firm/years/practice area, and how you want it phrased.)

### 2.3 Name the buyer

The copy speaks to a generic "you." Your buyers are two specific people: the **managing partner** (owns the P&L, fears falling behind, fears embarrassment more) and the **CAO / firm administrator** (owns the tools, evaluates you first, forwards the link). Add one "who this is for" moment on the homepage and a role field on the intake form. The CAO is also your lead-magnet reader — the playbooks page (Part 3.6) is largely for them.

### 2.4 Proof strategy for a young practice

You can't cite a body of engagements yet. That's fine — but then the site must generate trust from things that are *verifiably true today*:

1. **Workflow math, labeled as illustration.** "An intake summary is ~45 minutes of cleanup per new matter. With a saved prompt in the AI tool you already pay for, it's about five. Multiply by your new matters this month." Concrete, checkable, honest.
2. **Process promises you control.** Flat pricing, month-to-month, no vendor kickbacks, "if it's not working, we stop." (You already have these — the "Three promises" card is the best trust asset on the site. Keep it.)
3. **Demonstrated expertise: the playbooks.** Fourteen finished, practice-area-specific deliverables *are* your track record right now. Showing them beats claiming averages.
4. **The audit-first structure.** "Every roadmap shows the before/after math for your matters before you commit to anything" turns absent proof into a selling point: you don't ask to be believed, you offer to demonstrate.
5. **Later:** the moment you have one nameable client outcome or quotable testimonial, add a testimonial section and reinstate real numbers with attribution. The README's instinct ("no testimonial carousel until you have real ones") is correct.

### 2.5 Conversion architecture — one primary action, one secondary, every page

Right now the site's CTAs point at a form that doesn't work, and pricing tiers link at themselves (`index.html` tier buttons → `pricing.html`, where buttons → the broken contact form). Restructure so every page ends in exactly two possible actions:

- **Primary (goal 2): Book the intro call** → `https://calendly.com/gyates-actionableai/website-intro-call` — embedded inline on the booking page, linked everywhere else. You built this event for exactly this; it's currently orphaned.
- **Secondary (goal 3): Get a playbook** → Kit form (which enrolls them in the newsletter — your stated exchange).

Page-level map:

| Page | Primary CTA | Secondary CTA |
|---|---|---|
| Home | Book intro call | Small Firm AI Workflow Playbook |
| About | Book intro call | Newsletter |
| Playbooks (new) | The 14 magnets | Book intro call |
| Pricing | Tier-specific Calendly events (see 3.3) | Book intro call |
| Blog | Newsletter signup | Book intro call |
| Book a call (was Contact) | Calendly inline embed | Real email form fallback |

### 2.6 Fix the "assessment" name collision

Three different things are currently named "assessment": the paid $995 tier, a free Calendly event ("AI Readiness Assessment"), and a Kit lead magnet ("AI Readiness Assessment"). A prospect who saw the free PDF will not pay $995 for what sounds like the same thing. Recommended renames:

- Paid tier → **The AI Workflow Audit** ($995) — "audit" signals rigor and deliverable
- Free 30-min call → **Intro call** (the `website-intro-call` event)
- Kit magnet → **AI Readiness Self-Assessment** (a checklist you score yourself)

Rename the Calendly event types to match ("AI Readiness Assessment " → "Workflow Audit — working session"), and update the contact-form dropdown and all tier CTAs accordingly.

---

## Part 3 — Page-by-page, with rewrites

Copy below is written in your existing voice and ready to paste. Bracketed `[CONFIRM: …]` items are facts only you can supply — they're all collected in Part 5.

### 3.1 Home — complete rewrite

**`<title>`:** `AI Consulting for Small Law Firms in Florida | Actionable AI`
**Meta description:** `Former Big Law partner helping Florida firms of 25 lawyers or fewer get real results from the AI in tools they already pay for. Flat pricing. No vendor kickbacks.`

> **Eyebrow:** For Florida law firms · 25 lawyers or fewer
>
> **H1:** Practical AI for Florida's small law firms. No new software. No hype. Just the playbook.
>
> **Lead:** I'm Greg Yates — a former Big Law partner [CONFIRM phrasing] who now helps managing partners and firm administrators get measurable results from AI: hours back every week, faster intake, better client communication. Built almost entirely on the tools your firm already pays for.
>
> **Buttons:** [Book a 30-minute intro call] → calendly.com/gyates-actionableai/website-intro-call  ·  [Get the free playbook] → playbooks.html

**Section — The problem** (tightened, keeps your best lines):

> **Eyebrow:** The problem
>
> **H2:** Most AI sold to law firms is an overpriced chatbot with a legal skin.
>
> You already pay for Microsoft 365. You probably pay for Clio. A $20-a-month AI subscription covers most of the rest. That stack already handles the majority of what "legal AI" vendors will sell you for $400 a seat — *if* someone sets it up around how your firm actually works.
>
> The question isn't which tool to buy next. It's which tool you already own that isn't earning its keep.

**Section — What I do:** keep your three cards (Productivity / Revenue / Client delight) essentially as-is; they're good. One edit: in card 01, "work that shouldn't be billable" → "work you can't bill for anyway" (as written it can be misread as advocating billing judgment calls).

**Section — replace the stats block** (`index.html:82-102`) with illustration math:

> **Eyebrow:** Where the hours hide
>
> **H2:** The math is boring. That's the point.
>
> - **Intake summary** — ~45 minutes of note cleanup per new matter → about 5, with one saved prompt in the AI tool you already have.
> - **Engagement letter first draft** — starts from the intake form instead of a blank page. Partner review drops from forty-five minutes to ten.
> - **Client status updates** — meeting notes become a client-ready update in minutes, not a Friday-afternoon chore that slips to Tuesday.
>
> Illustrations, not promises — every firm's numbers differ. That's why engagements start with an audit: you see the before-and-after math for *your* matters, in writing, before you commit to anything.

**Section — NEW, Built for Florida practice** (this is the thought-leadership anchor):

> **Eyebrow:** Built for Florida practice
>
> **H2:** The Florida Bar has already answered "can we use AI?" The real question is "how, safely?"
>
> - **Ethics Opinion 24-1.** Florida lawyers may use generative AI — with duties: confidentiality, competence and oversight, honest billing. Every workflow I install is designed to those duties, including keeping client-confidential information out of tools that train on it.
> - **Technology CLE.** Florida was the first state to require tech CLE — three hours every cycle. Training your team on workflows you'll actually use is a better way to spend them than another webinar. [CONFIRM: whether your workshops carry CLE accreditation — if yes, say so explicitly; it's a differentiator]
> - **Florida matters.** Playbooks tuned to the work Florida small firms actually do: personal injury, real estate, trusts & estates, family, business.

**Section — Why me:** keep the "Three promises" card verbatim (it's the best thing on the page). Rewrite the left column to carry the credential:

> **H2:** I'm not a vendor. I don't resell software. I don't take referral fees.
>
> I spent [CONFIRM: N years] in practice, including [CONFIRM: partner at an AmLaw/large firm — how you want it phrased]. I know what a matter looks like from inside, what privilege actually requires, and how little patience a busy partner has for tools that don't work on the first try.
>
> Most people pitching AI to law firms have something to sell you — a platform, a subscription, a prompt pack. I don't. My job is to tell you what's worth doing and what isn't, using the stack you already have. I work with a small number of firms at a time. I answer my own email. And I'll tell you plainly if AI isn't the answer to the problem you're describing.

**Section — pricing teaser:** replace the full three-tier grid (`index.html:106-161`) with one line + link — the homepage's job is trust and the call, not the menu:

> Engagements are flat-priced and start at $995, with no lock-ins and no "contact sales" tiers. **See pricing →**

**Section — NEW, lead-magnet band** (above the final CTA):

> **H2:** Steal the playbook first. Hire me later — or never.
>
> **The Small Firm AI Workflow Playbook** — the workflows I install most often, written out step-by-step for firms of 25 lawyers or fewer. Free, in exchange for your email. You'll also get *The Small Law Firm AI Workflow Brief* — one workflow, one honest take, weekly. Unsubscribe anytime.
>
> [Kit embed: form `a102d27b6a` — "The Small Firm AI Workflow Playbook"]

**Final CTA (ink band):** keep, with two edits — "20-minute" → "30-minute", and link straight to Calendly instead of the contact page.

### 3.2 About — complete rewrite

**`<title>`:** `About Greg Yates — Actionable AI | Former Big Law Partner, AI Consultant for Florida Law Firms`

> **H1:** A guide, not a vendor. A practitioner, not a futurist.
>
> **Lead:** I'm Greg Yates. I spent [CONFIRM: N years] as a lawyer, including [CONFIRM: partner at (firm/type)]. Now I help Florida firms of 25 lawyers or fewer use AI for the things that actually matter to a practice: reclaiming time, growing revenue, and making clients glad they hired you.
>
> *(Keep your existing second and third paragraphs — "breathless or paranoid… what should I do on Monday morning?" is the best writing on the site. Change nothing.)*
>
> **What I bring**
> [CONFIRM: rewrite around the real résumé. Suggested shape:] Years inside a large firm taught me how legal work actually flows — and how partners actually decide. Since then I've built and shipped AI workflows for the tools small firms already run on: Microsoft 365, Clio, and the major AI assistants. I publish the specifics — fourteen practice-area playbooks and a weekly brief — so you can judge the thinking before you ever pay me.
>
> I write *The Small Law Firm AI Workflow Brief*, a weekly newsletter on what's actually working in small-firm AI. I speak at bar associations, law-firm management conferences, and CLEs. I answer my own email.
>
> **What I don't do** — keep your list, two edits:
> - "Work with more firms than I can serve well. **I cap active engagements at [CONFIRM: number].**" (a cap is honest whether or not you're full; "that's typically eight to twelve active engagements" implies current volume)
> - Add: "**Put client-confidential information into tools that train on it.** Yours or anyone's."
>
> **Where I stand on a few things** — keep all three (they're strong), and add a fourth for Florida:
>
> **On the Florida Bar and AI.** Opinion 24-1 got it right: the question isn't whether lawyers may use AI — they may — it's whether you can show your use protects confidentiality, stays supervised, and bills honestly. Every workflow I build is designed so a managing partner could explain it to the Bar without flinching.
>
> **Outside the work** — keep, but replace "Based in the United States" with "Based in [CONFIRM: city], Florida." Keep the closing "boring thing, carefully, for a long time" line — it's excellent.
>
> **CTA:** Book a 30-minute intro call → Calendly `website-intro-call`

**Also:** replace the placeholder headshot block with a real `<img>` (`headshot.jpg` per the README instructions — you have a usable portrait on your Calendly profile if nothing newer exists).

### 3.3 Pricing — targeted revisions (page is fundamentally sound)

1. **Rename tier 1** "The Assessment" → **"The AI Workflow Audit"** (see 2.6). Kicker stays "Diagnosis before prescription."
2. **Point tier CTAs at the Calendly events you already built**, instead of the broken contact form:
   - Workflow Audit → `calendly.com/gyates-actionableai/ai-assessment` (button: "Book the audit working session")
   - Implementation Sprint → `calendly.com/gyates-actionableai/ai-implementation-discussion`
   - Retainer → `calendly.com/gyates-actionableai/monthly-retainer-discussion`
   - Undecided (bottom CTA) → `website-intro-call`
3. **Add one Florida line** under the tier grid: "Workshops and CLE bookings priced separately" → "Workshops, firm retreats, and Florida tech-CLE sessions priced separately [CONFIRM CLE status] — get in touch."
4. **FAQ:** keep all eight (they're good — the last one is your whole pitch in two lines). Add two:
   - *"How do you handle the Florida Bar's AI guidance?"* → "Every workflow is designed to Ethics Opinion 24-1: confidential information stays out of self-learning tools, lawyers stay in the loop on anything resembling judgment, and nothing in the setup lets you bill for time you didn't spend. I'll walk your team through the why, not just the how."
   - *"Are you a lawyer?"* → [CONFIRM: your preferred one-line answer re: bar status — this question comes on every first call anyway; answering it on the site builds trust]
5. **Final CTA band:** "20 minutes" → "30 minutes," link → Calendly.

### 3.4 Contact → rename "Book a call" — complete rewrite

Rename nav label and page purpose around the call (the form becomes the fallback, not the star).

> **H1:** Book an intro call.
>
> **Lead:** Thirty minutes, free, no pitch. Bring one workflow that's slower or more annoying than it should be — intake, client updates, drafting, follow-ups. I'll tell you honestly whether an engagement makes sense. If it doesn't, you'll leave with the first thing to try on your own either way.
>
> **[Calendly inline embed — `website-intro-call`]**
> ```html
> <div class="calendly-inline-widget"
>      data-url="https://calendly.com/gyates-actionableai/website-intro-call?hide_gdpr_banner=1"
>      style="min-width:320px;height:700px;"></div>
> <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
> ```
>
> **Sidebar — "Rather not book yet?"**
> Email: gyates@actionableai.net *(or hello@actionableai.net — [CONFIRM which mailboxes exist]; kill every `.casa` reference)*
> LinkedIn: [CONFIRM real URL]
> *(Phone: drop it, or use a Florida/toll-free number — see Part 1 #6)*
>
> **Keep the "What happens next" card** — it's excellent and directly serves goal 2. One edit: step 2 becomes "We talk for 30 minutes" since booking now *is* the first step.
>
> **Keep the press/podcast card** as-is (with fixed email domain).

**Fallback form** (for the "I don't book calls with strangers" persona — real, at these firms): wire to a real backend (Formspree, Basin, or Netlify Forms — the README already suggests these; any of them is fine). Field changes:
- Add **Role**: Managing partner / Firm administrator (CAO, COO, office manager) / Lawyer / Other
- **Firm size**: Solo / 2–5 / 6–10 / 11–25 / Over 25 ("I mostly work with smaller firms")
- **Interest** options renamed to match 2.6: Intro call / AI Workflow Audit ($995) / Implementation Sprint ($1,995) / Retainer ($2,995/mo) / Speaking, workshop, or CLE / Not sure yet

### 3.5 Blog — honest restructure

The page currently lists eight posts; seven link to `#`. Two options, in order of preference:

- **A (recommended): trim to what exists.** Keep only posts with a live destination — `post-example.html` today, plus your Kit-published pieces as they go up (link out to `actionable-ai-for-law.kit.com` posts; the README already anticipates this pattern). Delete "Older posts →" until it's true. A blog with two real posts reads as *young*; a blog with seven dead links reads as *fake*. Young is fine. Fake is fatal.
- **B: publish the drafts.** The eight titles are genuinely good (the ABA-guidance one should become a Florida Opinion 24-1 piece — see Part 6). If you'd rather backfill than trim, prioritize: the intake workflow (exists), the Opinion 24-1 explainer, and the "five prompts" playbook.

**Newsletter band rewrite** (bottom of blog page — this is goal 3's page-level home):

> **Eyebrow:** The newsletter
>
> **H2:** The Small Law Firm AI Workflow Brief
>
> One email a week: one workflow, one honest take, zero vendor hype. Written for managing partners and administrators at firms of 25 lawyers or fewer. Unsubscribe in two clicks.
>
> [Kit embed: General Sign Up Form — `8f364d0a1a`]
> ```html
> <script async data-uid="8f364d0a1a" src="https://actionable-ai-for-law.kit.com/8f364d0a1a/index.js"></script>
> ```

Also: "Follow on X" → "Connect on LinkedIn" (your channel is LinkedIn; the X link currently points at twitter.com's homepage). Delete the "Currently hosted on Beehiiv" line.

### 3.6 NEW page — `playbooks.html` (the lead-magnet hub)

This is the missing limb of the site. You have **fourteen finished lead magnets with live Kit forms**, and they do double duty: goal 3 (email exchange) *and* goal 1 (a wall of finished, specific work is thought-leadership proof no blog post matches). Add "Playbooks" to the nav.

> **Eyebrow:** Free playbooks
>
> **H1:** Pick your practice area. Steal the workflows.
>
> **Lead:** Each playbook maps AI-assisted workflows to one practice area — what to automate, what to leave alone, and how to stay inside the ethics lines — using tools your firm already pays for. Free, in exchange for your email. Each comes with a subscription to *The Small Law Firm AI Workflow Brief* (weekly, unsubscribe anytime).

**Practice-area grid** (link each card to its Kit-hosted landing page — zero backend work, forms already live):

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

**Second row — firm-level guides** (these speak straight to the CAO):

| Guide | Kit URL |
|---|---|
| The Small Firm AI Workflow Playbook (start here) | actionable-ai-for-law.kit.com/small-firm-ai-workflows |
| Intake Workflow Playbook | actionable-ai-for-law.kit.com/intake-workflow-playbook |
| AI Ethics Quick Reference | actionable-ai-for-law.kit.com/ethics-reference |
| AI Vendor Evaluation Worksheet | actionable-ai-for-law.kit.com/ai-vendor-evaluation-worksheet |
| AI Readiness Self-Assessment | actionable-ai-for-law.kit.com/ai-readiness-assessment |

*(Housekeeping while you're in Kit: the form named "Copy of Vendor Evaluation Worksheet" should be renamed, and "Vendor AI & Data Governance Audit Plan" vs "AI Insurance Audit Playbook" overlap with the worksheet — pick the strongest one to feature; a 14-item wall can also be curated down to ~10 with the rest linked from a "more" row.)*

**Bottom CTA:** "Want the playbook installed instead of just downloaded? → Book a 30-minute intro call."

### 3.7 Sitewide — nav and footer

**Nav:** Home · About · Playbooks · Pricing · Blog · **[Book a call]** (button, unchanged style)

**Footer, all pages:**
- Tagline: "Practical AI for Florida's small law firms. No hype. Just the playbook."
- Connect column: real LinkedIn URL · Newsletter → `actionable-ai-for-law.kit.com/general-subscription` · Playbooks → playbooks.html
- Contact column: `gyates@actionableai.net` (or hello@ — whichever is real)
- Bottom row: "© 2026 Actionable AI · Greg Yates" + "Serving law firms across Florida" (replaces "Built in the USA")

---

## Part 4 — Technical checklist

1. **Calendly:** inline embed on Book-a-call (snippet in 3.4); plain links everywhere else. Keep using distinct event types per source (website-intro-call vs newsletter-scheduling etc.) — your existing setup already gives you channel attribution for free. Consider renaming the stray "AI Readiness Assessment " event (note the trailing space in its name) per 2.6.
2. **Kit embeds:** each form has a script embed (`https://actionable-ai-for-law.kit.com/<uid>/index.js`). Homepage band → `a102d27b6a`; blog/newsletter → `8f364d0a1a`; playbook cards → Kit-hosted landing pages (no embed needed).
3. **Form backend:** Formspree/Basin/Netlify Forms for the fallback form. Never `mailto:`.
4. **Favicon:** add `<link rel="icon" href="favicon.svg" type="image/svg+xml">` to all pages.
5. **SEO baseline:** per-page titles/descriptions with "small law firm(s) + Florida + AI" phrasing (drafts in Part 3); canonical tags; Open Graph + Twitter card tags (og:title, og:description, og:image — a simple branded card image); `sitemap.xml` + `robots.txt`.
6. **Structured data:** JSON-LD `ProfessionalService` (name, founder Person "Greg Yates", `areaServed: Florida`, url, email) on the homepage; `FAQPage` schema on pricing (eight ready-made Q&As — free rich-result real estate).
7. **Analytics:** Cloudflare Web Analytics or Plausible (README's instinct is right — no cookie banner needed). Without it you'll never know which of the three goals the site is actually serving. Track: Calendly link clicks, Kit form conversions, playbook page visits.
8. **Accessibility quick wins:** the form labels are already proper; add `alt` text when the headshot lands; ensure the ink-section link colors pass contrast.

---

## Part 5 — Facts to confirm before publishing (the [CONFIRM] list)

1. Big Law history: firm (or "an AmLaw 100 firm"), role, years, practice area — and exactly how you want it phrased publicly.
2. Bar status today (active/retired/which state) — for the "Are you a lawyer?" FAQ and general accuracy.
3. Your Florida city (About + local SEO). Also whether the (212) number should be replaced, kept, or dropped.
4. Which mailboxes actually exist on actionableai.net (gyates@ confirmed via Calendly; hello@?). All `.casa` references get replaced regardless.
5. Real LinkedIn URL.
6. CLE status of your workshops (accredited in Florida? planned?) — determines how hard the tech-CLE angle can be pushed.
7. The origin of the current stats (8.5 hrs / 3 days→4 hrs). Real and attributable → keep with attribution. Otherwise → replace per 3.1.
8. Which blog titles have finished drafts (determines Blog option A vs B).
9. Headshot file.
10. Engagement cap number for the About page.

---

## Part 6 — Prioritized rollout

**Day 1 (an hour of find-and-replace — stops active harm):**
- Replace every `actionableai.casa` email with the real .net address
- Point every "Book a call" CTA at `calendly.com/gyates-actionableai/website-intro-call`; change "20-minute" → "30-minute"
- Fix or remove all `#` links (LinkedIn, X, Newsletter, dead blog posts, "Older posts")
- Remove the stats block (or attribute it); soften the implied-history lines (Part 1 #11)
- Fix "Beehiiv" → Kit; add the favicon link tag; fix the contact form size options

**Week 1 (the conversion build):**
- Rewrite Home and About per 3.1/3.2 (needs Part 5 answers)
- Rebuild Contact as Book-a-call with the Calendly embed; wire the fallback form to a real backend
- Build `playbooks.html` from the table in 3.6; add to nav
- Swap newsletter forms for Kit embeds; drop the real headshot in
- Add analytics

**Month 1 (the thought-leadership flywheel):**
- Publish the cornerstone piece: **"Florida Bar Opinion 24-1, translated for managing partners"** — your single best trust + SEO asset; it pairs naturally with the AI Ethics Quick Reference magnet (write once, capture emails forever). Source it from the [opinion itself](https://www.floridabar.org/etopinions/opinion-24-1/).
- Publish two more from the existing title list (intake workflow is nearly done; "five prompts" is high-search)
- Add JSON-LD, sitemap, OG images
- Start collecting the first quotable testimonial; the moment one exists, add a testimonial section to Home and real numbers to the proof section

---

*Review conducted against the site source in this repo. If the deployed site at actionableai.net has drifted from `02-website/`, reconcile before applying — but every finding above was verified in the files, and the Calendly/Kit findings were verified against the live accounts.*
