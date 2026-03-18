from fastapi import APIRouter
import random
from jwt_handler import create_token

router = APIRouter()

fake_db = {}

@router.post("/auth/send-otp")
def send_otp(email: str):
    otp = random.randint(1000, 9999)
    fake_db[email] = otp
    return {"message": "OTP sent", "otp": otp}  # remove otp in production

@router.post("/auth/verify-otp")
def verify_otp(email: str, otp: int):
    if fake_db.get(email) == otp:
        token = create_token({"email": email})
        return {"access_token": token}
    return {"error": "Invalid OTP"}

from pydantic import BaseModel

class EmailRequest(BaseModel):
    email: str

@router.post("/auth/send-otp")
def send_otp(data: EmailRequest):
    otp = random.randint(1000, 9999)
    fake_db[data.email] = otp
    return {"message": "OTP sent", "otp": otp}
class VerifyRequest(BaseModel):
    email: str
    otp: int

@router.post("/auth/verify-otp")
def verify_otp(data: VerifyRequest):
    if fake_db.get(data.email) == data.otp:
        token = create_token({"email": data.email})
        return {"access_token": token}
    return {"error": "Invalid OTP"}