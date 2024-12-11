from Database.repository import SQLAlchemyRepository
from Models.Posts import PostOrm
from Models.Threads import ThreadOrm
from Models.Users import UserOrm


class UsersRepository(SQLAlchemyRepository):
    model = UserOrm

class ThreadsRepository(SQLAlchemyRepository):
    model = ThreadOrm

class PostsRepository(SQLAlchemyRepository):
    model = PostOrm