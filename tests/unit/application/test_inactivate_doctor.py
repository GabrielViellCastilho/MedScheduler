from unittest.mock import Mock
from uuid import uuid4
from src.application.use_cases.inactivate_doctor import InactivateDoctor


def test_inactivate_doctor_not_found_returns_false():
    repo = Mock()
    repo.find_by_id.return_value = None

    use_case = InactivateDoctor(repo)

    assert use_case.execute(uuid4()) is False
    repo.inactivate.assert_not_called()


def test_inactivate_doctor_success_calls_soft_delete():
    repo = Mock()
    repo.find_by_id.return_value = "doctor"

    use_case = InactivateDoctor(repo)
    doctor_id = uuid4()

    assert use_case.execute(doctor_id) is True
    repo.inactivate.assert_called_once_with(doctor_id)
    repo.delete.assert_not_called()
