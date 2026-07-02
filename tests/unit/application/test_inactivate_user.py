from unittest.mock import Mock
from uuid import uuid4

from src.application.use_cases.inactivate_user import InactivateUser


def test_inactivate_user_not_found_returns_false():
    repo = Mock()

    repo.find_by_id.return_value = None

    use_case = InactivateUser(repo)

    result = use_case.execute(uuid4())

    assert result is False
    repo.inactivate.assert_not_called()


def test_inactivate_user_success():
    repo = Mock()

    repo.find_by_id.return_value = "user"

    use_case = InactivateUser(repo)

    user_id = uuid4()

    result = use_case.execute(user_id)

    assert result is True
    repo.inactivate.assert_called_once_with(user_id)