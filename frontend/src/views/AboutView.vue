<template>
  <div class="about-page">
    <!-- Hero -->
    <section class="hero">
      <div class="container">
        <h1>О нас</h1>
        <p class="lead">Сообщество волонтёров, которое меняет мир к лучшему</p>
      </div>
    </section>

    <!-- Content -->
    <section class="section">
      <div class="container">
        <div class="story">
          <h2>Кто мы</h2>
          <p>
            Мы — открытая волонтёрская платформа, созданная для того, чтобы объединять людей, 
            готовых помогать. Наша цель — сделать участие в добрых делах максимально простым, 
            удобным и вдохновляющим.
          </p>
          <p>
            Проект начался в 2023 году как студенческая инициатива. Сегодня к нам присоединились 
            тысячи волонтёров из разных городов России. Мы организуем экологические акции, помогаем 
            приютам, поддерживаем пожилых людей, детей и семьи в трудной ситуации.
          </p>
        </div>

        <div class="stats">
          <div class="stat-item">
            <div class="stat-number">5 000+</div>
            <div class="stat-label">Волонтёров</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">450+</div>
            <div class="stat-label">Мероприятий</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">12</div>
            <div class="stat-label">Городов</div>
          </div>
        </div>

        <div class="values">
          <h2>Наши ценности</h2>
          <div class="values-grid">
            <div class="value">
              <h3>Ответственность</h3>
              <p>Все мероприятия тщательно проверяются, чтобы вы могли доверять</p>
            </div>
            <div class="value">
              <h3>Открытость</h3>
              <p>Мы рады каждому новому участнику и каждой новой идее</p>
            </div>
            <div class="value">
              <h3>Взаимопомощь</h3>
              <p>Поддерживаем друг друга в добрых делах и растём вместе</p>
            </div>
          </div>
        </div>

        <div class="team">
          <h2>Наша команда</h2>
          <p class="team-text">
            Проект развивается небольшой, но очень мотивированной командой из 8 человек. 
            Мы все сами волонтёры и делаем этот сайт для себя и для вас.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.about-page .hero {
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

.story {
  max-width: 800px;
  margin: 0 auto 5rem;
  font-size: 1.15rem;
}

.story p {
  margin-bottom: 1.5rem;
}

.stats {
  display: flex;
  justify-content: center;
  gap: 4rem;
  flex-wrap: wrap;
  margin: 5rem 0;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2.8rem;
  font-weight: 700;
  color: var(--primary);
}

.stat-label {
  color: var(--text-muted);
  margin-top: 0.5rem;
}

.values h2 {
  text-align: center;
  margin-bottom: 3rem;
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.value {
  text-align: center;
  padding: 1.5rem;
}

.value h3 {
  margin-bottom: 1rem;
  font-size: 1.35rem;
}

.team {
  text-align: center;
  margin-top: 6rem;
}

.team h2 {
  margin-bottom: 1.5rem;
}

.team-text {
  max-width: 700px;
  margin: 0 auto;
  font-size: 1.1rem;
  color: var(--text-muted);
}
</style>