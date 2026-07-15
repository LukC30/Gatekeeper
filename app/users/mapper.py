from app.models.user_model import User
from app.users.dto import UserDTO

class UserMapper():
    @staticmethod
    def to_user_model(user_dto: UserDTO):
        return User(email=user_dto.email, senha=user_dto.senha)