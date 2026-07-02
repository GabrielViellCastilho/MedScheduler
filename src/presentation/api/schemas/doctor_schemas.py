from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CreateDoctorRequest(BaseModel):
    user_id: Optional[UUID] = None
    name: str
    crm: str
    specialty_id: UUID


class UpdateDoctorRequest(BaseModel):
    user_id: Optional[UUID] = None
    name: str
    crm: str
    specialty_id: UUID
