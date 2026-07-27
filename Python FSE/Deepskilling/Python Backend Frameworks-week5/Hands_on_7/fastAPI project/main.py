from fastapi import (FastAPI, Depends,HTTPException,status,BackgroundTasks)

from contextlib import asynccontextmanager


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import engine, Base, get_db
from models import Course, Student, Enrollment
import models

from schemas import (CourseCreate, CourseResponse, CourseUpdate,StudentResponse,EnrollmentCreate,EnrollmentResponse)
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Course Management API",
    description="REST API for managing Courses, Students, and Enrollments using FastAPI and SQLAlchemy.",
    version="1.0",
    contact={
    "name": "Archana S",
    "email": "archana@example.com"
},
    lifespan=lifespan
)



@app.get("/",tags=["Home"])
async def root():
    return {"message": "API running"}

# create a course
@app.post(
    "/api/courses/",
    tags = ["Courses"],
    response_model=CourseResponse,
    status_code = status.HTTP_201_CREATED,
        summary="Create a new course"

)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    return new_course

# get courses 
@app.get(
    "/api/courses/",
    tags=["Courses"],
    response_model=list[CourseResponse]
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Course)

    if department_id is not None:
        stmt = stmt.where(Course.department_id == department_id)

    stmt = stmt.offset(skip).limit(limit)

    result = await db.execute(stmt)

    return result.scalars().all()


# get course by id
@app.get(
    "/api/courses/{course_id}",
      tags=["Courses"],
    response_model=CourseResponse
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Course).where(Course.id == course_id)

    result = await db.execute(stmt)

    course = result.scalar_one_or_none()

    if course is None:
        return {"message": "Course not found"}

    return course

#update course data
@app.put("api/courses/{course_id}",
         tags=["Courses"],response_model = CourseResponse)
async def update_course(course_id: int,course:CourseUpdate,db:AsyncSession = Depends(get_db)):

    stmt = select(Course).where(Course.id == course_id)
    result = await db.execute(stmt)
    existing_course = result.scalar_one_or_none()
    if existing_course is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Course not found")
    update_data = course.model_dump(exclude_unset = True)
    
    for key,value in update_data.items():
        setattr(existing_course,key,value)
        
    await db.commit()
    await db.refresh(existing_course)

    return existing_course

# delete course data
@app.delete(
    "/api/courses/{course_id}",
    tags=["Courses"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Course).where(Course.id == course_id)
    result = await db.execute(stmt)
    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    await db.delete(course)
    await db.commit()

@app.get(
    "/api/courses/{course_id}/students/",
    tags=["Students"],
    response_model=list[StudentResponse]
)
async def get_students_by_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    stmt = (
    select(Student)
    .join(
        Enrollment,
        Student.id == Enrollment.student_id
    )
    .where(
        Enrollment.course_id == course_id
    )
)
    result = await db.execute(stmt)
    students = result.scalars().all()

    return students

@app.post(
    "/api/enrollments/",
    tags=["Enrollements"],
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    new_enrollment = Enrollment(
    course_id=enrollment.course_id,
    student_id=enrollment.student_id
)

    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)
    stmt = select(Student).where(
        Student.id == enrollment.student_id
    )

    result = await db.execute(stmt)

    student = result.scalar_one_or_none()

    if student:
        background_tasks.add_task(
            send_confirmation_email,
            student.email
        )

    return new_enrollment

    
def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")