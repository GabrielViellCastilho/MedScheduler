from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime


class UserModel(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str
    role: str

    created_at: datetime
    updated_at: datetime