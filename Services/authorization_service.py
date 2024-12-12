from datetime import datetime

from fastapi import HTTPException

from Models.Authorization import SUserRegister
from Models.Users import SUserAdd
from authorization import security, config
from dependencies import users_service

class AuthService:
    async def login_user(self, login_data: SUserRegister, resp):
        correct_data = await users_service().get_user_by_login(login_data.login)
        if correct_data != None:
            if correct_data.password == login_data.password:
                token = security.create_access_token(str(correct_data.id))
                return {"access_token": token}
            raise HTTPException(status_code=401, detail="Incorrect Username or Login")

    async def register_user(self, register_data: SUserRegister):

        user_data = SUserAdd(
            login=register_data.login,
            username=register_data.login,
            password=register_data.password,
            about="",
            permission_level=0,
            time_created=datetime.now().strftime("%H:%M:%S %d.%m.%Y")
        )
        user_id = await users_service().add_user(user_data)

        if user_id == 0:
            return {"result": "User is already exists"}

        return {"result": "OK"}