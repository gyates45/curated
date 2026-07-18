import { shallowMount, RouterLinkStub } from '@vue/test-utils'
import TheHeader from '~/components/TheHeader.vue'
import getConfig from '~/services/getConfig'

const mountTheHeader = (propsData) =>
  shallowMount(TheHeader, {
    propsData: {
      title: 'My stack',
      description: 'curated tools',
      ...propsData
    },
    stubs: { 'nuxt-link': RouterLinkStub }
  })

describe('TheHeader', () => {
  it('renders the title and the description', () => {
    const wrapper = mountTheHeader()
    expect(wrapper.find('h1').text()).toBe('My stack')
    expect(wrapper.find('.subtitle').text()).toBe('curated tools')
  })

  it('shows the site logo when no category icon is given', () => {
    const wrapper = mountTheHeader()
    expect(wrapper.find('img').attributes('src')).toBe(getConfig().icon)
  })

  it('shows the category icon instead of the logo when given', () => {
    const wrapper = mountTheHeader({ icon: '🎨' })
    expect(wrapper.find('img').exists()).toBe(false)
    expect(wrapper.find('.icon').text()).toBe('🎨')
  })

  it('prefixes the description with the number of links when given', () => {
    const wrapper = mountTheHeader({ count: 12 })
    expect(wrapper.find('.subtitle').text()).toBe('12 curated tools')
  })
})
