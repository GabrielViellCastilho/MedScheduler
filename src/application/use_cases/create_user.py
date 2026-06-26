from src.domain.entities.user import User, UserRole
from src.domain.repositories.user_repository import UserRepository
from src.domain.services.security_service import SecurityService


class CreateUser:

    def __init__(self, repo: UserRepository, security: SecurityService):
        self.repo = repo
        self.security = security

    def execute(self, name: str, email: str, password: str, role: str):

        hashed_password = self.security.hash_password(password)

        user = User.create(
            name=name,
            email=email,
            password=hashed_password,
            role=UserRole(role),
        )

        return self.repo.save(user)