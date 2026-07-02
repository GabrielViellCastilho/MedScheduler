from datetime import datetime, timezone
from uuid import UUID

from src.domain.entities.appointment import AppointmentStatus
from src.domain.repositories.appointment_repository import AppointmentRepository


class CancelAppointment:

    def __init__(self, repo: AppointmentRepository):
        self.repo = repo

    def execute(self, appointment_id: UUID) -> bool:
        appointment = self.repo.find_by_id(appointment_id)

        if appointment is None:
            return False

        appointment.status = AppointmentStatus.CANCELLED
        appointment.cancelled_at = datetime.now(timezone.utc)
        appointment.updated_at = datetime.now(timezone.utc)

        self.repo.update(appointment)

        return True