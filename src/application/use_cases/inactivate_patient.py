from uuid import UUID

from src.domain.repositories.patient_repository import PatientRepository


class InactivatePatient:

    def __init__(self, repo: PatientRepository):
        self.repo = repo

    def execute(self, patient_id: UUID) -> bool:
        patient = self.repo.find_by_id(patient_id)
        if patient is None:
            return False

        self.repo.inactivate(patient_id)
        return True
