from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.models.user_model import User

class BaseUserRepository(ABC):

    def __init__(self, async_session_factory):
        self.async_session_factory: async_sessionmaker[AsyncSession] = async_session_factory

    @abstractmethod
    async def create(self, user: User):
        pass

    @abstractmethod
    async def get_by_email(self, email: str):
        pass
    
    @abstractmethod
    async def update(self, id: int, user: User):
        pass