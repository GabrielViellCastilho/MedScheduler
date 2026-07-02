import logging

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.core.database import get_session
from src.application.use_cases.create_user import CreateUser
from src.infrastructure.database.repositories.user_repository_impl import UserRepositoryImpl
from src.infrastructure.auth.bcrypt_security_service import BcryptSecurityService
from src.presentation.api.controllers.user_controller import UserController
from src.presentation.api.schemas.user_schemas import CreateUserRequest

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/users", tags=["Users"])


def get_controller(session: Session = Depends(get_session)):
    repo = UserRepositoryImpl(session)
    security = BcryptSecurityService()

    use_case = CreateUser(repo, security)
    return UserController(use_case)


@router.post("/")
def create_user(
    request: CreateUserRequest,
    controller: UserController = Depends(get_controller),
):
    user = controller.create_user(request)
    logger.info("CREATE User id=%s email=%s", user.id, user.email)
    return user
