from uuid import UUID

from src.domain.repositories.doctor_repository import DoctorRepository


class InactivateDoctor:

    def __init__(self, repo: DoctorRepository):
        self.repo = repo

    def execute(self, doctor_id: UUID) -> bool:
        doctor = self.repo.find_by_id(doctor_id)
        if doctor is None:
            return False

        self.repo.inactivate(doctor_id)
        return True
