import { Routes } from '@angular/router';
import { CourseListComponent } from './course-list/course-list';
import { StudentProfile } from './student-profile/student-profile';

export const routes: Routes = [
  { path: '', component: CourseListComponent },
  { path: 'profile', component: StudentProfile },
  { path: '**', redirectTo: '' },
];
