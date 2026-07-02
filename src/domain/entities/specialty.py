from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import datetime, timezone


@dataclass
class Specialty:
    id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(name: str, description: str):
        now = datetime.now(timezone.utc)
        return Specialty(
            id=uuid4(),
            name=name,
            description=description,
            created_at=now,
            updated_at=now,
        )
