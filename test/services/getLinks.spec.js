import { getLinks } from '~/services/getLinks'

jest.mock('~/content/links.json', () => ({
  links: [
    {
      name: 'Alpha',
      description: 'Alpha description',
      url: 'https://alpha.example.com',
      icon: '/images/logos/alpha.png',
      categories_slugs: ['design', 'productivity']
    },
    {
      name: 'Beta',
      description: 'Beta description',
      url: 'https://beta.example.com',
      icon: '/images/logos/beta.png',
      categories_slugs: ['design']
    },
    {
      name: 'Gamma',
      description: 'Gamma description',
      url: 'https://gamma.example.com',
      icon: '/images/logos/gamma.png',
      categories_slugs: ['finance']
    }
  ]
}))

describe('getLinks', () => {
  it('returns all links when called without a slug', () => {
    expect(getLinks()).toHaveLength(3)
  })

  it('returns only the links tagged with the given category slug', () => {
    const links = getLinks('design')
    expect(links.map((link) => link.name)).toEqual(['Alpha', 'Beta'])
  })

  it('returns an empty array for a slug no link is tagged with', () => {
    expect(getLinks('unknown-slug')).toEqual([])
  })
})
