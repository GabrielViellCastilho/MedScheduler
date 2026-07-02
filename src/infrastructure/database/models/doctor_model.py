from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class DoctorModel(SQLModel, table=True):
    __tablename__ = "doctors"

    id: UUID = Field(primary_key=True)
    user_id: Optional[UUID] = Field(default=None, foreign_key="users.id")

    name: str
    crm: str
    specialty_id: UUID = Field(foreign_key="specialties.id")
    active: bool = Field(default=True)

    created_at: datetime
    updated_at: datetime
