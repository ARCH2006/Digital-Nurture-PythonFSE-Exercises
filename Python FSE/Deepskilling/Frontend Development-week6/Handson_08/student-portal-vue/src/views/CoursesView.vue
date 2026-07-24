<script setup>
import { ref, onMounted, computed } from 'vue';
import { useEnrollmentStore } from '../stores/enrollment';
import CourseCard from '../components/CourseCard.vue';

const store = useEnrollmentStore();

const courses = ref([]);
const searchTerm = ref('');

onMounted(() => {
  courses.value = [
    { id: 1, code: 'CS-101', name: 'Data Structures & Algorithms', credits: 4 },
    { id: 2, code: 'CS-102', name: 'Web Development Basics', credits: 3 },
    { id: 3, code: 'CS-201', name: 'Database Management Systems', credits: 4 },
    { id: 4, code: 'CS-202', name: 'Operating Systems Foundations', credits: 3 },
    { id: 5, code: 'CS-301', name: 'Software Engineering Principles', credits: 4 }
  ];
});

const filteredCourses = computed(() => {
  return courses.value.filter(course => 
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
    course.code.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});

const isEnrolledInStore = (courseId) => {
  return store.enrolledCourses.some(item => item.id === courseId);
};
</script>

<template>
  <div class="catalog-container">
    <div class="catalog-header">
      <h2 class="title">Available Course Catalog</h2>
      <div class="store-badge">
        Enrolled Units: <strong>{{ store.totalCredits }}</strong>
      </div>
    </div>

    <input 
      v-model="searchTerm" 
      type="text" 
      placeholder="Search by course name or code..." 
      class="search-input"
    />
    
    <div class="courses-grid">
      <CourseCard 
        v-for="course in filteredCourses" 
        :key="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :isEnrolled="isEnrolledInStore(course.id)"
        
        @enroll-click="store.enroll(course)"
        @unenroll-click="store.unenroll(course.id)"
      />
    </div>
  </div>
</template>

<style scoped>
.catalog-container { padding: 2rem; background: #f8fafc; min-height: 100vh; }
.catalog-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.title { color: #0f172a; margin: 0; font-size: 1.75rem; }
.store-badge { background: #e0f2fe; color: #0369a1; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 500; }
.search-input { padding: 0.6rem 1rem; width: 300px; border: 1px solid #cbd5e1; border-radius: 6px; margin-bottom: 1.5rem; outline: none; }
.courses-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }
</style>