from uuid import UUID

from src.domain.repositories.specialty_repository import SpecialtyRepository


class GetSpecialty:

    def __init__(self, repo: SpecialtyRepository):
        self.repo = repo

    def execute(self, specialty_id: UUID):
        return self.repo.find_by_id(specialty_id)
