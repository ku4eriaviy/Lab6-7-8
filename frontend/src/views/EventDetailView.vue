<template>
  <div v-if="loading">Загрузка...</div>
  <div v-else-if="event" class="event-detail">
    <h1>{{ event.title }}</h1>
    <p class="meta">
      <strong>Организатор:</strong> {{ event.organizer_name }}<br>
      <strong>Когда:</strong> {{ formatDate(event.date_start) }} — {{ formatDate(event.date_end) }}<br>
      <strong>Где:</strong> {{ event.location }}<br>
      <strong>Мест:</strong> {{ event.participants_count }} / {{ event.max_participants }}
    </p>
    <div class="description" v-html="event.description"></div>

    <div v-if="auth.isAuthenticated()">
      <button v-if="alreadyParticipated" class="btn btn-primary" disabled>Вы уже подали заявку</button>
      <button v-else @click="showForm = true" class="btn btn-primary">Подать заявку</button>

      <ParticipationForm v-if="showForm" :event-id="event.id" @close="showForm = false" @submitted="onSubmitted" />
    </div>
    <p v-else>Чтобы подать заявку — <router-link to="/login">войдите</router-link></p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { auth } from '../stores/auth'
import ParticipationForm from '../components/ParticipationForm.vue'

const route = useRoute()
const event = ref(null)
const loading = ref(true)
const showForm = ref(false)
const alreadyParticipated = ref(false)

onMounted(async () => {
  try {
    const res = await axios.get(`/api/events/${route.params.id}/`)
    event.value = res.data

    // Проверяем, подана ли заявка
    if (auth.isAuthenticated()) {
      const parts = await axios.get('/api/participations/')
      // parts.data — это { count, next, previous, results }
      // поэтому берём results — это массив заявок
      alreadyParticipated.value = parts.data.results.some(p => p.event === event.value.id)
    }
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
})

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString('ru-RU', {
    day: '2-digit',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

function onSubmitted() {
  showForm.value = false
  alreadyParticipated.value = true
}
</script>

<style scoped>
.event-detail {
  max-width: 800px;
  margin: 0 auto;
}

.meta {
  margin: 16px 0 32px;
  line-height: 1.6;
}

.description {
  line-height: 1.7;
}
</style>