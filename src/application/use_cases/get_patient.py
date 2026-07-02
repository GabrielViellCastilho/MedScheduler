from uuid import UUID

from src.domain.repositories.patient_repository import PatientRepository


class GetPatient:

    def __init__(self, repo: PatientRepository):
        self.repo = repo

    def execute(self, patient_id: UUID):
        return self.repo.find_by_id(patient_id)
