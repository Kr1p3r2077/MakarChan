from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

from Database.database import Model


class SUserAdd(BaseModel):
    login: str
    password: str
    username: str = ''
    about: str = ''
    time_created: str = '01:02:03 10.12.24'
    permission_level: int = 0


class SUser(SUserAdd):
    id: int


class UserOrm(Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    username: Mapped[str]
    about: Mapped[str]
    permission_level: Mapped[int]
    time_created: Mapped[str]

    def to_read_model(self) -> SUser:
        return SUser(
            id=self.id,
            login=self.login,
            password=self.password,
            username=self.username,
            about=self.about,
            permission_level=self.permission_level,
            time_created=self.time_created
        )
