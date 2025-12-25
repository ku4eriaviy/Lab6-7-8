<template>
  <div>
    <h1>Мероприятия</h1>
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else-if="events.length === 0">Мероприятий пока нет</div>
    <div v-else class="events-grid">
      <EventCard v-for="event in events" :key="event.id" :event="event" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import EventCard from '../components/EventCard.vue'

const events = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await axios.get('/api/events/')
    events.value = res.data.results || res.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.events-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}
</style>