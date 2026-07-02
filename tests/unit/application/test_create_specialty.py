from unittest.mock import Mock
from src.application.use_cases.create_specialty import CreateSpecialty


def test_create_specialty_success():
    repo = Mock()

    use_case = CreateSpecialty(repo)

    use_case.execute(name="Cardiology", description="Heart specialist")

    repo.save.assert_called_once()
