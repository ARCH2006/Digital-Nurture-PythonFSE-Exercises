<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  isEnrolled: Boolean
});

defineEmits(['enroll-click', 'unenroll-click']);
</script>

<template>
  <div class="course-card">
    <div class="card-header">
      <span class="course-id">{{ code }}</span>
      <h3>{{ name }}</h3>
    </div>
    <p class="credits">Credits: {{ credits }} Units</p>
    
    <button 
      v-if="isEnrolled" 
      @click="$emit('unenroll-click')" 
      class="unenroll-btn"
    >
      Drop Course
    </button>
    <button 
      v-else 
      @click="$emit('enroll-click')" 
      class="enroll-btn"
    >
      Enroll in Course
    </button>
  </div>
</template>

<style scoped>
.course-card {
  background: #ffffff;
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.course-id { font-size: 0.85rem; color: #2563eb; font-weight: bold; }
h3 { margin: 0.5rem 0; color: #0f172a; }
.credits { color: #64748b; font-size: 0.9rem; margin-bottom: 1rem; }
.enroll-btn {
  width: 100%; padding: 0.6rem; background: #2563eb; color: white;
  border: none; border-radius: 4px; font-weight: 600; cursor: pointer;
}
.unenroll-btn {
  width: 100%; padding: 0.6rem; background: #ef4444; color: white;
  border: none; border-radius: 4px; font-weight: 600; cursor: pointer;
}
</style>