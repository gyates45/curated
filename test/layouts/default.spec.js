import { mount } from '@vue/test-utils'
import DefaultLayout from '~/layouts/default.vue'

describe('default layout', () => {
  it('renders the page content slot and the footer', () => {
    const wrapper = mount(DefaultLayout, {
      stubs: { nuxt: true },
      mocks: { $t: (key) => key }
    })
    expect(wrapper.find('footer').exists()).toBe(true)
  })
})
