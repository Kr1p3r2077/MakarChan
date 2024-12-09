from typing import Annotated

from fastapi import APIRouter, Depends

from Database.repository import ThreadRepository
from schemas import SThreadCreate

threads_router = APIRouter(
    prefix='/threads',
    tags=['Треды']
)

@threads_router.post('/create/{thread_id}')
async def thread_create(
        thread: Annotated[SThreadCreate, Depends()]
):
    thread_id = await ThreadRepository.create_one(thread)
    return { "ok": True, "thread_id": thread_id}


@threads_router.get('/getall')
async def get_all_threads():
    threads = await ThreadRepository.find_all()
    return { "threads": threads }

@threads_router.post('/remove/{thread_id}')
async def thread_remove(
        thread_id: int
):
    result = await ThreadRepository.remove_one(thread_id)
    return result