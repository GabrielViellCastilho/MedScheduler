from uuid import UUID

from src.domain.repositories.user_repository import UserRepository


class InactivateUser:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user_id: UUID) -> bool:
        user = self.repo.find_by_id(user_id)

        if user is None:
            return False

        self.repo.inactivate(user_id)

        return True