from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi import APIRouter

from Models.Threads import SThreadAdd
from Services.threads_service import ThreadsService
from dependencies import threads_service

threads_router = APIRouter(
    prefix='/threads',
    tags=['Треды']
)


@threads_router.post('/add')
async def add_thread(
        thread: SThreadAdd,
        threads_service: Annotated[ThreadsService, Depends(threads_service)]
):
    thread_id = await threads_service.add_thread(thread)
    return { 'thread_id': thread_id }

@threads_router.delete('/delete')
async def delete_thread(
        threads_service: Annotated[ThreadsService, Depends(threads_service)],
        thread_id: int
):
    result = await threads_service.delete_thread(thread_id)
    return { 'result': result }

@threads_router.get('/getall')
async def get_all_threads(
        threads_service: Annotated[ThreadsService, Depends(threads_service)]
):
    threads = await threads_service.get_threads()
    return { 'threads': threads }

@threads_router.get('/get')
async def get_thread(
        threads_service: Annotated[ThreadsService, Depends(threads_service)],
        thread_id: int
):
    thread = await threads_service.get_thread(thread_id)
    return { 'thread': thread }