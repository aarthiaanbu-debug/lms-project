from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Attendance
from datetime import datetime

router = APIRouter()

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# MARK ATTENDANCE
@router.post("/attendance/mark")
def mark_attendance(data: dict, db: Session = Depends(get_db)):
    for record in data["records"]:
     exists = db.query(Attendance).filter_by(
        student_id=record["student_id"],
        course_id=data["course_id"],
        date=datetime.strptime(data["date"], "%Y-%m-%d").date()
    ).first()

    if exists:
        raise HTTPException(400, "Duplicate attendance")

    new = Attendance(
        student_id=record["student_id"],
        course_id=data["course_id"],
        date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
        status=record["status"]
    )
    db.add(new)

    db.commit()
    return {"message": "Attendance marked"}