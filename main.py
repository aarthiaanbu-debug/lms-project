from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from datetime import datetime

app = FastAPI(title="Learning Management System API")


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home API
@app.get("/")
def home():
    return {"message": "LMS API Running Successfully"}


# 1️⃣ Get all courses
@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()


# 2️⃣ Get lessons by course
@app.get("/courses/{course_id}/lessons")
def get_lessons_by_course(course_id: int, db: Session = Depends(get_db)):
    return db.query(models.Lesson).filter(models.Lesson.course_id == course_id).all()


# 3️⃣ Get all lessons
@app.get("/lessons")
def get_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).all()


# 4️⃣ Enroll student

@app.post("/enroll")
def enroll_student(user_id: int, course_id: int, db: Session = Depends(get_db)):

    new_enrollment = models.Enrollment(
        user_id=user_id,
        course_id=course_id,
        enrolled_on=datetime.utcnow()
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return {
        "message": "Student enrolled successfully",
        "enrollment_id": new_enrollment.id
    }


# 5️⃣ Update progress
@app.post("/progress")
def update_progress(enrollment_id: int, completed_lessons: int, progress_percent: int, db: Session = Depends(get_db)):
    progress = models.Progress(
        enrollment_id=enrollment_id,
        completed_lessons=completed_lessons,
        progress_percent=progress_percent
    )

    db.add(progress)
    db.commit()

    return {"message": "Progress updated successfully"}


# 6️⃣ Get enrolled courses for a user
@app.get("/users/{user_id}/courses")
def get_user_courses(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Enrollment).filter(models.Enrollment.user_id == user_id).all()