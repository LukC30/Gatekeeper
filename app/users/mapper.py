from app.models.user_model import User
from app.users.dto import UserDTO, UserResponseDTO

class UserMapper():

    @staticmethod
    def to_user_model(user_dto: UserDTO):
        return User(email=user_dto.email, senha=user_dto.senha)

    @staticmethod
    def to_user_response(user_model: User):
        return UserResponseDTO(id=user_model.id, email=user_model.email)