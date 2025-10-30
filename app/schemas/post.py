from datetime import datetime
from pydantic import BaseModel

from app.schemas.user import UserDisplay

class PostBase(BaseModel):
    title: str
    content: str

class PostDisplay(BaseModel):
    id: int
    title: str
    content: str
    timestamp: datetime
    creator: UserDisplay

    class Config:
        orm_mode = True

class UserPostDisplay(BaseModel):
    id: int
    title: str
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True