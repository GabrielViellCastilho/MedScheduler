from uuid import UUID

from src.domain.repositories.doctor_repository import DoctorRepository


class GetDoctor:

    def __init__(self, repo: DoctorRepository):
        self.repo = repo

    def execute(self, doctor_id: UUID):
        return self.repo.find_by_id(doctor_id)
