from fastapi import FastAPI

from src.presentation.api.routes.user_routes import router as user_router

app = FastAPI(title="MedScheduler")

app.include_router(user_router)


@app.get("/health")
def health():
    return {"status": "ok"}