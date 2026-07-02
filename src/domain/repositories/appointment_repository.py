from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from src.domain.entities.appointment import Appointment


class AppointmentRepository(ABC):

    @abstractmethod
    def save(self, appointment: Appointment) -> Appointment:
        pass

    @abstractmethod
    def find_by_id(self, appointment_id: UUID) -> Optional[Appointment]:
        pass

    @abstractmethod
    def find_all(
        self,
        limit: int,
        offset: int,
        doctor_id: Optional[UUID] = None,
        patient_id: Optional[UUID] = None,
        status: Optional[str] = None,
    ) -> List[Appointment]:
        pass

    @abstractmethod
    def count(
        self,
        doctor_id: Optional[UUID] = None,
        patient_id: Optional[UUID] = None,
        status: Optional[str] = None,
    ) -> int:
        pass

    @abstractmethod
    def update(self, appointment: Appointment) -> Appointment:
        pass

    @abstractmethod
    def has_conflict(
        self,
        doctor_id: UUID,
        start_datetime: datetime,
        end_datetime: datetime,
        exclude_appointment_id: UUID | None = None,
    ) -> bool:
        pass