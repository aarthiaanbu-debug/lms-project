from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Notification

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ CREATE NOTIFICATION
@router.post("/notify")
def create_notification(message: str, db: Session = Depends(get_db)):
    notif = Notification(
        user_id=1,   # 🔥 MUST ADD
        message=message
    )
    db.add(notif)
    db.commit()
    return {"message": "Notification sent"}


# ✅ GET NOTIFICATIONS
@router.get("/notifications")
def get_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).all()