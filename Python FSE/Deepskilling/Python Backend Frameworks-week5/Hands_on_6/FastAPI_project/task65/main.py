from fastapi import FastAPI
from typing import Optional
from schemas import CourseCreate
from database import engine, Base
import models
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import Course
from schemas import CourseCreate

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Course Management API",
    version="1.0",
    lifespan=lifespan
)

courses = []


@app.get("/")
async def root():
    return {"message": "API running"}


@app.post("/api/courses/")
async def create_course(course: CourseCreate):
    course_data = course.model_dump()
    course_data["id"] = len(courses) + 1
    courses.append(course_data)
    return course_data


@app.get("/api/courses/")
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None
):
    filtered_courses = courses

    if department_id is not None:
        filtered_courses = [
            course
            for course in courses
            if course["department_id"] == department_id
        ]

    return filtered_courses[skip:skip + limit]


@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course

    return {"message": "Course not found"}