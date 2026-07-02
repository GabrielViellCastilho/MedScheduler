from unittest.mock import Mock
from uuid import uuid4

from src.application.use_cases.cancel_appointment import CancelAppointment


def test_cancel_appointment_success():
    repo = Mock()
    repo.find_by_id.return_value = Mock()

    use_case = CancelAppointment(repo)

    result = use_case.execute(uuid4())

    assert result is True
    repo.update.assert_called_once()


def test_cancel_appointment_not_found():
    repo = Mock()
    repo.find_by_id.return_value = None

    use_case = CancelAppointment(repo)

    result = use_case.execute(uuid4())

    assert result is False
    repo.update.assert_not_called()