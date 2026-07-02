from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.domain.entities.specialty import Specialty


class SpecialtyRepository(ABC):

    @abstractmethod
    def save(self, specialty: Specialty) -> Specialty:
        pass

    @abstractmethod
    def find_by_id(self, specialty_id: UUID) -> Optional[Specialty]:
        pass

    @abstractmethod
    def find_all(self, limit: int, offset: int) -> List[Specialty]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def update(self, specialty: Specialty) -> Specialty:
        pass

    @abstractmethod
    def delete(self, specialty_id: UUID) -> None:
        pass
