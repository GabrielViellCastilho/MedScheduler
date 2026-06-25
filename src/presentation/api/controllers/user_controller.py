from src.application.use_cases.create_user import CreateUser
from src.presentation.api.schemas.user_schemas import CreateUserRequest


class UserController:

    def __init__(self, create_user_use_case: CreateUser):
        self.create_user_use_case = create_user_use_case

    def create_user(self, request: CreateUserRequest):
        return self.create_user_use_case.execute(
            name=request.name,
            email=request.email,
            password=request.password,
            role=request.role,
        )