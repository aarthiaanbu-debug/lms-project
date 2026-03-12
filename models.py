from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base
from sqlalchemy import Column, Integer, DateTime
from database import Base
import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, Boolean, DateTime
from database import Base
import datetime


class Course(Base):
    __tablename__ = "lms_admin_course"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    is_premium = Column(Boolean)


class Lesson(Base):
    __tablename__ = "lms_admin_lesson"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("lms_admin_course.id"))
    title = Column(String(255))
    content = Column(Text)
    video_url = Column(String(255))


class Enrollment(Base):
    __tablename__ = "lms_admin_enrollment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    course_id = Column(Integer)
    enrolled_on = Column(DateTime, default=datetime.datetime.utcnow)


class Progress(Base):
    __tablename__ = "lms_admin_progress"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer)
    completed_lessons = Column(Integer)
    progress_percent = Column(Integer)

    from sqlalchemy import Boolean, Float

class Plan(Base):
    __tablename__ = "lms_admin_plan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
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