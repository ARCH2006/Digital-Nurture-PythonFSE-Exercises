<script setup>
import { RouterLink, RouterView } from 'vue-router';
import Header from './components/Header.vue';
</script>

<template>
  <div class="app-wrapper">
    <Header />
    
    <nav class="navigation-bar">
      <RouterLink to="/" class="nav-item">Home</RouterLink>
      <RouterLink to="/courses" class="nav-item">Courses Catalog</RouterLink>
      <RouterLink to="/profile" class="nav-item">My Profile</RouterLink>
    </nav>
    
    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<style>
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: #f8fafc;
}

.app-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navigation-bar {
  background: #ffffff;
  border-bottom: 1px solid #e2e8f0;
  padding: 0.75rem 2rem;
  display: flex;
  gap: 1.5rem;
}

.nav-item {
  color: #64748b;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  padding: 0.25rem 0.5rem;
  transition: color 0.2s;
}

.nav-item:hover {
  color: #2563eb;
}

.router-link-active {
  color: #2563eb;
  font-weight: 600;
  border-bottom: 2px solid #2563eb;
}

.main-content {
  flex: 1;
}
</style>