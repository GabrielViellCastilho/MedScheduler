import pytest

from src.domain.value_objects.cpf import CPF
from src.domain.value_objects.exceptions import DomainValidationError


def test_valid_cpf_is_accepted():
    cpf = CPF("529.982.247-25")
    assert str(cpf) == "52998224725"


def test_cpf_with_wrong_length_raises():
    with pytest.raises(DomainValidationError):
        CPF("123456789")


def test_cpf_with_repeated_digits_raises():
    with pytest.raises(DomainValidationError):
        CPF("11111111111")


def test_cpf_with_wrong_check_digit_raises():
    with pytest.raises(DomainValidationError):
        CPF("52998224700")
