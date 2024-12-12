from pydantic import BaseModel


class SUserRegister(BaseModel):
    login: str
    password: str