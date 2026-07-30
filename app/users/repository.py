from .interface import BaseUserRepository
from app.models.user_model import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

class UserRepository(BaseUserRepository):
    def __init__(self, async_session_factory):
        super().__init__(async_session_factory)

    async def create(self, user_model: User):
        async with self.async_session_factory.begin() as session:
            session.add(user_model)
            await session.commit()
        return user_model

    async def get_by_id(self, id):
        async with self.async_session_factory.begin() as session:
            model = (await session.execute(select(User).where(User.id == id))).scalar_one_or_none()
            return model
         
        

    async def get_by_email(self, email: str):
        async with self.async_session_factory.begin() as session:
            model = (await session.execute(select(User).where(User.email == email))).scalar_one_or_none()
            return model


    async def update(self, id: int, user_model: User):
        async with self.async_session_factory.begin() as session:
            result = (await session.scalars(
                update(User)
                .where(User.id == id)
                .values(email=user_model.email, senha=user_model.senha)
            )).one_or_none()

            return result