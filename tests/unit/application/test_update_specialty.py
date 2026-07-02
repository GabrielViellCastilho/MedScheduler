from unittest.mock import Mock
from uuid import uuid4
from types import SimpleNamespace
from src.application.use_cases.update_specialty import UpdateSpecialty


def test_update_specialty_not_found_returns_none():
    repo = Mock()
    repo.find_by_id.return_value = None

    use_case = UpdateSpecialty(repo)

    result = use_case.execute(uuid4(), name="New", description="New desc")

    assert result is None
    repo.update.assert_not_called()


def test_update_specialty_success():
    repo = Mock()
    existing = SimpleNamespace(name="Old", description="Old desc", updated_at=None)
    repo.find_by_id.return_value = existing
    repo.update.return_value = existing

    use_case = UpdateSpecialty(repo)

    use_case.execute(uuid4(), name="New", description="New desc")

    assert existing.name == "New"
    assert existing.description == "New desc"
    repo.update.assert_called_once_with(existing)
