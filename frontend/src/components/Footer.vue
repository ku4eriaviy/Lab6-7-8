<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div>
          <div class="logo">Волонтёры</div>
          <p class="text-muted">Помогаем вместе</p>
        </div>
        <div class="footer-nav">
          <router-link to="/events">Мероприятия</router-link>
          <router-link to="/news">Новости</router-link>
          <router-link to="/about">О нас</router-link>
        </div>
        <div class="copyright">
          © 2025 Волонтёрская платформа. Все права защищены.
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: white;
  border-top: 1px solid var(--border);
  padding: 3rem 0 1.5rem;
  margin-top: auto;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 2rem;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary);
}

.footer-nav {
  display: flex;
  gap: 2rem;
}

.footer-nav a {
  color: var(--text-muted);
  text-decoration: none;
  font-weight: 500;
}

.footer-nav a:hover {
  color: var(--primary);
}

.copyright {
  color: var(--text-muted);
  font-size: 0.95rem;
  text-align: center;
  width: 100%;
  margin-top: 1.5rem;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
  }
}
</style>