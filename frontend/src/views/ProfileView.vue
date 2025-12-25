<template>
  <div>
    <h1>Профиль</h1>
    <div v-if="auth.user" class="profile-card">
      <p><strong>Имя:</strong> {{ auth.user.first_name }} {{ auth.user.last_name }}</p>
      <p><strong>Логин:</strong> {{ auth.user.username }}</p>
      <p><strong>Email:</strong> {{ auth.user.email || 'не указан' }}</p>
      <p><strong>Телефон:</strong> {{ auth.user.phone || 'не указан' }}</p>
      <p><strong>Город:</strong> {{ auth.user.city || 'не указан' }}</p>
      <p><strong>Волонтёр:</strong> {{ auth.user.is_volunteer ? 'Да' : 'Нет' }}</p>
    </div>
    <div v-else>Загрузка...</div>
  </div>
</template>

<script setup>
import { auth } from '../stores/auth'
</script>

<style scoped>
.profile-card {
  background: white;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  max-width: 500px;
}

.profile-card p {
  margin: 12px 0;
}
</style>