from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

from Database.database import Model


class SThreadAdd(BaseModel):
    topic: str
    text: str = ''
    board: str = 'all'
    creator_id: int = 1
    created_time: str = '12:44:55 10.12.2024'


class SThread(SThreadAdd):
    id: int


class ThreadOrm(Model):
    __tablename__ = 'threads'

    id: Mapped[int] = mapped_column(primary_key=True)
    topic: Mapped[str]
    text: Mapped[str]
    board: Mapped[str]
    creator_id: Mapped[int]
    created_time: Mapped[str]

    def to_read_model(self) -> SThread:
        return SThread(
            id=self.id,
            topic=self.topic,
            text=self.text,
            board=self.board,
            creator_id=self.creator_id,
            created_time=self.created_time
        )
