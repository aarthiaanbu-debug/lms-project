from pydantic import BaseModel

class Course(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class Lesson(BaseModel):
    id: int
    title: str
    content: str
    video_url: str

    class Config:
        orm_mode = True