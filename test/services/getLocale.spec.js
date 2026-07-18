import getLocale from '~/services/getLocale'

describe('getLocale', () => {
  it('returns the messages of an existing locale', () => {
    const locale = getLocale('en')
    expect(locale.title).toEqual(expect.any(String))
    expect(locale.tools.title).toEqual(expect.any(String))
  })

  it('throws for a language that has no locale file', () => {
    expect(() => getLocale('xx')).toThrow()
  })
})
