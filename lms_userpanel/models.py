from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from datetime import datetime
from database import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    room = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# ✅ Notification (UPDATED as per task)
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)   # 🔥 important
    message = Column(String)
    is_read = Column(Boolean, default=False)   # 🔥 important
    created_at = Column(DateTime, default=datetime.utcnow)


# ✅ Attendance
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    date = Column(Date)
    status = Column(String)


# ✅ Assignment (FIXED - வெளியே கொண்டு வந்தோம்)
class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    deadline = Column(DateTime)
    file_url = Column(String)


# ✅ Submission
class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer)
    student_id = Column(Integer)
    file_url = Column(String)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    grade = Column(String)
    remarks = Column(String)