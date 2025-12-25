import { ref } from 'vue'
import axios from 'axios'

const token = ref(localStorage.getItem('token') || null)
const user = ref(null)

if (token.value) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
}

export const auth = {
  token,
  user,

  isAuthenticated: () => !!token.value,

  async login(username, password) {
    try {
      const res = await axios.post('/api/token/', { username, password })
      token.value = res.data.access
      localStorage.setItem('token', token.value)
      axios.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
      await auth.fetchUser()
      return true
    } catch (err) {
      throw err.response?.data || err
    }
  },

  async register(data) {
    try {
      await axios.post('/api/register/', data)
      return true
    } catch (err) {
      throw err.response?.data || err
    }
  },

  async fetchUser() {
    if (!token.value) return
    try {
      const res = await axios.get('/api/me/')
      user.value = res.data
    } catch {
      auth.logout()
    }
  },

  logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
    delete axios.defaults.headers.common['Authorization']
  }
}

// Инициализация при загрузке страницы
auth.fetchUser()