from unittest.mock import Mock
from uuid import uuid4
from src.application.use_cases.inactivate_patient import InactivatePatient


def test_inactivate_patient_not_found_returns_false():
    repo = Mock()
    repo.find_by_id.return_value = None

    use_case = InactivatePatient(repo)

    assert use_case.execute(uuid4()) is False
    repo.inactivate.assert_not_called()


def test_inactivate_patient_success_calls_soft_delete():
    repo = Mock()
    repo.find_by_id.return_value = "patient"

    use_case = InactivatePatient(repo)
    patient_id = uuid4()

    assert use_case.execute(patient_id) is True
    repo.inactivate.assert_called_once_with(patient_id)
    repo.delete.assert_not_called()
