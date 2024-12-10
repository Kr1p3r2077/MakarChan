from Database.repository import SQLAlchemyRepository
from Models.Users import UserOrm


class UsersRepository(SQLAlchemyRepository):
    model = UserOrm