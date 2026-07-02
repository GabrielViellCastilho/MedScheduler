from datetime import datetime, timezone
from uuid import UUID

from src.domain.repositories.specialty_repository import SpecialtyRepository


class UpdateSpecialty:

    def __init__(self, repo: SpecialtyRepository):
        self.repo = repo

    def execute(self, specialty_id: UUID, name: str, description: str):
        specialty = self.repo.find_by_id(specialty_id)
        if specialty is None:
            return None

        specialty.name = name
        specialty.description = description
        specialty.updated_at = datetime.now(timezone.utc)

        return self.repo.update(specialty)
