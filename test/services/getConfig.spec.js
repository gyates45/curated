import config from '~/content/config.json'
import getConfig from '~/services/getConfig'

describe('getConfig', () => {
  it('returns the site configuration from content/config.json', () => {
    expect(getConfig()).toEqual(config)
  })
})
