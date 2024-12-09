from pydantic import BaseModel


class DefaulResponse(BaseModel):
    result: bool
    desc: str

class UserRegisterResponse(BaseModel):
    result: bool
    user_id: int
