from datetime import datetime, timezone
from uuid import UUID

from src.domain.entities.user import UserRole
from src.domain.repositories.user_repository import UserRepository
from src.domain.services.security_service import SecurityService


class UpdateUser:

    def __init__(
        self,
        repo: UserRepository,
        security: SecurityService,
    ):
        self.repo = repo
        self.security = security

    def execute(
        self,
        user_id: UUID,
        name: str,
        email: str,
        password: str | None,
        role: str,
    ):
        user = self.repo.find_by_id(user_id)

        if user is None:
            return None

        existing = self.repo.find_by_email(email)
        if existing is not None and existing.id != user_id:
            raise ValueError(f"User with email {email} already exists")

        user.name = name
        user.email = email
        user.role = UserRole(role)

        if password:
            user.password = self.security.hash_password(password)

        user.updated_at = datetime.now(timezone.utc)

        return self.repo.update(user)