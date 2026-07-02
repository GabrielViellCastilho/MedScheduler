from uuid import UUID

from src.domain.repositories.specialty_repository import SpecialtyRepository


class DeleteSpecialty:

    def __init__(self, repo: SpecialtyRepository):
        self.repo = repo

    def execute(self, specialty_id: UUID) -> bool:
        specialty = self.repo.find_by_id(specialty_id)
        if specialty is None:
            return False

        self.repo.delete(specialty_id)
        return True
