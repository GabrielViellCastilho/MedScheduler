from typing import Optional
from uuid import UUID

from src.domain.repositories.appointment_repository import AppointmentRepository


class ListAppointments:

    def __init__(self, repo: AppointmentRepository):
        self.repo = repo

    def execute(
        self,
        limit: int,
        offset: int,
        doctor_id: Optional[UUID] = None,
        patient_id: Optional[UUID] = None,
        status: Optional[str] = None,
    ):
        items = self.repo.find_all(
            limit=limit,
            offset=offset,
            doctor_id=doctor_id,
            patient_id=patient_id,
            status=status,
        )

        total = self.repo.count(
            doctor_id=doctor_id,
            patient_id=patient_id,
            status=status,
        )

        return {
            "items": items,
            "total": total,
            "limit": limit,
            "offset": offset,
        }