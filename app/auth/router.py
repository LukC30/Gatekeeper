from fastapi import APIRouter, Depends, HTTPException
from app.auth.service import AuthService
from app.config.dependencies import get_auth_service
from app.users.dto import UserDTO

router = APIRouter(
    prefix="/auth"
)

@router.post('/login')
async def login(user_dto: UserDTO, auth_service: AuthService = Depends(get_auth_service)):
    token = await auth_service.login(user_dto)
    return token