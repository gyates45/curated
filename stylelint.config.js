module.exports = {
  extends: ['stylelint-config-standard', 'stylelint-config-prettier'],
  // 02-website is a standalone static site, not part of the nuxt app
  ignoreFiles: ['02-website/**', 'coverage/**', 'node_modules/**'],
  // add your custom config here
  // https://stylelint.io/user-guide/configuration
  rules: {}
}
