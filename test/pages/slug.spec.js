import CategoryPage from '~/pages/_slug/index.vue'
import getConfig from '~/services/getConfig'
import { getCategories, getCategoriesMenu } from '~/services/getCategories'
import { getLinks } from '~/services/getLinks'

const existingSlug = () => getCategories()[0].slug

describe('category page (_slug)', () => {
  it('accepts existing category slugs', () => {
    expect(CategoryPage.validate({ params: { slug: existingSlug() } })).toBe(
      true
    )
  })

  // Regression test: unknown slugs used to crash the page with
  // "Cannot read property 'name' of undefined" instead of returning a 404.
  it('rejects unknown category slugs so nuxt renders a 404', () => {
    expect(CategoryPage.validate({ params: { slug: 'not-a-category' } })).toBe(
      false
    )
  })

  it('loads the category, its links and the rotated categories menu', () => {
    const slug = existingSlug()
    const data = CategoryPage.asyncData({ params: { slug } })
    expect(data.slug).toBe(slug)
    expect(data.category).toEqual(getCategories(slug)[0])
    expect(data.links).toEqual(getLinks(slug))
    expect(data.categories).toEqual(getCategoriesMenu(slug))
    expect(data.categories[0].slug).toBe(slug)
  })

  it('only loads links that belong to the category', () => {
    const slug = existingSlug()
    const { links } = CategoryPage.asyncData({ params: { slug } })
    expect(links.length).toBeGreaterThan(0)
    for (const link of links) {
      expect(link.categories_slugs).toContain(slug)
    }
  })

  it('builds the page title and meta description from the category', () => {
    const category = getCategories()[0]
    const links = getLinks(category.slug)
    const head = CategoryPage.head.call({ category, links })
    expect(head.title).toBe(`${getConfig().title} | ${category.name}`)
    const description = head.meta.find((tag) => tag.hid === 'description')
    expect(description.content).toBe(links.length + ' ' + category.description)
  })
})
