from ..utils.auth_utils import verify_password, _generate_token
from ..users.interface import BaseUserRepository
from ..users.dto import UserDTO
from ..models.user_model import User
class AuthService():
    def __init__(self, user_repo: BaseUserRepository):
        self.user_repo = user_repo
        

    async def login(self, user: UserDTO):
        user_model: User = await self.user_repo.get_by_email(email=user.email)
        if not verify_password(user.senha, user_model.senha):
            return

        