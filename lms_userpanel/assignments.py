from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Assignment, Submission
from datetime import datetime
import shutil
import os
from models import Notification  

router = APIRouter()

# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE ASSIGNMENT
@router.post("/assignments/create")
def create_assignment(
    course_id: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    deadline: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # convert deadline
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")

    # save file
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    assignment = Assignment(
        course_id=course_id,
        title=title,
        description=description,
        deadline=deadline_date,
        file_url=file_path
    )

    db.add(assignment)
    db.commit()

    # 🔥 Notification
    from models import Notification
    notif = Notification(user_id=1, message=f"New Assignment: {title}")
    db.add(notif)
    db.commit()

    return {"message": "Assignment created"}
@router.post("/assignments/submit")
def submit_assignment(
    assignment_id: int = Form(...),
    student_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    assignment = db.query(Assignment).get(assignment_id)

    if not assignment:
        raise HTTPException(404, "Assignment not found")

    # 🔥 DEADLINE VALIDATION
    if datetime.utcnow() > assignment.deadline:
        raise HTTPException(400, "Deadline passed ❌")

    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    submission = Submission(
        assignment_id=assignment_id,
        student_id=student_id,
        file_url=file_path
    )

    db.add(submission)
    db.commit()

    return {"message": "Submitted successfully"}


@router.post("/assignments/grade")
def grade_assignment(data: dict, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == data["submission_id"]).first()

    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    submission.grade = data["grade"]
    submission.remarks = data["remarks"]

    # 🔔 AUTO NOTIFICATION
    message = f"Your assignment (ID: {submission.assignment_id}) has been graded: {data['grade']}"
    notification = Notification(message=message)

    db.add(notification)
    db.commit()

    return {"message": "Graded + Notification sent"}