import { shallowMount } from '@vue/test-utils'
import TheFooter from '~/components/TheFooter.vue'
import getConfig from '~/services/getConfig'

const mountTheFooter = () =>
  shallowMount(TheFooter, { mocks: { $t: (key) => key } })

describe('TheFooter', () => {
  it('links the contact button to the configured contact url', () => {
    const wrapper = mountTheFooter()
    expect(wrapper.find('.button').attributes('href')).toBe(
      getConfig().contact_link
    )
  })

  it('renders the translated footer texts', () => {
    const wrapper = mountTheFooter()
    expect(wrapper.text()).toContain('footer.title')
    expect(wrapper.text()).toContain('footer.description')
    expect(wrapper.text()).toContain('buttons.footer.contact')
  })
})
