from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    is_active: Optional[bool] = True

class UserInDB(User):
    id: str