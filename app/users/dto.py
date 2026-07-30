from pydantic import BaseModel

class UserDTO(BaseModel):
    email: str
    senha: str

class UserUpdateDTO(BaseModel):
    email: str
    senha: str
    nova_senha: str
