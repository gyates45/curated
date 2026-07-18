import { getCategories, getCategoriesMenu } from '~/services/getCategories'

jest.mock('~/content/categories.json', () => ({
  categories: [
    { name: 'Design', slug: 'design', description: 'Design tools', icon: '🎨' },
    {
      name: 'Finance',
      slug: 'finance',
      description: 'Finance tools',
      icon: '💰'
    },
    { name: 'Books', slug: 'books', description: 'Books to read', icon: '📚' }
  ]
}))

describe('getCategories', () => {
  it('returns all categories when called without a slug', () => {
    expect(getCategories().map((category) => category.slug)).toEqual([
      'design',
      'finance',
      'books'
    ])
  })

  it('returns only the category matching the given slug', () => {
    const categories = getCategories('finance')
    expect(categories).toHaveLength(1)
    expect(categories[0].name).toBe('Finance')
  })

  it('returns an empty array for an unknown slug', () => {
    expect(getCategories('unknown-slug')).toEqual([])
  })
})

describe('getCategoriesMenu', () => {
  it('rotates the menu so the active category comes first', () => {
    expect(
      getCategoriesMenu('finance').map((category) => category.slug)
    ).toEqual(['finance', 'books', 'design'])
  })

  it('keeps the default order when the first category is active', () => {
    expect(
      getCategoriesMenu('design').map((category) => category.slug)
    ).toEqual(['design', 'finance', 'books'])
  })

  it('keeps the default order when called without a slug', () => {
    expect(getCategoriesMenu().map((category) => category.slug)).toEqual([
      'design',
      'finance',
      'books'
    ])
  })

  // Regression test: an unknown slug used to rotate the last category to the
  // front because indexOf(undefined) is -1 and splice(-1) grabs the last item.
  it('keeps the default order for an unknown slug', () => {
    expect(
      getCategoriesMenu('unknown-slug').map((category) => category.slug)
    ).toEqual(['design', 'finance', 'books'])
  })

  it('does not mutate the underlying categories list', () => {
    getCategoriesMenu('books')
    expect(getCategories()).toHaveLength(3)
  })
})
