from datetime import date
from typing import Optional
from uuid import UUID

from src.domain.entities.patient import Patient
from src.domain.exceptions import EntityAlreadyExistsError
from src.domain.repositories.patient_repository import PatientRepository
from src.domain.value_objects.cpf import CPF


class CreatePatient:

    def __init__(self, repo: PatientRepository):
        self.repo = repo

    def execute(
        self,
        name: str,
        cpf: str,
        birth_date: date,
        phone: str,
        email: str,
        user_id: Optional[UUID] = None,
    ):
        cpf_vo = CPF(cpf)

        if self.repo.find_by_cpf(str(cpf_vo)) is not None:
            raise EntityAlreadyExistsError(f"Patient with CPF {cpf_vo} already exists")

        patient = Patient.create(
            name=name,
            cpf=str(cpf_vo),
            birth_date=birth_date,
            phone=phone,
            email=email,
            user_id=user_id,
        )
        return self.repo.save(patient)
