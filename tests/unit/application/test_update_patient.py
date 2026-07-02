from datetime import date
from types import SimpleNamespace
from unittest.mock import Mock
from uuid import uuid4

import pytest

from src.application.use_cases.update_patient import UpdatePatient
from src.domain.exceptions import EntityAlreadyExistsError

VALID_CPF = "52998224725"


def test_update_patient_not_found_returns_none():
    repo = Mock()
    repo.find_by_id.return_value = None

    use_case = UpdatePatient(repo)

    result = use_case.execute(
        uuid4(),
        name="New",
        cpf=VALID_CPF,
        birth_date=date(1990, 1, 1),
        phone="11999999999",
        email="new@email.com",
    )

    assert result is None
    repo.update.assert_not_called()


def test_update_patient_success():
    patient_id = uuid4()
    repo = Mock()
    existing = SimpleNamespace(
        id=patient_id,
        name="Old",
        cpf="old",
        birth_date=date(1990, 1, 1),
        phone="0",
        email="old@email.com",
        user_id=None,
        updated_at=None,
    )
    repo.find_by_id.return_value = existing
    repo.find_by_cpf.return_value = None
    repo.update.return_value = existing

    use_case = UpdatePatient(repo)

    use_case.execute(
        patient_id,
        name="New",
        cpf=VALID_CPF,
        birth_date=date(1991, 2, 2),
        phone="11999999999",
        email="new@email.com",
    )

    assert existing.name == "New"
    assert str(existing.cpf) == VALID_CPF
    repo.update.assert_called_once_with(existing)


def test_update_patient_keeping_own_cpf_does_not_raise():
    patient_id = uuid4()
    repo = Mock()
    existing = SimpleNamespace(
        id=patient_id,
        name="Old",
        cpf=VALID_CPF,
        birth_date=date(1990, 1, 1),
        phone="0",
        email="old@email.com",
        user_id=None,
        updated_at=None,
    )
    repo.find_by_id.return_value = existing
    repo.find_by_cpf.return_value = existing
    repo.update.return_value = existing

    use_case = UpdatePatient(repo)

    use_case.execute(
        patient_id,
        name="Old",
        cpf=VALID_CPF,
        birth_date=date(1990, 1, 1),
        phone="0",
        email="old@email.com",
    )

    repo.update.assert_called_once_with(existing)


def test_update_patient_with_cpf_taken_by_another_patient_raises():
    patient_id = uuid4()
    other_patient = SimpleNamespace(id=uuid4(), cpf=VALID_CPF)
    repo = Mock()
    existing = SimpleNamespace(
        id=patient_id,
        name="Old",
        cpf="11144477735",
        birth_date=date(1990, 1, 1),
        phone="0",
        email="old@email.com",
        user_id=None,
        updated_at=None,
    )
    repo.find_by_id.return_value = existing
    repo.find_by_cpf.return_value = other_patient

    use_case = UpdatePatient(repo)

    with pytest.raises(EntityAlreadyExistsError):
        use_case.execute(
            patient_id,
            name="Old",
            cpf=VALID_CPF,
            birth_date=date(1990, 1, 1),
            phone="0",
            email="old@email.com",
        )

    repo.update.assert_not_called()
