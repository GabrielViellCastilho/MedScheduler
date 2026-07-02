from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from src.domain.entities.patient import Patient


class PatientRepository(ABC):

    @abstractmethod
    def save(self, patient: Patient) -> Patient:
        pass

    @abstractmethod
    def find_by_id(self, patient_id: UUID) -> Optional[Patient]:
        pass

    @abstractmethod
    def find_by_cpf(self, cpf: str) -> Optional[Patient]:
        pass

    @abstractmethod
    def find_all(self, limit: int, offset: int, active: Optional[bool] = None) -> List[Patient]:
        pass

    @abstractmethod
    def count(self, active: Optional[bool] = None) -> int:
        pass

    @abstractmethod
    def update(self, patient: Patient) -> Patient:
        pass

    @abstractmethod
    def inactivate(self, patient_id: UUID) -> None:
        pass
