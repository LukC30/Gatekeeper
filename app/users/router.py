from fastapi import APIRouter, Depends

from app.models.user_model import User
from app.users.service import UserService
from .dto import UserDTO
from app.config.dependencies import get_user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post('/', status_code=201)
async def create_user(user_dto: UserDTO, user_service: UserService = Depends(get_user_service)):
    result = await user_service.create(user_dto)
    if result is None:
        return {"success": False}

    return result

@router.get("/{email}", status_code=200)
async def get_user_by_email(email: str, user_service: UserService = Depends(get_user_service)):
    result: User = await user_service.get_by_email(email)
    if result is None:
        return {"success": False}    
    
    return result.model_dump()