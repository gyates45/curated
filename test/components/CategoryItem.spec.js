import { shallowMount, RouterLinkStub } from '@vue/test-utils'
import CategoryItem from '~/components/CategoryItem.vue'

const mountCategoryItem = () =>
  shallowMount(CategoryItem, {
    propsData: { name: 'Design', slug: 'design', icon: '🎨' },
    stubs: { 'nuxt-link': RouterLinkStub }
  })

describe('CategoryItem', () => {
  it('links to the category page with a trailing slash', () => {
    const wrapper = mountCategoryItem()
    expect(wrapper.findComponent(RouterLinkStub).props('to')).toBe('/design/')
  })

  it('renders the category name and icon', () => {
    const wrapper = mountCategoryItem()
    expect(wrapper.text()).toContain('Design')
    expect(wrapper.text()).toContain('🎨')
  })
})
