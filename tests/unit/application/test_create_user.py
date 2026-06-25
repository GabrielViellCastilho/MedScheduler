from unittest.mock import Mock
from src.application.use_cases.create_user import CreateUser


def test_create_user_success():
    repo = Mock()
    security = Mock()

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