from sqlalchemy import select

from Database.database import UserOrm, new_session
from Database.repository import UserRepository
from schemas import SUserRegister


async def check_user_is_valid(user: UserOrm) -> bool:
    async with new_session() as session:
        result = await session.execute(select(UserOrm).where(UserOrm.login == user.login))
    return result.scalar_one_or_none() is None

async def RegisterUser(user: SUserRegister):
    if not await check_user_is_valid(user):
        return { "user_id": 0 }

    if user.username is None:
        user.username = user.login
    return {"user_id": await UserRepository.create_one(user) }