<template>
  <div class="auth-page">
    <div class="auth-container">
      <h1>Регистрация</h1>
      <p class="subtitle">Присоединяйтесь к нашему сообществу волонтёров</p>

      <form @submit.prevent="register" class="form">
        <div class="form-group">
          <label for="username">Имя пользователя</label>
          <input id="username" v-model="form.username" type="text" required />
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" v-model="form.email" type="email" />
        </div>

        <div class="form-group">
          <label for="password">Пароль</label>
          <input id="password" v-model="form.password" type="password" required />
        </div>

        <div class="form-group">
          <label for="first_name">Имя</label>
          <input id="first_name" v-model="form.first_name" type="text" />
        </div>

        <div class="form-group">
          <label for="last_name">Фамилия</label>
          <input id="last_name" v-model="form.last_name" type="text" />
        </div>

        <div class="form-group">
          <label for="phone">Телефон</label>
          <input id="phone" v-model="form.phone" type="tel" />
        </div>

        <div class="form-group">
          <label for="city">Город</label>
          <input id="city" v-model="form.city" type="text" />
        </div>

        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
        </button>

        <p v-if="error" class="error-message">{{ error }}</p>
      </form>

      <p class="footer-text">
        Уже есть аккаунт? <router-link to="/login">Войти</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { auth } from '../stores/auth'

const router = useRouter()

const form = ref({
  username: '',
  email: '',
  password: '',
  first_name: '',
  last_name: '',
  phone: '',
  city: ''
})

const loading = ref(false)
const error = ref('')

const register = async () => {
  loading.value = true
  error.value = ''

  try {
    await auth.register(form.value)
    router.push('/login')
  } catch (err) {
    error.value = err.detail || 'Произошла ошибка при регистрации'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page {
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4rem 0;
}

.auth-container {
  background: white;
  padding: 3rem 2.5rem;
  border-radius: var(--radius);
  box-shadow: var(--shadow-md);
  width: 100%;
  max-width: 480px;
  text-align: center;
}

h1 {
  font-size: 2.25rem;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: var(--text-muted);
  margin-bottom: 2.5rem;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-group {
  text-align: left;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: var(--text-muted);
}

input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 1rem;
}

input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.btn-primary {
  margin-top: 1rem;
  width: 100%;
}

.error-message {
  color: #ef4444;
  margin-top: 1rem;
  font-size: 0.95rem;
}

.footer-text {
  margin-top: 2rem;
  color: var(--text-muted);
}

.footer-text a {
  color: var(--primary);
  font-weight: 500;
  text-decoration: none;
}
</style>