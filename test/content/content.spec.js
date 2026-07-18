import fs from 'fs'
import path from 'path'
import categoriesObject from '~/content/categories.json'
import config from '~/content/config.json'
import linksObject from '~/content/links.json'
import en from '~/locales/en.json'
import {
  findDuplicateUrls,
  INTENTIONAL_DUPLICATE_URLS
} from '~/scripts/lib/analyzeLinks'

const { categories } = categoriesObject
const { links } = linksObject

const SLUG_PATTERN = /^[a-z0-9]+(-[a-z0-9]+)*$/

describe('content/categories.json', () => {
  it('contains at least one category', () => {
    expect(categories.length).toBeGreaterThan(0)
  })

  it('gives every category a name, a slug, a description and an icon', () => {
    for (const category of categories) {
      for (const field of ['name', 'slug', 'description', 'icon']) {
        if (typeof category[field] !== 'string' || category[field] === '') {
          throw new Error(
            `Category "${category.name || category.slug}" is missing "${field}"`
          )
        }
      }
    }
  })

  it('uses kebab-case slugs so they work as urls', () => {
    for (const category of categories) {
      if (!SLUG_PATTERN.test(category.slug)) {
        throw new Error(`Category slug "${category.slug}" is not kebab-case`)
      }
    }
  })

  it('has no duplicate slugs', () => {
    const slugs = categories.map((category) => category.slug)
    expect(new Set(slugs).size).toBe(slugs.length)
  })
})

describe('content/links.json', () => {
  it('contains at least one link', () => {
    expect(links.length).toBeGreaterThan(0)
  })

  it('gives every link a name and a url', () => {
    for (const link of links) {
      if (typeof link.name !== 'string' || link.name === '') {
        throw new Error(`Link "${link.url}" is missing a name`)
      }
      if (typeof link.url !== 'string' || !/^https?:\/\//.test(link.url)) {
        throw new Error(`Link "${link.name}" needs an absolute http(s) url`)
      }
      expect(() => new URL(link.url)).not.toThrow()
    }
  })

  it('tags every link with at least one existing category', () => {
    const knownSlugs = new Set(categories.map((category) => category.slug))
    for (const link of links) {
      if (
        !Array.isArray(link.categories_slugs) ||
        link.categories_slugs.length === 0
      ) {
        throw new Error(`Link "${link.name}" has no categories_slugs`)
      }
      for (const slug of link.categories_slugs) {
        if (!knownSlugs.has(slug)) {
          throw new Error(
            `Link "${link.name}" references the unknown category "${slug}"`
          )
        }
      }
    }
  })

  it('has no duplicate urls besides the intentional call-to-action', () => {
    expect(findDuplicateUrls(links, INTENTIONAL_DUPLICATE_URLS)).toEqual([])
  })

  it('points every icon at an existing file in static/', () => {
    for (const link of links) {
      if (!link.icon) {
        continue
      }
      if (!link.icon.startsWith('/')) {
        throw new Error(`Icon of "${link.name}" must start with a slash`)
      }
      const iconPath = path.join(__dirname, '../../static', link.icon)
      if (!fs.existsSync(iconPath)) {
        throw new Error(`Icon of "${link.name}" not found: static${link.icon}`)
      }
    }
  })
})

describe('content/config.json', () => {
  it('defines the fields used by nuxt.config.js and the components', () => {
    expect(config.title).toEqual(expect.any(String))
    expect(config.shortname).toEqual(expect.any(String))
    expect(config.description).toEqual(expect.any(String))
    expect(config.contact_link).toEqual(expect.any(String))
    expect(config.icon).toMatch(/^\//)
    expect(config.hostname).toMatch(/^https?:\/\//)
    expect(typeof config.floatingPrompt.disabled).toBe('boolean')
  })
})

describe('locales/en.json', () => {
  it('defines every translation key the pages and components use', () => {
    expect(en.title).toEqual(expect.any(String))
    expect(en.description).toEqual(expect.any(String))
    expect(en.tools.title).toEqual(expect.any(String))
    expect(en.tools.description).toEqual(expect.any(String))
    expect(en.footer.title).toEqual(expect.any(String))
    expect(en.footer.description).toEqual(expect.any(String))
    expect(en.footer.copyright).toEqual(expect.any(String))
    expect(en.footer.author.name).toEqual(expect.any(String))
    expect(en.footer.author.website).toEqual(expect.any(String))
    expect(en.buttons.navigation.back).toEqual(expect.any(String))
    expect(en.buttons.footer.contact).toEqual(expect.any(String))
    expect(en['lunr-module'].placeholderText).toEqual(expect.any(String))
  })
})
