<template>
  <div class="news-page">
    <!-- Hero -->
    <section class="hero">
      <div class="container">
        <h1>Новости</h1>
        <p class="lead">Последние события и достижения нашего сообщества</p>
      </div>
    </section>

    <!-- News List -->
    <section class="section">
      <div class="container">
        <div class="news-grid">
          <div class="news-card card" v-for="item in news" :key="item.id">
            <div class="news-date">{{ item.date }}</div>
            <h3>{{ item.title }}</h3>
            <p class="excerpt">{{ item.excerpt }}</p>
            <div class="read-more">Читать далее →</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const news = [
  {
    id: 1,
    title: 'Успешно завершена акция помощи приютам',
    date: '18 декабря 2025',
    excerpt: 'Благодаря вашим заявкам мы собрали и передали более 2 тонн корма и наполнителя для животных в приютах Москвы и области.'
  },
  {
    id: 2,
    title: 'Новый рекорд: 300 участников на эко-субботнике',
    date: '30 ноября 2025',
    excerpt: 'В Москве и Санкт-Петербурге одновременно прошло 12 уборок парков. Мы убрали более 3 тонн мусора.'
  },
  {
    id: 3,
    title: 'Запущена программа поддержки пожилых людей',
    date: '15 ноября 2025',
    excerpt: 'Теперь вы можете помогать одиноким пенсионерам с покупками, прогулками и общением.'
  },
  {
    id: 4,
    title: 'Новогодняя акция «Подарок от сердца»',
    date: '10 декабря 2025',
    excerpt: 'Собираем подарки для детей из малообеспеченных семей. Присоединяйтесь!'
  }
]
</script>

<style scoped>
.news-page .hero {
  background: white;
  padding: 140px 0 100px;
  text-align: center;
  border-bottom: 1px solid var(--border);
}

.hero h1 {
  font-size: 3.5rem;
  margin-bottom: 1rem;
}

.lead {
  font-size: 1.4rem;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto;
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 2.5rem;
  margin-top: 2rem;
}

.news-card {
  padding: 2rem;
  display: flex;
  flex-direction: column;
}

.news-date {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 0.75rem;
}

.news-card h3 {
  margin-bottom: 1rem;
  font-size: 1.4rem;
}

.excerpt {
  color: var(--text-muted);
  margin-bottom: 1.5rem;
  flex: 1;
}

.read-more {
  color: var(--primary);
  font-weight: 600;
  text-decoration: none;
  align-self: flex-start;
}

.read-more:hover {
  text-decoration: underline;
}
</style>