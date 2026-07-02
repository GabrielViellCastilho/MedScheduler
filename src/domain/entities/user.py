from dataclasses import dataclass
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime, timezone


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    RECEPTIONIST = "RECEPTIONIST"
    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"


@dataclass
class User:
    id: UUID
    name: str
    email: str
    password: str
    role: UserRole
    active: bool
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(name: str, email: str, password: str, role: UserRole):
        now = datetime.now(timezone.utc)
        return User(
            id=uuid4(),
            name=name,
            email=email,
            password=password,
            role=role,
            active=True,
            created_at=now,
            updated_at=now,
        )