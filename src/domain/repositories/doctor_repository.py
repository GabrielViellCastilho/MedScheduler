from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.domain.entities.doctor import Doctor


class DoctorRepository(ABC):

    @abstractmethod
    def save(self, doctor: Doctor) -> Doctor:
        pass

    @abstractmethod
    def find_by_id(self, doctor_id: UUID) -> Optional[Doctor]:
        pass

    @abstractmethod
    def find_all(
        self,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
        specialty_id: Optional[UUID] = None,
    ) -> List[Doctor]:
        pass

    @abstractmethod
    def count(self, active: Optional[bool] = None, specialty_id: Optional[UUID] = None) -> int:
        pass

    @abstractmethod
    def update(self, doctor: Doctor) -> Doctor:
        pass

    @abstractmethod
    def inactivate(self, doctor_id: UUID) -> None:
        pass
