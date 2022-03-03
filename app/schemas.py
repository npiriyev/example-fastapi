from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserIn(BaseModel):
    email : str
    password : str

class UserOut(BaseModel):
    id: int
    email : str
    created_at : datetime

    class Config:
        orm_mode = True