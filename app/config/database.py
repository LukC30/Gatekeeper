from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel

from dotenv import load_dotenv

import os

load_dotenv()

DB_USER = os.getenv("USER_DB")
DB_PASSWORD = os.getenv("PASSWORD", "")
DB_PORT = os.getenv("PORT")
DB_HOST = os.getenv("HOST")
DB_NAME = os.getenv("DATABASE")


DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(DATABASE_URL)
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)

async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False

)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)