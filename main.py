from fastapi import FastAPI

from app.config.lifespan import lifespan
from dotenv import load_dotenv

from app.users.router import router as user_router

import uvicorn

api = FastAPI(
    description="it is the main guardian of your application.",
    title="Gatekeeper",
    version="0.01",
    lifespan=lifespan
)

api.include_router(user_router)

@api.get("/")
def test_route():
    return {"message": "initializing..."}

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app="main:api", reload=True)