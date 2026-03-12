from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas
from datetime import datetime, timedelta

app = FastAPI(title="Learning Management System API")


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def home():
    return {"message": "LMS API Running Successfully"}


@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()

@app.get("/courses/{user_id}")
def get_courses(user_id: int, db: Session = Depends(get_db)):

    subscription = db.query(models.Subscription).filter(
        models.Subscription.user_id == user_id,
        models.Subscription.status == True
    ).first()

    if subscription:
        return db.query(models.Course).all()
    else:
        return db.query(models.Course).all()

@app.get("/lessons")
def get_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).all()

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

@app.post("/progress")
def update_progress(data: schemas.ProgressRequest, db: Session = Depends(get_db)):

    progress = models.Progress(
        enrollment_id=data.enrollment_id,
        completed_lessons=data.completed_lessons,
        progress_percent=data.progress_percent
    )

    db.add(progress)
    db.commit()

    return {"message": "Progress updated successfully"}

@app.get("/users/{user_id}/courses")
def get_user_courses(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Enrollment).filter(models.Enrollment.user_id == user_id).all()
@app.get("/plans")
def get_plans(db: Session = Depends(get_db)):
    return db.query(models.Plan).all()
@app.post("/subscribe")
def subscribe(data: schemas.SubscribeRequest, db: Session = Depends(get_db)):

    plan = db.query(models.Plan).filter(models.Plan.id == data.plan_id).first()

    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=plan.duration_days)

    new_subscription = models.Subscription(
        user_id=data.user_id,
        plan_id=data.plan_id,
        start_date=start_date,
        end_date=end_date,
        status=True
    )

    db.add(new_subscription)
    db.commit()

    payment = models.Payment(
        user_id=data.user_id,
        plan_id=data.plan_id,
        amount=plan.price,
        payment_date=datetime.utcnow()
    )

    db.add(payment)
    db.commit()

    return {"message": "Subscription activated"}
@app.get("/users/{user_id}/subscription")
def get_subscription(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Subscription).filter(
        models.Subscription.user_id == user_id,
        models.Subscription.status == True
    ).first()