export const resolveLogoUrl = (iconUrl, siteUrl) => {
  return new URL(iconUrl, siteUrl).href
}
