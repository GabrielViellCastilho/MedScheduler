from sqlmodel import Session, select, func
from uuid import UUID

from src.domain.entities.specialty import Specialty
from src.domain.repositories.specialty_repository import SpecialtyRepository
from src.infrastructure.database.models.specialty_model import SpecialtyModel


class SpecialtyRepositoryImpl(SpecialtyRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, specialty: Specialty) -> Specialty:
        model = SpecialtyModel(**specialty.__dict__)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return specialty

    def find_by_id(self, specialty_id: UUID):
        return self.session.exec(
            select(SpecialtyModel).where(SpecialtyModel.id == specialty_id)
        ).first()

    def find_all(self, limit: int, offset: int):
        return self.session.exec(
            select(SpecialtyModel).offset(offset).limit(limit)
        ).all()

    def count(self) -> int:
        return self.session.exec(
            select(func.count()).select_from(SpecialtyModel)
        ).one()

    def update(self, specialty: Specialty) -> Specialty:
        model = self.session.get(SpecialtyModel, specialty.id)
        model.name = specialty.name
        model.description = specialty.description
        model.updated_at = specialty.updated_at
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return specialty

    def delete(self, specialty_id: UUID) -> None:
        model = self.session.get(SpecialtyModel, specialty_id)
        self.session.delete(model)
        self.session.commit()
