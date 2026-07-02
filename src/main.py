from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from src.core.logging_config import configure_logging
from src.domain.exceptions import EntityAlreadyExistsError, RelatedEntityNotFoundError
from src.domain.value_objects.exceptions import DomainValidationError
from src.presentation.api.routes.user_routes import router as user_router
from src.presentation.api.routes.specialty_routes import router as specialty_router
from src.presentation.api.routes.patient_routes import router as patient_router
from src.presentation.api.routes.doctor_routes import router as doctor_router
from src.presentation.api.routes.appointment_routes import router as appointment_router

configure_logging()

app = FastAPI(title="MedScheduler")

app.include_router(user_router)
app.include_router(specialty_router)
app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)


@app.exception_handler(DomainValidationError)
def handle_domain_validation_error(request, exc: DomainValidationError):
    return JSONResponse(status_code=422, content={"detail": str(exc)})


@app.exception_handler(EntityAlreadyExistsError)
def handle_entity_already_exists_error(request, exc: EntityAlreadyExistsError):
    return JSONResponse(status_code=409, content={"detail": str(exc)})


@app.exception_handler(RelatedEntityNotFoundError)
def handle_related_entity_not_found_error(request, exc: RelatedEntityNotFoundError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.exception_handler(IntegrityError)
def handle_integrity_error(request, exc: IntegrityError):
    diag = getattr(getattr(exc, "orig", None), "diag", None)
    detail = getattr(diag, "message_detail", None) or "Database constraint violated"
    return JSONResponse(status_code=409, content={"detail": detail})


@app.get("/health")
def health():
    return {"status": "ok"}