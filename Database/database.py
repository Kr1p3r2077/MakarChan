from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    'sqlite+aiosqlite:///makarchan.db'
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class ThreadOrm(Model):
    __tablename__ = 'threads'

    id: Mapped[int] = mapped_column(primary_key=True)
    topic: Mapped[str]
    text: Mapped[Optional[str]]
    board: Mapped[str]
    creator_id: Mapped[int]
    created_time: Mapped[str]


class PostOrm(Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    board_id: Mapped[int]
    creator_id: Mapped[int]
    posted_time: Mapped[str]

class UserOrm(Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    username: Mapped[Optional[str]]
    about: Mapped[Optional[str]]
    friends: Mapped[Optional[str]]
    permission_level: Mapped[int]
    time_created: Mapped[str]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
