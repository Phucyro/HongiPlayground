<template>
  <header>
    <div class="left-header">
      <RouterLink to="/">
        <img src="./assets/logo.png" alt="Logo" class="logo">
      </RouterLink>
    </div>

    <div class="right-header">
      <nav>
        <div class="routers">
          <div class="router-box">
            <RouterLink to="/">Home</RouterLink>
          </div>
          <div class="router-box">
            <RouterLink to="/todo">To Do</RouterLink>
          </div>
        </div>
      </nav>
    </div>
  </header>

  <main class="content">
    <RouterView />
  </main>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

/* Header styles */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #f0f0f0; /* Light grey background color */
  color: #333; /* Text color */
}

/* Logo styles */
.logo {
  width: 150px; /* Adjust width to make it bigger */
  height: auto;
}

/* Navigation styles */
.routers {
  display: flex;
}

.router-box {
  margin-right: 10px;
  border: 1px solid #ccc; /* Light grey border */
  padding: 10px; /* Increased padding */
  background-color: #eee; /* Light grey background color for boxes */
}

.router-box a {
  color: #333; /* Text color for links */
  text-decoration: none; /* Remove underline */
}

.router-box a:hover {
  text-decoration: underline; /* Underline on hover */
}

/* Content styles */
.content {
  padding-top: 1rem;
}

</style>
