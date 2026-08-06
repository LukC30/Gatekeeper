from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
import pytest
from main import api
from app.users.service import UserService
from app.models.user_model import User
from app.config.dependencies import get_user_service

# Mock UserService
mock_user_service = AsyncMock(spec=UserService)

@pytest.fixture(autouse=True)
def setup_teardown():
    """
    Fixture to reset mock state before and after each test.
    """
    mock_user_service.reset_mock()
    yield
    mock_user_service.reset_mock()

def override_get_user_service():
    return mock_user_service

api.dependency_overrides[get_user_service] = override_get_user_service

client = TestClient(api)

@pytest.mark.asyncio
async def test_create_user_endpoint():
    """
    Test the endpoint for creating a user.
    """
    # Arrange
    user_data = {"email": "test@example.com", "senha": "password"}
    returned_user = User(id=1, email="test@example.com", senha="password")
    
    # Configure the mock service to return the user
    mock_user_service.create.return_value = returned_user

    # Act
    response = client.post("/user/", json=user_data)

    # Assert
    assert response.status_code == 201
    assert response.json() == returned_user.model_dump()
    mock_user_service.create.assert_called_once()

@pytest.mark.asyncio
async def test_get_user_by_email_endpoint():
    """
    Test the endpoint for retrieving a user by email.
    """
    # Arrange
    returned_user = User(id=1, email="test@example.com", senha="password")
    mock_user_service.get_by_email.return_value = returned_user

    # Act
    response = client.get("/user/email/test@example.com")

    # Assert
    assert response.status_code == 200
    assert response.json() == returned_user.model_dump()
    mock_user_service.get_by_email.assert_called_once_with("test@example.com")
