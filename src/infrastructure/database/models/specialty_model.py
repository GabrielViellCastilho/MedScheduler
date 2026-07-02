from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime


class SpecialtyModel(SQLModel, table=True):
    __tablename__ = "specialties"

    id: UUID = Field(primary_key=True)
    name: str
    description: str

    created_at: datetime
    updated_at: datetime
