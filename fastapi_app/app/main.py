from fastapi import FastAPI
from auth_google import router as google_router
from auth_facebook import router as fb_router
from auth_github import router as github_router
from auth_otp import router as otp_router
from payment import router as payment_router

app = FastAPI()

app.include_router(google_router)
app.include_router(fb_router)
app.include_router(github_router)
app.include_router(otp_router)
app.include_router(payment_router)