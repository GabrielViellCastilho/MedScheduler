from unittest.mock import Mock
from src.application.use_cases.list_patients import ListPatients


def test_list_patients_returns_envelope():
    repo = Mock()
    repo.find_all.return_value = ["patient-1"]
    repo.count.return_value = 1

    use_case = ListPatients(repo)

    result = use_case.execute(limit=20, offset=0)

    repo.find_all.assert_called_once_with(20, 0, active=None)
    repo.count.assert_called_once_with(active=None)
    assert result == {"items": ["patient-1"], "total": 1, "limit": 20, "offset": 0}


def test_list_patients_filters_by_active():
    repo = Mock()
    repo.find_all.return_value = ["patient-1"]
    repo.count.return_value = 1

    use_case = ListPatients(repo)

    use_case.execute(limit=20, offset=0, active=True)

    repo.find_all.assert_called_once_with(20, 0, active=True)
    repo.count.assert_called_once_with(active=True)
