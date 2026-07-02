from typing import Optional

from sqlmodel import Session, select, func
from uuid import UUID

from src.domain.entities.doctor import Doctor
from src.domain.repositories.doctor_repository import DoctorRepository
from src.infrastructure.database.models.doctor_model import DoctorModel


class DoctorRepositoryImpl(DoctorRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, doctor: Doctor) -> Doctor:
        model = DoctorModel(
            id=doctor.id,
            user_id=doctor.user_id,
            name=doctor.name,
            crm=str(doctor.crm),
            specialty_id=doctor.specialty_id,
            active=doctor.active,
            created_at=doctor.created_at,
            updated_at=doctor.updated_at,
        )
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def find_by_id(self, doctor_id: UUID):
        return self.session.exec(
            select(DoctorModel).where(DoctorModel.id == doctor_id)
        ).first()

    def find_all(
        self,
        limit: int,
        offset: int,
        active: Optional[bool] = None,
        specialty_id: Optional[UUID] = None,
    ):
        statement = select(DoctorModel)
        if active is not None:
            statement = statement.where(DoctorModel.active == active)
        if specialty_id is not None:
            statement = statement.where(DoctorModel.specialty_id == specialty_id)
        return self.session.exec(statement.offset(offset).limit(limit)).all()

    def count(self, active: Optional[bool] = None, specialty_id: Optional[UUID] = None) -> int:
        statement = select(func.count()).select_from(DoctorModel)
        if active is not None:
            statement = statement.where(DoctorModel.active == active)
        if specialty_id is not None:
            statement = statement.where(DoctorModel.specialty_id == specialty_id)
        return self.session.exec(statement).one()

    def update(self, doctor: Doctor) -> Doctor:
        model = self.session.get(DoctorModel, doctor.id)
        model.user_id = doctor.user_id
        model.name = doctor.name
        model.crm = str(doctor.crm)
        model.specialty_id = doctor.specialty_id
        model.updated_at = doctor.updated_at
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def inactivate(self, doctor_id: UUID) -> None:
        model = self.session.get(DoctorModel, doctor_id)
        model.active = False
        self.session.add(model)
        self.session.commit()
