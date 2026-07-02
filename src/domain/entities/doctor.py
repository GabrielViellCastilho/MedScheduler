from dataclasses import dataclass
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone

from src.domain.value_objects.crm import CRM


@dataclass
class Doctor:
    id: UUID
    user_id: Optional[UUID]
    name: str
    crm: CRM
    specialty_id: UUID
    active: bool
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(
        name: str,
        crm: str,
        specialty_id: UUID,
        user_id: Optional[UUID] = None,
    ):
        now = datetime.now(timezone.utc)
        return Doctor(
            id=uuid4(),
            user_id=user_id,
            name=name,
            crm=CRM(crm),
            specialty_id=specialty_id,
            active=True,
            created_at=now,
            updated_at=now,
        )
