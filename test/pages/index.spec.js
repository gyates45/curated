import IndexPage from '~/pages/index.vue'
import { getCategories } from '~/services/getCategories'

const app = { i18n: { t: (key) => `t:${key}` } }

describe('home page', () => {
  it('loads the translated texts and all categories', () => {
    const data = IndexPage.asyncData({ app })
    expect(data.title).toBe('t:title')
    expect(data.description).toBe('t:description')
    expect(data.sectionTitle).toBe('t:tools.title')
    expect(data.sectionDescription).toBe('t:tools.description')
    expect(data.categories).toEqual(getCategories())
  })

  it('builds the page title from the site title and description', () => {
    const head = IndexPage.head.call({
      title: 'My stack',
      description: 'curated tools'
    })
    expect(head.title).toBe('My stack | curated tools')
  })
})
