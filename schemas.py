from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Students(BaseModel):
    name: Optional[str]=None
    contact_details: Optional[str]=None


class ReadStudents(BaseModel):
    name: Optional[str]=None
    contact_details: Optional[str]=None
    class Config:
        from_attributes = True


class Courses(BaseModel):
    name: Optional[str]=None
    credits: Optional[int]=None
    instructor_id: Optional[int]=None


class ReadCourses(BaseModel):
    name: Optional[str]=None
    credits: Optional[int]=None
    instructor_id: Optional[int]=None
    class Config:
        from_attributes = True


class Instructors(BaseModel):
    name: Optional[str]=None


class ReadInstructors(BaseModel):
    name: Optional[str]=None
    class Config:
        from_attributes = True


class Enrollments(BaseModel):
    student_id: Optional[int]=None
    course_id: Optional[int]=None
    enrollment_date: Optional[datetime.date]=None
    grade: Optional[str]=None


class ReadEnrollments(BaseModel):
    student_id: Optional[int]=None
    course_id: Optional[int]=None
    enrollment_date: Optional[datetime.date]=None
    grade: Optional[str]=None
    class Config:
        from_attributes = True




class PostStudents(BaseModel):
    name: Optional[str]=None
    contact_details: Optional[str]=None

    class Config:
        from_attributes = True



class PutStudentsStudentId(BaseModel):
    student_id: Optional[int]=None
    name: Optional[str]=None
    contact_details: Optional[str]=None

    class Config:
        from_attributes = True



class PostCourses(BaseModel):
    name: Optional[str]=None
    credits: Optional[int]=None
    instructor_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutCoursesCourseId(BaseModel):
    course_id: Optional[int]=None
    name: Optional[str]=None
    credits: Optional[int]=None
    instructor_id: Optional[int]=None

    class Config:
        from_attributes = True



class PostInstructors(BaseModel):
    name: Optional[str]=None

    class Config:
        from_attributes = True



class PutInstructorsInstructorId(BaseModel):
    instructor_id: Optional[int]=None
    name: Optional[str]=None

    class Config:
        from_attributes = True



class PostEnrollments(BaseModel):
    student_id: Optional[int]=None
    course_id: Optional[int]=None
    enrollment_date: Optional[Any]=None
    grade: Optional[str]=None

    class Config:
        from_attributes = True



class PutEnrollmentsEnrollmentId(BaseModel):
    enrollment_id: Optional[int]=None
    student_id: Optional[int]=None
    course_id: Optional[int]=None
    enrollment_date: Optional[Any]=None
    grade: Optional[str]=None

    class Config:
        from_attributes = True

