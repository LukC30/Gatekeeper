from .interface import BaseUserRepository
from app.models.user_model import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class UserRepository(BaseUserRepository):
    def __init__(self, async_session_factory):
        super().__init__(async_session_factory)

    async def create(self, user_model: User):
        async with self.async_session_factory.begin() as session:
            session.add(user_model)
            await session.commit()

    async def get_by_email(self, email: str):
        async with self.async_session_factory.begin() as session:
            model = await session.execute(select(User).where(User.email == email))
            return model


    async def update(self, id: int, user_model: User):
        async with self.async_session_factory.begin() as session:
            model = await session.execute(select(User).where(User.id == user_model.id))

