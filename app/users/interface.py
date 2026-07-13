from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

class BaseUserRepository(ABC):

    def __init__(self, async_session_factory):
        self.async_session_factory: async_sessionmaker[AsyncSession] = async_session_factory

    @abstractmethod
    async def create(self):
        pass

    @abstractmethod
    async def update(self):
        pass