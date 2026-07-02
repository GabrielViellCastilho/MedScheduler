from datetime import datetime

from src.domain.entities.appointment import Appointment
from src.domain.exceptions import (
    RelatedEntityNotFoundError,
    ScheduleConflictError,
)
from src.domain.repositories.appointment_repository import AppointmentRepository
from src.domain.repositories.doctor_repository import DoctorRepository
from src.domain.repositories.patient_repository import PatientRepository


class CreateAppointment:

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
        patient_id,
        doctor_id,
        start_datetime: datetime,
        end_datetime: datetime,
        notes: str | None = None,
    ):
        patient = self.patient_repo.find_by_id(patient_id)

        if patient is None:
            raise RelatedEntityNotFoundError(
                f"Patient {patient_id} not found"
            )

        if not patient.active:
            raise ValueError("Patient is inactive")

        doctor = self.doctor_repo.find_by_id(doctor_id)

        if doctor is None:
            raise RelatedEntityNotFoundError(
                f"Doctor {doctor_id} not found"
            )

        if not doctor.active:
            raise ValueError("Doctor is inactive")

        if end_datetime <= start_datetime:
            raise ValueError(
                "End datetime must be after start datetime"
            )

        if self.repo.has_conflict(
            doctor_id,
            start_datetime,
            end_datetime,
        ):
            raise ScheduleConflictError(
                "Doctor already has an appointment in this period"
            )

        appointment = Appointment.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            notes=notes,
        )

        return self.repo.save(appointment)