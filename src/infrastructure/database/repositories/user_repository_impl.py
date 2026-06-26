from sqlmodel import Session, select
from uuid import UUID

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.infrastructure.database.models.user_model import UserModel


class UserRepositoryImpl(UserRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        model = UserModel(**user.__dict__)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return user

    def find_by_id(self, user_id: UUID):
        return self.session.exec(
            select(UserModel).where(UserModel.id == user_id)
        ).first()

    def find_by_email(self, email: str):
        return self.session.exec(
            select(UserModel).where(UserModel.email == email)
        ).first()