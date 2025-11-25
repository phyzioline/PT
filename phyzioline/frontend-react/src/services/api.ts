import axios from 'axios'

const api = axios.create({
  baseURL: '/api/v1',
  headers: { 'Content-Type': 'application/json' }
})

// attach token if present
api.interceptors.request.use(config => {
  const token = localStorage.getItem('accessToken')
  if (token && config.headers) {
    config.headers['Authorization'] = `Bearer ${token}`
  }
  return config
})

// basic response interceptor to try refresh on 401
api.interceptors.response.use(
  res => res,
  async err => {
    const original = err.config
    if (err.response && err.response.status === 401 && !original._retry) {
      original._retry = true
      const refreshToken = localStorage.getItem('refreshToken')
      if (refreshToken) {
        try {
          const r = await axios.post('/api/token/refresh/', { refresh: refreshToken })
          localStorage.setItem('accessToken', r.data.access)
          api.defaults.headers.common['Authorization'] = `Bearer ${r.data.access}`
          original.headers['Authorization'] = `Bearer ${r.data.access}`
          return api(original)
        } catch(e) {
          // refresh failed
          localStorage.removeItem('accessToken')
          localStorage.removeItem('refreshToken')
        }
      }
    }
    return Promise.reject(err)
  }
)

export default api
