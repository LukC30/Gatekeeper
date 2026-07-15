from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config.database import init_db
from .config import get_database_config

import logging
from dotenv import load_dotenv
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    await init_db()
    logging.info(f"[INIT] Iniciando ciclo de vida da aplicação")
    yield
    logging.info(f"[ENDING] Encerrando ciclo de vida da aplicação")