from typing import Annotated

from fastapi import APIRouter, Depends

from Database.repository import UserRepository
from responses import DefaulResponse, UserRegisterResponse
from schemas import SUserRegister

users_router = APIRouter(
    prefix='/users',
    tags=['Пользователи']
)

@users_router.post('/register',response_model=UserRegisterResponse)
async def user_register(
    post: Annotated[SUserRegister, Depends()]
):
    response = await UserRepository.create_one(post)
    return response

@users_router.get('/get/{user_id}')
async def user_get(
    user_id
):
    user = await UserRepository.get_user(user_id)
    return { "user": user }

@users_router.get('/getall')
async def get_all_users():
    users = await UserRepository.get_all()
    return {"users": users}

@users_router.post('/remove/{user_id}')
async def user_remove(
        user_id
):
    response = await UserRepository.remove_one(user_id)
    return response