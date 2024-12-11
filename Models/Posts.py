from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from Database.database import Model


class SPostAdd(BaseModel):
    text: str
    thread_id: int = 1
    creator_id: int = 1
    posted_time: str = '12:44:55 10.12.2024'


class SPost(SPostAdd):
    id: int


class PostOrm(Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    thread_id: Mapped[int]
    creator_id: Mapped[int]
    posted_time: Mapped[str]

    def to_read_model(self) -> SPost:
        return SPost(
            id=self.id,
            text=self.text,
            thread_id=self.thread_id,
            creator_id=self.creator_id,
            posted_time=self.posted_time
        )
