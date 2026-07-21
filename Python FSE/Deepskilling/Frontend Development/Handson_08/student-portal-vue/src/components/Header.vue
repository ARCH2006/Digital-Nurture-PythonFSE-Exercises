<script setup>
// Step 120: Import your global store hook to read state anywhere
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();

const portalTitle = "Student Portal Dashboard";
const studentName = "DeepSkill Candidate";
</script>

<template>
  <header class="main-header">
    <h1>{{ portalTitle }}</h1>
    
    <div class="user-info">
      <span class="count-badge">Courses: {{ store.enrolledCourses.length }}</span>
      <div class="user-badge">{{ studentName }}</div>
    </div>
  </header>
</template>

<style scoped>
.main-header {
  background: #0f172a;
  color: #ffffff;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.count-badge {
  background: #1e293b;
  color: #38bdf8;
  border: 1px solid #38bdf8;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
}

.user-badge {
  background: #2563eb;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
}
</style>