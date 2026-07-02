from typing import Optional

from src.domain.repositories.user_repository import UserRepository


class ListUsers:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(
        self,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
    ):
        items = self.repo.find_all(limit, offset, active=active)
        total = self.repo.count(active=active)

        return {
            "items": items,
            "total": total,
            "limit": limit,
            "offset": offset,
        }