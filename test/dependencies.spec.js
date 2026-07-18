import pkg from '~/package.json'

// These majors are load-bearing, and Dependabot keeps proposing bumps past
// them (#7, #15, #18). A bump would not fail lint or unit tests on its own —
// the site build itself cannot run in CI — so this makes such a proposal turn
// CI red instead of silently breaking the Netlify build after merge.
describe('dependency guardrails', () => {
  it('stays on nuxt 2 (nuxt 3 is a different framework, not an upgrade)', () => {
    expect(pkg.dependencies.nuxt).toMatch(/^\^?2\./)
  })

  it('stays on jest 27 (@vue/vue2-jest and jsdom setup require it)', () => {
    expect(pkg.devDependencies.jest).toMatch(/^\^?27\./)
  })
})
