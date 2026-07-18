// The template intentionally lists its call-to-action link twice (at the top
// and at the bottom of every category), so that url is a known duplicate.
export const INTENTIONAL_DUPLICATE_URLS = [
  'https://github.com/sandoche/CuratedStack-nocode-template'
]

export const countCategories = (links) => {
  const counts = {}
  for (const link of links) {
    for (const slug of link.categories_slugs) {
      counts[slug] = 1 + (counts[slug] || 0)
    }
  }
  return counts
}

export const findDuplicateUrls = (links, allowedUrls = []) => {
  const seen = new Set()
  const duplicates = new Set()
  for (const link of links) {
    if (seen.has(link.url) && !allowedUrls.includes(link.url)) {
      duplicates.add(link.url)
    }
    seen.add(link.url)
  }
  return [...duplicates]
}
