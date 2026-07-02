import logging
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from uuid import UUID
from src.core.database import get_session
from src.application.use_cases.create_appointment import CreateAppointment
from src.application.use_cases.list_appointments import ListAppointments
from src.application.use_cases.get_appointment import GetAppointment
from src.application.use_cases.update_appointment import UpdateAppointment
from src.application.use_cases.cancel_appointment import CancelAppointment

from src.infrastructure.database.repositories.appointment_repository_impl import (
    AppointmentRepositoryImpl,
)
from src.infrastructure.database.repositories.patient_repository_impl import (
    PatientRepositoryImpl,
)
from src.infrastructure.database.repositories.doctor_repository_impl import (
    DoctorRepositoryImpl,
)

from src.presentation.api.controllers.appointment_controller import (
    AppointmentController,
)

from src.presentation.api.schemas.appointment_schemas import (
    CreateAppointmentRequest,
    UpdateAppointmentRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/appointments", tags=["Appointments"])


def get_controller(session: Session = Depends(get_session)):
    appointment_repo = AppointmentRepositoryImpl(session)
    patient_repo = PatientRepositoryImpl(session)
    doctor_repo = DoctorRepositoryImpl(session)

    return AppointmentController(
        create_appointment_use_case=CreateAppointment(
            appointment_repo,
            patient_repo,
            doctor_repo,
        ),
        list_appointments_use_case=ListAppointments(
            appointment_repo,
        ),
        get_appointment_use_case=GetAppointment(
            appointment_repo,
        ),
        update_appointment_use_case=UpdateAppointment(
            appointment_repo,
        ),
        cancel_appointment_use_case=CancelAppointment(
            appointment_repo,
        ),
    )


@router.post("/")
def create_appointment(
    request: CreateAppointmentRequest,
    controller: AppointmentController = Depends(get_controller),
):
    appointment = controller.create_appointment(request)
    logger.info("CREATE Appointment id=%s", appointment.id)
    return appointment


@router.get("/")
def list_appointments(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    controller: AppointmentController = Depends(get_controller),
):
    return controller.list_appointments(
        limit=limit,
        offset=offset,
    )


@router.get("/{appointment_id}")
def get_appointment(
    appointment_id: UUID,
    controller: AppointmentController = Depends(get_controller),
):
    appointment = controller.get_appointment(appointment_id)

    if appointment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found",
        )

    return appointment


@router.put("/{appointment_id}")
def update_appointment(
    appointment_id: UUID,
    request: UpdateAppointmentRequest,
    controller: AppointmentController = Depends(get_controller),
):
    appointment = controller.update_appointment(
        appointment_id,
        request,
    )

    if appointment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found",
        )

    logger.info("UPDATE Appointment id=%s", appointment_id)

    return appointment


@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_appointment(
    appointment_id: UUID,
    controller: AppointmentController = Depends(get_controller),
):
    cancelled = controller.cancel_appointment(appointment_id)

    if not cancelled:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found",
        )

    logger.info("CANCEL Appointment id=%s", appointment_id)