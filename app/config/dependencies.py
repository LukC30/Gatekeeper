from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.users.repository import UserRepository
from app.users.service import UserService
from .database import async_session_factory

def get_engine_database() -> async_sessionmaker:
    return async_session_factory

def get_user_repo() -> UserRepository:
    return UserRepository(get_engine_database())

def get_user_service() -> UserService:
    return UserService(get_user_repo())