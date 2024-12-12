from contextlib import asynccontextmanager

from fastapi import FastAPI

from Database.database import create_tables, delete_tables
from Routers.posts_router import posts_router
from Routers.threads_router import threads_router
from Routers.users_router import users_router
from fastapi.middleware.cors import CORSMiddleware


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
app.include_router(users_router)


origins = [
    "http://localhost:5173",
    "http://0.0.0.0:5173",
    "http://127.0.0.1:5173",
    "http://localhost",
    "http://0.0.0.0",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)