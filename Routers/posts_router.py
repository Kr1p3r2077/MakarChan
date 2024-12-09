from typing import Annotated

from fastapi import APIRouter, Depends

from Database.repository import PostRepository
from schemas import SPostCreate

posts_router = APIRouter(
    prefix='/posts',
    tags=['Посты']
)

@posts_router.post('/create')
async def post_create(
    post: Annotated[SPostCreate, Depends()]
):
    post_id = await PostRepository.create_one(post)
    return { "ok": True, "post_id": post_id}

@posts_router.get('/get')
async def post_get(
    thread_id
):
    posts = await PostRepository.find_all(thread_id)
    return { "posts": posts }

@posts_router.post('/remove/{post_id}')
async def post_remove(
        post_id
):
    response = await PostRepository.remove_one(post_id)
    return response