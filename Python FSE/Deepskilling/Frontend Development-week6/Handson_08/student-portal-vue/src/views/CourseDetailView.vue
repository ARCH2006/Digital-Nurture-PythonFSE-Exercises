<script setup>
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const courseId = route.params.id;

const router = useRouter();

const courseDetails = {
  id: courseId,
  code: 'CS-' + courseId,
  name: courseId === '1' ? 'Data Structures & Algorithms' : 'Advanced Web Architecture',
  credits: 4,
  description: 'In-depth exploration of data structures, execution complexity algorithms, and performance troubleshooting frameworks.'
};

const handleEnrollmentRedirect = () => {
  console.log(`Enrolling student into course item: ${courseId}`);
  
  router.push('/profile');
};
</script>

<template>
  <div class="detail-container">
    <div class="detail-card">
      <span class="badge">{{ courseDetails.code }}</span>
      <h2>{{ courseDetails.name }}</h2>
      <p class="credits">Academic Weight: {{ courseDetails.credits }} Units</p>
      <p class="description">{{ courseDetails.description }}</p>
      
      <div class="action-row">
        <button @click="handleEnrollmentRedirect" class="confirm-btn">
          Confirm & Enroll in Course
        </button>
        <button @click="router.back()" class="back-btn">Cancel</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.detail-container {
  padding: 3rem 2rem;
  max-width: 600px;
  margin: 0 auto;
}
.detail-card {
  background: #ffffff;
  padding: 2.5rem;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}
.badge {
  background: #eff6ff;
  color: #2563eb;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-weight: 700;
  font-size: 0.85rem;
}
h2 {
  color: #0f172a;
  margin: 1rem 0 0.5rem 0;
}
.credits {
  color: #64748b;
  font-weight: 500;
  margin-bottom: 1.5rem;
}
.description {
  color: #334155;
  line-height: 1.6;
  margin-bottom: 2rem;
}
.action-row {
  display: flex;
  gap: 1rem;
}
.confirm-btn {
  background: #2563eb;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  flex: 2;
}
.back-btn {
  background: #f1f5f9;
  color: #475569;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  flex: 1;
}
</style>