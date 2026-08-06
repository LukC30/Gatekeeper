from pydantic import BaseModel

class UserResponseDTO(BaseModel):
    id: int
    email: str

class UserDTO(BaseModel):
    email: str
    senha: str

class UserUpdateDTO(BaseModel):
    email: str
    senha: str
    nova_senha: str
