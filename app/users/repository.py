from .interface import BaseUserRepository
from app.models.user_model import User
from 

class UserRepository(BaseUserRepository):
    def __init__(self, session):
        super().__init__(session)

    async def create(self, user_model: User):
        
