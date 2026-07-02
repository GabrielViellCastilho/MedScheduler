from unittest.mock import Mock
from uuid import uuid4

import pytest

from src.application.use_cases.create_doctor import CreateDoctor
from src.domain.exceptions import RelatedEntityNotFoundError
from src.domain.value_objects.crm import CRM
from src.domain.value_objects.exceptions import DomainValidationError


def test_create_doctor_success():
    repo = Mock()
    specialty_repo = Mock()
    specialty_repo.find_by_id.return_value = "specialty"

    use_case = CreateDoctor(repo, specialty_repo)

    use_case.execute(name="Dr. John", crm="12345-SP", specialty_id=uuid4())

    repo.save.assert_called_once()
    saved_doctor = repo.save.call_args.args[0]
    assert isinstance(saved_doctor.crm, CRM)


def test_create_doctor_with_invalid_crm_raises_before_saving():
    repo = Mock()
    specialty_repo = Mock()
    specialty_repo.find_by_id.return_value = "specialty"

    use_case = CreateDoctor(repo, specialty_repo)

    with pytest.raises(DomainValidationError):
        use_case.execute(name="Dr. John", crm="", specialty_id=uuid4())

    repo.save.assert_not_called()


def test_create_doctor_with_missing_specialty_raises_before_saving():
    repo = Mock()
    specialty_repo = Mock()
    specialty_repo.find_by_id.return_value = None

    use_case = CreateDoctor(repo, specialty_repo)

    with pytest.raises(RelatedEntityNotFoundError):
        use_case.execute(name="Dr. John", crm="12345-SP", specialty_id=uuid4())

    repo.save.assert_not_called()
