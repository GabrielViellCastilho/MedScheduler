from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4


class AppointmentStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    NO_SHOW = "NO_SHOW"


class ConfirmationStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    DECLINED = "DECLINED"


@dataclass
class Appointment:
    id: UUID

    patient_id: UUID
    doctor_id: UUID

    start_datetime: datetime
    end_datetime: datetime

    status: AppointmentStatus
    confirmation_status: ConfirmationStatus

    notes: Optional[str]

    reminder_sent_at: Optional[datetime]
    confirmed_at: Optional[datetime]
    cancelled_at: Optional[datetime]
    no_show_at: Optional[datetime]

    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(
        patient_id: UUID,
        doctor_id: UUID,
        start_datetime: datetime,
        end_datetime: datetime,
        notes: Optional[str] = None,
    ):
        now = datetime.now(timezone.utc)

        return Appointment(
            id=uuid4(),
            patient_id=patient_id,
            doctor_id=doctor_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            status=AppointmentStatus.SCHEDULED,
            confirmation_status=ConfirmationStatus.PENDING,
            notes=notes,
            reminder_sent_at=None,
            confirmed_at=None,
            cancelled_at=None,
            no_show_at=None,
            created_at=now,
            updated_at=now,
        )