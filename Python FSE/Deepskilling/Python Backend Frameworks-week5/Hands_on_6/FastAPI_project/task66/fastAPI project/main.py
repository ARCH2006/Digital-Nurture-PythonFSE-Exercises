from fastapi import FastAPI, Depends,HTTPException,status

from contextlib import asynccontextmanager


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import engine, Base, get_db
from models import Course
import models

from schemas import CourseCreate, CourseResponse, CourseUpdate
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Course Management API",
    version="1.0",
    lifespan=lifespan
)



@app.get("/")
async def root():
    return {"message": "API running"}

@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code = status.HTTP_201_CREATED
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
@app.get(
    "/api/courses/",
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


@app.get(
    "/api/courses/{course_id}",
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

@app.put("api/courses/{course_id}",response_model = CourseResponse)
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

@app.delete(
    "/api/courses/{course_id}",
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
