import { resolveLogoUrl } from '~/scripts/lib/resolveLogoUrl'

describe('resolveLogoUrl', () => {
  it('keeps absolute http(s) urls as they are', () => {
    expect(
      resolveLogoUrl(
        'https://cdn.example.com/logo.png',
        'https://site.example.com'
      )
    ).toBe('https://cdn.example.com/logo.png')
  })

  it('resolves root-relative urls against the site origin', () => {
    expect(
      resolveLogoUrl('/favicon.ico', 'https://site.example.com/some/page')
    ).toBe('https://site.example.com/favicon.ico')
  })

  it('resolves relative urls against the page url', () => {
    expect(
      resolveLogoUrl('favicon.ico', 'https://site.example.com/docs/')
    ).toBe('https://site.example.com/docs/favicon.ico')
  })

  it('resolves protocol-relative urls with the site protocol', () => {
    expect(
      resolveLogoUrl('//cdn.example.com/logo.png', 'https://site.example.com')
    ).toBe('https://cdn.example.com/logo.png')
  })
})
