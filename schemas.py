from pydantic import BaseModel


class Course(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True


class Lesson(BaseModel):
    id: int
    title: str
    content: str
    video_url: str

    class Config:
        from_attributes = True


class SubscribeRequest(BaseModel):
    user_id: int
    plan_id: int


class ProgressRequest(BaseModel):
    enrollment_id: int
    completed_lessons: int
    progress_percent: int