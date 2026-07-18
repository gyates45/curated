/* eslint-disable no-console */
import fs from 'fs'
import download from 'download'
import scrape from 'html-metadata'
import { getLinks } from '../services/getLinks.js'
import { resolveLogoUrl } from './lib/resolveLogoUrl.js'

const getLogos = async (links) => {
  console.log('[Get Logos] - Starting')
  for (const link of links) {
    const path = './static' + link.icon
    const url = link.url
    if (!isLogoAlreadyDownloaded(path)) {
      console.log('[Get Logo] - Downloading logo from ' + url)
      try {
        const urlLogo = await getLogoUrl(url)
        const data = await download(urlLogo)
        fs.writeFileSync(path, data)
        console.log('[Get Logo] - Logo saved in ' + path)
      } catch (error) {
        console.log('[Get Logo] - Failed to download the logo of ' + url)
      }
    }
  }
}

const isLogoAlreadyDownloaded = (path) => {
  return fs.existsSync(path)
}

const getLogoUrl = async (url) => {
  const metadata = await scrape(url)
  const imageUrl = metadata.general.icons[0].href
  return resolveLogoUrl(imageUrl, url)
}

const links = getLinks()
getLogos(links)
