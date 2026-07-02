from unittest.mock import Mock

import pytest

from src.application.use_cases.create_user import CreateUser
from src.domain.exceptions import EntityAlreadyExistsError


def test_create_user_success():
    repo = Mock()
    security = Mock()

    repo.find_by_email.return_value = None
    security.hash_password.return_value = "hashed"

    use_case = CreateUser(repo, security)

    use_case.execute(
        name="John",
        email="john@email.com",
        password="123",
        role="ADMIN"
    )

    security.hash_password.assert_called_once_with("123")
    repo.save.assert_called_once()


def test_create_user_with_existing_email_raises_before_saving():
    repo = Mock()
    security = Mock()

    repo.find_by_email.return_value = "existing-user"

    use_case = CreateUser(repo, security)

    with pytest.raises(EntityAlreadyExistsError):
        use_case.execute(
            name="John",
            email="john@email.com",
            password="123",
            role="ADMIN",
        )

    security.hash_password.assert_not_called()
    repo.save.assert_not_called()