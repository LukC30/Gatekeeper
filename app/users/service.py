from app.users.dto import UserDTO
from app.users.interface import BaseUserRepository
from .mapper import UserMapper
from ..utils.auth_utils import encrypt_password

class UserService():
    def __init__(self, user_repo: BaseUserRepository):
        self.user_repo = user_repo
        
    async def create(self, user_dto: UserDTO):
        user_dto.senha = encrypt_password(user_dto.senha)
        user_model = UserMapper.to_user_model(user_dto)
        result = await self.user_repo.create(user_model)
        return result

    