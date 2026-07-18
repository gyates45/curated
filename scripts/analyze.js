/* eslint-disable no-console */
import { getLinks } from '../services/getLinks.js'
import {
  countCategories,
  findDuplicateUrls,
  INTENTIONAL_DUPLICATE_URLS
} from './lib/analyzeLinks.js'

console.log('[analyze] - Starting')

const links = getLinks()

console.log('[analyze] - The links contains the following categories')
console.log(countCategories(links))

console.log('[analyze] - Check duplicates URL')
const duplicates = findDuplicateUrls(links, INTENTIONAL_DUPLICATE_URLS)

if (duplicates.length === 0) {
  console.log('[analyze] - No duplicates found')
} else {
  for (const url of duplicates) {
    console.log('[analyze] - Duplicate URL: ' + url)
  }
  process.exitCode = 1
}
