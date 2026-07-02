from unittest.mock import Mock
from uuid import uuid4

from src.application.use_cases.get_appointment import GetAppointment


def test_get_appointment():
    repo = Mock()
    repo.find_by_id.return_value = "appointment"

    use_case = GetAppointment(repo)

    result = use_case.execute(uuid4())

    repo.find_by_id.assert_called_once()
    assert result == "appointment"