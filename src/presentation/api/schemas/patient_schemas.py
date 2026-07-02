from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CreatePatientRequest(BaseModel):
    user_id: Optional[UUID] = None
    name: str
    cpf: str
    birth_date: date
    phone: str
    email: str


class UpdatePatientRequest(BaseModel):
    user_id: Optional[UUID] = None
    name: str
    cpf: str
    birth_date: date
    phone: str
    email: str
