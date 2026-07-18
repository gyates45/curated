import { shallowMount } from '@vue/test-utils'
import TheSearch from '~/components/TheSearch.vue'

const mountTheSearch = () =>
  shallowMount(TheSearch, { stubs: { LunrSearch: true } })

describe('TheSearch', () => {
  it('renders the search widget container', () => {
    expect(mountTheSearch().find('.the-search').exists()).toBe(true)
  })

  it('navigates to the clicked search result', () => {
    delete window.location
    window.location = { href: '' }
    mountTheSearch().vm.openLink('https://tool.example.com')
    expect(window.location.href).toBe('https://tool.example.com')
  })
})
