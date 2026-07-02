from unittest.mock import Mock
from uuid import uuid4
from src.application.use_cases.get_patient import GetPatient


def test_get_patient_found():
    repo = Mock()
    patient_id = uuid4()
    repo.find_by_id.return_value = "patient"

    use_case = GetPatient(repo)

    result = use_case.execute(patient_id)

    repo.find_by_id.assert_called_once_with(patient_id)
    assert result == "patient"
