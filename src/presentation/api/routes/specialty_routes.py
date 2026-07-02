import logging

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from uuid import UUID

from src.core.database import get_session
from src.application.use_cases.create_specialty import CreateSpecialty
from src.application.use_cases.list_specialties import ListSpecialties
from src.application.use_cases.get_specialty import GetSpecialty
from src.application.use_cases.update_specialty import UpdateSpecialty
from src.application.use_cases.delete_specialty import DeleteSpecialty
from src.infrastructure.database.repositories.specialty_repository_impl import (
    SpecialtyRepositoryImpl,
)
from src.presentation.api.controllers.specialty_controller import SpecialtyController
from src.presentation.api.schemas.specialty_schemas import (
    CreateSpecialtyRequest,
    UpdateSpecialtyRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/specialties", tags=["Specialties"])


def get_controller(session: Session = Depends(get_session)):
    repo = SpecialtyRepositoryImpl(session)

    return SpecialtyController(
        create_specialty_use_case=CreateSpecialty(repo),
        list_specialties_use_case=ListSpecialties(repo),
        get_specialty_use_case=GetSpecialty(repo),
        update_specialty_use_case=UpdateSpecialty(repo),
        delete_specialty_use_case=DeleteSpecialty(repo),
    )


@router.post("/")
def create_specialty(
    request: CreateSpecialtyRequest,
    controller: SpecialtyController = Depends(get_controller),
):
    specialty = controller.create_specialty(request)
    logger.info("CREATE Specialty id=%s name=%s", specialty.id, specialty.name)
    return specialty


@router.get("/")
def list_specialties(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    controller: SpecialtyController = Depends(get_controller),
):
    return controller.list_specialties(limit=limit, offset=offset)


@router.get("/{specialty_id}")
def get_specialty(
    specialty_id: UUID,
    controller: SpecialtyController = Depends(get_controller),
):
    specialty = controller.get_specialty(specialty_id)
    if specialty is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialty not found")
    return specialty


@router.put("/{specialty_id}")
def update_specialty(
    specialty_id: UUID,
    request: UpdateSpecialtyRequest,
    controller: SpecialtyController = Depends(get_controller),
):
    specialty = controller.update_specialty(specialty_id, request)
    if specialty is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialty not found")
    logger.info("UPDATE Specialty id=%s", specialty_id)
    return specialty


@router.delete("/{specialty_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_specialty(
    specialty_id: UUID,
    controller: SpecialtyController = Depends(get_controller),
):
    deleted = controller.delete_specialty(specialty_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Specialty not found")
    logger.info("DELETE Specialty id=%s", specialty_id)
