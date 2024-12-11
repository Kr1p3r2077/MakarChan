from Repositories.Repositories import UsersRepository, ThreadsRepository, PostsRepository
from Services.posts_service import PostsService
from Services.threads_service import ThreadsService
from Services.users_service import UsersService


def users_service():
    return UsersService(UsersRepository)

def threads_service():
    return ThreadsService(ThreadsRepository)

def posts_service():
    return PostsService(PostsRepository)