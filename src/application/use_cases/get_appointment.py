from uuid import UUID

from src.domain.repositories.appointment_repository import AppointmentRepository


class GetAppointment:

    def __init__(self, repo: AppointmentRepository):
        self.repo = repo

    def execute(self, appointment_id: UUID):
        return self.repo.find_by_id(appointment_id)