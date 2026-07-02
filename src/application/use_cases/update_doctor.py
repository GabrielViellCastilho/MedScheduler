from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from src.domain.exceptions import RelatedEntityNotFoundError
from src.domain.repositories.doctor_repository import DoctorRepository
from src.domain.repositories.specialty_repository import SpecialtyRepository
from src.domain.value_objects.crm import CRM


class UpdateDoctor:

    def __init__(self, repo: DoctorRepository, specialty_repo: SpecialtyRepository):
        self.repo = repo
        self.specialty_repo = specialty_repo

    def execute(
        self,
        doctor_id: UUID,
        name: str,
        crm: str,
        specialty_id: UUID,
        user_id: Optional[UUID] = None,
    ):
        doctor = self.repo.find_by_id(doctor_id)
        if doctor is None:
            return None

        if self.specialty_repo.find_by_id(specialty_id) is None:
            raise RelatedEntityNotFoundError(f"Specialty {specialty_id} not found")

        doctor.name = name
        doctor.crm = CRM(crm)
        doctor.specialty_id = specialty_id
        doctor.user_id = user_id
        doctor.updated_at = datetime.now(timezone.utc)

        return self.repo.update(doctor)
