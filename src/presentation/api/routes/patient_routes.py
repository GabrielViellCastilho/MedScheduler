import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from uuid import UUID

from src.core.database import get_session
from src.application.use_cases.create_patient import CreatePatient
from src.application.use_cases.list_patients import ListPatients
from src.application.use_cases.get_patient import GetPatient
from src.application.use_cases.update_patient import UpdatePatient
from src.application.use_cases.inactivate_patient import InactivatePatient
from src.infrastructure.database.repositories.patient_repository_impl import (
    PatientRepositoryImpl,
)
from src.presentation.api.controllers.patient_controller import PatientController
from src.presentation.api.schemas.patient_schemas import (
    CreatePatientRequest,
    UpdatePatientRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/patients", tags=["Patients"])


def get_controller(session: Session = Depends(get_session)):
    repo = PatientRepositoryImpl(session)

    return PatientController(
        create_patient_use_case=CreatePatient(repo),
        list_patients_use_case=ListPatients(repo),
        get_patient_use_case=GetPatient(repo),
        update_patient_use_case=UpdatePatient(repo),
        inactivate_patient_use_case=InactivatePatient(repo),
    )


@router.post("/")
def create_patient(
    request: CreatePatientRequest,
    controller: PatientController = Depends(get_controller),
):
    patient = controller.create_patient(request)
    logger.info("CREATE Patient id=%s", patient.id)
    return patient


@router.get("/")
def list_patients(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    active: Optional[bool] = Query(None, description="Filtra por pacientes ativos (true) ou inativos (false)"),
    controller: PatientController = Depends(get_controller),
):
    return controller.list_patients(limit=limit, offset=offset, active=active)


@router.get("/{patient_id}")
def get_patient(
    patient_id: UUID,
    controller: PatientController = Depends(get_controller),
):
    patient = controller.get_patient(patient_id)
    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    return patient


@router.put("/{patient_id}")
def update_patient(
    patient_id: UUID,
    request: UpdatePatientRequest,
    controller: PatientController = Depends(get_controller),
):
    patient = controller.update_patient(patient_id, request)
    if patient is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    logger.info("UPDATE Patient id=%s", patient_id)
    return patient


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def inactivate_patient(
    patient_id: UUID,
    controller: PatientController = Depends(get_controller),
):
    inactivated = controller.inactivate_patient(patient_id)
    if not inactivated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient not found")
    logger.info("INACTIVATE Patient id=%s", patient_id)
