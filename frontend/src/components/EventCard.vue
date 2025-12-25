<template>
  <div class="event-card card">
    <div class="event-content">
      <h3>{{ event.title }}</h3>
      <div class="meta">
        <div>{{ formatDate(event.date_start) }} — {{ formatDate(event.date_end) }}</div>
        <div>{{ event.location }}</div>
      </div>
      <div class="participants">
        Участники: {{ event.participants_count }} / {{ event.max_participants }}
      </div>
      <div class="actions">
        <router-link :to="`/events/${event.id}`" class="btn btn-primary">Подробнее</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({ event: Object })

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString('ru-RU', {
    day: '2-digit',
    month: 'long',
    year: 'numeric'
  })
}
</script>

<style scoped>
.event-card {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.event-content {
  padding: 1.75rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

h3 {
  margin-bottom: 1rem;
  font-size: 1.4rem;
}

.meta {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 1rem;
}

.meta div {
  margin-bottom: 0.5rem;
}

.participants {
  margin-top: auto;
  color: var(--primary);
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.actions {
  text-align: center;
}
</style>