from fastapi import FastAPI, WebSocket, UploadFile, File
import shutil
import os

from database import engine, Base
from chat.websocket import chat_endpoint
from notifications.api import router as notification_router
from attendance import router as attendance_router
import models

app = FastAPI(title="LMS Real-Time Chat API")
from assignments import router as assignment_router

app.include_router(assignment_router)


app.include_router(attendance_router)
app.include_router(notification_router)
from analytics import router as analytics_router
app.include_router(analytics_router)

# ✅ THEN create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "LMS Real-Time Chat Running"}


# ---------------- WebSocket Chat ---------------- #

@app.websocket("/ws/chat/{room}")
async def websocket_chat(websocket: WebSocket, room: str):
    await chat_endpoint(websocket, room)


# ---------------- File Upload ---------------- #

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


from fastapi import UploadFile, File
import shutil

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "file_url": file_location
    }


# ---------------- Chat Analytics ---------------- #

messages = []

@app.post("/chat/log")
def log_message(user: str):

    messages.append(user)

    return {"status": "logged"}


@app.get("/chat/analytics")
def analytics():

    return {
        "total_messages": len(messages),
        "active_users": len(set(messages))
    }


# ---------------- Notifications ---------------- #

app.include_router(notification_router)
from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Assignment, Submission, Attendance

app = FastAPI()

@app.get("/analytics")
def get_analytics():
    db: Session = SessionLocal()

    total_assignments = db.query(Assignment).count()
    total_submissions = db.query(Submission).count()
    total_attendance = db.query(Attendance).count()

    present = db.query(Attendance).filter(Attendance.status == "present").count()
    absent = db.query(Attendance).filter(Attendance.status == "absent").count()

    return {
        "total_assignments": total_assignments,
        "total_submissions": total_submissions,
        "total_attendance_records": total_attendance,
        "attendance": {
            "present": present,
            "absent": absent
        }
    }