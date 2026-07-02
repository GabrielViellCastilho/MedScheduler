from unittest.mock import Mock
from uuid import uuid4
from src.application.use_cases.delete_specialty import DeleteSpecialty


def test_delete_specialty_not_found_returns_false():
    repo = Mock()
    repo.find_by_id.return_value = None

    use_case = DeleteSpecialty(repo)

    assert use_case.execute(uuid4()) is False
    repo.delete.assert_not_called()


def test_delete_specialty_success_returns_true():
    repo = Mock()
    repo.find_by_id.return_value = "specialty"

    use_case = DeleteSpecialty(repo)
    specialty_id = uuid4()

    assert use_case.execute(specialty_id) is True
    repo.delete.assert_called_once_with(specialty_id)
