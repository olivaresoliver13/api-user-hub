from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]
    is_active: Optional[bool]

class UserInDB(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    is_active: Optional[bool] = True