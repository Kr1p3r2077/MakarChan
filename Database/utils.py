# utils.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from Database.database import UserOrm


async def check_user_is_valid(user: UserOrm, session: AsyncSession) -> bool:
    result = await session.execute(select(UserOrm).where(UserOrm.login == user.login))
    #print(result.scalar_one_or_none())
    return result.scalar_one_or_none() is None