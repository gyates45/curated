import { shallowMount, RouterLinkStub } from '@vue/test-utils'
import TheNavbar from '~/components/TheNavbar.vue'
import getConfig from '~/services/getConfig'

const categories = [
  { name: 'Design', slug: 'design', icon: '🎨' },
  { name: 'Finance', slug: 'finance', icon: '💰' }
]

const mountTheNavbar = (propsData) =>
  shallowMount(TheNavbar, {
    propsData: { categories, ...propsData },
    stubs: { 'nuxt-link': RouterLinkStub, TheSearch: true },
    mocks: { $t: (key) => key }
  })

describe('TheNavbar', () => {
  it('links every category to its page', () => {
    const wrapper = mountTheNavbar()
    const targets = wrapper
      .findAllComponents(RouterLinkStub)
      .wrappers.map((link) => link.props('to'))
    expect(targets).toContain('/design/')
    expect(targets).toContain('/finance/')
  })

  it('shows the site logo from the config', () => {
    const wrapper = mountTheNavbar()
    expect(wrapper.find('img').attributes('src')).toBe(getConfig().icon)
  })

  it('marks only the active category', () => {
    const wrapper = mountTheNavbar({ slug: 'design' })
    const active = wrapper.findAll('.category-button--active')
    expect(active).toHaveLength(1)
    expect(active.at(0).text()).toContain('Design')
  })

  it('marks no category as active without a slug', () => {
    const wrapper = mountTheNavbar()
    expect(wrapper.findAll('.category-button--active')).toHaveLength(0)
  })
})
