// Minimal stand-in for the `lunr-module/search` component, which only
// exists as a webpack alias created by @nuxtjs/lunr-module at build time.
export default {
  name: 'LunrSearch',
  render(createElement) {
    return createElement('div', { class: 'lunr-search' })
  }
}
