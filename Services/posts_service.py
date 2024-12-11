from Database.repository import AbstractRepository
from Models.Posts import SPostAdd


class PostsService:
    def __init__(self, posts_repo: AbstractRepository):
        self.posts_repo: AbstractRepository = posts_repo()

    async def add_post(self, post: SPostAdd):
        post_dict = post.model_dump()
        post_id = await self.posts_repo.add_one(post_dict)
        return post_id

    async def delete_post(self, post_id: int):
        res = await self.posts_repo.delete_one(post_id)
        return res

    async def get_posts(self):
        res = await self.posts_repo.find_all()
        return res

    async def get_post(self, post_id: int):
        post = await self.posts_repo.find_one(post_id)
        return post

    async def get_posts_from_thread(self, thread_id: int):
        posts = self.posts_repo.find_by_conditions({"thread_id": thread_id})
        return posts