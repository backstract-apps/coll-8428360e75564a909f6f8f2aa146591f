from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def post_students(db: Session, raw_data: schemas.PostStudents):
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"name": name, "contact_details": contact_details}
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    res = {
        "students_inserted_record": students_inserted_record,
    }
    return res


async def put_students_student_id(db: Session, raw_data: schemas.PutStudentsStudentId):
    student_id: int = raw_data.student_id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {
            "name": name,
            "student_id": student_id,
            "contact_details": contact_details,
        }.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def get_courses(db: Session):

    query = db.query(models.Courses)

    courses_all = query.all()
    courses_all = (
        [new_data.to_dict() for new_data in courses_all] if courses_all else courses_all
    )
    res = {
        "courses_all": courses_all,
    }
    return res


async def get_courses_course_id(db: Session, course_id: int):

    query = db.query(models.Courses)
    query = query.filter(and_(models.Courses.course_id == course_id))

    courses_one = query.first()

    courses_one = (
        (
            courses_one.to_dict()
            if hasattr(courses_one, "to_dict")
            else vars(courses_one)
        )
        if courses_one
        else courses_one
    )

    res = {
        "courses_one": courses_one,
    }
    return res


async def post_courses(db: Session, raw_data: schemas.PostCourses):
    name: str = raw_data.name
    credits: int = raw_data.credits
    instructor_id: int = raw_data.instructor_id

    record_to_be_added = {
        "name": name,
        "credits": credits,
        "instructor_id": instructor_id,
    }
    new_courses = models.Courses(**record_to_be_added)
    db.add(new_courses)
    db.commit()
    db.refresh(new_courses)
    courses_inserted_record = new_courses.to_dict()

    res = {
        "courses_inserted_record": courses_inserted_record,
    }
    return res


async def put_courses_course_id(db: Session, raw_data: schemas.PutCoursesCourseId):
    course_id: int = raw_data.course_id
    name: str = raw_data.name
    credits: int = raw_data.credits
    instructor_id: int = raw_data.instructor_id

    query = db.query(models.Courses)
    query = query.filter(and_(models.Courses.course_id == course_id))
    courses_edited_record = query.first()

    if courses_edited_record:
        for key, value in {
            "name": name,
            "credits": credits,
            "course_id": course_id,
            "instructor_id": instructor_id,
        }.items():
            setattr(courses_edited_record, key, value)

        db.commit()
        db.refresh(courses_edited_record)

        courses_edited_record = (
            courses_edited_record.to_dict()
            if hasattr(courses_edited_record, "to_dict")
            else vars(courses_edited_record)
        )
    res = {
        "courses_edited_record": courses_edited_record,
    }
    return res


async def delete_courses_course_id(db: Session, course_id: int):

    query = db.query(models.Courses)
    query = query.filter(and_(models.Courses.course_id == course_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        courses_deleted = record_to_delete.to_dict()
    else:
        courses_deleted = record_to_delete
    res = {
        "courses_deleted": courses_deleted,
    }
    return res


async def get_instructors(db: Session):

    query = db.query(models.Instructors)

    instructors_all = query.all()
    instructors_all = (
        [new_data.to_dict() for new_data in instructors_all]
        if instructors_all
        else instructors_all
    )
    res = {
        "instructors_all": instructors_all,
    }
    return res


async def get_instructors_instructor_id(db: Session, instructor_id: int):

    query = db.query(models.Instructors)
    query = query.filter(and_(models.Instructors.instructor_id == instructor_id))

    instructors_one = query.first()

    instructors_one = (
        (
            instructors_one.to_dict()
            if hasattr(instructors_one, "to_dict")
            else vars(instructors_one)
        )
        if instructors_one
        else instructors_one
    )

    res = {
        "instructors_one": instructors_one,
    }
    return res


async def post_instructors(db: Session, raw_data: schemas.PostInstructors):
    name: str = raw_data.name

    record_to_be_added = {"name": name}
    new_instructors = models.Instructors(**record_to_be_added)
    db.add(new_instructors)
    db.commit()
    db.refresh(new_instructors)
    instructors_inserted_record = new_instructors.to_dict()

    res = {
        "instructors_inserted_record": instructors_inserted_record,
    }
    return res


async def put_instructors_instructor_id(
    db: Session, raw_data: schemas.PutInstructorsInstructorId
):
    instructor_id: int = raw_data.instructor_id
    name: str = raw_data.name

    query = db.query(models.Instructors)
    query = query.filter(and_(models.Instructors.instructor_id == instructor_id))
    instructors_edited_record = query.first()

    if instructors_edited_record:
        for key, value in {"name": name, "instructor_id": instructor_id}.items():
            setattr(instructors_edited_record, key, value)

        db.commit()
        db.refresh(instructors_edited_record)

        instructors_edited_record = (
            instructors_edited_record.to_dict()
            if hasattr(instructors_edited_record, "to_dict")
            else vars(instructors_edited_record)
        )
    res = {
        "instructors_edited_record": instructors_edited_record,
    }
    return res


async def delete_instructors_instructor_id(db: Session, instructor_id: int):

    query = db.query(models.Instructors)
    query = query.filter(and_(models.Instructors.instructor_id == instructor_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        instructors_deleted = record_to_delete.to_dict()
    else:
        instructors_deleted = record_to_delete
    res = {
        "instructors_deleted": instructors_deleted,
    }
    return res


async def get_enrollments(db: Session):

    query = db.query(models.Enrollments)

    enrollments_all = query.all()
    enrollments_all = (
        [new_data.to_dict() for new_data in enrollments_all]
        if enrollments_all
        else enrollments_all
    )
    res = {
        "enrollments_all": enrollments_all,
    }
    return res


async def get_enrollments_enrollment_id(db: Session, enrollment_id: int):

    query = db.query(models.Enrollments)
    query = query.filter(and_(models.Enrollments.enrollment_id == enrollment_id))

    enrollments_one = query.first()

    enrollments_one = (
        (
            enrollments_one.to_dict()
            if hasattr(enrollments_one, "to_dict")
            else vars(enrollments_one)
        )
        if enrollments_one
        else enrollments_one
    )

    res = {
        "enrollments_one": enrollments_one,
    }
    return res


async def post_enrollments(db: Session, raw_data: schemas.PostEnrollments):
    student_id: int = raw_data.student_id
    course_id: int = raw_data.course_id
    enrollment_date: datetime.date = raw_data.enrollment_date
    grade: str = raw_data.grade

    record_to_be_added = {
        "grade": grade,
        "course_id": course_id,
        "student_id": student_id,
        "enrollment_date": enrollment_date,
    }
    new_enrollments = models.Enrollments(**record_to_be_added)
    db.add(new_enrollments)
    db.commit()
    db.refresh(new_enrollments)
    enrollments_inserted_record = new_enrollments.to_dict()

    res = {
        "enrollments_inserted_record": enrollments_inserted_record,
    }
    return res


async def put_enrollments_enrollment_id(
    db: Session, raw_data: schemas.PutEnrollmentsEnrollmentId
):
    enrollment_id: int = raw_data.enrollment_id
    student_id: int = raw_data.student_id
    course_id: int = raw_data.course_id
    enrollment_date: datetime.date = raw_data.enrollment_date
    grade: str = raw_data.grade

    query = db.query(models.Enrollments)
    query = query.filter(and_(models.Enrollments.enrollment_id == enrollment_id))
    enrollments_edited_record = query.first()

    if enrollments_edited_record:
        for key, value in {
            "grade": grade,
            "course_id": course_id,
            "student_id": student_id,
            "enrollment_id": enrollment_id,
            "enrollment_date": enrollment_date,
        }.items():
            setattr(enrollments_edited_record, key, value)

        db.commit()
        db.refresh(enrollments_edited_record)

        enrollments_edited_record = (
            enrollments_edited_record.to_dict()
            if hasattr(enrollments_edited_record, "to_dict")
            else vars(enrollments_edited_record)
        )
    res = {
        "enrollments_edited_record": enrollments_edited_record,
    }
    return res


async def delete_enrollments_enrollment_id(db: Session, enrollment_id: int):

    query = db.query(models.Enrollments)
    query = query.filter(and_(models.Enrollments.enrollment_id == enrollment_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        enrollments_deleted = record_to_delete.to_dict()
    else:
        enrollments_deleted = record_to_delete
    res = {
        "enrollments_deleted": enrollments_deleted,
    }
    return res
