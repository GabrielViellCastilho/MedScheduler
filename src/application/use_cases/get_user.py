from uuid import UUID

from src.domain.repositories.user_repository import UserRepository


class GetUser:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user_id: UUID):
        return self.repo.find_by_id(user_id)