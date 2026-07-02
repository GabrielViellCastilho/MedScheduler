from dataclasses import dataclass

from src.domain.value_objects.exceptions import DomainValidationError


@dataclass(frozen=True)
class CPF:
    value: str

    def __post_init__(self):
        digits = "".join(filter(str.isdigit, self.value))
        if len(digits) != 11 or not self._is_valid(digits):
            raise DomainValidationError(f"Invalid CPF: {self.value}")
        object.__setattr__(self, "value", digits)

    @staticmethod
    def _is_valid(digits: str) -> bool:
        if digits == digits[0] * len(digits):
            return False

        def check_digit(base: str) -> int:
            weight = len(base) + 1
            total = sum(int(d) * (weight - i) for i, d in enumerate(base))
            remainder = total % 11
            return 0 if remainder < 2 else 11 - remainder

        first = check_digit(digits[:9])
        second = check_digit(digits[:9] + str(first))
        return digits[-2:] == f"{first}{second}"

    def __str__(self) -> str:
        return self.value
