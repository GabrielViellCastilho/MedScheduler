from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime, timezone

from src.domain.value_objects.cpf import CPF


@dataclass
class Patient:
    id: UUID
    user_id: Optional[UUID]
    name: str
    cpf: CPF
    birth_date: date
    phone: str
    email: str
    active: bool
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(
        name: str,
        cpf: str,
        birth_date: date,
        phone: str,
        email: str,
        user_id: Optional[UUID] = None,
    ):
        now = datetime.now(timezone.utc)
        return Patient(
            id=uuid4(),
            user_id=user_id,
            name=name,
            cpf=CPF(cpf),
            birth_date=birth_date,
            phone=phone,
            email=email,
            active=True,
            created_at=now,
            updated_at=now,
        )
