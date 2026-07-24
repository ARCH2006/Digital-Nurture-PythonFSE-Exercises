import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCardComponent } from '../course-card/course-card';
import { Course, CourseService } from '../courseService';

@Component({
  selector: 'app-course-list',
  imports: [CommonModule, FormsModule, CourseCardComponent],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css',
})
export class CourseListComponent implements OnInit {
  searchTerm: string = '';
  courses: Course[] = [];
  
  loading: boolean = false; 

  constructor(
    private readonly courseService: CourseService,
    private readonly changeDetector: ChangeDetectorRef,
  ) {}

  ngOnInit(): void {
    this.loading = true;

    this.courseService.getCourses().subscribe({
      next: (data: Course[]) => {
        this.courses = data;
        this.loading = false;
        this.changeDetector.markForCheck();
      },
      error: (err: unknown) => {
        console.error('Failed to load courses', err);
        this.loading = false;
        this.changeDetector.markForCheck();
      }
    });
  }

  get filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
      course.code.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }
}
