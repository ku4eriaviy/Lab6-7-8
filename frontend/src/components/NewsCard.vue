<template>
  <div class="news-card card">
    <div class="news-image" v-if="news.image">
      <img :src="news.image" alt="" />
    </div>
    <div class="news-content">
      <div class="news-date">{{ formatDate(news.date) }}</div>
      <h3>{{ news.title }}</h3>
      <p class="excerpt">{{ news.excerpt }}</p>
      <router-link :to="`/news/${news.id}`" class="read-more">Читать далее →</router-link>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  news: Object
})

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString('ru-RU', {
    day: '2-digit',
    month: 'long',
    year: 'numeric'
  })
}
</script>

<style scoped>
.news-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.news-image {
  height: 200px;
  overflow: hidden;
}

.news-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s;
}

.news-card:hover .news-image img {
  transform: scale(1.1);
}

.news-content {
  padding: 1.8rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.news-date {
  color: var(--gray);
  font-size: 0.95rem;
  margin-bottom: 0.8rem;
}

.excerpt {
  margin-top: 1rem;
  color: var(--text-light);
  flex: 1;
}

.read-more {
  color: var(--primary);
  font-weight: 600;
  text-decoration: none;
  margin-top: 1rem;
  display: inline-block;
}

.read-more:hover {
  text-decoration: underline;
}
</style>