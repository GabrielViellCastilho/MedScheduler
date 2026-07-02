from unittest.mock import Mock
from uuid import uuid4
from src.application.use_cases.get_doctor import GetDoctor


def test_get_doctor_found():
    repo = Mock()
    doctor_id = uuid4()
    repo.find_by_id.return_value = "doctor"

    use_case = GetDoctor(repo)

    result = use_case.execute(doctor_id)

    repo.find_by_id.assert_called_once_with(doctor_id)
    assert result == "doctor"
