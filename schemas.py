from pydantic import BaseModel


class ProgressRequest(BaseModel):
    enrollment_id: int
    completed_lessons: int
    progress_percent: float


class SubscribeRequest(BaseModel):
    user_id: int
    plan_id: int


class NotificationCreate(BaseModel):
    message: str


class LoginRequest(BaseModel):
    username: str
    password: str