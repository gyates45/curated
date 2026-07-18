import { firstLetter } from '~/utils/filters'

describe('firstLetter', () => {
  it('returns the first character of a name', () => {
    expect(firstLetter('Kanbanote')).toBe('K')
  })

  it('returns an empty string for empty values', () => {
    expect(firstLetter('')).toBe('')
    expect(firstLetter(null)).toBe('')
    expect(firstLetter(undefined)).toBe('')
  })

  it('stringifies non-string values', () => {
    expect(firstLetter(42)).toBe('4')
  })
})
