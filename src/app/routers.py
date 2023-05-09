from fastapi import FastAPI

from app.user.v1.routers import router as user_router


def register_routers(app: FastAPI):
    app.include_router(user_router, prefix="/user")
