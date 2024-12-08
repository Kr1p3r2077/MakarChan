from fastapi import FastAPI
from contextlib import asynccontextmanager
from Database.database import create_tables, delete_tables
from fastapi.middleware.cors import CORSMiddleware

from Routers.threads_router import threads_router
from Routers.posts_router import posts_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('DROPPING database.')
    await create_tables()
    print('Database is ready.')
    yield
    print('Makarchan Shutting down.')


app = FastAPI(lifespan=lifespan)
app.include_router(threads_router)
app.include_router(posts_router)

