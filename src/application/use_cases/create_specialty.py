from src.domain.entities.specialty import Specialty
from src.domain.repositories.specialty_repository import SpecialtyRepository


class CreateSpecialty:

    def __init__(self, repo: SpecialtyRepository):
        self.repo = repo

    def execute(self, name: str, description: str):
        specialty = Specialty.create(name=name, description=description)
        return self.repo.save(specialty)
