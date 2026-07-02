import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from uuid import UUID

from src.core.database import get_session
from src.application.use_cases.create_doctor import CreateDoctor
from src.application.use_cases.list_doctors import ListDoctors
from src.application.use_cases.get_doctor import GetDoctor
from src.application.use_cases.update_doctor import UpdateDoctor
from src.application.use_cases.inactivate_doctor import InactivateDoctor
from src.infrastructure.database.repositories.doctor_repository_impl import (
    DoctorRepositoryImpl,
)
from src.infrastructure.database.repositories.specialty_repository_impl import (
    SpecialtyRepositoryImpl,
)
from src.presentation.api.controllers.doctor_controller import DoctorController
from src.presentation.api.schemas.doctor_schemas import (
    CreateDoctorRequest,
    UpdateDoctorRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/doctors", tags=["Doctors"])


def get_controller(session: Session = Depends(get_session)):
    repo = DoctorRepositoryImpl(session)
    specialty_repo = SpecialtyRepositoryImpl(session)

    return DoctorController(
        create_doctor_use_case=CreateDoctor(repo, specialty_repo),
        list_doctors_use_case=ListDoctors(repo),
        get_doctor_use_case=GetDoctor(repo),
        update_doctor_use_case=UpdateDoctor(repo, specialty_repo),
        inactivate_doctor_use_case=InactivateDoctor(repo),
    )


@router.post("/")
def create_doctor(
    request: CreateDoctorRequest,
    controller: DoctorController = Depends(get_controller),
):
    doctor = controller.create_doctor(request)
    logger.info("CREATE Doctor id=%s", doctor.id)
    return doctor


@router.get("/")
def list_doctors(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    active: Optional[bool] = Query(None, description="Filtra por médicos ativos (true) ou inativos (false)"),
    specialty_id: Optional[UUID] = Query(None, description="Filtra médicos por especialidade"),
    controller: DoctorController = Depends(get_controller),
):
    return controller.list_doctors(limit=limit, offset=offset, active=active, specialty_id=specialty_id)


@router.get("/{doctor_id}")
def get_doctor(
    doctor_id: UUID,
    controller: DoctorController = Depends(get_controller),
):
    doctor = controller.get_doctor(doctor_id)
    if doctor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    return doctor


@router.put("/{doctor_id}")
def update_doctor(
    doctor_id: UUID,
    request: UpdateDoctorRequest,
    controller: DoctorController = Depends(get_controller),
):
    doctor = controller.update_doctor(doctor_id, request)
    if doctor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    logger.info("UPDATE Doctor id=%s", doctor_id)
    return doctor


@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def inactivate_doctor(
    doctor_id: UUID,
    controller: DoctorController = Depends(get_controller),
):
    inactivated = controller.inactivate_doctor(doctor_id)
    if not inactivated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Doctor not found")
    logger.info("INACTIVATE Doctor id=%s", doctor_id)
