import axios from 'axios'

axios.defaults.headers['Content-Type'] = 'application/json;charset=utf-8'
// Creating an axios instance
const service = axios.create({
  timeout: 100000
})

export default service
