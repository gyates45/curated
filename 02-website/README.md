# Actionable AI — Website

A clean, coded 5-page site. No WordPress, no plugins, no database. Five HTML files, one CSS file, fonts pulled from Google Fonts. That's it.

## What's here

```
02-website/
├── index.html        Home
├── about.html        About
├── pricing.html      Pricing (three tiers)
├── blog.html         Blog index + newsletter signup
├── post-example.html Sample full-length article (for layout demo)
├── contact.html      Contact + form
└── styles.css        Shared stylesheet
```

## Why this instead of WordPress

- **Faster.** Loads in under 500ms on any decent host.
- **Cheaper.** Runs on free static hosting (Cloudflare Pages, Netlify, GitHub Pages, Vercel).
- **Safer.** No admin panel to hack, no plugins to update, no database to back up.
- **Portable.** If you ever want to switch hosts, you drag five files.
- **Editable.** You can open any file in a text editor, change the words, and republish.

## How to deploy (the fast way)

### Option A — Cloudflare Pages (free, fastest)
1. Create a Cloudflare account (free).
2. Go to Pages → Upload assets.
3. Drag the entire `02-website` folder into the browser.
4. Point `actionableai.casa` DNS to Cloudflare (instructions shown in dashboard).
5. Done. You'll have SSL automatically.

### Option B — Netlify (free, nearly as fast)
1. Create a Netlify account.
2. Drag the `02-website` folder onto app.netlify.com.
3. In domain settings, connect `actionableai.casa`.
4. Done.

### Option C — GitHub Pages
1. Create a new GitHub repo.
2. Push the folder contents to the root.
3. Settings → Pages → Deploy from branch: main.
4. Add custom domain.

You can migrate from WordPress by leaving the WP install in place, then pointing DNS to the new host. If anything breaks, repoint DNS back — takes minutes.

## Customization map

**Change the nav/footer logo text.** Search `actionable` in each file. It appears in 2 places per file: header and footer.

**Change the brand color.** Open `styles.css` and update `--blue-600` in the `:root` block. Every blue on the site pulls from that variable.

**Add a real headshot.** Drop `headshot.jpg` in the folder. Edit `about.html` and replace the `<div class="headshot">…</div>` block with `<img src="headshot.jpg" alt="Greg Yates" class="headshot">`.

**Connect the contact form to something real.** The form currently uses `mailto:`. Upgrade to [Formspree](https://formspree.io), [Basin](https://usebasin.com), or Netlify Forms by changing the `action` attribute.

**Hook up the newsletter signup.** Replace the `<form>` blocks in `blog.html` and `post-example.html` with the embed code from your Beehiiv dashboard (Publication Settings → Signup Form).

**Add Google Analytics or Plausible.** Paste the tracking snippet into the `<head>` of each page. Or, better, use Cloudflare's built-in analytics — privacy-friendly, no cookie banner needed.

## Writing blog posts

`post-example.html` shows the article layout. To add a new post:

1. Duplicate `post-example.html` → rename to a slug like `2026-05-01-prompt-library.html`.
2. Update the `<title>`, `<meta description>`, `h1`, tag, and date.
3. Write the body inside `<div class="narrow">…</div>`.
4. Add an entry to the post list in `blog.html` (copy an existing `.post-item` block).

If you'd rather keep blog on Beehiiv and just link out: delete the `post-example.html` link and replace the titles in `blog.html` with direct Beehiiv URLs.

## Things I didn't do (on purpose)

- **No JavaScript framework.** You don't need React for a 5-page site. This site loads in plain HTML because that's the correct engineering choice here.
- **No cookie banner.** Without tracking cookies, you don't need one. Keep it this way as long as you can.
- **No testimonial carousel.** The second you have named, quotable testimonials, add a simple `<section>` to `index.html` — no widget required.
- **No gated content.** Every page is fully visible. Lawyers hate gates more than most audiences.

## File sizes
- Total site: ~80KB HTML + ~12KB CSS + fonts (pulled from Google).
- Largest file is the CSS. Nothing here needs optimizing.
