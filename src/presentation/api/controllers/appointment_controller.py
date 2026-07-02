from uuid import UUID

from src.application.use_cases.cancel_appointment import CancelAppointment
from src.application.use_cases.create_appointment import CreateAppointment
from src.application.use_cases.get_appointment import GetAppointment
from src.application.use_cases.list_appointments import ListAppointments
from src.application.use_cases.update_appointment import UpdateAppointment
from src.presentation.api.schemas.appointment_schemas import (
    CreateAppointmentRequest,
    UpdateAppointmentRequest,
)


class AppointmentController:

    def __init__(
        self,
        create_appointment_use_case: CreateAppointment,
        list_appointments_use_case: ListAppointments,
        get_appointment_use_case: GetAppointment,
        update_appointment_use_case: UpdateAppointment,
        cancel_appointment_use_case: CancelAppointment,
    ):
        self.create_appointment_use_case = create_appointment_use_case
        self.list_appointments_use_case = list_appointments_use_case
        self.get_appointment_use_case = get_appointment_use_case
        self.update_appointment_use_case = update_appointment_use_case
        self.cancel_appointment_use_case = cancel_appointment_use_case

    def create_appointment(self, request: CreateAppointmentRequest):
        return self.create_appointment_use_case.execute(
            patient_id=request.patient_id,
            doctor_id=request.doctor_id,
            start_datetime=request.start_datetime,
            end_datetime=request.end_datetime,
            notes=request.notes,
        )

    def list_appointments(self, limit: int, offset: int):
        return self.list_appointments_use_case.execute(
            limit=limit,
            offset=offset,
        )

    def get_appointment(self, appointment_id: UUID):
        return self.get_appointment_use_case.execute(appointment_id)

    def update_appointment(
        self,
        appointment_id: UUID,
        request: UpdateAppointmentRequest,
    ):
        return self.update_appointment_use_case.execute(
            appointment_id=appointment_id,
            patient_id=request.patient_id,
            doctor_id=request.doctor_id,
            start_datetime=request.start_datetime,
            end_datetime=request.end_datetime,
            notes=request.notes,
        )

    def cancel_appointment(self, appointment_id: UUID):
        return self.cancel_appointment_use_case.execute(appointment_id)