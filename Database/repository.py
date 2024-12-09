from Database.database import new_session, ThreadOrm, PostOrm, UserOrm
from sqlalchemy import select, delete

from Database.utils import check_user_is_valid
from responses import UserRegisterResponse
from schemas import SThreadCreate, SPostCreate, SUserRegister


class ThreadRepository:
    @classmethod
    async def create_one(cls, data: SThreadCreate):
        async with new_session() as session:
            thread_dict = data.model_dump()

            thread = ThreadOrm(**thread_dict)
            session.add(thread)
            await session.flush()
            await session.commit()
            return thread.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ThreadOrm)
            result = await session.execute(query)
            thread_models = result.scalars().all()
            return thread_models

    @classmethod
    async def remove_one(cls, thread_id: int):
        async with new_session() as session:
            query = delete(ThreadOrm).where(ThreadOrm.id == thread_id)

            await session.execute(query)

            await session.commit()
            return {"result": True}


class PostRepository:
    @classmethod
    async def create_one(cls, data: SPostCreate):
        async with new_session() as session:
            post_dict = data.model_dump()

            post = PostOrm(**post_dict)
            session.add(post)
            await session.flush()
            await session.commit()
            return post.id

    @classmethod
    async def find_all(cls, thread_id):
        async with new_session() as session:
            query = select(PostOrm).where(PostOrm.board_id == thread_id)
            result = await session.execute(query)
            post_models = result.scalars().all()
            return post_models

    @classmethod
    async def remove_one(cls, post_id: int):
        async with new_session() as session:
            query = delete(PostOrm).where(PostOrm.id == post_id)

            await session.execute(query)

            await session.commit()
            return {"result": True}


class UserRepository:
    @classmethod
    async def create_one(cls, data: SUserRegister):
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UserOrm(**user_dict)

            if not await check_user_is_valid(user, session):
                return {"result": False, "user_id":0}

            if user.username is None:
                user.username = user.login

            session.add(user)
            await session.flush()
            await session.commit()
            return {"result": True, "user_id":user.id}

    @classmethod
    async def get_user(cls, user_id):
        async with new_session() as session:
            return await session.get(UserOrm, user_id)

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models

    @classmethod
    async def remove_one(cls, user_id: int):
        async with new_session() as session:
            query = delete(UserOrm).where(UserOrm.id == user_id)

            await session.execute(query)

            await session.commit()
            return {"result": True}
