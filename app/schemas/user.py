from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
    email: str
    class Config:
        orm_mode = True
