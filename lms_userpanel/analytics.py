from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Assignment, Submission, Attendance

router = APIRouter()

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    
    total_assignments = db.query(Assignment).count()
    total_submissions = db.query(Submission).count()
    total_attendance = db.query(Attendance).count()

    present_count = db.query(Attendance).filter(Attendance.status == "Present").count()
    absent_count = db.query(Attendance).filter(Attendance.status == "Absent").count()

    return {
        "total_assignments": total_assignments,
        "total_submissions": total_submissions,
        "total_attendance_records": total_attendance,
        "attendance": {
            "present": present_count,
            "absent": absent_count
        }
    }