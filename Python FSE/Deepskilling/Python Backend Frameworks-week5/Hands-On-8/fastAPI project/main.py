from fastapi import (FastAPI, Depends,HTTPException,status,BackgroundTasks,Response)
from fastapi.responses import JSONResponse
from fastapi import Request
from contextlib import asynccontextmanager


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,func,or_

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

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": "NOT_FOUND" if exc.status_code == 404 else "ERROR",
                "message": exc.detail,
                "field": None
            }
        }
    )

@app.get("/",tags=["Home"])
async def root():
    return {"message": "API running"}

# create a course
@app.post(
    "/api/v1/courses/",
    tags = ["Courses"],
    response_model=CourseResponse,
    status_code = status.HTTP_201_CREATED,
        summary="Create a new course"

)
async def create_course(
    course: CourseCreate,
    response: Response,
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
    response.headers["Location"] = f"/api/courses/{new_course.id}"

    return new_course

@app.get(
    "/api/v1/courses/",
    tags=["Courses"],
    response_model=None
)
async def get_courses(
    page: int = 1,
    page_size: int = 10,
    department_id: int | None = None,
    search: str | None = None,
    db: AsyncSession = Depends(get_db)
):
    # Count total courses
    count_stmt = select(func.count()).select_from(Course)

    if department_id is not None:
        count_stmt = count_stmt.where(
            Course.department_id == department_id
        )

    total = await db.scalar(count_stmt)

    # Calculate offset
    offset = (page - 1) * page_size

    stmt = select(Course)

    if department_id is not None:
        stmt = stmt.where(
            Course.department_id == department_id
        )

    if search:
        stmt = stmt.where(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%")
            )
        )

    stmt = stmt.offset(offset).limit(page_size)

    result = await db.execute(stmt)

    courses = result.scalars().all()

    # Next page URL
    if offset + page_size < total:
        next_url = (
            f"/api/v1/courses/?page={page+1}"
            f"&page_size={page_size}"
            f"&search={search or ''}"
        )
    else:
        next_url = None

    # Previous page URL
    if page > 1:
        previous_url = (
            f"/api/v1/courses/?page={page-1}"
            f"&page_size={page_size}"
            f"&search={search or ''}"
        )
    else:
        previous_url = None

    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }
# # get courses 
# @app.get(
#     "/api/v1/courses/",
#     tags=["Courses"],
#     response_model=list[CourseResponse]
# )
# async def get_courses(
#     skip: int = 0,
#     limit: int = 10,
#     department_id: int | None = None,
#     db: AsyncSession = Depends(get_db)
# ):
#     stmt = select(Course)

#     if department_id is not None:
#         stmt = stmt.where(Course.department_id == department_id)

#     stmt = stmt.offset(skip).limit(limit)

#     result = await db.execute(stmt)

#     return result.scalars().all()


# get course by id
@app.get(
    "/api/v1/courses/{course_id}",
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} does not exist"
        )

    return course

#update course data
@app.put("/api/v1/courses/{course_id}",
         tags=["Courses"],response_model = CourseResponse)
async def update_course(course_id: int,course:CourseUpdate,db:AsyncSession = Depends(get_db)):

    stmt = select(Course).where(Course.id == course_id)
    result = await db.execute(stmt)
    existing_course = result.scalar_one_or_none()
    if existing_course is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Course with id {course_id} does not exist"
    )
    update_data = course.model_dump(exclude_unset = True)
    
    for key,value in update_data.items():
        setattr(existing_course,key,value)
        
    await db.commit()
    await db.refresh(existing_course)

    return existing_course

# delete course data
@app.delete(
    "/api/v1/courses/{course_id}",
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
    "/api/v1/courses/{course_id}/students/",
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