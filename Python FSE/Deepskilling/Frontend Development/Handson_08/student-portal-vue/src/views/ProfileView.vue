<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();
</script>

<template>
  <div class="profile-container">
    <h2>Student Profile Dashboard</h2>
    
    <div class="profile-card">
      <h3>Academic Summary</h3>
      <p class="summary-text">Total Enrolled Weight: <strong>{{ store.totalCredits }} Credits</strong></p>
    </div>

    <div class="enrolled-section">
      <h3>Your Registered Schedule</h3>
      
      <p v-if="store.enrolledCourses.length === 0" class="empty-msg">
        You haven't enrolled in any academic courses yet. Go to the Catalog tab to add items.
      </p>
      
      <div v-else class="schedule-list">
        <div v-for="course in store.enrolledCourses" :key="course.id" class="schedule-item">
          <div class="item-info">
            <span class="item-code">{{ course.code }}</span>
            <span class="item-name">{{ course.name }}</span>
          </div>
          <button @click="store.unenroll(course.id)" class="drop-btn">Drop</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-container { padding: 2rem; max-width: 800px; margin: 0 auto; }
.profile-card { background: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 2rem; }
.summary-text { font-size: 1.1rem; color: #334155; margin: 0; }
.enrolled-section { background: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e2e8f0; }
.empty-msg { color: #64748b; font-style: italic; }
.schedule-list { display: flex; flex-direction: column; gap: 1rem; }
.schedule-item { display: flex; justify-content: space-between; align-items: center; padding: 1rem; background: #f8fafc; border-radius: 6px; border: 1px solid #f1f5f9; }
.item-code { font-weight: bold; color: #2563eb; margin-right: 1rem; }
.item-name { color: #0f172a; }
.drop-btn { background: none; border: none; color: #ef4444; font-weight: 600; cursor: pointer; }
.drop-btn:hover { text-decoration: underline; }
</style>