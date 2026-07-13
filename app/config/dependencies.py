from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker
from .database import async_session_factory

def get_engine_database() -> async_sessionmaker:
    return async_session_factory

