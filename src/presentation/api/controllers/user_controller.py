from uuid import UUID
from src.application.use_cases.create_user import CreateUser
from src.application.use_cases.get_user import GetUser
from src.application.use_cases.inactivate_user import InactivateUser
from src.application.use_cases.list_users import ListUsers
from src.application.use_cases.update_user import UpdateUser
from src.presentation.api.schemas.user_schemas import ( CreateUserRequest, UpdateUserRequest )


class UserController:

    def __init__(
        self,
        create_user_use_case: CreateUser,
        list_users_use_case: ListUsers,
        get_user_use_case: GetUser,
        update_user_use_case: UpdateUser,
        inactivate_user_use_case: InactivateUser,
    ):
        self.create_user_use_case = create_user_use_case
        self.list_users_use_case = list_users_use_case
        self.get_user_use_case = get_user_use_case
        self.update_user_use_case = update_user_use_case
        self.inactivate_user_use_case = inactivate_user_use_case

    def create_user(self, request: CreateUserRequest):
        return self.create_user_use_case.execute(
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
        )

    def list_users(self, limit: int, offset: int, active: bool | None = None):
        return self.list_users_use_case.execute(
            limit=limit,
            offset=offset,
            active=active,
        )

    def get_user(self, user_id: UUID):
        return self.get_user_use_case.execute(user_id)

    def update_user(self, user_id: UUID, request: UpdateUserRequest):
        return self.update_user_use_case.execute(
            user_id=user_id,
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
        )

    def inactivate_user(self, user_id: UUID):
        return self.inactivate_user_use_case.execute(user_id)