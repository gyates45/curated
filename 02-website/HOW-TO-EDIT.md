# How to Edit the Site + Activate the Buttons

You have plain HTML/CSS files. Every change is one of three things: **edit text**, **swap a placeholder link**, or **connect a form to a service**. No build step, no framework, no CMS. Just files.

---

## Part 1 — The Editing Loop

Whatever tool you use, the loop is the same:

1. **Edit the HTML file** on your computer (use any editor — Notion's code blocks won't work; use VS Code, Sublime, or even TextEdit in plain-text mode).
2. **Preview locally** by double-clicking the `.html` file to open in your browser. It renders exactly how Cloudflare will render it.
3. **Push to Cloudflare.** Two options:
   - **Drag-drop:** Cloudflare Dashboard → Pages → your project → Create deployment → drop the whole `02-website` folder.
   - **GitHub hook-up (better):** push the folder to a GitHub repo, connect Cloudflare to the repo, now every `git push` auto-deploys in ~30 seconds.

If you don't want to touch Git, drag-drop is fine. Most small sites never outgrow it.

---

## Part 2 — Modifying Copy

Every page is in `02-website/`. The pages and what lives on each:

| File | Page |
|------|------|
| `index.html` | Home (hero, pillars, stats, pricing preview, why me) |
| `about.html` | About (bio, positioning, what I bring/don't) |
| `pricing.html` | Pricing (three tiers, what's included, FAQ) |
| `blog.html` | Blog index + newsletter signup |
| `contact.html` | Contact form + press card |
| `post-example.html` | Template for individual blog posts |

### How to edit text

Open the file in any text editor. Find the text you want to change. Change it. Save. Done.

Example — changing the hero headline on the home page:

Open `index.html`, search for the existing headline (something like `Practical AI for small law firms`). Replace between the `>` and the `<`:

```html
<h1>Practical AI for small law firms.</h1>
```

becomes

```html
<h1>AI that actually ships, for firms that actually bill.</h1>
```

That's it. Don't touch anything outside the `>...<` section unless you know what you're doing.

### Rules so you don't break anything

- **Never delete a `<` or `>` bracket.** That's the tag. Only edit text between tags.
- **If a word is wrapped in `<strong>`, `<em>`, or `<a>` tags**, edit the text but keep the tags.
- **Save as plain text** — never as `.docx` or `.rtf`. The file extension stays `.html`.
- **When in doubt, copy the original file first**, edit the copy, reload in your browser, confirm it looks right, then overwrite the live one.

### A quick find-and-replace for common changes

Your **email** shows up as `hello@actionableai.casa` in several places. If you want to change it to `greg@actionableai.casa`, use your editor's Find-and-Replace-in-Files (VS Code does this in 10 seconds with the magnifying-glass icon). Search: `hello@actionableai.casa` → Replace: `greg@actionableai.casa` → Replace All.

Same pattern for any repeated copy change: company tagline, price, name.

---

## Part 3 — Activating the Buttons

Here's every placeholder on the site and how to turn it on. Work top to bottom; you can do these over an afternoon.

### 3.1 "Book a call" / "Book a free assessment" buttons

**What they do now:** send people to `contact.html` (the form page). That's fine but not great — most people will abandon a form.

**Better:** send them to a calendar booking link so they pick a time right there.

**Setup (10 minutes):**

1. Sign up at **Cal.com** (free) or **Calendly** (free tier available).
2. Create an event type called "Free 30-min AI Readiness Review," 30 minutes, zero cost.
3. Copy your booking URL. It'll look like `https://cal.com/gregyates/readiness` or `https://calendly.com/gregyates/30min`.
4. In every HTML file, find every instance of `href="contact.html"` that sits on a "Book a call" button and swap it:

   ```html
   <!-- BEFORE -->
   <a href="contact.html" class="btn btn-primary btn-arrow">Book a free assessment</a>
   
   <!-- AFTER -->
   <a href="https://cal.com/gregyates/readiness" class="btn btn-primary btn-arrow">Book a free assessment</a>
   ```

   Leave nav-bar "Book a call" links pointing to `contact.html` — the nav should go to a real page, not pop open an external site.

### 3.2 The contact form (`contact.html`)

**What it does now:** the form tag reads `action="mailto:hello@actionableai.casa"`. That technically works but is ugly — it opens the user's default mail app with a badly formatted email, and iOS/web users often have no default mail app configured at all. **Treat the mailto form as broken.**

**Fix — three options, easiest first:**

**Option A: Formspree (5 minutes, free for 50 submissions/month).**

1. Sign up at **formspree.io**, create a new form, copy your endpoint. It'll look like `https://formspree.io/f/xyzabc123`.
2. Open `contact.html`, find this line:

   ```html
   <form action="mailto:hello@actionableai.casa" method="POST" enctype="text/plain">
   ```

3. Replace with:

   ```html
   <form action="https://formspree.io/f/xyzabc123" method="POST">
   ```

4. Save, deploy, submit a test. You'll get the first one as an email asking to confirm the address. Done.

**Option B: Web3Forms (free, unlimited, no signup needed).**

1. Go to **web3forms.com**, enter your email, copy the generated access key.
2. Replace the form tag the same way, plus add one hidden field:

   ```html
   <form action="https://api.web3forms.com/submit" method="POST">
     <input type="hidden" name="access_key" value="YOUR-KEY-HERE">
     <!-- rest of the form stays the same -->
   </form>
   ```

**Option C: Cloudflare Pages Functions (free, advanced).**

If you're already on Cloudflare Pages, you can write a small serverless function that forwards form submissions to your email or Slack. This takes 30 minutes to set up and costs nothing. If you want this route, the pattern is: create `/functions/submit.js` in the site folder and change the form's `action` to `/submit`. Ask when you're ready.

**Pick A or B unless you specifically want the Cloudflare-native route.**

### 3.3 Newsletter signup form (`blog.html` + anywhere else you add it)

**What it does now:** the form exists but has no `action` attribute. It submits nowhere. Treat as broken.

**Fix — use your Beehiiv embed:**

1. Log into Beehiiv → Publication → Custom forms → Create new form.
2. Beehiiv gives you either a full embed code (iframe-style) or a URL endpoint. Use the URL endpoint.
3. In `blog.html`, find the newsletter form (around line 140):

   ```html
   <form style="display:flex;gap:8px;max-width:460px;margin:0 auto;flex-wrap:wrap">
     <!-- email input -->
     <button type="submit" class="btn btn-primary btn-arrow">Subscribe</button>
   </form>
   ```

4. Change the opening `<form>` tag to:

   ```html
   <form action="https://embeds.beehiiv.com/YOUR-FORM-ID" method="POST" target="_blank" style="display:flex;gap:8px;max-width:460px;margin:0 auto;flex-wrap:wrap">
   ```

5. Make sure the email input has `name="email"`:

   ```html
   <input type="email" name="email" placeholder="your@firm.com" required>
   ```

6. Save, deploy, test. Check your Beehiiv dashboard — the new subscriber should appear.

**Alternative (zero code):** Beehiiv's default "embed form" is an iframe. You can just drop that entire iframe code block in place of the existing form. It'll look slightly different from the brand but works out of the box.

### 3.4 Blog post links

**What they do now:** every blog post headline links to `href="#"` which goes nowhere.

**Fix:**

- **If your posts live on Beehiiv:** change each `href="#"` to the full Beehiiv post URL, e.g. `href="https://actionableai.beehiiv.com/p/most-legal-ai-is-a-wrapper"`. Set `target="_blank"` so the post opens in a new tab.
- **If you want posts on your own domain:** duplicate `post-example.html` once per post, rename (e.g. `posts/legal-ai-wrappers.html`), edit the content, and link to it from `blog.html` with `href="posts/legal-ai-wrappers.html"`.

The cleanest setup for a one-person brand is: write in Beehiiv, link out from the site. You don't want to maintain post pages manually.

### 3.5 Footer social links

In **every** HTML file, the footer has three placeholder links:

```html
<li><a href="#" target="_blank" rel="noopener">LinkedIn</a></li>
<li><a href="#" target="_blank" rel="noopener">X / Twitter</a></li>
<li><a href="#" target="_blank" rel="noopener">Newsletter</a></li>
```

Replace each `#` with the real URL:

```html
<li><a href="https://linkedin.com/in/gregyates" target="_blank" rel="noopener">LinkedIn</a></li>
<li><a href="https://x.com/gregyates" target="_blank" rel="noopener">X / Twitter</a></li>
<li><a href="https://actionableai.beehiiv.com" target="_blank" rel="noopener">Newsletter</a></li>
```

Use VS Code's "Find in Files" to do all four pages at once.

### 3.6 The "mailto:" links

Every email link currently reads:

```html
<a href="mailto:hello@actionableai.casa">hello@actionableai.casa</a>
```

If your real email is `greg@actionableai.casa`, Find-and-Replace across all files: `hello@actionableai.casa` → `greg@actionableai.casa`. Do both the `mailto:` and the display text.

---

## Part 4 — Priority Order (if you do nothing else, do these)

1. **Swap the Book-a-call buttons** to a real Cal.com or Calendly link. Biggest conversion lift. (10 min)
2. **Connect the contact form** to Formspree or Web3Forms. The form is the front door. (5 min)
3. **Connect the newsletter form** to Beehiiv. Otherwise subscribers silently disappear. (15 min)
4. **Fix the footer social links.** One search-and-replace. (2 min)
5. **Fix the `hello@` email if your real one is different.** (1 min)
6. Everything else can wait.

Total: ~35 minutes to go from "looks done" to actually working.

---

## Part 5 — After You've Made Changes

Every change follows the same deploy pattern:

1. Save the edited HTML file.
2. Open it in your browser locally to confirm it looks right.
3. Deploy to Cloudflare:
   - **Drag-drop:** zip the `02-website` folder → Cloudflare Pages → your project → Create deployment → upload.
   - **GitHub:** `git add . && git commit -m "updated copy" && git push`. Done. Cloudflare picks it up in ~30 seconds.
4. Visit `actionableai.casa` in an incognito window (so you're not seeing a cached version).

If something looks wrong on live but right locally, it's almost always browser cache. Hard refresh with Cmd+Shift+R (Mac) or Ctrl+F5 (Windows).

---

## Part 6 — If You Break Something

Three safety nets:

1. **Cloudflare keeps every deployment.** Pages → your project → Deployments → find the last working one → click "Rollback." 30-second recovery.
2. **Before any significant edit**, copy the file you're editing (e.g. `contact.html` → `contact-BACKUP.html`). If you trash it, delete the broken one, rename the backup.
3. **If you use GitHub**, every push is a snapshot. `git log` shows history. `git revert` undoes.

Don't be precious. It's HTML. You cannot permanently damage it.

---

## Part 7 — When to Stop Editing and Let It Cook

The site is launched. Resist the urge to keep tweaking. Fix the five things in Part 4, then leave it alone for 30 days and focus on publishing the newsletter. You'll learn more from what people actually click than from anything you change now.
