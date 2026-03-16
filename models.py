from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class Course(Base):
    __tablename__ = "lms_admin_course"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    is_premium = Column(Boolean)

class Lesson(Base):
    __tablename__ = "lms_admin_lesson"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    course_id = Column(Integer)


class Enrollment(Base):
    __tablename__ = "lms_admin_enrollment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    enrolled_on = Column(DateTime, default=datetime.utcnow)


class Progress(Base):
    __tablename__ = "lms_admin_progress"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer)
    completed_lessons = Column(Integer)
    progress_percent = Column(Float)


class Plan(Base):
    __tablename__ = "lms_admin_plan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    duration_days = Column(Integer)


class Subscription(Base):
    __tablename__ = "lms_admin_subscription"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    plan_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(Boolean)


class Payment(Base):
    __tablename__ = "lms_admin_payment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    plan_id = Column(Integer)
    amount = Column(Float)
    payment_date = Column(DateTime)


class Notification(Base):
    __tablename__ = "lms_admin_notification"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    created_at = Column(DateTime)