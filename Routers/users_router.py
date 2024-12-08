from typing import Annotated

from fastapi import APIRouter, Depends

from Database.repository import UserRepository
from schemas import SUserRegister

users_router = APIRouter(
    prefix='/users',
    tags=['Пользователи']
)

@users_router.post('/register')
async def user_register(
    post: Annotated[SUserRegister, Depends()]
):
    user_id = await UserRepository.create_one(post)
    return { "ok": True, "user_id": user_id}

@users_router.get('/get')
async def user_get(
    user_id
):
    user = await UserRepository.get_user(user_id)
    return { "user": user }

@users_router.get('/makefriends')
async def user_get(
    user_id1,
    user_id2
):
    result = await UserRepository.make_friends(user_id1, user_id2)
    return { "result": result }