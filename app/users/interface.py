from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio.engine import AsyncEngine

class BaseUserRepository(ABC):

    def __init__(self, engine):
        self.engine: AsyncEngine = engine

    @abstractmethod
    async def create(self):
        pass

    @abstractmethod
    async def update(self):
        pass