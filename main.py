from contextlib import asynccontextmanager

from fastapi import FastAPI

from Database.database import create_tables, delete_tables
from Routers.posts_router import posts_router
from Routers.threads_router import threads_router
from Routers.users_router import users_router


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

# if __name__ == "__main__":
#    uvicorn.run(app, host='0.0.0.0', port=8888)
