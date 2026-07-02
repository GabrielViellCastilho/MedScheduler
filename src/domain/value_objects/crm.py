from dataclasses import dataclass

from src.domain.value_objects.exceptions import DomainValidationError


@dataclass(frozen=True)
class CRM:
    value: str

    def __post_init__(self):
        cleaned = self.value.strip()
        alnum = cleaned.replace("-", "")
        if not alnum.isalnum() or not (4 <= len(cleaned) <= 20):
            raise DomainValidationError(f"Invalid CRM: {self.value}")
        object.__setattr__(self, "value", cleaned.upper())

    def __str__(self) -> str:
        return self.value
