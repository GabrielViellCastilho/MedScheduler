from typing import Optional
from uuid import UUID

from src.application.use_cases.create_patient import CreatePatient
from src.application.use_cases.list_patients import ListPatients
from src.application.use_cases.get_patient import GetPatient
from src.application.use_cases.update_patient import UpdatePatient
from src.application.use_cases.inactivate_patient import InactivatePatient
from src.presentation.api.schemas.patient_schemas import (
    CreatePatientRequest,
    UpdatePatientRequest,
)


class PatientController:

    def __init__(
        self,
        create_patient_use_case: CreatePatient,
        list_patients_use_case: ListPatients,
        get_patient_use_case: GetPatient,
        update_patient_use_case: UpdatePatient,
        inactivate_patient_use_case: InactivatePatient,
    ):
        self.create_patient_use_case = create_patient_use_case
        self.list_patients_use_case = list_patients_use_case
        self.get_patient_use_case = get_patient_use_case
        self.update_patient_use_case = update_patient_use_case
        self.inactivate_patient_use_case = inactivate_patient_use_case

    def create_patient(self, request: CreatePatientRequest):
        return self.create_patient_use_case.execute(
            name=request.name,
            cpf=request.cpf,
            birth_date=request.birth_date,
            phone=request.phone,
            email=request.email,
            user_id=request.user_id,
        )

    def list_patients(self, limit: int, offset: int, active: Optional[bool] = None):
        return self.list_patients_use_case.execute(limit=limit, offset=offset, active=active)

    def get_patient(self, patient_id: UUID):
        return self.get_patient_use_case.execute(patient_id)

    def update_patient(self, patient_id: UUID, request: UpdatePatientRequest):
        return self.update_patient_use_case.execute(
            patient_id=patient_id,
            name=request.name,
            cpf=request.cpf,
            birth_date=request.birth_date,
            phone=request.phone,
            email=request.email,
            user_id=request.user_id,
        )

    def inactivate_patient(self, patient_id: UUID):
        return self.inactivate_patient_use_case.execute(patient_id)
