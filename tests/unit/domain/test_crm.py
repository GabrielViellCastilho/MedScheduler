import pytest

from src.domain.value_objects.crm import CRM
from src.domain.value_objects.exceptions import DomainValidationError


def test_valid_crm_is_accepted():
    crm = CRM("12345-sp")
    assert str(crm) == "12345-SP"


def test_empty_crm_raises():
    with pytest.raises(DomainValidationError):
        CRM("   ")


def test_too_short_crm_raises():
    with pytest.raises(DomainValidationError):
        CRM("12")


def test_too_long_crm_raises():
    with pytest.raises(DomainValidationError):
        CRM("1" * 21)


def test_non_alphanumeric_crm_raises():
    with pytest.raises(DomainValidationError):
        CRM("1234@5")
