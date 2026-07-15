from unittest.mock import AsyncMock, MagicMock

import pytest
from ..users.repository import UserRepository

from ..models.user_model import User

@pytest.mark.asyncio
async def test_create_user():
    """
    Test case for creating a user.

    This test mocks the database session and ensures that the create method
    calls the session's add and commit methods.
    """
    # 1. Arrange: Prepare the test data and mocks
    mock_user = User(id=1, email="test@example.com", senha="password")

    # Mock the session and its methods
    mock_session = AsyncMock()
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()

    # Mock the async_session_factory to return our mock_session
    mock_session_factory = MagicMock()
    # Configure the context manager to return the mock_session
    mock_session_factory.begin.return_value.__aenter__.return_value = mock_session

    # 2. Act: Instantiate the repository and call the method
    user_repo = UserRepository(async_session_factory=mock_session_factory)
    await user_repo.create(mock_user)

    # 3. Assert: Verify that the expected methods were called
    mock_session.add.assert_called_once_with(mock_user)
    mock_session.commit.assert_called_once()

@pytest.mark.asyncio
async def test_get_by_email():
    """
    Test case for retrieving a user by email.

    This test mocks the database session and the execute method to return a mock user,
    ensuring the get_by_email method functions correctly.
    """
    # 1. Arrange
    mock_user = User(id=1, email="test@example.com", senha="password")

    # Mock the result of the select query
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_user

    mock_session = AsyncMock()
    mock_session.execute.return_value = mock_result

    mock_session_factory = MagicMock()
    mock_session_factory.begin.return_value.__aenter__.return_value = mock_session

    # 2. Act
    user_repo = UserRepository(async_session_factory=mock_session_factory)
    result_user = await user_repo.get_by_email("test@example.com")

    # 3. Assert
    assert result_user == mock_user
    mock_session.execute.assert_called_once()

# You can add more detailed assertions about the `select` statement if needed
# by inspecting the call arguments to mock_session.execute.