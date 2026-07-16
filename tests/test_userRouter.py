from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock
import pytest
from main import app 
from app.users.service import UserService
from app.users.dto import UserDTO
from app.models.user_model import User
from app.config.dependencies import get_user_service

# Mock UserService
mock_user_service = AsyncMock(spec=UserService)

def override_get_user_service():
    return mock_user_service

app.dependency_overrides[get_user_service] = override_get_user_service

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_user_endpoint():
    # Arrange
    user_data = {"email": "test@example.com", "username": "testuser", "password": "password"}
    mock_user_service.create_user.return_value = User(id=1, email="test@example.com", username="testuser")
    user_data = {"email": "test@example.com", "senha": "password"}
    mock_user_service.create.return_value = User(id=1, email="test@example.com", senha="password")

    # Act
    response = client.post("/users", json=user_data)
    response = client.post("/user/", json=user_data)

    # Assert
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
    mock_user_service.create_user.assert_called_once()
    mock_user_service.create.assert_called_once()

@pytest.mark.asyncio
async def test_get_user_by_email_endpoint():
    # Arrange
    mock_user_service.get_user_by_email.return_value = User(id=1, email="test@example.com", username="testuser")
    mock_user_service.get_by_email.return_value = User(id=1, email="test@example.com", senha="password")

    # Act
    response = client.get("/users/test@example.com")
    response = client.get("/user/test@example.com")

    # Assert
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    mock_user_service.get_user_by_email.assert_called_once_with("test@example.com")
    mock_user_service.get_by_email.assert_called_once_with("test@example.com")
