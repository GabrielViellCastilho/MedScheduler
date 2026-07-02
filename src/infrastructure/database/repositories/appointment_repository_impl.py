from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Session, func, select

from src.domain.entities.appointment import Appointment
from src.domain.repositories.appointment_repository import AppointmentRepository
from src.infrastructure.database.models.appointment_model import AppointmentModel


class AppointmentRepositoryImpl(AppointmentRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, appointment: Appointment) -> Appointment:
        model = AppointmentModel(
            id=appointment.id,
            patient_id=appointment.patient_id,
            doctor_id=appointment.doctor_id,
            start_datetime=appointment.start_datetime,
            end_datetime=appointment.end_datetime,
            status=appointment.status,
            confirmation_status=appointment.confirmation_status,
            notes=appointment.notes,
            reminder_sent_at=appointment.reminder_sent_at,
            confirmed_at=appointment.confirmed_at,
            cancelled_at=appointment.cancelled_at,
            no_show_at=appointment.no_show_at,
            created_at=appointment.created_at,
            updated_at=appointment.updated_at,
        )

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return model

    def find_by_id(self, appointment_id: UUID):
        return self.session.exec(
            select(AppointmentModel).where(
                AppointmentModel.id == appointment_id
            )
        ).first()

    def find_all(
        self,
        limit: int,
        offset: int,
        doctor_id: Optional[UUID] = None,
        patient_id: Optional[UUID] = None,
        status: Optional[str] = None,
    ):
        statement = select(AppointmentModel)

        if doctor_id is not None:
            statement = statement.where(
                AppointmentModel.doctor_id == doctor_id
            )

        if patient_id is not None:
            statement = statement.where(
                AppointmentModel.patient_id == patient_id
            )

        if status is not None:
            statement = statement.where(
                AppointmentModel.status == status
            )

        return self.session.exec(
            statement.offset(offset).limit(limit)
        ).all()

    def count(
        self,
        doctor_id: Optional[UUID] = None,
        patient_id: Optional[UUID] = None,
        status: Optional[str] = None,
    ) -> int:
        statement = select(func.count()).select_from(AppointmentModel)

        if doctor_id is not None:
            statement = statement.where(
                AppointmentModel.doctor_id == doctor_id
            )

        if patient_id is not None:
            statement = statement.where(
                AppointmentModel.patient_id == patient_id
            )

        if status is not None:
            statement = statement.where(
                AppointmentModel.status == status
            )

        return self.session.exec(statement).one()

    def update(self, appointment: Appointment):
        model = self.session.get(AppointmentModel, appointment.id)

        model.patient_id = appointment.patient_id
        model.doctor_id = appointment.doctor_id
        model.start_datetime = appointment.start_datetime
        model.end_datetime = appointment.end_datetime
        model.status = appointment.status
        model.confirmation_status = appointment.confirmation_status
        model.notes = appointment.notes
        model.reminder_sent_at = appointment.reminder_sent_at
        model.confirmed_at = appointment.confirmed_at
        model.cancelled_at = appointment.cancelled_at
        model.no_show_at = appointment.no_show_at
        model.updated_at = appointment.updated_at

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return model
    
    def has_conflict(
        self,
        doctor_id: UUID,
        start_datetime: datetime,
        end_datetime: datetime,
        exclude_appointment_id: UUID | None = None,
    ) -> bool:

        statement = (
            select(AppointmentModel)
            .where(AppointmentModel.doctor_id == doctor_id)
            .where(AppointmentModel.start_datetime < end_datetime)
            .where(AppointmentModel.end_datetime > start_datetime)
        )

        if exclude_appointment_id is not None:
            statement = statement.where(
                AppointmentModel.id != exclude_appointment_id
            )

        return self.session.exec(statement).first() is not None