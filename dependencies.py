from Repositories.Users import UsersRepository
from Services.Users import UsersService


def users_service():
    return UsersService(UsersRepository)