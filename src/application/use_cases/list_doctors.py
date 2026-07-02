from typing import Optional
from uuid import UUID

from src.domain.repositories.doctor_repository import DoctorRepository


class ListDoctors:

    def __init__(self, repo: DoctorRepository):
        self.repo = repo

    def execute(
        self,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
        specialty_id: Optional[UUID] = None,
    ):
        items = self.repo.find_all(limit, offset, active=active, specialty_id=specialty_id)
        total = self.repo.count(active=active, specialty_id=specialty_id)
        return {"items": items, "total": total, "limit": limit, "offset": offset}
