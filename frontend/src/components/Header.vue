<template>
  <header class="header">
    <div class="container">
      <div class="header-inner">
        <router-link to="/" class="logo">
          Волонтёры
        </router-link>

        <nav class="nav">
          <router-link to="/events">Мероприятия</router-link>
          <router-link to="/news">Новости</router-link>
          <router-link to="/about">О нас</router-link>

          <div class="auth-buttons">
            <template v-if="auth.isAuthenticated()">
              <router-link to="/profile" class="profile-link">
                {{ auth.user?.username }}
              </router-link>
              <button @click="logout" class="btn btn-secondary">Выйти</button>
            </template>
            <template v-else>
              <router-link to="/login" class="btn btn-secondary">Войти</router-link>
              <router-link to="/register" class="btn btn-primary">Регистрация</router-link>
            </template>
          </div>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
import { auth } from '../stores/auth'
import { useRouter } from 'vue-router'

const router = useRouter()

const logout = () => {
  auth.logout()
  router.push('/login')
}
</script>

<style scoped>
.header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: white;
  border-bottom: 1px solid var(--border);
}

.header-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem 0;
}

.logo {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--primary);
  text-decoration: none;
}

.nav {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.nav a {
  color: var(--text-muted);
  font-weight: 500;
  text-decoration: none;
  transition: var(--transition);
}

.nav a:hover,
.nav a.router-link-active {
  color: var(--primary);
}

.auth-buttons {
  display: flex;
  gap: 1rem;
}

.profile-link {
  color: var(--primary);
  font-weight: 600;
  text-decoration: none;
}

@media (max-width: 768px) {
  .nav {
    gap: 1.5rem;
  }
  .auth-buttons {
    gap: 0.75rem;
  }
  .btn {
    padding: 10px 16px;
    font-size: 0.95rem;
  }
}
</style>