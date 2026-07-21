import { Injectable } from '@angular/core'; 
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

export interface Course {
  id: number;
  name: string;
  code: string;
  credits: number;
  grade?: string;
}

interface CourseApiResponse {
  id: number;
  title: string;
}

@Injectable({
  providedIn: 'root' // This means the entire app shares this single service instance
})
export class CourseService {

  constructor(private readonly http: HttpClient) {}

  getCourses(): Observable<Course[]> {
    return this.http
      .get<CourseApiResponse[]>('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .pipe(
        map((courses) =>
          courses.map((course) => ({
            id: course.id,
            name: course.title,
            code: `COURSE-${course.id.toString().padStart(3, '0')}`,
            credits: 3,
          })),
        ),
      );
  }
}
