from Database.database import new_session, ThreadOrm, PostOrm, UserOrm
from sqlalchemy import select

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


class UserRepository:
    @classmethod
    async def create_one(cls, data: SUserRegister):
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UserOrm(**user_dict)

            if user.username is None:
                user.username = user.login

            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_user(cls, user_id):
        async with new_session() as session:
            #query = select(UserOrm).where(UserOrm.id == user_id)
            #result = await session.execute(query)
            #user_models = result.scalars().all()
            return await session.get(UserOrm, user_id)

    @classmethod
    async def make_friends(cls, user_id1, user_id2):
        async with new_session() as session:
            user1 = await session.get(UserOrm, user_id1)
            user2 = await session.get(UserOrm, user_id2)
            user1.friends = user1.friends + user_id2 + " "
            user2.friends = user2.friends + user_id1 + " "
            await session.commit()
            return 0
