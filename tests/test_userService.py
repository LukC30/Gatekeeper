from unittest.mock import AsyncMock, MagicMock
import pytest
from app.users.service import UserService
from app.users.interface import BaseUserRepository
from app.models.user_model import User
from app.users.dto import UserDTO

@pytest.fixture
def mock_user_repository():
    return AsyncMock(spec=BaseUserRepository)

@pytest.mark.asyncio
async def test_create_user(mock_user_repository):
    # Arrange
    user_dto = UserDTO(email="test@example.com", senha="password")

    # Configure the mock to return a user
    mock_user_repository.create.return_value = User(id=1, email="test@example.com", username="testuser")

    user_service = UserService(mock_user_repository)

    # Act
    result = await user_service.create(user_dto)

    # Assert
    assert result.id == 1
    assert result.email == "test@example.com"
    mock_user_repository.create.assert_called_once()

@pytest.mark.asyncio
async def test_get_user_by_email(mock_user_repository):
    # Arrange
    mock_user_repository.get_by_email.return_value = User(id=1, email="test@example.com", username="testuser")
    user_service = UserService(mock_user_repository)

    # Act
    result = await user_service.get_by_email("test@example.com")

    # Assert
    assert result is not None
    assert result.email == "test@example.com"
    mock_user_repository.get_by_email.assert_called_once_with("test@example.com")
