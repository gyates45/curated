# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository layout: two independent projects

This repo contains two unrelated websites that share nothing but the git history:

1. **Repo root** — the CuratedStack Nocode Template: a Nuxt 2 statically-generated directory of curated links, editable through Netlify CMS. Everything outside `02-website/` belongs to it.
2. **`02-website/`** — "Actionable AI": a standalone 5-page plain HTML/CSS site (no framework, no build step) for actionableai.casa. It is deployed separately (drag-drop to Cloudflare Pages or similar) and is NOT part of the Nuxt build or the Netlify deploy.

Keep changes to the two projects in separate commits. Note that `npm run lint:style` globs `**/*.{vue,css}`, so it will also lint (and auto-fix) `02-website/styles.css`.

## CuratedStack site (repo root)

### Commands

```sh
npm install          # legacy toolchain: node-sass 4.x only compiles on old Node (≤14)
npm run dev          # dev server with hot reload
npm run generate     # static build to dist/ (this is what Netlify deploys; see netlify.toml)
npm run lint         # lint:js (ESLint, --fix) + lint:style (Stylelint, --fix)
npm run lint:js      # ESLint only, .js/.vue
npm run lint:style   # Stylelint only, .vue/.css
npm run analyze      # report link count per category + detect duplicate URLs in links.json
npm run get-logos    # download missing logos for links into static/images/logos
```

There is no test suite. `analyze` and `get-logos` run via babel-node against the content JSON.

### Architecture

This is a full-static Nuxt 2 site (`target: 'static'`). All content is data, not markup:

- **`content/config.json`** — site config (title, hostname, analytics ID, icon, floating prompt widget).
- **`content/categories.json`** — categories: `{ slug, name, description, icon (emoji) }`.
- **`content/links.json`** — the directory entries: `{ name, description, url, icon (path under /images/logos), categories_slugs[] }`. Links reference categories many-to-many via `categories_slugs`.
- **`locales/en.json`** — all UI strings (nuxt-i18n, English only).

The **`services/`** layer (`getConfig`, `getCategories`, `getLinks`, `getLocale`) imports these JSON files directly at build time. Pages consume services in `asyncData`; there is no store, API, or runtime data fetching.

Routes: `pages/index.vue` renders the category grid + search bar; `pages/_slug/index.vue` renders one category page at `/<category-slug>`, listing all links whose `categories_slugs` include that slug.

**Search** (`@nuxtjs/lunr-module`): the index is built at build time in the `hooks.ready` section of `nuxt.config.js`, which feeds every link as a lunr document (indexed fields: name, description, tags = category slugs; `meta` carries name/url/icon for rendering). `components/TheSearch.vue` renders results and navigates straight to the external URL.

**Netlify CMS**: the admin panel lives at `static/admin/` (`/admin` on the deployed site) and edits the four content files above via git-gateway against branch `main` (squash merges). The field schema in `static/admin/config.yml` duplicates the JSON shape — **if you change the structure of any content file, update `static/admin/config.yml` to match** (and the lunr document mapping in `nuxt.config.js` if links are affected).

**Dark mode** is `nuxtjs-darkmode-js-module`; its styling is done with `mix-blend-mode` overrides under `.darkmode--activated` in `assets/style/main.scss`. Global SCSS variables/mixins live in `assets/style/_variables.scss` and `_mixins.scss` and are `@import`ed per component.

### Adding a link (core content workflow)

1. Add an entry to `content/links.json` with `categories_slugs` matching slugs in `categories.json` and an `icon` path under `/images/logos/`.
2. Run `npm run analyze` to check category distribution and duplicates.
3. Run `npm run get-logos` to fetch the logo into `static/images/logos/` (it skips files that already exist; scrapes the site's favicon metadata).

### Conventions

- Prettier: no semicolons, single quotes, no trailing commas. ESLint extends `@nuxtjs` + prettier; Stylelint extends `stylelint-config-standard`.
- Conventional commits enforced by commitlint; husky pre-commit runs lint-staged (ESLint + Stylelint on staged files).
- Path aliases `~/` and `@/` resolve to the repo root (see `jsconfig.json`).
- Components are auto-imported (`components: true` in nuxt.config), though existing pages import them explicitly.

## 02-website (Actionable AI static site)

Five HTML pages (`index`, `about`, `pricing`, `blog`, `contact`, plus `post-example.html` as the blog-post template) sharing one `styles.css`. Deliberately zero JavaScript, no framework, no build step — preview by opening the files in a browser.

- Brand color is the `--blue-600` CSS variable in the `:root` block of `styles.css`; all blues derive from it.
- Header/footer markup (logo text, nav, social links) is duplicated in every page — copy changes must be applied to all files (use find-and-replace across the folder).
- New blog posts: duplicate `post-example.html`, edit title/meta/body, and add a `.post-item` entry to `blog.html`.
- `README.md` and `HOW-TO-EDIT.md` inside the folder document deployment (Cloudflare Pages) and which placeholder links/forms (booking buttons, contact form, newsletter signup, footer socials) still need to be wired to real services.
