from sqlmodel import Session, func, select
from typing import Optional
from uuid import UUID

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.database.models.user_model import UserModel


class UserRepositoryImpl(UserRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            role=user.role,
            active=user.active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def find_by_id(self, user_id: UUID):
        return self.session.exec(
            select(UserModel).where(UserModel.id == user_id)
        ).first()

    def find_by_email(self, email: str):
        return self.session.exec(
            select(UserModel).where(UserModel.email == email)
        ).first()

    def find_all(self, limit: int, offset: int, active: Optional[bool] = None):
        statement = select(UserModel)

        if active is not None:
            statement = statement.where(UserModel.active == active)

        return self.session.exec(
            statement.offset(offset).limit(limit)
        ).all()

    def count(self, active: Optional[bool] = None) -> int:
        statement = select(func.count()).select_from(UserModel)

        if active is not None:
            statement = statement.where(UserModel.active == active)

        return self.session.exec(statement).one()

    def update(self, user: User):
        model = self.session.get(UserModel, user.id)

        model.name = user.name
        model.email = user.email
        model.password = user.password
        model.role = user.role
        model.active = user.active
        model.updated_at = user.updated_at

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return model

    def inactivate(self, user_id: UUID):
        model = self.session.get(UserModel, user_id)

        model.active = False

        self.session.add(model)
        self.session.commit()