// The babel options are passed inline so that Jest never picks up the root
// .babelrc, which is a Babel 6 config reserved for the babel-node scripts.
const babelOptions = {
  babelrc: false,
  configFile: false,
  presets: [['@babel/preset-env', { targets: { node: 'current' } }]]
}

module.exports = {
  testEnvironment: 'jsdom',
  moduleFileExtensions: ['js', 'json', 'vue'],
  transform: {
    '^.+\\.js$': ['babel-jest', babelOptions],
    '^.+\\.vue$': ['@vue/vue2-jest', { babelConfig: babelOptions }]
  },
  moduleNameMapper: {
    '^~/(.*)$': '<rootDir>/$1',
    '^@/(.*)$': '<rootDir>/$1',
    '^lunr-module/search$': '<rootDir>/test/__mocks__/LunrSearchStub.js'
  },
  testMatch: ['<rootDir>/test/**/*.spec.js'],
  collectCoverageFrom: [
    'components/**/*.vue',
    'layouts/**/*.vue',
    'pages/**/*.vue',
    'services/**/*.js',
    'utils/**/*.js',
    'scripts/lib/**/*.js'
  ],
  coverageDirectory: 'coverage'
}
