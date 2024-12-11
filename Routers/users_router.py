from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi import APIRouter
from Models.Users import SUserAdd
from dependencies import users_service
from Services.users_service import UsersService

users_router = APIRouter(
    prefix='/users',
    tags=['Пользователи']
)


@users_router.post('/add')
async def add_user(
        user: SUserAdd,
        users_service: Annotated[UsersService, Depends(users_service)]
):
    user_id = await users_service.add_user(user)
    return { 'user_id': user_id }

@users_router.delete('/delete')
async def delete_user(
        users_service: Annotated[UsersService, Depends(users_service)],
        id: int
):
    result = await users_service.delete_user(id)
    return { 'result': result }

@users_router.get('/getall')
async def get_all_users(
        users_service: Annotated[UsersService, Depends(users_service)]
):
    users = await users_service.get_users()
    return { 'users': users }

@users_router.get('/get')
async def get_user(
        users_service: Annotated[UsersService, Depends(users_service)],
        id: int
):
    user = await users_service.get_user(id)
    return { 'user': user }
