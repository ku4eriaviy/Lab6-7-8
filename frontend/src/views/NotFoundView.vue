<template>
  <div class="not-found">
    <h1>404</h1>
    <p>Страница не найдена</p>
    <router-link to="/" class="btn btn-primary">На главную</router-link>
  </div>
</template>

<style scoped>
.not-found {
  text-align: center;
  padding: 120px 20px;
}

.not-found h1 {
  font-size: 6rem;
  color: var(--primary);
}
</style>