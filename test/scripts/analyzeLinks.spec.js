import { countCategories, findDuplicateUrls } from '~/scripts/lib/analyzeLinks'

describe('countCategories', () => {
  it('counts how many links each category has', () => {
    const links = [
      { url: 'https://a.example.com', categories_slugs: ['design', 'finance'] },
      { url: 'https://b.example.com', categories_slugs: ['design'] }
    ]
    expect(countCategories(links)).toEqual({ design: 2, finance: 1 })
  })

  it('returns an empty object when there are no links', () => {
    expect(countCategories([])).toEqual({})
  })
})

describe('findDuplicateUrls', () => {
  it('returns each duplicated url once', () => {
    const links = [
      { url: 'https://a.example.com' },
      { url: 'https://b.example.com' },
      { url: 'https://a.example.com' },
      { url: 'https://a.example.com' }
    ]
    expect(findDuplicateUrls(links)).toEqual(['https://a.example.com'])
  })

  it('returns an empty array when all urls are unique', () => {
    const links = [
      { url: 'https://a.example.com' },
      { url: 'https://b.example.com' }
    ]
    expect(findDuplicateUrls(links)).toEqual([])
  })

  it('ignores urls that are allowed to appear more than once', () => {
    const links = [
      { url: 'https://cta.example.com' },
      { url: 'https://a.example.com' },
      { url: 'https://cta.example.com' },
      { url: 'https://a.example.com' }
    ]
    expect(findDuplicateUrls(links, ['https://cta.example.com'])).toEqual([
      'https://a.example.com'
    ])
  })
})
