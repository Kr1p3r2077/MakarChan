from Database.repository import AbstractRepository
from Models.Users import SUserAdd


class UsersService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def add_user(self, user: SUserAdd):
        user_dict = user.model_dump()
        user_id = await self.users_repo.add_one(user_dict)
        return user_id

    async def delete_user(self, id: int):
        res = await self.users_repo.delete_one(id)
        return res

    async def get_users(self):
        res = await self.users_repo.find_all()
        return res

    async def get_user(self, id: int):
        user = await self.users_repo.find_one(id)
        return user