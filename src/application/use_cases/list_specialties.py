from src.domain.repositories.specialty_repository import SpecialtyRepository


class ListSpecialties:

    def __init__(self, repo: SpecialtyRepository):
        self.repo = repo

    def execute(self, limit: int, offset: int):
        items = self.repo.find_all(limit, offset)
        total = self.repo.count()
        return {"items": items, "total": total, "limit": limit, "offset": offset}
