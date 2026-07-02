from datetime import datetime, timezone
from uuid import UUID

from src.domain.exceptions import (
    RelatedEntityNotFoundError,
    ScheduleConflictError,
)
from src.domain.repositories.appointment_repository import AppointmentRepository
from src.domain.repositories.doctor_repository import DoctorRepository
from src.domain.repositories.patient_repository import PatientRepository


class UpdateAppointment:

    def __init__(
        self,
        repo: AppointmentRepository,
        doctor_repo: DoctorRepository,
        patient_repo: PatientRepository,
    ):
        self.repo = repo
        self.doctor_repo = doctor_repo
        self.patient_repo = patient_repo

    def execute(
        self,
        appointment_id: UUID,
        patient_id: UUID,
        doctor_id: UUID,
        start_datetime: datetime,
        end_datetime: datetime,
        notes: str | None = None,
    ):
        appointment = self.repo.find_by_id(appointment_id)

        if appointment is None:
            return None

        patient = self.patient_repo.find_by_id(patient_id)
        if patient is None:
            raise RelatedEntityNotFoundError(f"Patient {patient_id} not found")

        if not patient.active:
            raise ValueError("Patient is inactive")

        doctor = self.doctor_repo.find_by_id(doctor_id)
        if doctor is None:
            raise RelatedEntityNotFoundError(f"Doctor {doctor_id} not found")

        if not doctor.active:
            raise ValueError("Doctor is inactive")

        if end_datetime <= start_datetime:
            raise ValueError("End datetime must be after start datetime")

        if self.repo.has_conflict(
            doctor_id=doctor_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            exclude_appointment_id=appointment.id,
        ):
            raise ScheduleConflictError(
                "Doctor already has an appointment in this period"
            )

        appointment.patient_id = patient_id
        appointment.doctor_id = doctor_id
        appointment.start_datetime = start_datetime
        appointment.end_datetime = end_datetime
        appointment.notes = notes
        appointment.updated_at = datetime.now(timezone.utc)

        return self.repo.update(appointment)