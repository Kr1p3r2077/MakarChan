from Database.database import new_session, ThreadOrm, PostOrm
from sqlalchemy import select

from schemas import SThreadCreate, SPostCreate


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
            query = select(PostOrm)
            result = await session.execute(query)
            post_models = result.scalars().all()
            return post_models
