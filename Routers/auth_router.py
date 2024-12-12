from typing import Annotated

from fastapi import APIRouter, Depends, Response

from Models.Authorization import SUserRegister
from Services.authorization_service import AuthService
from Services.users_service import UsersService

auth_router = APIRouter(
    prefix='/auth',
    tags=['Аутентификация & Авторизация']
)

@auth_router.post('/register')
async def register(
        register_data: SUserRegister,
        auth_service: Annotated[AuthService, Depends(AuthService)],
):
    result = await auth_service.register_user(register_data)
    return result


@auth_router.post('/login')
async def login(
        register_data: SUserRegister,
        auth_service: Annotated[AuthService, Depends(AuthService)],
        response: Response
):
    result = await auth_service.login_user(register_data, response)
    return result