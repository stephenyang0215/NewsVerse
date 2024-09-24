export function getTime() {
  const now = new Date()

  const year = now.getFullYear()
  const month = now.getMonth() + 1
  const day = now.getDate()
  const hours = now.getHours()
  const minutes = now.getMinutes()
  const seconds = now.getSeconds()

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
}

export function removeHtmlTags(html) {
  if (html) {
    return html.replace(/<[^>]*>/g, '')
  }
}
