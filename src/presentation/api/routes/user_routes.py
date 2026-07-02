import logging
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from src.application.use_cases.create_user import CreateUser
from src.application.use_cases.get_user import GetUser
from src.application.use_cases.inactivate_user import InactivateUser
from src.application.use_cases.list_users import ListUsers
from src.application.use_cases.update_user import UpdateUser
from src.core.database import get_session
from src.infrastructure.auth.bcrypt_security_service import BcryptSecurityService
from src.infrastructure.database.repositories.user_repository_impl import UserRepositoryImpl
from src.presentation.api.controllers.user_controller import UserController
from src.presentation.api.schemas.user_schemas import ( CreateUserRequest, UpdateUserRequest, )

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/users", tags=["Users"])


def get_controller(session: Session = Depends(get_session)):
    repo = UserRepositoryImpl(session)
    security = BcryptSecurityService()

    return UserController(
        create_user_use_case=CreateUser(repo, security),
        list_users_use_case=ListUsers(repo),
        get_user_use_case=GetUser(repo),
        update_user_use_case=UpdateUser(repo, security),
        inactivate_user_use_case=InactivateUser(repo),
    )


@router.post("/")
def create_user(
    request: CreateUserRequest,
    controller: UserController = Depends(get_controller),
):
    user = controller.create_user(request)
    logger.info("CREATE User id=%s email=%s", user.id, user.email)
    return user


@router.get("/")
def list_users(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    active: bool | None = Query(None),
    controller: UserController = Depends(get_controller),
):
    return controller.list_users(
        limit=limit,
        offset=offset,
        active=active,
    )


@router.get("/{user_id}")
def get_user(
    user_id: UUID,
    controller: UserController = Depends(get_controller),
):
    user = controller.get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.put("/{user_id}")
def update_user(
    user_id: UUID,
    request: UpdateUserRequest,
    controller: UserController = Depends(get_controller),
):
    user = controller.update_user(user_id, request)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    logger.info("UPDATE User id=%s", user_id)
    return user


@router.patch("/{user_id}/inactivate", status_code=status.HTTP_204_NO_CONTENT)
def inactivate_user(
    user_id: UUID,
    controller: UserController = Depends(get_controller),
):
    deleted = controller.inactivate_user(user_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    logger.info("INACTIVATE User id=%s", user_id)