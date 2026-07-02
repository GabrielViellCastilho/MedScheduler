from pydantic import BaseModel


class CreateSpecialtyRequest(BaseModel):
    name: str
    description: str


class UpdateSpecialtyRequest(BaseModel):
    name: str
    description: str
