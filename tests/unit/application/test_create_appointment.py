from datetime import datetime, timedelta
from unittest.mock import Mock
from uuid import uuid4

import pytest

from src.application.use_cases.create_appointment import CreateAppointment
from src.domain.exceptions import RelatedEntityNotFoundError, ScheduleConflictError


def test_create_appointment_success():
    repo = Mock()
    doctor_repo = Mock()
    patient_repo = Mock()

    patient_repo.find_by_id.return_value = Mock(active=True)
    doctor_repo.find_by_id.return_value = Mock(active=True)
    repo.has_conflict.return_value = False

    use_case = CreateAppointment(repo, doctor_repo, patient_repo)

    start = datetime.utcnow()
    end = start + timedelta(hours=1)

    result = use_case.execute(
        patient_id=uuid4(),
        doctor_id=uuid4(),
        start_datetime=start,
        end_datetime=end,
        notes="ok",
    )

    repo.save.assert_called_once()
    assert result is not None


def test_create_appointment_patient_not_found():
    repo = Mock()
    doctor_repo = Mock()
    patient_repo = Mock()

    patient_repo.find_by_id.return_value = None

    use_case = CreateAppointment(repo, doctor_repo, patient_repo)

    with pytest.raises(RelatedEntityNotFoundError):
        use_case.execute(uuid4(), uuid4(), datetime.utcnow(), datetime.utcnow())


def test_create_appointment_doctor_not_found():
    repo = Mock()
    doctor_repo = Mock()
    patient_repo = Mock()

    patient_repo.find_by_id.return_value = Mock(active=True)
    doctor_repo.find_by_id.return_value = None

    use_case = CreateAppointment(repo, doctor_repo, patient_repo)

    with pytest.raises(RelatedEntityNotFoundError):
        use_case.execute(uuid4(), uuid4(), datetime.utcnow(), datetime.utcnow())


def test_create_appointment_conflict():
    repo = Mock()
    doctor_repo = Mock()
    patient_repo = Mock()

    patient_repo.find_by_id.return_value = Mock(active=True)
    doctor_repo.find_by_id.return_value = Mock(active=True)
    repo.has_conflict.return_value = True

    use_case = CreateAppointment(repo, doctor_repo, patient_repo)

    with pytest.raises(ScheduleConflictError):
        use_case.execute(uuid4(), uuid4(), datetime.utcnow(), datetime.utcnow())