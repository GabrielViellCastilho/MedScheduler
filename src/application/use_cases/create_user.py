from src.domain.entities.user import User, UserRole
from src.domain.exceptions import EntityAlreadyExistsError
from src.domain.repositories.user_repository import UserRepository
from src.domain.services.security_service import SecurityService


class CreateUser:

    def __init__(self, repo: UserRepository, security: SecurityService):
        self.repo = repo
        self.security = security

    def execute(self, name: str, email: str, password: str, role: str):

        if self.repo.find_by_email(email) is not None:
            raise EntityAlreadyExistsError(f"User with email {email} already exists")

        hashed_password = self.security.hash_password(password)

        user = User.create(
            name=name,
            email=email,
            password=hashed_password,
            role=UserRole(role),
        )

        return self.repo.save(user)