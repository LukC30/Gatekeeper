from fastapi import APIRouter
from .dto import UserDTO


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post('/', response_class=UserDTO, status_code=201)
async def create_user(user_dto: UserDTO):
    return {"success": False}

@router.get("/:email", response_class=UserDTO, status_code=200)
async def get_user():
    
    
    return