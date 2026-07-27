from pydantic import BaseModel,EmailStr
from typing import Optional
from pydantic import BaseModel, ConfigDict



class UserRegister(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = {
        "from_attributes": True
    }
    
class CourseCreate(BaseModel):
    name:str
    code:str
    credits:int
    department_id:int
    
class CourseUpdate(BaseModel):
    name:Optional[str] = None
    code:Optional[str] = None
    credits:Optional[int] = None
    department_id:Optional[int] = None
    


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    model_config = ConfigDict(from_attributes=True)
    
class DepartmentResponse(BaseModel):
    id:int
    name:str
    courses : list[CourseResponse]
    
class StudentCreate(BaseModel):
    name: str
    email: str
    
class StudentUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True
    )
    
class EnrollmentCreate(BaseModel):
    course_id: int
    student_id: int
    
class EnrollmentResponse(BaseModel):
    id: int
    course_id: int
    student_id: int

    model_config = ConfigDict(
        from_attributes=True
    )