from fastapi import APIRouter
from jwt_handler import create_token

router = APIRouter()

@router.get("/auth/facebook")
def facebook_login():
    return {"url": "https://www.facebook.com/dialog/oauth"}

@router.get("/auth/facebook/callback")
def facebook_callback():
    user = {"email": "fbuser@gmail.com"}
    token = create_token(user)
    return {"access_token": token}