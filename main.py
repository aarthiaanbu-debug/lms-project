from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
from datetime import datetime, timedelta

# CREATE TABLES
models.Base.metadata.create_all(bind=engine)



app = FastAPI(title="Learning Management System API")


# database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "LMS API Running Successfully"}

# ---------------- LOGIN ---------------- #

from fastapi import HTTPException

@app.post("/login")
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.username == data.username,
        models.User.password == data.password
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "user_id": user.id
    }


# ---------------- COURSES ---------------- #

@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()


@app.get("/courses/{user_id}")
def get_courses_by_user(user_id: int, db: Session = Depends(get_db)):

    subscription = db.query(models.Subscription).filter(
        models.Subscription.user_id == user_id,
        models.Subscription.status == True
    ).first()

    if subscription:
        return db.query(models.Course).all()
    else:
        return db.query(models.Course).all()


# ---------------- LESSONS ---------------- #

@app.get("/lessons")
def get_lessons(db: Session = Depends(get_db)):
    return db.query(models.Lesson).all()


# ---------------- ENROLL ---------------- #

from datetime import datetime

@app.post("/enroll")
def enroll(user_id: int, course_id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == user_id).first()
    course = db.query(models.Course).filter(models.Course.id == course_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    enrollment = models.Enrollment(
        user_id=user_id,
        course_id=course_id,
        enrolled_on=datetime.utcnow()
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return {
        "message": "Enrollment successful",
        "enrollment_id": enrollment.id
    }

# ---------------- PROGRESS ---------------- #

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


# ---------------- USER COURSES ---------------- #

@app.get("/users/{user_id}/courses")
def get_user_courses(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Enrollment).filter(
        models.Enrollment.user_id == user_id
    ).all()


# ---------------- PLANS ---------------- #

@app.get("/plans")
def get_plans(db: Session = Depends(get_db)):
    return db.query(models.Plan).all()


# ---------------- SUBSCRIBE ---------------- #

from fastapi import HTTPException

@app.post("/subscribe")
def subscribe(data: schemas.SubscribeRequest, db: Session = Depends(get_db)):

    # check plan
    plan = db.query(models.Plan).filter(models.Plan.id == data.plan_id).first()

    if plan is None:
        raise HTTPException(status_code=404, detail="Plan not found")

    start_date = datetime.utcnow()
    end_date = start_date + timedelta(days=plan.duration_days)

    subscription = models.Subscription(
        user_id=data.user_id,
        plan_id=data.plan_id,
        start_date=start_date,
        end_date=end_date,
        status=True
    )

    db.add(subscription)
    db.commit()

    payment = models.Payment(
        user_id=data.user_id,
        plan_id=data.plan_id,
        amount=plan.price,
        payment_date=datetime.utcnow()
    )

    db.add(payment)
    db.commit()

    return {
        "message": "Subscription activated"
    }


# ---------------- USER SUBSCRIPTION ---------------- #

@app.get("/users/{user_id}/subscription")
def get_subscription(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Subscription).filter(
        models.Subscription.user_id == user_id,
        models.Subscription.status == True
    ).first()


# ---------------- NOTIFICATIONS ---------------- #

@app.get("/notifications")
def get_notifications(db: Session = Depends(get_db)):
    return db.query(models.Notification).order_by(
        models.Notification.id.desc()
    ).all()


@app.post("/notifications")
def create_notification(data: schemas.NotificationCreate, db: Session = Depends(get_db)):

    notification = models.Notification(
        message=data.message,
        created_at=datetime.utcnow()
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return {
        "message": "Notification created",
        "notification_id": notification.id
    }


# ---------------- DASHBOARD ANALYTICS ---------------- #

@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):

    total_users = db.query(models.User).count()
    total_courses = db.query(models.Course).count()
    total_enrollments = db.query(models.Enrollment).count()
    total_payments = db.query(models.Payment).count()

    return {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments,
        "total_payments": total_payments
    }