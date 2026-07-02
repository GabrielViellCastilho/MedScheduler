from uuid import UUID

from src.application.use_cases.create_specialty import CreateSpecialty
from src.application.use_cases.list_specialties import ListSpecialties
from src.application.use_cases.get_specialty import GetSpecialty
from src.application.use_cases.update_specialty import UpdateSpecialty
from src.application.use_cases.delete_specialty import DeleteSpecialty
from src.presentation.api.schemas.specialty_schemas import (
    CreateSpecialtyRequest,
    UpdateSpecialtyRequest,
)


class SpecialtyController:

    def __init__(
        self,
        create_specialty_use_case: CreateSpecialty,
        list_specialties_use_case: ListSpecialties,
        get_specialty_use_case: GetSpecialty,
        update_specialty_use_case: UpdateSpecialty,
        delete_specialty_use_case: DeleteSpecialty,
    ):
        self.create_specialty_use_case = create_specialty_use_case
        self.list_specialties_use_case = list_specialties_use_case
        self.get_specialty_use_case = get_specialty_use_case
        self.update_specialty_use_case = update_specialty_use_case
        self.delete_specialty_use_case = delete_specialty_use_case

    def create_specialty(self, request: CreateSpecialtyRequest):
        return self.create_specialty_use_case.execute(
            name=request.name,
            description=request.description,
        )

    def list_specialties(self, limit: int, offset: int):
        return self.list_specialties_use_case.execute(limit=limit, offset=offset)

    def get_specialty(self, specialty_id: UUID):
        return self.get_specialty_use_case.execute(specialty_id)

    def update_specialty(self, specialty_id: UUID, request: UpdateSpecialtyRequest):
        return self.update_specialty_use_case.execute(
            specialty_id=specialty_id,
            name=request.name,
            description=request.description,
        )

    def delete_specialty(self, specialty_id: UUID):
        return self.delete_specialty_use_case.execute(specialty_id)
