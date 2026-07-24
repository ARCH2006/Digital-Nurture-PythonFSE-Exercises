import { ref, computed } from 'vue';
import { defineStore } from 'pinia';

export const useEnrollmentStore = defineStore('enrollment', () => {
  
  const enrolledCourses = ref([]);

  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce((total, course) => total + course.credits, 0);
  });

  const enroll = (course) => {
    const alreadyEnrolled = enrolledCourses.value.some(item => item.id === course.id);
    if (!alreadyEnrolled) {
      enrolledCourses.value.push(course);
      console.log(`Global Store: Enrolled in ${course.name}`);
    }
  };

  const unenroll = (courseId) => {
    enrolledCourses.value = enrolledCourses.value.filter(item => item.id !== courseId);
    console.log(`Global Store: Unenrolled from course ID ${courseId}`);
  };

  return {
    enrolledCourses,
    totalCredits,
    enroll,
    unenroll
  };
});