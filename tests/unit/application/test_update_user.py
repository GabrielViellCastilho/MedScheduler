from types import SimpleNamespace
from unittest.mock import Mock
from uuid import uuid4

import pytest

from src.application.use_cases.update_user import UpdateUser


def test_update_user_not_found_returns_none():
    repo = Mock()
    security = Mock()

    repo.find_by_id.return_value = None

    use_case = UpdateUser(repo, security)

    result = use_case.execute(
        user_id=uuid4(),
        name="New",
        email="new@email.com",
        password="123",
        role="ADMIN",
    )

    assert result is None
    repo.update.assert_not_called()
    security.hash_password.assert_not_called()


def test_update_user_success():
    user_id = uuid4()

    repo = Mock()
    security = Mock()

    security.hash_password.return_value = "hashed"

    existing = SimpleNamespace(
        id=user_id,
        name="Old",
        email="old@email.com",
        password="old",
        role="ADMIN",
        updated_at=None,
    )

    repo.find_by_id.return_value = existing
    repo.update.return_value = existing
    repo.find_by_email.return_value = None

    use_case = UpdateUser(repo, security)

    result = use_case.execute(
        user_id=user_id,
        name="New",
        email="new@email.com",
        password="123",
        role="ADMIN",
    )

    assert existing.name == "New"
    assert existing.email == "new@email.com"
    assert existing.password == "hashed"

    security.hash_password.assert_called_once_with("123")
    repo.update.assert_called_once_with(existing)