from typing import Annotated

from fastapi import Depends

from fastapi import APIRouter

from Models.Posts import SPostAdd
from Services.posts_service import PostsService
from dependencies import posts_service

posts_router = APIRouter(
    prefix='/posts',
    tags=['Посты']
)


@posts_router.post('/add')
async def add_post(
        thread: SPostAdd,
        threads_service: Annotated[PostsService, Depends(posts_service)]
):
    post_id = await threads_service.add_post(thread)
    return { 'post_id': post_id }

@posts_router.delete('/delete')
async def delete_post(
        posts_service: Annotated[PostsService, Depends(posts_service)],
        post_id: int
):
    result = await posts_service.delete_post(post_id)
    return { 'result': result }

@posts_router.get('/getall')
async def get_all_posts(
        posts_service: Annotated[PostsService, Depends(posts_service)]
):
    posts = await posts_service.get_posts()
    return { 'posts': posts }

@posts_router.get('/getfrom')
async def get_from_thread(
        posts_service: Annotated[PostsService, Depends(posts_service)],
        from_thread_id: int
):
    posts = await posts_service.get_posts_from_thread(from_thread_id)
    return { 'posts': posts }

@posts_router.get('/get')
async def get_post(
        posts_service: Annotated[PostsService, Depends(posts_service)],
        post_id: int
):
    post = await posts_service.get_post(post_id)
    return { 'post': post }