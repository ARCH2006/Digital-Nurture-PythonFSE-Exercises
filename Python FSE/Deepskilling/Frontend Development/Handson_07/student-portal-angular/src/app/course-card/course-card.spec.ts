import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseCardComponent } from './course-card';

describe('CourseCardComponent', () => {
  let component: CourseCardComponent;
  let fixture: ComponentFixture<CourseCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CourseCardComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(CourseCardComponent);
    component = fixture.componentInstance;
    fixture.componentRef.setInput('name', 'Angular');
    fixture.componentRef.setInput('code', 'NG-101');
    fixture.componentRef.setInput('credits', 3);
    fixture.detectChanges();
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
