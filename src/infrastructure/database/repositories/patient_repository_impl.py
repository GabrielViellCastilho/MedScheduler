from typing import Optional

from sqlmodel import Session, select, func
from uuid import UUID

from src.domain.entities.patient import Patient
from src.domain.repositories.patient_repository import PatientRepository
from src.infrastructure.database.models.patient_model import PatientModel


class PatientRepositoryImpl(PatientRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, patient: Patient) -> Patient:
        model = PatientModel(
            id=patient.id,
            user_id=patient.user_id,
            name=patient.name,
            cpf=str(patient.cpf),
            birth_date=patient.birth_date,
            phone=patient.phone,
            email=patient.email,
            active=patient.active,
            created_at=patient.created_at,
            updated_at=patient.updated_at,
        )
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def find_by_id(self, patient_id: UUID):
        return self.session.exec(
            select(PatientModel).where(PatientModel.id == patient_id)
        ).first()

    def find_by_cpf(self, cpf: str):
        return self.session.exec(
            select(PatientModel).where(PatientModel.cpf == cpf)
        ).first()

    def find_all(self, limit: int, offset: int, active: Optional[bool] = None):
        statement = select(PatientModel)
        if active is not None:
            statement = statement.where(PatientModel.active == active)
        return self.session.exec(statement.offset(offset).limit(limit)).all()

    def count(self, active: Optional[bool] = None) -> int:
        statement = select(func.count()).select_from(PatientModel)
        if active is not None:
            statement = statement.where(PatientModel.active == active)
        return self.session.exec(statement).one()

    def update(self, patient: Patient) -> Patient:
        model = self.session.get(PatientModel, patient.id)
        model.user_id = patient.user_id
        model.name = patient.name
        model.cpf = str(patient.cpf)
        model.birth_date = patient.birth_date
        model.phone = patient.phone
        model.email = patient.email
        model.updated_at = patient.updated_at
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def inactivate(self, patient_id: UUID) -> None:
        model = self.session.get(PatientModel, patient_id)
        model.active = False
        self.session.add(model)
        self.session.commit()
