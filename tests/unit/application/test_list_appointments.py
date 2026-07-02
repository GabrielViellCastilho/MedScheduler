from unittest.mock import Mock

from src.application.use_cases.list_appointments import ListAppointments


def test_list_appointments():
    repo = Mock()
    repo.find_all.return_value = ["a1", "a2"]
    repo.count.return_value = 2

    use_case = ListAppointments(repo)

    result = use_case.execute(limit=10, offset=0)

    assert result["items"] == ["a1", "a2"]
    assert result["total"] == 2
    assert result["limit"] == 10
    assert result["offset"] == 0