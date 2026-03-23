from fastapi import APIRouter
from jwt_handler import create_token

router = APIRouter()

@router.get("/auth/google")
def google_login():
    return {"url": "https://accounts.google.com/o/oauth2/auth"}

@router.get("/auth/google/callback")
def google_callback():
    # simulate user data
    user = {"email": "user@gmail.com"}
    token = create_token(user)
    return {"access_token": token}