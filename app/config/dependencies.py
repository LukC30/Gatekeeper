from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from .database import engine

def get_engine_database() -> AsyncEngine:
    return engine

