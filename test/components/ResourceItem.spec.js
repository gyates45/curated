import { shallowMount } from '@vue/test-utils'
import ResourceItem from '~/components/ResourceItem.vue'

const defaultProps = {
  url: 'https://tool.example.com',
  name: 'Tool',
  description: 'A useful tool',
  icon: '/images/logos/tool.png'
}

const mountResourceItem = (propsData) =>
  shallowMount(ResourceItem, { propsData: { ...defaultProps, ...propsData } })

describe('ResourceItem', () => {
  it('links to the resource in a new tab', () => {
    const anchor = mountResourceItem().find('a')
    expect(anchor.attributes('href')).toBe(defaultProps.url)
    expect(anchor.attributes('target')).toBe('_blank')
  })

  it('renders the name and the description', () => {
    const wrapper = mountResourceItem()
    expect(wrapper.text()).toContain('Tool')
    expect(wrapper.text()).toContain('A useful tool')
  })

  it('renders the icon image when one is given', () => {
    const wrapper = mountResourceItem()
    expect(wrapper.find('img').attributes('src')).toBe(defaultProps.icon)
    expect(wrapper.find('.icon--placeholder').exists()).toBe(false)
  })

  it('falls back to the first letter of the name without an icon', () => {
    const wrapper = mountResourceItem({ icon: '' })
    expect(wrapper.find('img').exists()).toBe(false)
    expect(wrapper.find('.icon--placeholder').text()).toBe('T')
  })
})
