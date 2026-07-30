from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config.database import init_db

import logging
from dotenv import load_dotenv

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    await init_db()
    logging.info(f"[INIT] Iniciando ciclo de vida da aplicação")
    yield
    logging.info(f"[ENDING] Encerrando ciclo de vida da aplicação")