from typing import Optional
from uuid import UUID

from src.domain.entities.doctor import Doctor
from src.domain.exceptions import RelatedEntityNotFoundError
from src.domain.repositories.doctor_repository import DoctorRepository
from src.domain.repositories.specialty_repository import SpecialtyRepository


class CreateDoctor:

    def __init__(self, repo: DoctorRepository, specialty_repo: SpecialtyRepository):
        self.repo = repo
        self.specialty_repo = specialty_repo

    def execute(
        self,
        name: str,
        crm: str,
        specialty_id: UUID,
        user_id: Optional[UUID] = None,
    ):
        if self.specialty_repo.find_by_id(specialty_id) is None:
            raise RelatedEntityNotFoundError(f"Specialty {specialty_id} not found")

        doctor = Doctor.create(
            name=name,
            crm=crm,
            specialty_id=specialty_id,
            user_id=user_id,
        )
        return self.repo.save(doctor)
