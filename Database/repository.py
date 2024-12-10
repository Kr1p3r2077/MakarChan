from abc import ABC, abstractmethod

from sqlalchemy import insert, select, delete

from Database.database import new_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with new_session() as session:
            req = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(req)
            await session.commit()
            return res.scalar_one()

    async def delete_one(self, id: int) -> bool:
        async with new_session() as session:
            req = delete(self.model).where(self.model.id == id)
            await session.execute(req)
            await session.commit()
            return True

    async def find_all(self):
        async with new_session() as session:
            req = select(self.model)
            res = await session.execute(req)
            res = [row[0].to_read_model() for row in res.all()]
            return res