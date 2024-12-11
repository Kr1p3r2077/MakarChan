from abc import ABC, abstractmethod
from typing import Dict, Any

from sqlalchemy import insert, select, delete

from Database.database import new_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, obj_id: int):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def find_by_conditions(self, conditions: Dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, obj_id: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with new_session() as session:
            query = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(query)
            await session.commit()
            return res.scalar_one()

    async def delete_one(self, obj_id: int) -> bool:
        async with new_session() as session:
            delete_query = delete(self.model).where(self.model.id == obj_id)
            result = await session.execute(delete_query)

            if result.rowcount == 1:
                await session.commit()
                return True

            return False

    async def find_all(self):
        async with new_session() as session:
            query = select(self.model)
            res = await session.execute(query)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def find_by_conditions(self, conditions: Dict[str, Any]):
        async with new_session() as session:
            query = select(self.model)
            for column_name, value in conditions.items():
                query = query.filter(getattr(self.model, column_name) == value)

            res = await session.execute(query)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def find_one(self, obj_id: int):
        async with new_session() as session:
            res = await session.get(self.model, obj_id)
            return res