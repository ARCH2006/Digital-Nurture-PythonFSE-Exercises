import apiClient from './apiClient';

export const getAllCourses = () => apiClient.get('/courses');

export const getCourseById = (id) => apiClient.get(`/courses/${id}`);

export const enrollStudent = (studentId, courseId) =>
  apiClient.post('/enrollments', {
    studentId,
    courseId,
    enrolledAt: new Date().toISOString(),
  });
