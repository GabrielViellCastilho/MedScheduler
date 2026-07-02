from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from uuid import UUID


class CreateAppointmentRequest(BaseModel):
    patient_id: UUID
    doctor_id: UUID
    start_datetime: datetime
    end_datetime: datetime
    notes: Optional[str] = None


class UpdateAppointmentRequest(BaseModel):
    patient_id: UUID
    doctor_id: UUID
    start_datetime: datetime
    end_datetime: datetime
    notes: Optional[str] = None