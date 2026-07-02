from unittest.mock import Mock
from uuid import uuid4

from src.application.use_cases.list_doctors import ListDoctors


def test_list_doctors_returns_envelope():
    repo = Mock()
    repo.find_all.return_value = ["doctor-1"]
    repo.count.return_value = 1

    use_case = ListDoctors(repo)

    result = use_case.execute(limit=20, offset=0)

    repo.find_all.assert_called_once_with(20, 0, active=None, specialty_id=None)
    repo.count.assert_called_once_with(active=None, specialty_id=None)
    assert result == {"items": ["doctor-1"], "total": 1, "limit": 20, "offset": 0}


def test_list_doctors_filters_by_active_and_specialty():
    repo = Mock()
    repo.find_all.return_value = ["doctor-1"]
    repo.count.return_value = 1
    specialty_id = uuid4()

    use_case = ListDoctors(repo)

    use_case.execute(limit=20, offset=0, active=False, specialty_id=specialty_id)

    repo.find_all.assert_called_once_with(20, 0, active=False, specialty_id=specialty_id)
    repo.count.assert_called_once_with(active=False, specialty_id=specialty_id)
