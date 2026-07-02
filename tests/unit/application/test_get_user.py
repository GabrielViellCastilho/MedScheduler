from unittest.mock import Mock
from uuid import uuid4

from src.application.use_cases.get_user import GetUser


def test_get_user_found():
    repo = Mock()
    user_id = uuid4()

    repo.find_by_id.return_value = "user"

    use_case = GetUser(repo)

    result = use_case.execute(user_id)

    repo.find_by_id.assert_called_once_with(user_id)
    assert result == "user"