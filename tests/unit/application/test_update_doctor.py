from types import SimpleNamespace
from unittest.mock import Mock
from uuid import uuid4

import pytest

from src.application.use_cases.update_doctor import UpdateDoctor
from src.domain.exceptions import RelatedEntityNotFoundError


def test_update_doctor_not_found_returns_none():
    repo = Mock()
    specialty_repo = Mock()
    repo.find_by_id.return_value = None

    use_case = UpdateDoctor(repo, specialty_repo)

    result = use_case.execute(uuid4(), name="New", crm="12345-SP", specialty_id=uuid4())

    assert result is None
    repo.update.assert_not_called()


def test_update_doctor_success():
    repo = Mock()
    specialty_repo = Mock()
    specialty_repo.find_by_id.return_value = "specialty"
    existing = SimpleNamespace(
        name="Old",
        crm="old",
        specialty_id=uuid4(),
        user_id=None,
        updated_at=None,
    )
    repo.find_by_id.return_value = existing
    repo.update.return_value = existing

    use_case = UpdateDoctor(repo, specialty_repo)
    new_specialty_id = uuid4()

    use_case.execute(uuid4(), name="New", crm="54321-SP", specialty_id=new_specialty_id)

    assert existing.name == "New"
    assert str(existing.crm) == "54321-SP"
    assert existing.specialty_id == new_specialty_id
    repo.update.assert_called_once_with(existing)


def test_update_doctor_with_missing_specialty_raises():
    repo = Mock()
    specialty_repo = Mock()
    specialty_repo.find_by_id.return_value = None
    existing = SimpleNamespace(
        name="Old",
        crm="old",
        specialty_id=uuid4(),
        user_id=None,
        updated_at=None,
    )
    repo.find_by_id.return_value = existing

    use_case = UpdateDoctor(repo, specialty_repo)

    with pytest.raises(RelatedEntityNotFoundError):
        use_case.execute(uuid4(), name="New", crm="54321-SP", specialty_id=uuid4())

    repo.update.assert_not_called()
