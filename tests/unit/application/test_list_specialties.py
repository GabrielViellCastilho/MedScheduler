from unittest.mock import Mock
from src.application.use_cases.list_specialties import ListSpecialties


def test_list_specialties_returns_envelope():
    repo = Mock()
    repo.find_all.return_value = ["specialty-1"]
    repo.count.return_value = 1

    use_case = ListSpecialties(repo)

    result = use_case.execute(limit=20, offset=0)

    repo.find_all.assert_called_once_with(20, 0)
    assert result == {"items": ["specialty-1"], "total": 1, "limit": 20, "offset": 0}
