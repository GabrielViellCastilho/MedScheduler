from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field, SQLModel


class AppointmentModel(SQLModel, table=True):
    __tablename__ = "appointments"

    id: UUID = Field(primary_key=True)

    patient_id: UUID = Field(foreign_key="patients.id", index=True)
    doctor_id: UUID = Field(foreign_key="doctors.id", index=True)

    start_datetime: datetime
    end_datetime: datetime

    status: str
    confirmation_status: str

    notes: Optional[str] = None

    reminder_sent_at: Optional[datetime] = None
    confirmed_at: Optional[datetime] = None
    cancelled_at: Optional[datetime] = None
    no_show_at: Optional[datetime] = None

    created_at: datetime
    updated_at: datetime