from typing import Optional
from uuid import UUID

from src.application.use_cases.create_doctor import CreateDoctor
from src.application.use_cases.list_doctors import ListDoctors
from src.application.use_cases.get_doctor import GetDoctor
from src.application.use_cases.update_doctor import UpdateDoctor
from src.application.use_cases.inactivate_doctor import InactivateDoctor
from src.presentation.api.schemas.doctor_schemas import (
    CreateDoctorRequest,
    UpdateDoctorRequest,
)


class DoctorController:

    def __init__(
        self,
        create_doctor_use_case: CreateDoctor,
        list_doctors_use_case: ListDoctors,
        get_doctor_use_case: GetDoctor,
        update_doctor_use_case: UpdateDoctor,
        inactivate_doctor_use_case: InactivateDoctor,
    ):
        self.create_doctor_use_case = create_doctor_use_case
        self.list_doctors_use_case = list_doctors_use_case
        self.get_doctor_use_case = get_doctor_use_case
        self.update_doctor_use_case = update_doctor_use_case
        self.inactivate_doctor_use_case = inactivate_doctor_use_case

    def create_doctor(self, request: CreateDoctorRequest):
        return self.create_doctor_use_case.execute(
            name=request.name,
            crm=request.crm,
            specialty_id=request.specialty_id,
            user_id=request.user_id,
        )

    def list_doctors(
        self,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
        specialty_id: Optional[UUID] = None,
    ):
        return self.list_doctors_use_case.execute(
            limit=limit, offset=offset, active=active, specialty_id=specialty_id
        )

    def get_doctor(self, doctor_id: UUID):
        return self.get_doctor_use_case.execute(doctor_id)

    def update_doctor(self, doctor_id: UUID, request: UpdateDoctorRequest):
        return self.update_doctor_use_case.execute(
            doctor_id=doctor_id,
            name=request.name,
            crm=request.crm,
            specialty_id=request.specialty_id,
            user_id=request.user_id,
        )

    def inactivate_doctor(self, doctor_id: UUID):
        return self.inactivate_doctor_use_case.execute(doctor_id)
