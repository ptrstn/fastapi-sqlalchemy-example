# src/mypackage/api/api_v1/api.py

from fastapi import APIRouter
from .endpoints import users, items

api_router = APIRouter(prefix="/api")

api_router.include_router(users.router)
api_router.include_router(items.router)


@api_router.get("/")
def get_home():
    return {"Hello": "World"}
