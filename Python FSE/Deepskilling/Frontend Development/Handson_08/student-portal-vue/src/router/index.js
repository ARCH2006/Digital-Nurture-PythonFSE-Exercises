import { createRouter, createWebHistory } from 'vue-router';
// Import the view components we want to route to
import HomeView from '../views/HomeView.vue';
import CoursesView from '../views/CoursesView.vue';
import CourseDetailView from '../views/CourseDetailView.vue';
import ProfileView from '../views/ProfileView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/courses',
      name: 'courses',
      component: CoursesView
    },
    {
      path: '/courses/:id', // Dynamic parameter mapping
      name: 'course-detail',
      component: CourseDetailView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    }
  ]
});

router.beforeEach((to, from, next) => {
  // Log precisely where the application navigation engine is directing the browser context
  console.log(`Navigating to: ${to.path}`);
  
  // CRITICAL: Always invoke next() to tell the router engine to unblock and render the target page!
  next();
});


export default router;