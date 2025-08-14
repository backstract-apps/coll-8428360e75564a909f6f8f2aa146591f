from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/student_id')
async def get_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_student_id(db, student_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/student_id/')
async def put_students_student_id(raw_data: schemas.PutStudentsStudentId, db: Session = Depends(get_db)):
    try:
        return await service.put_students_student_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/student_id')
async def delete_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_student_id(db, student_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/courses/')
async def get_courses(db: Session = Depends(get_db)):
    try:
        return await service.get_courses(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/courses/course_id')
async def get_courses_course_id(course_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_courses_course_id(db, course_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/courses/')
async def post_courses(raw_data: schemas.PostCourses, db: Session = Depends(get_db)):
    try:
        return await service.post_courses(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/courses/course_id/')
async def put_courses_course_id(raw_data: schemas.PutCoursesCourseId, db: Session = Depends(get_db)):
    try:
        return await service.put_courses_course_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/courses/course_id')
async def delete_courses_course_id(course_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_courses_course_id(db, course_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/instructors/')
async def get_instructors(db: Session = Depends(get_db)):
    try:
        return await service.get_instructors(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/instructors/instructor_id')
async def get_instructors_instructor_id(instructor_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_instructors_instructor_id(db, instructor_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/instructors/')
async def post_instructors(raw_data: schemas.PostInstructors, db: Session = Depends(get_db)):
    try:
        return await service.post_instructors(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/instructors/instructor_id/')
async def put_instructors_instructor_id(raw_data: schemas.PutInstructorsInstructorId, db: Session = Depends(get_db)):
    try:
        return await service.put_instructors_instructor_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/instructors/instructor_id')
async def delete_instructors_instructor_id(instructor_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_instructors_instructor_id(db, instructor_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/enrollments/')
async def get_enrollments(db: Session = Depends(get_db)):
    try:
        return await service.get_enrollments(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/enrollments/enrollment_id')
async def get_enrollments_enrollment_id(enrollment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_enrollments_enrollment_id(db, enrollment_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/enrollments/')
async def post_enrollments(raw_data: schemas.PostEnrollments, db: Session = Depends(get_db)):
    try:
        return await service.post_enrollments(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/enrollments/enrollment_id/')
async def put_enrollments_enrollment_id(raw_data: schemas.PutEnrollmentsEnrollmentId, db: Session = Depends(get_db)):
    try:
        return await service.put_enrollments_enrollment_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/enrollments/enrollment_id')
async def delete_enrollments_enrollment_id(enrollment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_enrollments_enrollment_id(db, enrollment_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

