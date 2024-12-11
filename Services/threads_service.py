from Database.repository import AbstractRepository
from Models.Threads import SThreadAdd


class ThreadsService:
    def __init__(self, threads_repo: AbstractRepository):
        self.threads_repo: AbstractRepository = threads_repo()

    async def add_thread(self, thread: SThreadAdd):
        thread_dict = thread.model_dump()
        thread_id = await self.threads_repo.add_one(thread_dict)
        return thread_id

    async def delete_thread(self, thread_id: int):
        res = await self.threads_repo.delete_one(thread_id)
        return res

    async def get_threads(self):
        res = await self.threads_repo.find_all()
        return res

    async def get_thread(self, thread_id: int):
        user = await self.threads_repo.find_one(thread_id)
        return user