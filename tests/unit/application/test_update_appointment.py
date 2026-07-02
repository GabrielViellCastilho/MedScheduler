from datetime import datetime, timedelta
from unittest.mock import Mock
from uuid import uuid4

import pytest

from src.application.use_cases.update_appointment import UpdateAppointment
from src.domain.exceptions import RelatedEntityNotFoundError, ScheduleConflictError


def test_update_appointment_success():
    repo = Mock()
    doctor_repo = Mock()
    patient_repo = Mock()

    appointment = Mock()
    appointment.id = uuid4()

    repo.find_by_id.return_value = appointment
    repo.has_conflict.return_value = False
    patient_repo.find_by_id.return_value = Mock(active=True)
    doctor_repo.find_by_id.return_value = Mock(active=True)

    use_case = UpdateAppointment(repo, doctor_repo, patient_repo)

    start = datetime.utcnow()
    end = start + timedelta(hours=1)

    result = use_case.execute(
        appointment_id=appointment.id,
        patient_id=uuid4(),
        doctor_id=uuid4(),
        start_datetime=start,
        end_datetime=end,
        notes="updated",
    )

    repo.update.assert_called_once()
    assert result is not None


def test_update_appointment_not_found():
    repo = Mock()
    doctor_repo = Mock()
    patient_repo = Mock()

    repo.find_by_id.return_value = None

    use_case = UpdateAppointment(repo, doctor_repo, patient_repo)

    result = use_case.execute(
        uuid4(), uuid4(), uuid4(),
        datetime.utcnow(),
        datetime.utcnow(),
    )

    assert result is None
    repo.update.assert_not_called()


def test_update_appointment_conflict():
    repo = Mock()
    doctor_repo = Mock()
    patient_repo = Mock()

    appointment = Mock()
    appointment.id = uuid4()

    repo.find_by_id.return_value = appointment
    repo.has_conflict.return_value = True
    patient_repo.find_by_id.return_value = Mock(active=True)
    doctor_repo.find_by_id.return_value = Mock(active=True)

    use_case = UpdateAppointment(repo, doctor_repo, patient_repo)

    with pytest.raises(ScheduleConflictError):
        use_case.execute(
            appointment.id,
            uuid4(),
            uuid4(),
            datetime.utcnow(),
            datetime.utcnow(),
        )