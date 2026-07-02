from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID
from datetime import date, datetime


class PatientModel(SQLModel, table=True):
    __tablename__ = "patients"

    id: UUID = Field(primary_key=True)
    user_id: Optional[UUID] = Field(default=None, foreign_key="users.id")

    name: str
    cpf: str = Field(index=True, unique=True)
    birth_date: date
    phone: str
    email: str
    active: bool = Field(default=True)

    created_at: datetime
    updated_at: datetime
