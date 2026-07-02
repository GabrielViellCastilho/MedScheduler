from unittest.mock import Mock
from uuid import uuid4
from src.application.use_cases.get_specialty import GetSpecialty


def test_get_specialty_found():
    repo = Mock()
    specialty_id = uuid4()
    repo.find_by_id.return_value = "specialty"

    use_case = GetSpecialty(repo)

    result = use_case.execute(specialty_id)

    repo.find_by_id.assert_called_once_with(specialty_id)
    assert result == "specialty"
