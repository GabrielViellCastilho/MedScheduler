from datetime import date, datetime, timezone
from typing import Optional
from uuid import UUID

from src.domain.exceptions import EntityAlreadyExistsError
from src.domain.repositories.patient_repository import PatientRepository
from src.domain.value_objects.cpf import CPF


class UpdatePatient:

    def __init__(self, repo: PatientRepository):
        self.repo = repo

    def execute(
        self,
        patient_id: UUID,
        name: str,
        cpf: str,
        birth_date: date,
        phone: str,
        email: str,
        user_id: Optional[UUID] = None,
    ):
        patient = self.repo.find_by_id(patient_id)
        if patient is None:
            return None

        cpf_vo = CPF(cpf)
        existing = self.repo.find_by_cpf(str(cpf_vo))
        if existing is not None and existing.id != patient_id:
            raise EntityAlreadyExistsError(f"Patient with CPF {cpf_vo} already exists")

        patient.name = name
        patient.cpf = cpf_vo
        patient.birth_date = birth_date
        patient.phone = phone
        patient.email = email
        patient.user_id = user_id
        patient.updated_at = datetime.now(timezone.utc)

        return self.repo.update(patient)
