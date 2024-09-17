import request from '@/utils/request'

export const getRandomTitle = () => {
  return request({
    url: 'https://api.quotable.io/random',
    method: 'get'
  })
}

export const getRandomContent = () => {
  return request({
    url: 'https://api.chucknorris.io/jokes/random',
    method: 'get'
  })
}
