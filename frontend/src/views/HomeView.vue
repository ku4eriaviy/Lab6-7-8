<template>
  <div class="home">
    <!-- Hero -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <h1>Добро пожаловать в сообщество волонтёров</h1>
          <p class="lead">
            Находите мероприятия, помогайте людям и становитесь частью чего-то важного.
          </p>
          <div class="hero-actions">
            <router-link to="/events" class="btn btn-primary">Посмотреть мероприятия</router-link>
            <router-link v-if="!auth.isAuthenticated()" to="/register" class="btn btn-secondary">
              Стать волонтёром
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="section">
      <div class="container">
        <h2 class="section-title">Почему выбирают нас</h2>
        <div class="features-grid">
          <div class="feature">
            <h3>Проверенные мероприятия</h3>
            <p class="text-muted">Все события проходят модерацию, чтобы вы были уверены в их качестве</p>
          </div>
          <div class="feature">
            <h3>Простая регистрация</h3>
            <p class="text-muted">Подайте заявку за минуту и получите подтверждение</p>
          </div>
          <div class="feature">
            <h3>Сообщество единомышленников</h3>
            <p class="text-muted">Общайтесь, делитесь опытом и находите друзей</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Recent Events -->
    <section class="section" style="background: white;">
      <div class="container">
        <h2 class="section-title">Ближайшие события</h2>
        <div v-if="loading" class="loading">Загрузка...</div>
        <div v-else-if="events.length === 0" class="empty">Скоро добавим новые мероприятия</div>
        <div v-else class="events-grid">
          <EventCard v-for="event in events.slice(0, 6)" :key="event.id" :event="event" />
        </div>
        <div class="text-center" style="margin-top: 3rem;">
          <router-link to="/events" class="btn btn-primary">Все мероприятия</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { auth } from '../stores/auth'
import EventCard from '../components/EventCard.vue'

const events = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await axios.get('/api/events/?limit=6')
    events.value = res.data.results || res.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.hero {
  background: white;
  padding: 140px 0 120px;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
}

.lead {
  font-size: 1.4rem;
  color: var(--text-muted);
  margin-bottom: 2.5rem;
}

.hero-actions {
  display: flex;
  gap: 1.25rem;
  justify-content: center;
  flex-wrap: wrap;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature {
  text-align: center;
  padding: 1.5rem;
}

.feature h3 {
  margin-bottom: 1rem;
  font-size: 1.4rem;
}

.events-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 2rem;
}

.empty {
  text-align: center;
  color: var(--text-muted);
  font-size: 1.2rem;
  padding: 4rem 0;
}
</style>