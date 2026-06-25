from sqlmodel import Session

from src.application.use_cases.create_user import CreateUser
from src.infrastructure.database.repositories.user_repository_impl import UserRepositoryImpl
from src.infrastructure.auth.bcrypt_security_service import BcryptSecurityService
from src.presentation.api.controllers.user_controller import UserController


def get_user_controller(session: Session):
    repo = UserRepositoryImpl(session)
    security = BcryptSecurityService()

    use_case = CreateUser(
        repo,
        security
    )

    return UserController(use_case)