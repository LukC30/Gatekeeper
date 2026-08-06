from ..utils.auth_utils import verify_password, _generate_token
from ..users.interface import BaseUserRepository
from ..users.dto import UserDTO, UserResponseDTO
from ..models.user_model import User
from ..users.mapper import UserMapper

import asyncio

class AuthService():
    def __init__(self, user_repo: BaseUserRepository):
        self.user_repo = user_repo
        

    async def login(self, user_dto: UserDTO):
        user_model: User = await self.user_repo.get_by_email(email=user_dto.email)
        if not (await asyncio.to_thread(verify_password, user_dto.senha, user_model.senha)):
            return

        user_response = await asyncio.to_thread(UserMapper.to_user_response, user_model)
        token = await asyncio.to_thread(_generate_token, user_response.model_dump())
        return token

        