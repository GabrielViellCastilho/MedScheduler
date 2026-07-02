from datetime import date
from unittest.mock import Mock

import pytest

from src.application.use_cases.create_patient import CreatePatient
from src.domain.exceptions import EntityAlreadyExistsError
from src.domain.value_objects.cpf import CPF
from src.domain.value_objects.exceptions import DomainValidationError

VALID_CPF = "52998224725"


def test_create_patient_success():
    repo = Mock()
    repo.find_by_cpf.return_value = None

    use_case = CreatePatient(repo)

    use_case.execute(
        name="John",
        cpf=VALID_CPF,
        birth_date=date(1990, 1, 1),
        phone="11999999999",
        email="john@email.com",
    )

    repo.save.assert_called_once()
    saved_patient = repo.save.call_args.args[0]
    assert isinstance(saved_patient.cpf, CPF)


def test_create_patient_with_invalid_cpf_raises_before_saving():
    repo = Mock()

    use_case = CreatePatient(repo)

    with pytest.raises(DomainValidationError):
        use_case.execute(
            name="John",
            cpf="11111111111",
            birth_date=date(1990, 1, 1),
            phone="11999999999",
            email="john@email.com",
        )

    repo.save.assert_not_called()


def test_create_patient_with_existing_cpf_raises_before_saving():
    repo = Mock()
    repo.find_by_cpf.return_value = "existing-patient"

    use_case = CreatePatient(repo)

    with pytest.raises(EntityAlreadyExistsError):
        use_case.execute(
            name="John",
            cpf=VALID_CPF,
            birth_date=date(1990, 1, 1),
            phone="11999999999",
            email="john@email.com",
        )

    repo.save.assert_not_called()
