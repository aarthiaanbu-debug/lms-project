from fastapi import APIRouter
from jwt_handler import create_token

router = APIRouter()

@router.get("/auth/github")
def github_login():
    return {"url": "https://github.com/login/oauth/authorize"}

@router.get("/auth/github/callback")
def github_callback():
    user = {"email": "gituser@gmail.com"}
    token = create_token(user)
    return {"access_token": token}