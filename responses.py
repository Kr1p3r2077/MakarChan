from pydantic import BaseModel


class DefaulResponse(BaseModel):
    result: bool
    desc: str

class UserRegisterResponse(BaseModel):
    user_id: int
