from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, user_id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_all(self, limit: int, offset: int, active: Optional[bool] = None) -> List[User]:
        pass

    @abstractmethod
    def count(self, active: Optional[bool] = None) -> int:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def inactivate(self, user_id: UUID) -> None:
        pass