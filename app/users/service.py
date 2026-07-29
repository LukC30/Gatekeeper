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
    
    async def get_by_email(self, email: str):
        result = await self.user_repo.get_by_email(email)
        return result

    async def update(self, id, user_dto: UserDTO):
        user_comparative = await self.user_repo.get_by_email(user_dto.email)
        if user_comparative is None:
            return None

        if user_comparative.id != id:
            return None

        user_dto.senha = encrypt_password(user_dto.senha)
        user_model = UserMapper.to_user_model(user_dto)
        model = await self.user_repo.update(id, user_model)

        return model
        