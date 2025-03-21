from fastapi import FastAPI
from app.api.v1.endpoints import user

app = FastAPI(
    title="UserHub",
    description="API to manage users, developed with **FastAPI** and **MongoDB**. It offers CRUD operations, pagination, filters and data validations. Designed to be fast, secure and easy to use.",
    version="1.0.0"
)

app.include_router(user.router, prefix="/api/v1")