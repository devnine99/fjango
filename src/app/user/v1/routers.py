from fastapi import APIRouter, HTTPException

from app.user.models import User
from app.user.v1.schemas import UserSchema

router = APIRouter()


@router.get("", response_model=list[UserSchema])
async def user_set():
    return [user async for user in User.objects.all()]


@router.get("/{user_id}", response_model=UserSchema)
async def user(user_id):
    try:
        return await User.objects.aget(id=user_id)
    except User.DoesNotExist:
        raise HTTPException(status_code=404)
