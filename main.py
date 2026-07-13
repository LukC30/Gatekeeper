from fastapi import FastAPI

from app.config.lifespan import lifespan
from dotenv import load_dotenv

import uvicorn

api = FastAPI(
    description="it is the main guardian of your application.",
    title="Gatekeeper",
    version="0.01",
    lifespan=lifespan
)

@api.get("/test")
def test_route():
    return {"message": "initializing..."}

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app="main:api", reload=True)