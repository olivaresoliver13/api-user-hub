from app.db.mongodb import db
from app.schemas.user import UserCreate, UserUpdate
from bson.objectid import ObjectId

def get_user(user_id: str):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["id"] = str(user.pop("_id"))
        return user
    return None

def get_users(skip: int = 0, limit: int = 10, sort_by: str = None, order: str = "asc"):
    sort_order = 1 if order == "asc" else -1
    if sort_by:
        users = db.users.find().sort(sort_by, sort_order).skip(skip).limit(limit)
    else:
        users = db.users.find().skip(skip).limit(limit)
    user_list = []
    for user in users:
        user["id"] = str(user.pop("_id"))
        user_list.append(user)
    return user_list

def create_user(user: UserCreate):
    user_dict = user.dict()
    result = db.users.insert_one(user_dict)
    return str(result.inserted_id)

def update_user(user_id: str, user: UserUpdate):
    user_dict = user.dict(exclude_unset=True)
    db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})
    return get_user(user_id)

def delete_user(user_id: str):
    db.users.delete_one({"_id": ObjectId(user_id)})
    return {"message": "User deleted"}