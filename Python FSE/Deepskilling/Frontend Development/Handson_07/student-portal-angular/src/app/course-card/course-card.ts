import { ChangeDetectionStrategy, Component, input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './course-card.html',
  styleUrl: './course-card.css',
})
export class CourseCardComponent {
  readonly name = input.required<string>();
  readonly code = input.required<string>();
  readonly credits = input.required<number>();
  readonly grade = input<string>();
}
