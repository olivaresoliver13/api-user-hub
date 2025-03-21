from fastapi import APIRouter, HTTPException,  Query
from typing import List
from app.crud.user import get_user, get_users, create_user, update_user, delete_user
from app.schemas.user import UserCreate, UserUpdate, UserInDB

router = APIRouter()

@router.post("/users/", response_model=UserInDB)
def create_user_endpoint(user: UserCreate):
    user_id = create_user(user)
    return {**user.dict(), "id": user_id}

@router.get("/users/{user_id}", response_model=UserInDB)
def read_user(user_id: str):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserInDB)
def update_user_endpoint(user_id: str, user: UserUpdate):
    updated_user = update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.get("/users/", response_model=List[UserInDB])
def read_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    sort_by: str = Query(None, description="Sort by field (e.g., name, age)"),
    order: str = Query("asc", description="Sort order (asc or desc)")
):
    users = get_users(skip, limit, sort_by, order)
    return users

@router.delete("/users/{user_id}")
def delete_user_endpoint(user_id: str):
    delete_user(user_id)
    return {"message": "User deleted"}